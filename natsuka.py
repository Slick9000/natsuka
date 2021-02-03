import os
import aiohttp
import asyncio
import calendar

print("""
Welcome to the Natsuka downloader!
This is where you are able to download high quality audio from Spotify.

Thanks to JoshuaDoes for making this possible."""
      )

option = input("""
What would you like to do today?

Option 1 - Download a single track
Option 2 - Download Album
Option 3 - Search for track/album

:"""
               )

if option == "1":
    
    UID = input("""
Enter the track's URI

:"""
          )

    UID = UID.replace("spotify:track:", "")
    
            
    async def main():

        async with aiohttp.ClientSession() as session:

            async with session.get(f"http://joshuadoes.com:8080/track/{UID}?pass=hFUhqM9n") as resp:

                    trackData = await resp.json()

                    # print(trackData)

                    trackName = trackData['name']

                    trackAlbum = trackData['album']['name']

                    artistName = trackData['album']['artist'][0]['name']

                    albumRelease = trackData['album']['date']

                    print(f"Track Name: {trackName}")

                    print(f"Album Name: {trackAlbum}")

                    print(f"Artist Name: {artistName}")

                    print(f"Album Release: {calendar.month_name[albumRelease['month']]} {albumRelease['day']}th, {albumRelease['year']}")

        async with session.get(f"http://joshuadoes.com:8080/download/{UID}?pass=hFUhqM9n") as resp:

            trackAudio =  await resp.content.read()

            print(trackAudio)

                    
    loop = asyncio.get_event_loop()
    
    loop.run_until_complete(main())
    
    # os.system(f"curl http://joshuadoes.com:8080/download/{trackID}?pass=hFUhqM9n --output file.ogg")

if option == "2":

    pass

else:
    pass
