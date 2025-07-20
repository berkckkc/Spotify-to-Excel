# Spotify Playlist Exporter to Excel 🎵📊

A simple Python tool that exports all your Spotify playlists into an Excel file, with each playlist saved as a separate sheet.

---

## 📦 Features

- ✅ Exports **all user playlists**
- ✅ Each playlist becomes a **separate Excel sheet**
- ✅ Columns include: `Song Title` and `Artist`
- ✅ Automatically adjusts **column widths** for readability

---

## 🔧 Requirements

- Python 3.7+
- Spotify Developer Account (Free)
- Spotify App with:
  - **Client ID**
  - **Client Secret**
  - Redirect URI: `http://127.0.0.1:8888/callback`

---

## 📦 Installation

```bash
pip install spotipy pandas openpyxl
```
## 🚀 Usage
```bash

1. Clone the repo

2. Edit `spotify_to_excel.py` and replace:

   * `YOUR_CLIENT_ID_HERE`
   * `YOUR_CLIENT_SECRET_HERE`

3. Run the script:
python spotify_to_excel.py
```

4. After authentication, the script will create `playlists.xlsx` with all your playlists inside!

---

## 📁 Output Example

* `playlists.xlsx`
  ├── Chill Vibes (sheet)
  ├── Workout Mix (sheet)
  ├── Roadtrip Songs (sheet)
  └── ...

Each sheet contains:

| Şarkı Adı (Song Name) | Sanatçı (Artist) |
| -------------------- 	| ---------------  |
| Blinding Lights 	| The Weeknd 	   |
| Levitating      	| Dua Lipa         |

---

## 🛡 Disclaimer

This tool uses Spotify Web API under their terms of use. You need your own Client ID and Client Secret to access your account data.

---



