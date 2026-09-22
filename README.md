# Batch AnimeThemes Downloader

A command-line tool designed to download high-quality theme songs (OPs & EDs) from [AnimeThemes.moe](https://animethemes.moe) in bulk using your **MyAnimeList (MAL)** or **AniList** export files.

<div align="left">
<img src="https://github.com/user-attachments/assets/b43ef96b-4e4d-4b2f-8e26-982728811464" alt="Welcome to AniThemes Sourse Code" width="600" style="max-width: 100%;">
</div>

## Features

- **List Import**: Seamlessly parse XML export files from MyAnimeList or AniList.
- **Audio Extraction**: Downloads theme tracks directly in high-quality MP3 format.
- **Automated Organization**: Automatically names and structures output files by anime title and theme type (OP/ED).
- **Fast CLI Execution**: Lightweight, terminal-driven tool built for fast bulk processing.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Ffmpeg

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/reucon-684/Batch-AnimeThemes-Downloader.git

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Install Ffmpeg**:

   You can download it manually from the Official FFmpeg Download Page, 
   Extract the zip and then Copy everything inside the bin folder and
   paste it in the Desktop along with batch.py.

### How To Use

1. **Export Your List For MAL:**
Open your browser and log into MyAnimeList.
Navigate directly to the MyAnimeList Export Tool (Panel > Export).
Select you want to export your Anime List.
Click the Export My List button.
A Zip File will Download, Extract it and rename the xml to myanimelist.xml.
Then copypaste the XML to Desktop.
2. **Export Your List For AniList:**
Go to https://fern.ignoffo.dev/export.
Type your AniList Username, Pick Export Format myanimelist.
and Media Type Anime then click Export.
then rename the xml to anilist.xml.
Then copypaste the XML to Desktop.
3. **Run The CLI:**
Either double click or
   ```bash
   python batch.py

# Advanced Options & Video Support (Pro Version)

Looking for video downloads, advanced filtering, or an interactive interface? Check out Batch AnimeThemes Downloader Pro available on Gumroad:

- **Video Support**: Download themes in MP4 and WebM formats alongside MP3.
- **Graphical User Interface (GUI)**: Full desktop UI for easy point-and-click operation alongside the command-line utility.
- **Advanced Filters**: Exclude specific theme types (e.g., skip EDs, NC, or specific video resolutions).
- **Enhanced Downloading**: Utilizes the AnimeThemes Torrent Archive in a custom-built API dedicated specifically for Downloading
  instead of the usual AnimeThemes.moe API.

👉[Get the Pro Edition](https://reucon.gumroad.com/) or get the complete [Batch + URL Bundle](https://reucon.gumroad.com/) on Gumroad to unlock everything!

## AnimeThemes Downloader
🚀 Need to use a link and only download one anime worth of OP and ED instead? Then check out the [AnimeThemes Downloader!](https://github.com/reucon-684/AnimeThemes-Downloader)

## License
This project is licensed under the GPL v3 License - see the LICENSE file for details.
