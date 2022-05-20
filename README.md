
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
Option 6 - Search for Artist
Option 7 - Exit

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
Option 6 - Search for Artist
Option 7 - Exit

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
Option 6 - Search for Artist
Option 7 - Exit

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
Option 6 - Search for Artist
Option 7 - Exit

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
#### option 1: download song
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Exit

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

#### option 2: download album
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Exit

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
Option 6 - Search for Artist
Option 7 - Exit

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

**5: downloading song/album by search query**
#### option 1: download artist's top songs
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Exit

: 6
Input artist name

Type 'RETURN' to return to main menu
: Saba

Result number: 1
Artist: Saba

Result number: 2
Artist: Sabaton

Result number: 3
Artist: Saba

Result number: 4
Artist: Saba

Result number: 5
Artist: Powerwolf
Select a artist (1-5)

Type 'RETURN' to return to main menu
: 1

Option 1 - Download Artist's Top Songs
Option 2 - Download Album from Artist


Type 'RETURN' to return to main menu
: 1
Loading 10 songs...


Would you like to proceed downloading Saba's top songs?
1 - Yes
2 - No
: 1
Track Name: Photosynthesis
Album Name: Bucket List Project
Artist Name: Saba
Album Release: October 27, 2016

Song Downloaded!
Metadata Applied!


Track Name: Ziplock
Album Name: Ziplock / Rich Don't Stop
Artist Name: Saba
Album Release: March 18, 2021

Song Downloaded!
Metadata Applied!


Track Name: Still (feat. 6LACK and Smino)
Album Name: Few Good Things
Artist Name: Saba
Album Release: February 4, 2022

Song Downloaded!
Metadata Applied!


Track Name: an Interlude Called “Circus” (feat. Eryn Allen Kane)
Album Name: Few Good Things
Artist Name: Saba
Album Release: February 4, 2022

Song Downloaded!
Metadata Applied!


Track Name: LIFE
Album Name: CARE FOR ME
Artist Name: Saba
Album Release: April 5, 2018

Song Downloaded!
Metadata Applied!


Track Name: BUSY / SIRENS
Album Name: CARE FOR ME
Artist Name: Saba
Album Release: April 5, 2018

Song Downloaded!
Metadata Applied!


Track Name: One Way or Every N***a With a Budget
Album Name: Few Good Things
Artist Name: Saba
Album Release: February 4, 2022

Song Downloaded!
Metadata Applied!


Track Name: CALLIGRAPHY
Album Name: CARE FOR ME
Artist Name: Saba
Album Release: April 5, 2018

Song Downloaded!
Metadata Applied!


Track Name: Come My Way (feat. Krayzie Bone)
Album Name: Few Good Things
Artist Name: Saba
Album Release: February 4, 2022

Song Downloaded!
Metadata Applied!


Track Name: Lock It Up
Album Name: Minus The Bullshit Life's Great
Artist Name: Nascent
Album Release: May 14, 2021

Song Downloaded!
Metadata Applied!


Download time: 0:01:07

Press enter to continue.
```

<br/>

#### option 2: download artist's album (from list of albums in discography)
```
natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track by URL
Option 2 - Download multiple tracks by URL
Option 3 - Download Album by URL
Option 4 - Download Playlist by User ID and Playlist URL
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Exit

: 6
Input artist name

Type 'RETURN' to return to main menu
: Tyler the Creator

Result number: 1
Artist: Tyler, The Creator
Select a artist (1-5)

Type 'RETURN' to return to main menu
: 1

Option 1 - Download Artist's Top Songs
Option 2 - Download Album from Artist


Type 'RETURN' to return to main menu
: 2
Loading 8 albums...


Result number: 1
Album Name: CALL ME IF YOU GET LOST
Album Release: June 25, 2021


Result number: 2
Album Name: IGOR
Album Release: May 17, 2019


Result number: 3
Album Name: Flower Boy
Album Release: July 21, 2017


Result number: 4
Album Name: Cherry Bomb
Album Release: April 13, 2015


Result number: 5
Album Name: Cherry Bomb + Instrumentals
Album Release: April 13, 2015


Result number: 6
Album Name: Wolf
Album Release: April 1, 2013


Result number: 7
Album Name: Goblin
Album Release: May 9, 2011


Result number: 8
Album Name: Goblin
Album Release: May 9, 2011

Select an album (1-8)

Type 'RETURN' to return to main menu
: 2
Loading 12 songs...


Would you like to proceed downloading this album?
1 - Yes
2 - No
: 1
Track Name: IGOR'S THEME
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: EARFQUAKE
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: I THINK
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: EXACTLY WHAT YOU RUN FROM YOU END UP CHASING
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: RUNNING OUT OF TIME
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: NEW MAGIC WAND
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: A BOY IS A GUN*
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: PUPPET
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: WHAT'S GOOD
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: GONE, GONE / THANK YOU
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: I DON'T LOVE YOU ANYMORE
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Track Name: ARE WE STILL FRIENDS?
Album Name: IGOR
Artist Name: Tyler, The Creator
Album Release: May 17, 2019
Song Downloaded!
Metadata Applied!


Download time: 0:01:22.093000

Press enter to continue.
```

<br/>

## future goals
• add album art to tracks (requires rewrite of downloading, to use ffmpeg to download and convert file to mp3 rather than writing raw data stream to file)

<br/>

## known issues: 

• very rarely when trying to make a http request to spotify api an error will be thrown: `aiohttp.client_exceptions.ServerDisconnectedError: Server disconnected.` and it will crash. for the time being, simply restarting the program will fix this issue. in the future, except this error and add a retry for this http session with a delay, to allow the download to attempt to continue. a maximum of 3 retries will be made before ceasing download.

• sometimes `ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host` will be thrown as an error when the user is using natsuka for a prolonged period of time (for example, if the user took 3 minutes to input a url). this does not stop the functionality of natsuka at all and in fact is a good thing, as aiohttp restored the closed session, however i still plan to except this error in the future to avoid it from being output at all
