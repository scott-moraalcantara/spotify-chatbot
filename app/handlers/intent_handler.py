from app.handlers.commands import parse_user_query
from app.handlers.music import search_track, play_track

def handle_query(query):
    parsed_response = parse_user_query(query)

    if "play" in parsed_response.lower():
        song_name = parsed_response.split('Details:')[-1].strip()
        track_uri = search_track(song_name)

        if track_uri:
            play_track(track_uri)
            return f"Playing {song_name}."
        else:
            return "Track not found."
    else:
        return "I didn't understand your request."