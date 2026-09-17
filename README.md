# Batch AnimeThemes Downloader

A command-line tool designed to download high-quality theme songs (OPs & EDs) from [AnimeThemes.moe](https://animethemes.moe) in bulk using your **MyAnimeList (MAL)** or **AniList** export files.

---

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

2. **Install Ffmpeg**

   you can download it manually from the official FFmpeg download page, 
   extract the zip and then copy everything inside the bin folder and
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
- **Graphical User Interface (GUI)**: Full desktop UI for easy point-and-click operation alongside the CLI.
- **Advanced Filters**: Exclude specific theme types (e.g., skip EDs, NC, or specific video resolutions).
- **Enhanced Downloading**: Utilizes the Torrent Archive in my Server dedicated specifically for Downloading
  instead of the usual AnimeThemes.moe API.

👉[Get the Pro Edition on Gumroad](https://gumroad.com/)

## Support Me
If you find this tool helpful and want to support my other development or 
need technical help, feel free to buy me a coffee!

## License
This project is licensed under the GPL v3 License - see the LICENSE file for details.
