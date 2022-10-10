#!/usr/bin/env python3

import asyncio
import calendar
from datetime import timedelta
import os
import re
import sys
import time


#default bitrate
bitrate = "320"

#default download location
download_location = os.getcwd()

#automatic package installer
python = 'python3'

if 'win' in sys.platform:
    
    python = 'python'

#this allows the natsuka executable to use ffmpeg embedded in it
#for other users not using this exe, you will need to install ffmpeg yourself
#pyinstaller --add-data="ffmpeg.exe;." --icon=spotify.ico -F .\natsuka.py
if getattr(sys, 'frozen', False):

    #temporary folder for pyinstaller
    basedir = f"{sys._MEIPASS}/"

else:

    #just don't use it, and use ffmpeg from PATH
    basedir = ""


print('[*] Checking for required dependencies...\n')

while True:
    
    try:
        
        import aiohttp
        import eyed3
        from eyed3.id3.frames import ImageFrame
        from eyed3.core import Date
        
        break
    
    except ModuleNotFoundError as e:
        
        module = str(e)[17:-1]
        
        print(f'[*] Installing {module} module for python')
        
        try:
            
            if os.system(f'{python} -m pip install {module}') != 0:
                
                raise error
            
        except Exception:
            
            print(f'[!] Error installing "{module}" module. Pip may not be installed or no WiFi connection may be available.')
            
            input(f'[!] Failed to initialize natsuka. Press Ctrl+C to exit...')
            
            sys.exit()


async def main():

    session = aiohttp.ClientSession()

    try:

        async with session.get("https://music.joshuadoes.com/", timeout=5):

            print("[*] Connection established.\n")

            await session.close()

    except aiohttp.client_exceptions.ClientConnectorError:

        print("[!] No WiFi connection available. natsuka will now close...")

        await session.close()

        sys.exit()

    except asyncio.exceptions.TimeoutError:

        print("[!] API is unavailable at the moment (Server is most likely down).\n"
              "natsuka will now close..."
              )

        await session.close()

        sys.exit()
    
    print("natsuka - spotify downloader\n"
          "Thanks to JoshuaDoes for making this possible."
          )

    option = input(f"""
What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: {bitrate}kbps)
Option 8 - Change Download Location
Option 9 - Exit

: """
               )

    while not any(x in option for x in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]) or not int:

        print("Invalid option!")

        option = input(f"""
What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: {bitrate}kbps)
Option 8 - Change Download Location
Option 9 - Exit

: """
               )

    if option == "1":

        await trackProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "2":

        await albumProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "3":

        await playlistProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "4":

        await bestmatchProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "5":

        await songSearch()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "6":

        await artistSearch()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "7":

        await changeBitrate()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "8":

        await changeDownloadLocation()

        try:

            input("Press enter to continue.\n")

        except SyntaxError:

            pass

        await main()

    if option == "9":

        sys.exit()


async def trackProcess():

    global download_location

    songList = []

    URI = ""

    while URI != "START":

        URI = input(f"Enter songs (Current number of songs: {len(songList)})\n"
                    "Type 'START' to begin download.\n\n"
                    "Type 'RETURN' to return to main menu\n: "
                    )

        while len(re.findall(r'(https?://[^\s]+)', URI)) == 0 and URI != "START" and URI != "RETURN":

            print("Invalid URL!\n")

            URI = input(f"Enter songs (Current number of songs: {len(songList)})\n"
                        "Type 'START' to begin download.\n\n"
                        "Type 'RETURN' to return to main menu\n: "
                        )
        
        if URI == "RETURN":

            return

        query = "?"
    
        if query in URI:
        
            URI = URI.split(query)

            group = URI[0].split("/")

            URI = group[len(group) - 1]
        
        else:

            group = URI.split("/")

            URI = group[len(group) - 1]

        if URI != "START":

            songList.append(URI)

    if len(songList) == 0:

            print("\nCannot begin with no songs to download!\n")

            await trackProcess()

    print(f"Loading {len(songList)} songs...\n")

    if hasattr(sys, 'getandroidapilevel'):

        print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

            download_location = "storage/downloads"

    start_time = time.monotonic()

    session = aiohttp.ClientSession()

    for i in songList:

        #fix aiohttp server disconnected by adding a retry on failure

        async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                trackData = await trackJSON.json()

                if len(trackData) == 0:

                    print("Wrong URL input!\n"
                          "Returning to main menu...\n"
                          )

                    await session.close()

                    return
                    
                trackName = trackData['name']

                trackAlbum = trackData['album']['name']

                trackNumber = trackData['number']

                artistName = trackData['album']['artist'][0]['name']

                albumRelease = trackData['album']['date']

                print(f"Track Name: {trackName}")

                print(f"Album Name: {trackAlbum}")

                print(f"Artist Name: {artistName}")

                print(f"Album Release: {albumRelease['year']}\n")
                
                fileName = re.sub('\$', 'S', trackName)

                fileName = re.sub('[\/:*?"<>|]', '', fileName)

                if not os.path.exists(f"{download_location}/Music"):

                    os.makedirs(f"{download_location}/Music")

                if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                    print("Song already downloaded to this directory. Skipping...\n")

                else:
            
                    download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    

                    convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
            
                    async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                        embed = await embedData.json()

                        coverArt = embed['thumbnail_url']

                        async with session.get(coverArt) as img:

                            imgData = await img.read()

                        try:

                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")

                        except OSError:

                            os.remove(f"{download_location}/Music/{fileName}.ogg")

                            os.remove(f"{download_location}/Music/{fileName}.mp3")

                            print("\nSong does not contain download formats.")

                            print("Attempting to grab link with formats...")

                            print(f"\nTrack Name: {trackName}")

                            print(f"Album Name: {trackAlbum}")

                            print(f"Artist Name: {artistName}")

                            print(f"Album Release: {albumRelease['year']}\n")

                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    

                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')

                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                    
                        print("Song Downloaded!")

                        if (audioFile.tag == None):

                            audioFile.initTag()

                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                        audioFile.tag.title = trackName
                            
                        audioFile.tag.album = trackAlbum
                            
                        audioFile.tag.track_num = trackNumber
                            
                        audioFile.tag.artist = artistName

                        audioFile.tag.recording_date = Date(albumRelease['year'])

                        audioFile.tag.save()

                        os.remove(f"{download_location}/Music/{fileName}.ogg")

                        print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def albumProcess():

    global download_location

    URI = input("Enter the album's URL\n\n"
                "Type 'RETURN' to return to main menu\n: "
                )

    while len(re.findall(r'(https?://[^\s]+)', URI)) == 0 and URI != "RETURN":

        print("Invalid URL!\n")

        URI = input("Enter the album's URL\n\n"
                    "Type 'RETURN' to return to main menu\n: "
                )

    if URI == "RETURN":

        return

    query = "?"
    
    if query in URI:
        
        URI = URI.split(query)

        group = URI[0].split("/")

        URI = group[len(group) - 1]
        
    else:

        group = URI.split("/")

        URI = group[len(group) - 1]

    session = aiohttp.ClientSession()

    async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{URI}?pass=pleasesparemyendpoints&quality=2") as albumData:

        album = await albumData.json()

        if len(album) == 0:

            print("Wrong URL input!\n"
                  "Returning to main menu...\n"
                  )

            await session.close()

            return

        allTracks = album['disc']

        trackList = []
            
        trackURIS = []

        for i in allTracks:

            trackList += (i['track'])

        for i in range(len(trackList)):

            GID = trackList[i]['gid']

            async with session.get(f"https://music.joshuadoes.com/util/gid2id/?gid={GID}") as trackData:

                trackID = await trackData.json()

                trackURIS.append(trackID['id'])

    print(f"Loading {len(trackURIS)} songs...\n")

    if hasattr(sys, 'getandroidapilevel'):

        print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n")
                       )

            download_location = "storage/downloads"

    start_time = time.monotonic()    

    for i in trackURIS:

            #fix aiohttp server disconnected by adding a retry on failure

            async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                    trackData = await trackJSON.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {albumRelease['year']}\n")

                    fileName = re.sub('\$', 'S', trackName)
                    
                    fileName = re.sub('[\/:*?"<>|]', '', fileName)
                    
                    if not os.path.exists(f"{download_location}/Music"):

                        os.makedirs(f"{download_location}/Music")
                        
                    if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                        print("Song already downloaded to this directory. Skipping...\n")

                    else:
            
                        download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                        convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                        async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:
    
                            embed = await embedData.json()
    
                            coverArt = embed['thumbnail_url']
    
                        async with session.get(coverArt) as img:
    
                            imgData = await img.read()
    
                        try:
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                        except OSError:
    
                            os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                            os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                            print("\nSong does not contain download formats.")
    
                            print("Attempting to grab link with formats...")
    
                            print(f"\nTrack Name: {trackName}")
    
                            print(f"Album Name: {trackAlbum}")
    
                            print(f"Artist Name: {artistName}")
    
                            print(f"Album Release: {albumRelease['year']}\n")
    
                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                        
                        print("Song Downloaded!")
    
                        if (audioFile.tag == None):
    
                            audioFile.initTag()
    
                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                        audioFile.tag.title = trackName
                                
                        audioFile.tag.album = trackAlbum
                                
                        audioFile.tag.track_num = trackNumber
                                
                        audioFile.tag.artist = artistName
    
                        audioFile.tag.recording_date = Date(albumRelease['year'])
    
                        audioFile.tag.save()
    
                        os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                        print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def playlistProcess():

    global download_location

    userID = input("Input user ID\n\n"
                   "Type 'RETURN' to return to main menu\n: "
                   )

    while userID == "":

        print("User ID cannot be empty!\n")

        userID = input("Input user ID\n\n"
                   "Type 'RETURN' to return to main menu\n: "
                   )

    if userID == "RETURN":

        return

    playlistID = input("Input the playlist's URL\n\n"
                       "Type 'RETURN' to return to main menu\n: "
                       )

    while playlistID == "":

        print("Playlist URL cannot be empty!\n")

        playlistID = input("Input the playlist's URL\n\n"
                           "Type 'RETURN' to return to main menu\n: "
                           )

        if playlistID == "RETURN":

            return

    query = "?"
    
    if query in playlistID:
        
        playlistID = playlistID.split(query)

        group = playlistID[0].split("/")

        playlistID = group[len(group) - 1]
        
    else:

        group = playlistID.split("/")

        playlistID = group[len(group) - 1]

    session = aiohttp.ClientSession()

    async with session.get(f"https://music.joshuadoes.com/playlist/spotify:user:{userID}:playlist:{playlistID}?pass=pleasesparemyendpoints&quality=2") as playlistData:

        playlist = await playlistData.json()

        if len(playlist) == 0:

            print("Incorrect User ID or Playlist ID!\n"
                  "Returning to main menu...\n"
                  )

            await session.close()

            return

        playlistName = playlist['attributes']['name']

        if len(playlist['attributes']) == 2:

            playlistDescription = playlist['attributes']['description']

        else:

            playlistDescription = None

        playlistLength = playlist['length']

        playlistData = []

        playlistURIS = []

        playlistSongs = playlist['contents']['items']

        print(f"Playlist Name: {playlistName}")

        print(f"Description: {playlistDescription}")

        print(f"Playlist Length: {playlistLength} tracks")

        for index, song in enumerate(playlistSongs):

            playlistData.append(song)

            playlistURIS.append(playlistData[index]['uri'].split(":")[2])

    print(f"Loading {len(playlistURIS)} songs...\n")

    if hasattr(sys, 'getandroidapilevel'):

        print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

            download_location = "storage/downloads"

    start_time = time.monotonic()

    for i in playlistURIS:

            #fix aiohttp server disconnected by adding a retry on failure

            async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                    trackData = await trackJSON.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {albumRelease['year']}\n")

                    fileName = re.sub('\$', 'S', trackName)

                    fileName = re.sub('[\/:*?"<>|]', '', fileName)

                    if not os.path.exists(f"{download_location}/Music"):

                        os.makedirs(f"{download_location}/Music")
                        
                    if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                        print("Song already downloaded to this directory. Skipping...\n")

                    else:
            
                        download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                        convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                        async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:
    
                            embed = await embedData.json()
    
                            coverArt = embed['thumbnail_url']
    
                        async with session.get(coverArt) as img:
    
                            imgData = await img.read()
    
                        try:
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                        except OSError:
    
                            os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                            os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                            print("\nSong does not contain download formats.")
    
                            print("Attempting to grab link with formats...")
    
                            print(f"\nTrack Name: {trackName}")
    
                            print(f"Album Name: {trackAlbum}")
    
                            print(f"Artist Name: {artistName}")
    
                            print(f"Album Release: {albumRelease['year']}\n")
    
                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")    
                        
                        print("Song Downloaded!")
    
                        if (audioFile.tag == None):
    
                            audioFile.initTag()
    
                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                        audioFile.tag.title = trackName
                                
                        audioFile.tag.album = trackAlbum
                                
                        audioFile.tag.track_num = trackNumber
                                
                        audioFile.tag.artist = artistName
    
                        audioFile.tag.recording_date = Date(albumRelease['year'])
    
                        audioFile.tag.save()
    
                        os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                        print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def bestmatchProcess():

    global download_location

    songList = []

    song = ""

    while song != "START":

        song = input(f"Enter songs (Current number of songs: {len(songList)})\n"
                      "Type 'START' to begin download.\n"
                      "Tip: For best results, use format: (Song Name) (Artist Name)\n\n"
                      "Type 'RETURN' to return to main menu\n: "
                     )
        
        if song == "RETURN":

            return

        while song == "":

            print("Song name is empty!")

            song = input(f"Enter songs (Current number of songs: {len(songList)})\n"
                          "Type 'START' to begin download.\n"
                          "Tip: For best results, use format: (Song Name) (Artist Name)\n\n"
                          "Type 'RETURN' to return to main menu\n: "
                         )

        if song != "START":

            songList.append(song)

    print(f"Loading {len(songList)} songs...\n")

    if hasattr(sys, 'getandroidapilevel'):

        print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

            download_location = "storage/downloads"

    session = aiohttp.ClientSession()

    start_time = time.monotonic()

    for i in songList:

        #fix aiohttp server disconnected by adding a retry on failure

        async with session.get(f"https://music.joshuadoes.com/v1/bestmatch:{i}?pass=pleasesparemyendpoints&quality=2") as songJSON:

                songData = await songJSON.json()

                if len(songData) == 1:

                    print("No results for query. Try being more specific with your search!\n")

                    await session.close()

                    return

                URI = songData['object']['id']

                async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{URI}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                    trackData = await trackJSON.json()

                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {albumRelease['year']}\n")

                    fileName = re.sub('\$', 'S', trackName)

                    fileName = re.sub('[\/:*?"<>|]', '', fileName)

                    if not os.path.exists(f"{download_location}/Music"):

                        os.makedirs(f"{download_location}/Music")
                        
                    if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                        print("Song already downloaded to this directory. Skipping...\n")

                    else:
            
                        download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{URI}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                        convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                        async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{URI}") as embedData:
    
                            embed = await embedData.json()
    
                            coverArt = embed['thumbnail_url']
    
                        async with session.get(coverArt) as img:
    
                            imgData = await img.read()
    
                        try:
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                        except OSError:
    
                            os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                            os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                            print("\nSong does not contain download formats.")
    
                            print("Attempting to grab link with formats...")
    
                            print(f"\nTrack Name: {trackName}")
    
                            print(f"Album Name: {trackAlbum}")
    
                            print(f"Artist Name: {artistName}")
    
                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                        
                        print("Song Downloaded!")
    
                        if (audioFile.tag == None):
    
                            audioFile.initTag()
    
                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                        audioFile.tag.title = trackName
                                
                        audioFile.tag.album = trackAlbum
                                
                        audioFile.tag.track_num = trackNumber
                                
                        audioFile.tag.artist = artistName
    
                        audioFile.tag.recording_date = Date(albumRelease['year'])
    
                        audioFile.tag.save()
    
                        os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                        print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def songSearch():

    global download_location

    query = input("Input song name\n\n"
                  "Type 'RETURN' to return to main menu\n: "
                  )

    if query == "RETURN":

        return

    while query == "":

        print("Search is empty!")

        query = input("Input song name\n: ")

    session = aiohttp.ClientSession()

    async with session.get(f"https://music.joshuadoes.com/v1/search:{query}") as resp:

        results = await resp.json()

        try:

            searchData = results['object']['streams']

        except KeyError:

            print("No results for query. Try being more specific with your search!\n")

            await session.close()

            return

        songURIList = []

        albumURIList = []

        for index, song in enumerate(searchData):

            songName = song['object']['name']

            songCreator = song['object']['creators'][0]['object']['name']

            songURI = song['object']['uri']

            songURIList.append(songURI)

            songAlbum = song['object']['album']['object']['name']

            songAlbumURI = song['object']['album']['object']['uri']

            albumURIList.append(songAlbumURI)

            print(f"\nResult number: {index+1}")

            print(f"Song: {songName}")

            print(f"Song creator: {songCreator}")

            print(f"Song Album: {songAlbum}")


    chosenSong = input("Select a song (1-5)\n\n"
                       "Type 'RETURN' to return to main menu\n: "
                       )

    while not any(x in chosenSong for x in ["1", "2", "3", "4", "5", "RETURN"]):

        print("Invalid option!")

        chosenSong = input("Select a song (1-5)\n\n"
                           "Type 'RETURN' to return to main menu\n: "
                           )

    if chosenSong == "RETURN":

        await session.close()

        return

    selectedSong = songURIList[int(chosenSong)-1].split(":")[2]

    downloadOption = input("""
Option 1 - Download Song
Option 2 - Download Song's Album

Type 'RETURN' to return to main menu
: """
                           )

    while not any(x in downloadOption for x in ["1", "2", "RETURN"]):

        print("Invalid option!")

        downloadOption = input("""
Option 1 - Download Song
Option 2 - Download Song's Album

Type 'RETURN' to return to main menu
: """
                           )

    if downloadOption == "RETURN":

        await session.close()

        return

    if downloadOption == "1":

        if hasattr(sys, 'getandroidapilevel'):

            print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

            download_location = "storage/downloads"

        async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{selectedSong}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

            trackData = await trackJSON.json()
                    
            trackName = trackData['name']

            trackAlbum = trackData['album']['name']

            trackNumber = trackData['number']

            artistName = trackData['album']['artist'][0]['name']

            albumRelease = trackData['album']['date']

            print(f"\nTrack Name: {trackName}")

            print(f"Album Name: {trackAlbum}")

            print(f"Artist Name: {artistName}")

            print(f"Album Release: {albumRelease['year']}\n")

            fileName = re.sub('\$', 'S', trackName)

            fileName = re.sub('[\/:*?"<>|]', '', fileName)

            if not os.path.exists(f"{download_location}/Music"):

                os.makedirs(f"{download_location}/Music")
                
            if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                print("Song already downloaded to this directory. Skipping...\n")

            else:
            
                download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{selectedSong}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{selectedSong}") as embedData:
    
                    embed = await embedData.json()
    
                    coverArt = embed['thumbnail_url']
    
                async with session.get(coverArt) as img:
    
                    imgData = await img.read()
    
                try:
    
                    audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                except OSError:
    
                    os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                    os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                    print("\nSong does not contain download formats.")
    
                    print("Attempting to grab link with formats...")
    
                    print(f"\nTrack Name: {trackName}")
    
                    print(f"Album Name: {trackAlbum}")
    
                    print(f"Artist Name: {artistName}")
    
                    print(f"Album Release: {albumRelease['year']}\n")
    
                    download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                    convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                    audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                        
                print("Song Downloaded!")
    
                if (audioFile.tag == None):
    
                    audioFile.initTag()
    
                audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                audioFile.tag.title = trackName
                                
                audioFile.tag.album = trackAlbum
                                
                audioFile.tag.track_num = trackNumber
                                
                audioFile.tag.artist = artistName
    
                audioFile.tag.recording_date = Date(albumRelease['year'])
    
                audioFile.tag.save()
    
                os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                print("Metadata Applied!\n\n")

        end_time = time.monotonic()

        print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

        await session.close()

    if downloadOption == "2":

        selectedAlbum = albumURIList[int(chosenSong)-1].split(":")[2]
        
        async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{selectedAlbum}?pass=pleasesparemyendpoints&quality=2") as albumData:

            album = await albumData.json()

            allTracks = album['disc']

            trackList = []
            
            trackURIS = []

            for i in allTracks:

                trackList += i['track']

            for i in range(len(trackList)):

                GID = trackList[i]['gid']

                async with session.get(f"https://music.joshuadoes.com/util/gid2id/?gid={GID}") as trackData:

                    trackID = await trackData.json()

                    trackURIS.append(trackID['id'])

        print(f"Loading {len(trackURIS)} songs...\n")

        cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

        while not any(x in cont for x in ["1", "2"]):

            print("Invalid option!")

            cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

    
        if cont == "1":

            if hasattr(sys, 'getandroidapilevel'):

                print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

                download_location = "storage/downloads"

            start_time = time.monotonic()

            for i in trackURIS:

                #fix aiohttp server disconnected by adding a retry on failure

                async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                    trackData = await trackJSON.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {albumRelease['year']}\n")

                    fileName = re.sub('\$', 'S', trackName)

                    fileName = re.sub('[\/:*?"<>|]', '', fileName)

                    if not os.path.exists(f"{download_location}/Music"):

                        os.makedirs(f"{download_location}/Music")
                        
                    if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                        print("Song already downloaded to this directory. Skipping...\n")

                    else:
            
                        download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                        convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                        async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:
    
                            embed = await embedData.json()
    
                            coverArt = embed['thumbnail_url']
    
                        async with session.get(coverArt) as img:
    
                            imgData = await img.read()
    
                        try:
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                        except OSError:
    
                            os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                            os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                            print("\nSong does not contain download formats.")
    
                            print("Attempting to grab link with formats...")
    
                            print(f"\nTrack Name: {trackName}")
    
                            print(f"Album Name: {trackAlbum}")
    
                            print(f"Artist Name: {artistName}")
    
                            print(f"Album Release: {albumRelease['year']}\n")
    
                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                            audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                        
                        print("Song Downloaded!")
    
                        if (audioFile.tag == None):
    
                            audioFile.initTag()
    
                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                        audioFile.tag.title = trackName
                                
                        audioFile.tag.album = trackAlbum
                                
                        audioFile.tag.track_num = trackNumber
                                
                        audioFile.tag.artist = artistName
    
                        audioFile.tag.recording_date = Date(albumRelease['year'])
    
                        audioFile.tag.save()
    
                        os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                        print("Metadata Applied!\n\n")

            end_time = time.monotonic()

            print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

            await session.close()

        if cont == "2":

            await session.close()

            return


async def artistSearch():

    global download_location

    query = input("Input artist name\n\n"
                  "Type 'RETURN' to return to main menu\n: "
                  )

    if query == "RETURN":

        return

    while query == "":

        print("Search is empty!")

        query = input("Input artist name\n: ")

    session = aiohttp.ClientSession()

    async with session.get(f"https://music.joshuadoes.com/v1/search:{query}") as resp:

        results = await resp.json()

        if len(results['object']) == 1:

            print("No results for query. Try being more specific with your search!\n")

            await session.close()

            return

        try:

            artists = results['object']['creators']

        except KeyError:

            print("No artists found. Make sure you have not misspelt their name!\n")

            await session.close()

            return

        artistURIList = []

        for index in range(len(artists)):

            artist = artists[index]['object']['name']

            artistURI = artists[index]['object']['uri']

            artistURIList.append(artistURI)

            print(f"\nResult number: {index+1}")
            
            print(f"Artist: {artist}")

        chosenArtist = input("Select a artist (1-5)\n\n"
                             "Type 'RETURN' to return to main menu\n: "
                             )

        while not any(x in chosenArtist for x in ["1", "2", "3", "4", "5", "RETURN"]):

            print("Invalid option!")

            chosenArtist = input("Select an artist (1-5)\n\n"
                               "Type 'RETURN' to return to main menu\n: "
                               )

        if chosenArtist == "RETURN":

            await session.close()

            return

        selectedArtist = artistURIList[int(chosenArtist)-1].split(":")[2]

        async with session.get(f"https://music.joshuadoes.com/artist/{selectedArtist}?pass=pleasesparemyendpoints&quality=2") as artistJSON:

            artistData = await artistJSON.json()

        downloadOption = input("""
Option 1 - Download Artist's Top Songs
Option 2 - Download Album from Artist


Type 'RETURN' to return to main menu
: """
                           )

        while not any(x in downloadOption for x in ["1", "2", "3", "4", "RETURN"]):

            print("Invalid option!")

            downloadOption = input("""
Option 1 - Download Artist's Top Songs
Option 2 - Download Album from Artist


Type 'RETURN' to return to main menu
: """
                           )

        if downloadOption == "RETURN":

            await session.close()

            return

        if downloadOption == "1":

            topSongs = artistData['top_track']

            trackList = []

            trackURIS = []

            for i in topSongs:

                trackList += i['track']

            for i in range(len(trackList)):

                GID = trackList[i]['gid']

                async with session.get(f"https://music.joshuadoes.com/util/gid2id/?gid={GID}") as trackData:

                    trackID = await trackData.json()

                    trackURIS.append(trackID['id'])

                    artistName = artists[int(chosenArtist)-1]['object']['name']

            print(f"Loading {len(trackURIS)} songs...\n")

            cont = input(f"""
Would you like to proceed downloading {artistName}'s top songs?
1 - Yes
2 - No
: """
                             )

            while not any(x in cont for x in ["1", "2"]):

                print("Invalid option!")

                cont = input(f"""
Would you like to proceed downloading {artistName}'s top songs?
1 - Yes
2 - No
: """
                             )

            if cont == "1":

                if hasattr(sys, 'getandroidapilevel'):

                    print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

                    download_location = "storage/downloads"

                start_time = time.monotonic()

                for i in trackURIS:

                    #fix aiohttp server disconnected by adding a retry on failure

                    async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                        trackData = await trackJSON.json()
                    
                        trackName = trackData['name']

                        trackAlbum = trackData['album']['name']

                        trackNumber = trackData['number']

                        artistName = trackData['album']['artist'][0]['name']

                        albumRelease = trackData['album']['date']

                        print(f"Track Name: {trackName}")

                        print(f"Album Name: {trackAlbum}")

                        print(f"Artist Name: {artistName}")

                        print(f"Album Release: {albumRelease['year']}\n")

                        fileName = re.sub('\$', 'S', trackName)

                        fileName = re.sub('[\/:*?"<>|]', '', fileName)

                        if not os.path.exists(f"{download_location}/Music"):

                            os.makedirs(f"{download_location}/Music")
                            
                        if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                            print("Song already downloaded to this directory. Skipping...\n")

                        else:
            
                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                            async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:
    
                                embed = await embedData.json()
    
                                coverArt = embed['thumbnail_url']
    
                            async with session.get(coverArt) as img:
    
                                imgData = await img.read()
    
                            try:
    
                                audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                            except OSError:
    
                                os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                                os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                                print("\nSong does not contain download formats.")
    
                                print("Attempting to grab link with formats...")
    
                                print(f"\nTrack Name: {trackName}")
    
                                print(f"Album Name: {trackAlbum}")
    
                                print(f"Artist Name: {artistName}")
    
                                print(f"Album Release: {albumRelease['year']}\n")
    
                                download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                                convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                                audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                        
                            print("Song Downloaded!")
    
                            if (audioFile.tag == None):
    
                                audioFile.initTag()
    
                            audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                            audioFile.tag.title = trackName
                                
                            audioFile.tag.album = trackAlbum
                                
                            audioFile.tag.track_num = trackNumber
                                
                            audioFile.tag.artist = artistName
    
                            audioFile.tag.recording_date = Date(albumRelease['year'])
    
                            audioFile.tag.save()
    
                            os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                            print("Metadata Applied!\n\n")

                end_time = time.monotonic()

                print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

                await session.close()

            if cont == "2":

                await session.close()

                return

        if downloadOption == "2":

            artistAlbums = artistData['album_group']

            albumList = []

            albumURIList = []

            for album in artistAlbums:

                albumList += album['album']

            for i in range(len(albumList)):

                GID = albumList[i]['gid']

                async with session.get(f"https://music.joshuadoes.com/util/gid2id/?gid={GID}") as albumData:

                    albumID = await albumData.json()

                    albumURIList.append(albumID['id'])

            start_time = time.monotonic()

            print(f"Loading {len(albumURIList)} albums...\n")

            for index, i in enumerate(albumURIList):

                async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{i}?pass=pleasesparemyendpoints&quality=2") as albumsJSON:

                    albumsData = await albumsJSON.json()

                    print(f"\nResult number: {index+1}")

                    albumName = albumsData['name']

                    albumRelease = albumsData['date']

                    print(f"Album Name: {albumName}")

                    print(f"Album Release: {albumRelease['year']}\n")
            
            chosenAlbum = input(f"Select an album (1-{len(albumURIList)})\n\n"
                                 "Type 'RETURN' to return to main menu\n: "
                                )

            validChoice = list(range(1, len(albumURIList)+1))
                               
            while chosenAlbum != "RETURN" and not any(x in chosenAlbum for x in str(validChoice)):

                print("Invalid option!")

                chosenAlbum = input(f"Select an album (1-{len(albumURIList)})\n\n"
                                     "Type 'RETURN' to return to main menu\n: "
                                    )

            if chosenAlbum == "RETURN":

                await session.close()

                return

            selectedAlbum = albumURIList[int(chosenAlbum)-1]

            async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{selectedAlbum}?pass=pleasesparemyendpoints&quality=2") as albumData:

                album = await albumData.json()

                if len(album) == 0:

                    print("Wrong URL input!\n"
                          "Returning to main menu...\n"
                          )

                    await session.close()

                    return

                allTracks = album['disc']

                trackList = []
            
                trackURIS = []

                for i in allTracks:

                    trackList += (i['track'])

                for i in range(len(trackList)):

                    GID = trackList[i]['gid']

                    async with session.get(f"https://music.joshuadoes.com/util/gid2id/?gid={GID}") as trackData:

                        trackID = await trackData.json()

                        trackURIS.append(trackID['id'])

            print(f"Loading {len(trackURIS)} songs...\n")

            cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

            while not any(x in cont for x in ["1", "2"]):

                print("Invalid option!")

                cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

            if cont == "1":

                if hasattr(sys, 'getandroidapilevel'):

                    print("[*] Android OS detected. Songs will be downloaded to storage/emulated/0/Downloads/Music folder.\n"))

                    download_location = "storage/downloads"

                start_time = time.monotonic()

                for i in trackURIS:

                    #fix aiohttp server disconnected by adding a retry on failure

                    async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2") as trackJSON:

                        trackData = await trackJSON.json()
                    
                        trackName = trackData['name']

                        trackAlbum = trackData['album']['name']

                        trackNumber = trackData['number']

                        artistName = trackData['album']['artist'][0]['name']

                        albumRelease = trackData['album']['date']

                        print(f"Track Name: {trackName}")

                        print(f"Album Name: {trackAlbum}")

                        print(f"Artist Name: {artistName}")

                        print(f"Album Release: {albumRelease['year']}\n")

                        fileName = re.sub('\$', 'S', trackName)

                        fileName = re.sub('[\/:*?"<>|]', '', fileName)

                        if not os.path.exists(f"{download_location}/Music"):

                            os.makedirs(f"{download_location}/Music")
                            
                        if os.path.isfile(f"{download_location}/Music/{fileName}.mp3"):

                            print("Song already downloaded to this directory. Skipping...\n")

                        else:
            
                            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
                
                            async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:
    
                                embed = await embedData.json()
    
                                coverArt = embed['thumbnail_url']
    
                            async with session.get(coverArt) as img:
    
                                imgData = await img.read()
    
                            try:
    
                                audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
    
                            except OSError:
    
                                os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                                os.remove(f"{download_location}/Music/{fileName}.mp3")
    
                                print("\nSong does not contain download formats.")
    
                                print("Attempting to grab link with formats...")
    
                                print(f"\nTrack Name: {trackName}")
    
                                print(f"Album Name: {trackAlbum}")
    
                                print(f"Artist Name: {artistName}")
    
                                print(f"Album Release: {albumRelease['year']}\n")
    
                                download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/bestmatch:{artistName} {trackName}?pass=pleasesparemyendpoints&quality=2" -c copy "{download_location}/Music/{fileName}.ogg" -v quiet')    
    
                                convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "{download_location}/Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "{download_location}/Music/{fileName}.mp3" -v quiet')
    
                                audioFile = eyed3.load(f"{download_location}/Music/{fileName}.mp3")
                        
                            print("Song Downloaded!")
    
                            if (audioFile.tag == None):
    
                                audioFile.initTag()
    
                            audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')
    
                            audioFile.tag.title = trackName
                                
                            audioFile.tag.album = trackAlbum
                                
                            audioFile.tag.track_num = trackNumber
                                
                            audioFile.tag.artist = artistName
    
                            audioFile.tag.recording_date = Date(albumRelease['year'])
    
                            audioFile.tag.save()
    
                            os.remove(f"{download_location}/Music/{fileName}.ogg")
    
                            print("Metadata Applied!\n\n")
        
                end_time = time.monotonic()

                print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

                await session.close()

            if cont == "2":

                await session.close()

                return


async def changeBitrate():

    global bitrate

    option = input("""
Select new bitrate for download:
1 - 96kbps
2 - 128kbps
3 - 192kbps
4 - 320kbps (Highest Spotify Bitrate)
5 - Custom

Type 'RETURN' to return to main menu
: """
                    )


    while not any(x in option for x in ["1", "2", "3", "4", "5", "RETURN"]):

        print("Invalid option!")

        option = input("""
Select new bitrate for download:
1 - 96kbps
2 - 128kbps
3 - 192kbps
4 - 320kbps (Highest Spotify Bitrate)
5 - Custom

Type 'RETURN' to return to main menu
: """
                        )

    if option == "RETURN":

        return

    if option == "1":

        bitrate = "96"

    if option == "2":

        bitrate = "128"

    if option == "3":

        bitrate = "192"

    if option == "4":

        bitrate = "320"

    if option == "5":

        bitrate = input("Input new bitrate (320kbps maximum)\n: ")

        while not bitrate.isdigit():

            print("Invalid value!")

            bitrate = input("Input new bitrate (320kbps maximum)\n: ")


async def changeDownloadLocation():

    global download_location

    new_download_location = input(f"Current download location: {download_location}\n\n"
                                   "Enter new download location\n"
                                   "Type 'RESET' to reset\n\n"
                                   "Type 'RETURN' to return to main menu\n: "
                                  )

    if new_download_location == "RETURN":

        return

    if new_download_location == "RESET":

        download_location = os.getcwd()

    else:

        download_location = new_download_location


if __name__ == "__main__":

    asyncio.run(main())

