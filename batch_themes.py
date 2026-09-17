import os
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
import requests

# ==================== CONFIGURATION ====================
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
OUTPUT_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")
# =======================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

if not shutil.which("ffmpeg"):
    print("[-] CRITICAL ERROR: 'ffmpeg' executable not found in system PATH.")
    print("    Install FFmpeg or add its path to environment variables.")
    exit(1)

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

def find_xml_file():
    possible_files = ["anilist.xml", "myanimelist.xml", "animelist.xml"]
    for fname in possible_files:
        full_path = os.path.join(DESKTOP_PATH, fname)
        if os.path.exists(full_path):
            return full_path
    return None

def get_anime_data_from_xml(file_path):
    print(f"[+] Reading XML from: {file_path}")
    
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        anime_list = []
        seen_titles = set()

        for anime in root.findall('.//anime'):
            search_queries = []
            primary_title = None

            for tag in ['series_title', 'title', 'romaji_title']:
                elem = anime.find(tag)
                if elem is not None and elem.text and elem.text.strip():
                    primary_title = elem.text.strip()
                    break

            if not primary_title or primary_title in seen_titles:
                continue

            seen_titles.add(primary_title)
            search_queries.append(primary_title)

            for tag in ['series_title_english', 'english_title', 'user_jp_title', 'english']:
                elem = anime.find(tag)
                if elem is not None and elem.text and elem.text.strip():
                    eng_title = elem.text.strip()
                    if eng_title not in search_queries:
                        search_queries.append(eng_title)

            syn_elem = anime.find('series_synonyms')
            if syn_elem is not None and syn_elem.text and syn_elem.text.strip():
                synonyms = [s.strip() for s in syn_elem.text.split(';') if s.strip()]
                for syn in synonyms:
                    if syn not in search_queries:
                        search_queries.append(syn)

            anime_list.append({
                'primary_title': primary_title,
                'queries': search_queries
            })

        return anime_list
    except Exception as e:
        print(f"[-] XML Parsing Exception: {e}")
        return []

def download_theme(anime_info):
    primary_title = anime_info['primary_title']
    queries = anime_info['queries']

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AniListDownloader/1.0"
    }

    anime_results = []
    matched_query = ""

    for query in queries:
        clean_title = query.strip()
        if not clean_title:
            continue

        search_url = "https://api.animethemes.moe/search"
        params = {
            "q": clean_title,
            "include": "anime.animethemes.animethemeentries.videos,anime.images"
        }

        try:
            res = requests.get(search_url, params=params, headers=headers, timeout=10)
            
            if res.status_code == 422 or len(clean_title) < 3:
                fallback_url = "https://api.animethemes.moe/anime"
                fallback_params = {
                    "filter[name]": clean_title,
                    "include": "animethemes.animethemeentries.videos,images"
                }
                res = requests.get(fallback_url, params=fallback_params, headers=headers, timeout=10)
                if res.status_code == 200:
                    anime_results = res.json().get("anime", [])
            elif res.status_code == 200:
                anime_results = res.json().get("search", {}).get("anime", [])

            if anime_results:
                matched_query = clean_title
                break

        except Exception:
            continue

    if not anime_results:
        print(f"    [-] No search match found on AnimeThemes.")
        return

    target_anime = anime_results[0]
    anime_name = target_anime.get('name', primary_title)

    if matched_query != primary_title:
        print(f"    [+] Fallback matched using title: '{matched_query}'")

    images = target_anime.get("images", [])
    cover_url = None
    for img in images:
        if img.get("facet") in ["Large Cover", "Small Cover"]:
            cover_url = img.get("link")
            break
    if not cover_url and images:
        cover_url = images[0].get("link")

    temp_cover_path = os.path.join(OUTPUT_FOLDER, "_temp_cover.jpg")
    has_cover = False
    if cover_url:
        try:
            img_res = requests.get(cover_url, headers=headers, timeout=10)
            if img_res.status_code == 200:
                with open(temp_cover_path, "wb") as f:
                    f.write(img_res.content)
                has_cover = True
        except Exception:
            has_cover = False

    for theme in target_anime.get("animethemes", []):
        theme_type = theme.get("slug", "") or theme.get("type", "")

        if not (theme_type.startswith("OP") or theme_type.startswith("ED")):
            continue

        for entry in theme.get("animethemeentries", []):
            for video in entry.get("videos", []):
                audio_url = video.get("link")
                if not audio_url:
                    continue

                song_name = sanitize_filename(f"{anime_name} - {theme_type}")
                output_path = os.path.join(OUTPUT_FOLDER, f"{song_name}.mp3")

                if os.path.exists(output_path):
                    print(f"    [~] Already downloaded: {song_name}")
                    continue

                print(f"    [!] Downloading: {song_name}")

                if has_cover:
                    cmd = [
                        "ffmpeg", "-y",
                        "-i", audio_url,
                        "-i", temp_cover_path,
                        "-map", "0:a",
                        "-map", "1:v",
                        "-q:a", "0",
                        "-c:v", "mjpeg",
                        "-disposition:v", "attached_pic",
                        "-id3v2_version", "3",
                        "-metadata", f"title={song_name}",
                        "-metadata", f"artist={anime_name}",
                        output_path
                    ]
                else:
                    cmd = [
                        "ffmpeg", "-y",
                        "-i", audio_url,
                        "-vn",
                        "-q:a", "0",
                        "-id3v2_version", "3",
                        "-metadata", f"title={song_name}",
                        "-metadata", f"artist={anime_name}",
                        output_path
                    ]

                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"    [-] FFmpeg Error: {result.stderr.strip()[-150:]}")
                else:
                    print(f"    [+] Saved: {song_name}.mp3")
                break

    if os.path.exists(temp_cover_path):
        try:
            os.remove(temp_cover_path)
        except Exception:
            pass

def main():
    xml_path = find_xml_file()
    if not xml_path:
        print("[-] Error: Could not find 'anilist.xml' or 'myanimelist.xml' on your Desktop.")
        return

    anime_list = get_anime_data_from_xml(xml_path)
    if not anime_list:
        print("[-] Process aborted: 0 titles parsed from XML.")
        return

    print(f"[+] Loaded {len(anime_list)} anime titles from {os.path.basename(xml_path)}.\n")
    for idx, anime in enumerate(anime_list, 1):
        print(f"[{idx}/{len(anime_list)}] Processing: {anime['primary_title']}")
        download_theme(anime)

if __name__ == "__main__":
    main()