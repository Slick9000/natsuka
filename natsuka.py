#!/usr/bin/env python3

import aiohttp
import asyncio
import calendar
import re
import mutagen


print("natsuka - wip spotify downloader\n"
      "Thanks to JoshuaDoes for making this possible.\n"
     )

option = input("""
What would you like to do today?

Option 1 - Download a single track
Option 2 - Download Album          (Doesn't currently work)
Option 3 - Download Playlist       (Doesn't currently work)

: """
              )

while not any(x in option for x in ["1", "2", "3"]):

    print("Invalid option!")

    option = input("""
What would you like to do today?

Option 1 - Download a single track
Option 2 - Download Album          (Doesn't currently work)
Option 3 - Download Playlist       (Doesn't currently work)

: """
               )

if option == "1":
    
    UID = input("Enter the track's URL\n:")

    while len(re.findall(r'(https?://[^\s]+)', UID)) == 0:

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
    
    async def main():

        async with aiohttp.ClientSession() as session:

            async with session.get(f"https://music.joshuadoes.com/track/spotify:track:{UID}?pass=pleasesparemyendpoints&stream&quality=2") as resp:

                    trackData = await resp.json()
                    
                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    trackNumber = trackData['number']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    comment = f"{trackData['album']['label']}."

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}, {albumRelease['year']}")

            async with session.get(f"https://music.joshuadoes.com/v1/stream/spotify:track:{UID}?pass=pleasesparemyendpoints&stream&quality=2") as resp:

                    fileName = re.sub('[\/:*?"<>|]', '', trackName)

                    with open(f"{fileName}.ogg", "wb") as fd:

                        while True:

                            chunk = await resp.content.read()

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

                            meta['comment'] = comment

                            meta['year'] = str(albumRelease['year'])

                            try:

                                meta.save()

                            #due to a bug in mutagen, an error always occurs here
                            #although the data writes file. mutagen pls fix
                            except:

                                print("Metadata Applied!")
    
if option == "2":

    pass

if option == "3":

    pass

if __name__ == "__main__":

    asyncio.run(main())
