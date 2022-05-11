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
Option 3 - Download Album              (Doesn't currently work)
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Exit

: """
               )

    while not any(x in option for x in ["1", "2", "3", "4", "5"]):

        print("Invalid option!")

        option = input("""
What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album              (Doesn't currently work)
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Exit

: """
               )

    if option == "1":

        await singleTrackProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "2":

        await multiTrackProcess()

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        exit()

    if option == "3":

        print("Currently unimplemented.\n")

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "4":

        print("Currently unimplemented.\n")

        try:
        
            input("Press enter to continue.\n")
        
        except SyntaxError:
        
            pass
        
        await main()

    if option == "5":

        exit()

    
async def singleTrackProcess():

    UID = input("Enter the track's URL\n: ")

    while len(re.findall(r'(https?://[^\s]+)', UID)) == 0:

        print("Invalid URL!")

        UID = input("Enter the track's URL\n: ")

    query = "?"
    
    if query in UID:
        
        UID = UID.split(query)

        group = UID[0].split("/")

        UID = group[len(group) - 1]
        
    else:

        group = UID.split("/")

        UID = group[len(group) - 1]


    async with aiohttp.ClientSession() as session:

        async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{UID}?pass=pleasesparemyendpoints&stream&quality=2") as trackJSON:

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

        async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{UID}?pass=pleasesparemyendpoints&stream&quality=2") as audioData:

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


async def multiTrackProcess():

    songList = []

    UID = ""

    while UID != "START":

        UID = input(f"Enter songs (Current number of songs: {len(songList)})\n"
                    "Type 'START' to begin download.\n: "
                    )

        while len(re.findall(r'(https?://[^\s]+)', UID)) == 0 and UID != "START":

            print("Invalid URL!")

            UID = input("Enter the track's URL\n:")

        query = "?"
    
        if query in UID:
        
            UID = UID.split(query)

            group = UID[0].split("/")

            UID = group[len(group) - 1]
        
        else:

            group = UID.split("/")

            UID = group[len(group) - 1]

        if UID != "START":

            songList.append(UID)

    start_time = time.monotonic()

    print(f"Loading {len(songList)} songs...\n")

    for i in songList:

        async with aiohttp.ClientSession() as session:

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



if __name__ == "__main__":

    asyncio.run(main())
    
