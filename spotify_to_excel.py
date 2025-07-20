import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from openpyxl.utils import get_column_letter

# Add your personal info
CLIENT_ID = 'YOUR_CLIENT_ID_HERE'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET_HERE'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
SCOPE = 'playlist-read-private'

# Spotify API connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# Excel Writer
writer = pd.ExcelWriter("playlists.xlsx", engine='openpyxl')

# Get all user playlists
playlists = sp.current_user_playlists()

for playlist in playlists['items']:
    playlist_name = playlist['name']
    playlist_id = playlist['id']

    # Pull tracks from the playlist
    results = sp.playlist_tracks(playlist_id)
    tracks_data = []
    for item in results['items']:
        track = item['track']
        if track:
            name = track['name']
            artist = track['artists'][0]['name']
            tracks_data.append({'Song Name': name, 'Artist': artist})  

    # DataFrame and sheet name
    df = pd.DataFrame(tracks_data)
    clean_sheet_name = ''.join(c for c in playlist_name if c.isalnum() or c in (' ', '_')).strip()[:31]
    if not clean_sheet_name:
        clean_sheet_name = f"playlist_{playlist_id[:5]}"

    # Excel Page
    df.to_excel(writer, sheet_name=clean_sheet_name, index=False)

    # Automatic column width adjustment
    worksheet = writer.sheets[clean_sheet_name]
    for column_cells in worksheet.columns:
        max_length = 0
        column = column_cells[0].column
        column_letter = get_column_letter(column)
        for cell in column_cells:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        worksheet.column_dimensions[column_letter].width = max_length + 2

# Save
writer.close()
print("playlists.xlsx created successfully!")
