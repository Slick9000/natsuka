
# natsuka
a single file application giving you the ability to download music from spotify with id3 metadata (track title, track number, artist, album, release date)

initally made on **february 28th, 2021**, natsuka was made to download songs from spotify with metadata, a task other downloaders were not able to accomplish for me. on it's original creation, i was not very good at python. 

since then, i have drastically improved, and in about 2 days i was able to fully accomplish this task. welcome to natsuka 2.0, with **single-track, multi-track, album, playlist, and search query downloading.**

## credits
JoshuaDoes (for the API endpoint)

Skylar Bleed (for helping with several initial changes)

## [download](https://github.com/Slick9000/natsuka/releases/latest)

## requirements
[python 3.x](https://www.python.org/downloads/)

[aiohttp](https://pypi.org/project/aiohttp/)

[mutagen](https://pypi.org/project/mutagen/)

## features:
**1: single song download support**
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 1
Enter the track's URL
: https://open.spotify.com/track/6O9PAqJLef4tyQNadjb40u?si=149102c06360475c
Track Name: De roses et de colombes
Album Name: How Are You
Artist Name: Mounika.
Album Release: June 24, 2017
Song Downloaded!
Metadata Applied!


Press enter to continue.
```

<br/>

**2: multiple song download support**
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 2
Enter songs (Current number of songs: 0
Type 'START' to begin download.
: https://open.spotify.com/track/6O9PAqJLef4tyQNadjb40u?si=149102c06360475c
Enter songs (Current number of songs: 1
Type 'START' to begin download.
: https://open.spotify.com/track/3DYZKxjG8SZrWpVcoUilqQ?si=22dd2605a1834519
Enter songs (Current number of songs: 2
Type 'START' to begin download.
: START
Loading 2 songs...

Track Name: De roses et de colombes
Album Name: How Are You
Artist Name: Mounika.
Album Release: June 24, 2017
Song Downloaded!
Metadata Applied!


Track Name: Cut My Hair
Album Name: How Are You
Artist Name: Mounika.
Album Release: June 24, 2017
Song Downloaded!
Metadata Applied!


Download time: 0:00:10.344000

Press enter to continue.

```

<br/>

**3: album download support** (**NOTE: can download multi disc albums**)
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 3
Enter the album's URL
: https://open.spotify.com/album/5k1geNqLd4yHzyg5L6XF2z?si=i18yaK1cTESTw1zg3uBoqA
Loading 5 songs...

Track Name: HAZARD DUTY PAY!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: February 24, 2022
Song Downloaded!
Metadata Applied!


Track Name: DIKEMBE!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: February 24, 2022
Song Downloaded!
Metadata Applied!


Track Name: GOD DON'T LIKE UGLY!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: February 24, 2022
Song Downloaded!
Metadata Applied!


Track Name: UNTITLED
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: February 24, 2022
Song Downloaded!
Metadata Applied!


Track Name: 100 EMOJI!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: February 24, 2022
Song Downloaded!
Metadata Applied!


Download time: 0:00:25.859000

Press enter to continue.
```

<br/>

**4: playlist download support**
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 4
Input user ID

Type 'RETURN' to return to main menu
: 1xcmyijwkhfsqb1v7pxmb4dlv
Input the playlist's URL
: https://open.spotify.com/playlist/1CMD2NjsEPSVAzrPugTSs8?si=1b6270f97cae490e
Playlist Name: Short Sample Playlist
Description: None
Playlist Length: 3 tracks
Loading 3 songs...

Track Name: Mirror
Album Name: Mr. Morale & The Big Steppers
Artist Name: Kendrick Lamar
Album Release: May 13, 2022
Song Downloaded!
Metadata Applied!


Track Name: Mental [Feat. Saul Williams & Bridget Perez]
Album Name: Melt My Eyez See Your Future
Artist Name: Denzel Curry
Album Release: March 25, 2022
Song Downloaded!
Metadata Applied!


Track Name: Savior
Album Name: Mr. Morale & The Big Steppers
Artist Name: Kendrick Lamar
Album Release: May 13, 2022
Song Downloaded!
Metadata Applied!


Download time: 0:00:20.266000

Press enter to continue.
```

<br/>

**5: downloading song/album by search query**
#### option 1: download song by query
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 5
Input song name
: 16
Result number: 1
Song: 16
Song creator: Highly Suspect
Song Album: MCID

Result number: 2
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue

Result number: 3
Song: Sixteen Tons
Song creator: Tennessee Ernie Ford
Song Album: Vintage Collections

Result number: 4
Song: 16 Lines
Song creator: Lil Peep
Song Album: Come Over When You're Sober, Pt. 2

Result number: 5
Song: Dos Mil 16
Song creator: Bad Bunny
Song Album: Un Verano Sin Ti

Select a song (1-5)
: 2

Option 1 - Download Song
Option 2 - Download Song's Album
1

Track Name: 16
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Press enter to continue.
```

<br/>

#### option 2: download album by query
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 5
Input song name
: 16
Result number: 1
Song: 16
Song creator: Highly Suspect
Song Album: MCID

Result number: 2
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue

Result number: 3
Song: Sixteen Tons
Song creator: Tennessee Ernie Ford
Song Album: Vintage Collections

Result number: 4
Song: 16 Lines
Song creator: Lil Peep
Song Album: Come Over When You're Sober, Pt. 2

Result number: 5
Song: Dos Mil 16
Song creator: Bad Bunny
Song Album: Un Verano Sin Ti

Select a song (1-5)
: 2

Option 1 - Download Song
Option 2 - Download Song's Album
2
Loading 16 songs...

Track Name: trademark usa
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: pink panties
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: scapegoats
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: range brothers (with Kendrick Lamar)
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: issues
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: gorgeous
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: south africa
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: lost souls
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: cocoa (with Don Toliver)
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: family ties (with Kendrick Lamar)
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: scars
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: durag activity (with Travis Scott)
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: booman
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: first order of business
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: vent
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Track Name: 16
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Download time: 0:01:41.765000

Press enter to continue.
```

<br/>

**note: the more specific your search query is, the better the chance of finding the song**
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Exit

: 5
Input song name
: 16 baby keem
Result number: 1
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue

Result number: 2
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue

Select a song (1-5)
: 1

Option 1 - Download Song
Option 2 - Download Song's Album
1

Track Name: 16
Album Name: The Melodic Blue
Artist Name: Baby Keem
Album Release: September 10, 2021
Song Downloaded!
Metadata Applied!


Press enter to continue.
```

<br/>

## future goals
• add album art to tracks

• add script to automatically install missing required packages (aiohttp, mutagen etc)

• downloading to other audio formats (aac, mp3, flac, for example) rather than only the option of the default ogg vorbis provided by spotify

<br/>

## known issues: 

• very rarely when trying to make a http request to spotify api an error will be thrown: `aiohttp.client_exceptions.ServerDisconnectedError: Server disconnected.`

add a retry for this http session with a delay, to allow the download to attempt to continue

• sometimes `ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host` will be thrown as an error when the user is using natsuka for a prolonged period of time (for example, if the user took 3 minutes to input a url)

this does not stop the functionality of natsuka at all and in fact is a good thing, as aiohttp restored the closed session, however i still plan to except this error in the future to avoid it from being output at all
