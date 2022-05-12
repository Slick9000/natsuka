#!/usr/bin/env python3

import aiohttp
import asyncio
import calendar
from datetime import timedelta
import mutagen
import re
import time


async def main():
    print("natsuka - wip spotify downloader\n"
          "Thanks to JoshuaDoes for making this possible."
          )

    option = input("""
What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
Option 6 - Exit

: """
               )

    while not any(x in option for x in ["1", "2", "3", "4", "5", "6"]) or not int:

        print("Invalid option!")

        option = input("""
What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
Option 6 - Exit

: """
               )

    if option == "1":

        await singleTrackProcess()

        try:
        
            input("Press enter to exit.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "2":

        await multiTrackProcess()

        try:
        
            input("Press enter to exit.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "3":

        await albumProcess()

        try:
        
            input("Press enter to exit.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "4":

        print("Currently unimplemented.\n")

        try:
        
            input("Press enter to exit.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "5":

        await songSearch()

        try:
        
            input("Press enter to exit.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "6":

        exit()

    
async def singleTrackProcess():

    URI = input("Enter the track's URL\n: ")

    while len(re.findall(r'(https?://[^\s]+)', URI)) == 0:

        print("Invalid URL!")

        URI = input("Enter the track's URL\n: ")

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
                    
            trackName = trackData['name']

            trackAlbum = trackData['album']['name']

            trackNumber = trackData['number']

            artistName = trackData['album']['artist'][0]['name']

            albumRelease = trackData['album']['date']

            print(f"\nTrack Name: {trackName}")

            print(f"Album Name: {trackAlbum}")

            print(f"Artist Name: {artistName}")

            print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

    async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{URI}?pass=pleasesparemyendpoints&stream&quality=2") as audioData:

            fileName = re.sub('[\/:*?"<>|]', '', trackName)

            with open(f"{fileName}.ogg", "wb") as fd:

                while True:

                    chunk = await audioData.content.read()

                    if not chunk:

                        break

                    fd.write(chunk)

                    print("Song Downloaded!")

                    meta = mutagen.File(fd.name)

                    if meta.tags is None:

                        meta.tags = mutagen.id3.ID3()

                    meta['title'] = trackName
                            
                    meta['album'] = trackAlbum
                            
                    meta['tracknumber'] = str(trackNumber)
                            
                    meta['artist'] = artistName

                    meta['year'] = str(albumRelease['year'])

                    try:

                        meta.save()

                        meta.close()

                    #due to a bug in mutagen, an error always occurs here
                    #although the data writes to the file just fine. mutagen pls fix
                    except:

                        print("Metadata Applied!\n\n")

    await session.close()


async def multiTrackProcess():

    songList = []

    URI = ""

    while URI != "START":

        URI = input(f"Enter songs (Current number of songs: {len(songList)})\n"
                    "Type 'START' to begin download.\n: "
                    )

        while len(re.findall(r'(https?://[^\s]+)', URI)) == 0 and URI != "START":

            print("Invalid URL!")

            URI = input("Enter the track's URL\n:")

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

    for i in songList:

        session = aiohttp.ClientSession()

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

        async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as audioData:

                fileName = re.sub('[\/:*?"<>|]', '', trackName)

                with open(f"{fileName}.ogg", "wb") as fd:

                    while True:

                        chunk = await audioData.content.read()

                        if not chunk:

                            break

                        fd.write(chunk)

                        print("Song Downloaded!")

                        meta = mutagen.File(fd.name)

                        if meta.tags is None:

                            meta.tags = mutagen.id3.ID3()

                        meta['title'] = trackName
                            
                        meta['album'] = trackAlbum
                            
                        meta['tracknumber'] = str(trackNumber)
                            
                        meta['artist'] = artistName

                        meta['year'] = str(albumRelease['year'])
    
                        try:

                            meta.save()

                            meta.close()

                        #due to a bug in mutagen, an error always occurs here
                        #although the data writes to the file just fine. mutagen pls fix
                        except:

                            print("Metadata Applied!\n\n")

                            await session.close()
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")


async def albumProcess():

    URI = input("Enter the album's URL\n: ")

    while len(re.findall(r'(https?://[^\s]+)', URI)) == 0:

        print("Invalid URL!")

        URI = input("Enter the albums's URL\n: ")

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

            async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as audioData:

                    fileName = re.sub('[\/:*?"<>|]', '', trackName)

                    with open(f"{fileName}.ogg", "wb") as fd:

                        while True:

                            chunk = await audioData.content.read()

                            if not chunk:

                                break

                            fd.write(chunk)

                            print("Song Downloaded!")

                            meta = mutagen.File(fd.name)

                            if meta.tags is None:

                                meta.tags = mutagen.id3.ID3()

                            meta['title'] = trackName
                            
                            meta['album'] = trackAlbum
                            
                            meta['tracknumber'] = str(trackNumber)
                            
                            meta['artist'] = artistName

                            meta['year'] = str(albumRelease['year'])
    
                            try:

                                meta.save()

                                meta.close()

                            #due to a bug in mutagen, an error always occurs here
                            #although the data writes to the file just fine. mutagen pls fix
                            except:

                                print("Metadata Applied!\n\n")
        
    end_time = time.monotonic()

    print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

    await session.close()


async def songSearch():

    query = input("Input song name\n: ")

    while query == "":

        print("Search is empty!")

        query = input("Input song name\n: ")

    session = aiohttp.ClientSession()

    async with session.get(f"https://music.joshuadoes.com/v1/search:{query}") as resp:

        results = await resp.json()

        searchData = results['object']['streams']

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

            print(f"Result number: {index+1}")

            print(f"Song: {songName}")

            print(f"Song creator: {songCreator}")

            print(f"Song Album: {songAlbum}")

            print(f"Song Album URI: {songAlbumURI}\n")


    chosenSong = input("Select a song (1-5)\n: ")

    while not any(x in chosenSong for x in ["1", "2", "3", "4", "5"]):

        print("Invalid option!")

        chosenSong = input("Select a song (1-5)\n: ")

    downloadOption = input("""
Option 1 - Download Song
Option 2 - Download Song's Album
"""
                           )

    while not any(x in downloadOption for x in ["1", "2"]):

        print("Invalid option!")

        downloadOption = input("""
Option 1 - Download Song
Option 2 - Download Song's Album
"""
                           )

    if downloadOption == "1":

        selectedSong = songURIList[int(chosenSong)-1].split(":")[2]

        async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{selectedSong}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

            trackData = await trackJSON.json()
                    
            trackName = trackData['name']

            trackAlbum = trackData['album']['name']

            trackNumber = trackData['number']

            artistName = trackData['album']['artist'][0]['name']

            albumRelease = trackData['album']['date']

            print(f"\nTrack Name: {trackName}")

            print(f"Album Name: {trackAlbum}")

            print(f"Artist Name: {artistName}")

            print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

        async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{selectedSong}?pass=pleasesparemyendpoints&stream&quality=2") as audioData:
            
            fileName = re.sub('[\/:*?"<>|]', '', trackName)

            with open(f"{fileName}.ogg", "wb") as fd:

                while True:

                    chunk = await audioData.content.read()

                    if not chunk:

                        break

                    fd.write(chunk)

                    print("Song Downloaded!")

                    meta = mutagen.File(fd.name)

                    if meta.tags is None:

                        meta.tags = mutagen.id3.ID3()

                    meta['title'] = trackName
                            
                    meta['album'] = trackAlbum
                            
                    meta['tracknumber'] = str(trackNumber)
                            
                    meta['artist'] = artistName

                    meta['year'] = str(albumRelease['year'])

                    try:

                        meta.save()

                        meta.close()

                    #due to a bug in mutagen, an error always occurs here
                    #although the data writes to the file just fine. mutagen pls fix
                    except:

                        print("Metadata Applied!\n\n")

                        await session.close()

    if downloadOption == "2":

        selectedAlbum = albumURIList[int(chosenSong)-1].split(":")[2]
        
        async with session.get(f"https://music.joshuadoes.com/album/spotify:album:{selectedAlbum}?pass=pleasesparemyendpoints&stream&quality=2") as albumData:

            album = await albumData.json()

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

            async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{i}?pass=pleasesparemyendpoints&stream&quality=2") as audioData:

                    fileName = re.sub('[\/:*?"<>|]', '', trackName)

                    with open(f"{fileName}.ogg", "wb") as fd:

                        while True:

                            chunk = await audioData.content.read()

                            if not chunk:

                                break

                            fd.write(chunk)

                            print("Song Downloaded!")

                            meta = mutagen.File(fd.name)

                            if meta.tags is None:

                                meta.tags = mutagen.id3.ID3()

                            meta['title'] = trackName
                            
                            meta['album'] = trackAlbum
                            
                            meta['tracknumber'] = str(trackNumber)
                            
                            meta['artist'] = artistName

                            meta['year'] = str(albumRelease['year'])
    
                            try:

                                meta.save()

                                meta.close()

                            #due to a bug in mutagen, an error always occurs here
                            #although the data writes to the file just fine. mutagen pls fix
                            except:

                                print("Metadata Applied!\n\n")
        
        end_time = time.monotonic()

        print(f"Download time: {timedelta(seconds=end_time - start_time)}\n")

        await session.close()


if __name__ == "__main__":

    asyncio.run(main())
