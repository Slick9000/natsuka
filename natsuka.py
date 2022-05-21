#!/usr/bin/env python3

import asyncio
import calendar
from datetime import timedelta
import os
import re
import sys
import time

#this allows the natsuka executable to use ffmpeg embedded in it
#for other users not using this exe, you will need to install ffmpeg yourself
if getattr(sys, 'frozen', False):
    
    #temporary folder for pyinstaller
    basedir = f"{sys._MEIPASS}/"
    
else:

    #just don't use it, and use ffmpeg from PATH
    basedir = ""



bitrate = "320"

python = 'python3'

if 'win' in sys.platform:
    
    python = 'python'

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
            print(f'[!] Error installing "{module}" module. Do you have pip installed?')
            
            input(f'[!] Playlist generation failed. Press Ctrl+C to exit...')
            
            sys.exit()


async def main():
    
    print("natsuka - spotify downloader\n"
          "Thanks to JoshuaDoes for making this possible."
          )

    option = input(f"""
What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: {bitrate}kbps)
Option 8 - Exit

: """
               )

    while not any(x in option for x in ["1", "2", "3", "4", "5", "6", "7", "8"]) or not int:

        print("Invalid option!")

        option = input(f"""
What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: {bitrate}kbps)
Option 8 - Exit

: """
               )

    if option == "1":

        await singleTrackProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "2":

        await multiTrackProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "3":

        await albumProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "4":

        await playlistProcess()

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

        sys.exit()

    
async def singleTrackProcess():

    URI = input("Enter the track's URL\n\n"
                "Type 'RETURN' to return to main menu\n: "
                )

    while len(re.findall(r'(https?://[^\s]+)', URI)) == 0 and URI != "RETURN":

        print("Invalid URL!\n")

        URI = input("Enter the track's URL\n\n"
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

    async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{URI}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

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

            print(f"\nTrack Name: {trackName}")

            print(f"Album Name: {trackAlbum}")

            print(f"Artist Name: {artistName}")

            print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

            fileName = re.sub('[\/:*?"<>|]', '', trackName)

            if not os.path.exists("Music"):

                os.makedirs("Music")
            
            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{URI}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

            print("Song Downloaded!")
            
            async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{URI}") as embedData:

                embed = await embedData.json()

                coverArt = embed['thumbnail_url']

                async with session.get(coverArt) as img:

                    imgData = await img.read()

                audioFile = eyed3.load(f"Music/{fileName}.mp3")

                if (audioFile.tag == None):

                    audioFile.initTag()

                audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                audioFile.tag.title = trackName
                            
                audioFile.tag.album = trackAlbum
                            
                audioFile.tag.track_num = trackNumber
                            
                audioFile.tag.artist = artistName

                audioFile.tag.recording_date = Date(albumRelease['year'])

                audioFile.tag.save()

                os.remove(f"Music/{fileName}.ogg")

                print("Metadata Applied!\n\n")

    await session.close()


async def multiTrackProcess():

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

    start_time = time.monotonic()

    print(f"Loading {len(songList)} songs...\n")

    session = aiohttp.ClientSession()

    for i in songList:

        async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

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

                print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

                fileName = re.sub('[\/:*?"<>|]', '', trackName)

                if not os.path.exists("Music"):

                    os.makedirs("Music")
            
                download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

                convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

                print("Song Downloaded!")
            
                async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                    embed = await embedData.json()

                    coverArt = embed['thumbnail_url']

                    async with session.get(coverArt) as img:

                        imgData = await img.read()

                    audioFile = eyed3.load(f"Music/{fileName}.mp3")

                    if (audioFile.tag == None):

                        audioFile.initTag()

                    audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                    audioFile.tag.title = trackName
                            
                    audioFile.tag.album = trackAlbum
                            
                    audioFile.tag.track_num = trackNumber
                            
                    audioFile.tag.artist = artistName

                    audioFile.tag.recording_date = Date(albumRelease['year'])

                    audioFile.tag.save()

                    os.remove(f"Music/{fileName}.ogg")

                    print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def albumProcess():

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

    async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{URI}?pass=pleasesparemyendpoints&stream&quality=2") as albumData:

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

    start_time = time.monotonic()

    print(f"Loading {len(trackURIS)} songs...\n")

    for i in trackURIS:

            async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

                    trackData = await trackJSON.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

                    fileName = re.sub('[\/:*?"<>|]', '', trackName)

                    if not os.path.exists("Music"):

                        os.makedirs("Music")
            
                    download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

                    convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

                    print("Song Downloaded!")
            
                    async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                        embed = await embedData.json()

                        coverArt = embed['thumbnail_url']

                    async with session.get(coverArt) as img:

                        imgData = await img.read()

                    audioFile = eyed3.load(f"Music/{fileName}.mp3")

                    if (audioFile.tag == None):

                        audioFile.initTag()

                    audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                    audioFile.tag.title = trackName
                            
                    audioFile.tag.album = trackAlbum
                            
                    audioFile.tag.track_num = trackNumber
                            
                    audioFile.tag.artist = artistName

                    audioFile.tag.recording_date = Date(albumRelease['year'])

                    audioFile.tag.save()

                    os.remove(f"Music/{fileName}.ogg")

                    print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def playlistProcess():

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

    async with session.get(f"https://music.joshuadoes.com/playlist/spotify:user:{userID}:playlist:{playlistID}?pass=pleasesparemyendpoints&stream&quality=2") as playlistData:

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

    start_time = time.monotonic()

    print(f"Loading {len(playlistURIS)} songs...\n")

    for i in playlistURIS:

            async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

                    trackData = await trackJSON.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

                    fileName = re.sub('[\/:*?"<>|]', '', trackName)

                    if not os.path.exists("Music"):

                        os.makedirs("Music")
            
                    download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

                    convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

                    print("Song Downloaded!")
            
                    async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                        embed = await embedData.json()

                        coverArt = embed['thumbnail_url']

                    async with session.get(coverArt) as img:

                        imgData = await img.read()

                    audioFile = eyed3.load(f"Music/{fileName}.mp3")

                    if (audioFile.tag == None):

                        audioFile.initTag()

                    audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                    audioFile.tag.title = trackName
                            
                    audioFile.tag.album = trackAlbum
                            
                    audioFile.tag.track_num = trackNumber
                            
                    audioFile.tag.artist = artistName

                    audioFile.tag.recording_date = Date(albumRelease['year'])

                    audioFile.tag.save()

                    os.remove(f"Music/{fileName}.ogg")

                    print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def songSearch():

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

    try:

        selectedSong = songURIList[int(chosenSong)-1].split(":")[2]

    except IndexError:

            print("Song out of range! (No Result for selection)")

            await session.close()

            return

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

        async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{selectedSong}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

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

            print(f"\nTrack Name: {trackName}")

            print(f"Album Name: {trackAlbum}")

            print(f"Artist Name: {artistName}")

            print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

            fileName = re.sub('[\/:*?"<>|]', '', trackName)

            if not os.path.exists("Music"):

                os.makedirs("Music")
            
            download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{selectedSong}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

            convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

            print("Song Downloaded!")
            
            async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{selectedSong}") as embedData:

                embed = await embedData.json()

                coverArt = embed['thumbnail_url']

            async with session.get(coverArt) as img:

                imgData = await img.read()

            audioFile = eyed3.load(f"Music/{fileName}.mp3")

            if (audioFile.tag == None):

                audioFile.initTag()

            audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

            audioFile.tag.title = trackName
                            
            audioFile.tag.album = trackAlbum
                            
            audioFile.tag.track_num = trackNumber
                            
            audioFile.tag.artist = artistName

            audioFile.tag.recording_date = Date(albumRelease['year'])

            audioFile.tag.save()

            os.remove(f"Music/{fileName}.ogg")

            print("Metadata Applied!\n\n")

        await session.close()

    if downloadOption == "2":

        try:

            selectedAlbum = albumURIList[int(chosenSong)-1].split(":")[2]

        except IndexError:

            print("Album out of range! (No Result for selection)")

            await session.close()

            return
        
        async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{selectedAlbum}?pass=pleasesparemyendpoints&stream&quality=2") as albumData:

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


        start_time = time.monotonic()

        print(f"Loading {len(trackURIS)} songs...\n")

        cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

        while not any(x in downloadOption for x in ["1", "2"]):

            print("Invalid option!")

            cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

    
        if cont == "1":

            for i in trackURIS:

                async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

                    trackData = await trackJSON.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}\n")

                    fileName = re.sub('[\/:*?"<>|]', '', trackName)

                    if not os.path.exists("Music"):

                        os.makedirs("Music")
            
                    download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

                    convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

                    print("Song Downloaded!")
            
                    async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                        embed = await embedData.json()

                        coverArt = embed['thumbnail_url']

                    async with session.get(coverArt) as img:

                        imgData = await img.read()

                    audioFile = eyed3.load(f"Music/{fileName}.mp3")

                    if (audioFile.tag == None):

                        audioFile.initTag()

                    audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                    audioFile.tag.title = trackName
                            
                    audioFile.tag.album = trackAlbum
                            
                    audioFile.tag.track_num = trackNumber
                            
                    audioFile.tag.artist = artistName

                    audioFile.tag.recording_date = Date(albumRelease['year'])

                    audioFile.tag.save()

                    os.remove(f"Music/{fileName}.ogg")

                    print("Metadata Applied!\n\n")

            end_time = time.monotonic()

            print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

            await session.close()

        if cont == "2":

            await session.close()

            return


async def artistSearch():

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

        try:

            selectedArtist = artistURIList[int(chosenArtist)-1].split(":")[2]

        except IndexError:

            print("Artist out of range! (No Result for selection)")

            await session.close()

            return

        async with session.get(f"https://music.joshuadoes.com/artist/{selectedArtist}?pass=pleasesparemyendpoints&stream&quality=2") as artistJSON:

            artistData = await artistJSON.json()

            #LATER PARSE THE RESPONSE DATA, TO BE ABLE TO DISPLAY THE ARTIST'S TOP SONGS (1)
            #AS WELL AS ALL OF THE ARTIST'S ALBUMS (2)
            #THEN USE THE CODE FROM THE MULTITRACK DOWNLOAD TO MAKE THE DOWNLOAD TOP SONGS OPTION (3)
            #AND THEN USE THE CODE FROM THE ALBUM DOWNLOAD TO DOWNLOAD THE ALBUM SELECTED FROM THE LIST

        

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

            print(f"Loading {len(trackURIS)} songs...\n")

            cont = input(f"""
Would you like to proceed downloading {artists[int(chosenArtist)-1]['object']['name']}'s top songs?
1 - Yes
2 - No
: """
                             )

            while not any(x in downloadOption for x in ["1", "2"]):

                print("Invalid option!")

                cont = input(f"""
Would you like to proceed downloading {artistName}'s top songs?
1 - Yes
2 - No
: """
                             )

            if cont == "1":

                start_time = time.monotonic()

                for i in trackURIS:

                    async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

                        trackData = await trackJSON.json()
                    
                        trackName = trackData['name']

                        trackAlbum = trackData['album']['name']

                        trackNumber = trackData['number']

                        artistName = trackData['album']['artist'][0]['name']

                        albumRelease = trackData['album']['date']

                        print(f"Track Name: {trackName}")

                        print(f"Album Name: {trackAlbum}")

                        print(f"Artist Name: {artistName}")

                        print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}\n")

                        fileName = re.sub('[\/:*?"<>|]', '', trackName)

                        if not os.path.exists("Music"):

                            os.makedirs("Music")
            
                        download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

                        convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

                        print("Song Downloaded!")
            
                        async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                            embed = await embedData.json()

                            coverArt = embed['thumbnail_url']

                        async with session.get(coverArt) as img:

                            imgData = await img.read()

                        audioFile = eyed3.load(f"Music/{fileName}.mp3")

                        if (audioFile.tag == None):

                            audioFile.initTag()

                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                        audioFile.tag.title = trackName
                            
                        audioFile.tag.album = trackAlbum
                            
                        audioFile.tag.track_num = trackNumber
                            
                        audioFile.tag.artist = artistName

                        audioFile.tag.recording_date = Date(albumRelease['year'])

                        audioFile.tag.save()

                        os.remove(f"Music/{fileName}.ogg")

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

                async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{i}?pass=pleasesparemyendpoints&stream&quality=2") as albumsJSON:

                    albumsData = await albumsJSON.json()

                    print(f"\nResult number: {index+1}")

                    albumName = albumsData['name']

                    albumRelease = albumsData['date']

                    print(f"Album Name: {albumName}")

                    print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}\n")
            
            chosenAlbum = input(f"Select an album (1-{len(albumURIList)})\n\n"
                                 "Type 'RETURN' to return to main menu\n: "
                                )

            validChoice = list(range(1, len(albumURIList)+1))
                               
            while chosenAlbum != "RETURN" and not int(chosenAlbum) in validChoice:

                print("Invalid option!")

                chosenAlbum = input(f"Select an album (1-{len(albumURIList)})\n\n"
                                     "Type 'RETURN' to return to main menu\n: "
                                    )

            if chosenAlbum == "RETURN":

                await session.close()

                return

            try:

                selectedAlbum = albumURIList[int(chosenAlbum)-1]

            except IndexError:

                print("Album out of range! (No Result for selection)")

                await session.close()

                return

            async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{selectedAlbum}?pass=pleasesparemyendpoints&stream&quality=2") as albumData:

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

            start_time = time.monotonic()

            print(f"Loading {len(trackURIS)} songs...\n")

            cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

            while not any(x in downloadOption for x in ["1", "2"]):

                print("Invalid option!")

                cont = input(f"""
Would you like to proceed downloading this album?
1 - Yes
2 - No
: """
                             )

            if cont == "1":

                for i in trackURIS:

                    async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

                        trackData = await trackJSON.json()
                    
                        trackName = trackData['name']

                        trackAlbum = trackData['album']['name']

                        trackNumber = trackData['number']

                        artistName = trackData['album']['artist'][0]['name']

                        albumRelease = trackData['album']['date']

                        print(f"Track Name: {trackName}")

                        print(f"Album Name: {trackAlbum}")

                        print(f"Artist Name: {artistName}")

                        print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

                        fileName = re.sub('[\/:*?"<>|]', '', trackName)

                        if not os.path.exists("Music"):

                            os.makedirs("Music")
            
                        download = os.system(f'{basedir}ffmpeg -i "https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2" -c copy "Music/{fileName}.ogg" -v quiet')    

                        convert_to_mp3 = os.system(f'{basedir}ffmpeg -i "Music/{fileName}.ogg" -f mp3 -b:a {bitrate}k "Music/{fileName}.mp3" -v quiet')

                        print("Song Downloaded!")
            
                        async with session.get(f"https://open.spotify.com/oembed?url=spotify:track:{i}") as embedData:

                            embed = await embedData.json()

                            coverArt = embed['thumbnail_url']

                        async with session.get(coverArt) as img:

                            imgData = await img.read()

                        audioFile = eyed3.load(f"Music/{fileName}.mp3")

                        if (audioFile.tag == None):

                            audioFile.initTag()

                        audioFile.tag.images.set(ImageFrame.FRONT_COVER, imgData, 'image/jpeg')

                        audioFile.tag.title = trackName
                            
                        audioFile.tag.album = trackAlbum
                            
                        audioFile.tag.track_num = trackNumber
                            
                        audioFile.tag.artist = artistName

                        audioFile.tag.recording_date = Date(albumRelease['year'])

                        audioFile.tag.save()

                        os.remove(f"Music/{fileName}.ogg")

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


if __name__ == "__main__":

    asyncio.run(main())
