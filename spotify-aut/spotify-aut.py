import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

clientID = "19fd8a875b294d64961930781fb2ec70"
clientSecret = "f1155fa0b33343a7a6160b1ff15f1b83"
redirectURL = "https://www.google.com/"
username = "wui5sa0fm7e298dkak11vlhxx"

# oauth object
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURL)

# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# To print the response in readable format.
print(json.dumps(user,sort_keys=True, indent=4))



while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Exit")
    print("1 - Search for a Song")
    choice = int(input("Your Choice: "))
    if choice == 1:
        # Logic for search functionality
        # Get the Song Name.
        searchQuery = input("Enter Song Name: ")
        # Search for the Song.
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('Song has opened in your browser.')
    
    elif choice == 0:
        break
    else:
        print("Enter valid choice.")