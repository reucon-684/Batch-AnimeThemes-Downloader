# Batch AnimeThemes Downloader

A command-line tool designed to download high-quality theme songs (OPs & EDs) from [AnimeThemes.moe](https://animethemes.moe) in bulk using your **MyAnimeList (MAL)** or **AniList** export files.

---

## Features

- **List Import**: Seamlessly parse XML export files from MyAnimeList or AniList.
- **Audio Extraction**: Downloads theme tracks directly in high-quality MP3 format.
- **Automated Organization**: Automatically names and structures output files by anime title, song title, and theme type (OP/ED).
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
   cd batch-animethemes-downloader

2. **Install Ffmpeg**
**For Windows**
   ```bash
   winget install Gyan.FFmpeg
   
**For Linux, Windows and MacOS**
you can download it manually from the official FFmpeg download page, 
extract the zip and then copy everything inside the bin folder and
paste it in batch-animethemes-downloader folder.
