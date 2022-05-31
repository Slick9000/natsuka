
# natsuka
a single file application giving you the ability to download music from spotify with id3 metadata (track title, track number, artist, album, cover art, release date)

initally made on **february 28th, 2021**, natsuka was made to download songs from spotify with metadata, a task other downloaders were not able to accomplish for me.

welcome to natsuka 2.0, with **single-track, multi-track, album, playlist, and search query downloading.**

## credits
JoshuaDoes (for the API endpoint)

Skylar Bleed (for helping with several initial changes)

## [download](https://github.com/Slick9000/natsuka/releases/latest)

## requirements
[aiohttp](https://pypi.org/project/aiohttp/)

[eyed3](https://pypi.org/project/eyed3/)

(natsuka automatically installs these python packages if not installed)

[ffmpeg](https://ffmpeg.org), in PATH. 

**NOTE: users using the natsuka.exe from the download page won't need to download anything, as everything is already included in the executable. for all other users, you will need to install ffmpeg yourself.**

## features:

**1: song(s) download support by url**
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

: 1
Enter songs (Current number of songs: 0)
Type 'START' to begin download.

Type 'RETURN' to return to main menu
: https://open.spotify.com/track/6O9PAqJLef4tyQNadjb40u?si=149102c06360475c
Enter songs (Current number of songs: 1)
Type 'START' to begin download.

Type 'RETURN' to return to main menu
: https://open.spotify.com/track/3DYZKxjG8SZrWpVcoUilqQ?si=22dd2605a1834519
Enter songs (Current number of songs: 2)
Type 'START' to begin download.

Type 'RETURN' to return to main menu
: START
Loading 2 songs...

Track Name: De roses et de colombes
Album Name: How Are You
Artist Name: Mounika.
Album Release: 2017
Song Downloaded!
Metadata Applied!


Track Name: Cut My Hair
Album Name: How Are You
Artist Name: Mounika.
Album Release: 2017
Song Downloaded!
Metadata Applied!


Download time: 0:00:38.593000

Press enter to continue.

```

<br/>

**2: album download support by url** (**NOTE: can download multi disc albums**)
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

: 2
Enter the album's URL

Type 'RETURN' to return to main menu
: https://open.spotify.com/album/5k1geNqLd4yHzyg5L6XF2z?si=i18yaK1cTESTw1zg3uBoqA
Loading 5 songs...

Track Name: HAZARD DUTY PAY!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: 2022
Song Downloaded!
Metadata Applied!


Track Name: DIKEMBE!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: 2022
Song Downloaded!
Metadata Applied!


Track Name: GOD DON'T LIKE UGLY!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: 2022
Song Downloaded!
Metadata Applied!


Track Name: UNTITLED
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: 2022
Song Downloaded!
Metadata Applied!


Track Name: 100 EMOJI!
Album Name: OFFLINE!
Artist Name: JPEGMAFIA
Album Release: 2022
Song Downloaded!
Metadata Applied!


Download time: 0:01:43.765000

Press enter to continue.
```

<br/>

**3: playlist download support by url**
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

: 3
Input user ID

Type 'RETURN' to return to main menu
: 1xcmyijwkhfsqb1v7pxmb4dlv
Input the playlist's URL

Type 'RETURN' to return to main menu
: https://open.spotify.com/playlist/3tOMpRplT8CA4HDQIrCPa2?si=f5aceed75edb4df5
Playlist Name: Short Sample Playlist
Description: Short sample playlist I made
Playlist Length: 3 tracks
Loading 3 songs...

Track Name: Mirror
Album Name: Mr. Morale & The Big Steppers
Artist Name: Kendrick Lamar
Album Release: 2022
Song Downloaded!
Metadata Applied!


Track Name: Mental [Feat. Saul Williams & Bridget Perez]
Album Name: Melt My Eyez See Your Future
Artist Name: Denzel Curry
Album Release: 2022
Song Downloaded!
Metadata Applied!


Track Name: Savior
Album Name: Mr. Morale & The Big Steppers
Artist Name: Kendrick Lamar
Album Release: 2022
Song Downloaded!
Metadata Applied!


Download time: 0:01:22.625000

Press enter to continue.
```

<br/>

**4: song(s) download support by search query (bestmatch, no menu)**
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

: 4
Enter songs (Current number of songs: 0)
Type 'START' to begin download.
Tip: For best results, use format: (Song Name) (Artist Name)

Type 'RETURN' to return to main menu
: Nights Frank Ocean
Enter songs (Current number of songs: 1)
Type 'START' to begin download.
Tip: For best results, use format: (Song Name) (Artist Name)

Type 'RETURN' to return to main menu
: Brambleton Pusha T
Enter songs (Current number of songs: 2)
Type 'START' to begin download.
Tip: For best results, use format: (Song Name) (Artist Name)

Type 'RETURN' to return to main menu
: START
Loading 2 songs...

Track Name: Nights
Album Name: Blonde
Artist Name: Frank Ocean
Album Release: 2016
Song Downloaded!
Metadata Applied!


Track Name: Brambleton
Album Name: It's Almost Dry
Artist Name: Pusha T
Album Release: 2022
Song Downloaded!
Metadata Applied!


Download time: 0:01:03.516000

Press enter to continue.
```

<br/>

**5: song/album download support by search query**
#### option 1: download song
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

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
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

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

**note: the more specific your search query is, the better the chance of finding the song (bestmatch)**
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

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

**6: artist top songs/album download support by search query**
#### option 1: download artist's top songs
```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

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
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

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

**7: change bitrate of download**
#### selecting a common preset bitrate

```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

: 7

Select new bitrate for download:
1 - 96kbps
2 - 128kbps
3 - 192kbps
4 - 320kbps (Highest Spotify Bitrate)
5 - Custom
: 1
Press enter to continue.

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 96kbps)
Option 8 - Exit

: 
```

<br/>

#### selecting a custom bitrate

```
[*] Checking for required dependencies...

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 320kbps)
Option 8 - Exit

: 7

Select new bitrate for download:
1 - 96kbps
2 - 128kbps
3 - 192kbps
4 - 320kbps (Highest Spotify Bitrate)
5 - Custom
: 5
Input new bitrate (320kbps maximum)
: 48
Press enter to continue.

natsuka - spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download Track(s) by URL
Option 2 - Download Album by URL
Option 3 - Download Playlist by User ID and Playlist URL
Option 4 - Download Tracks(s) by Song Name and Artist Name (Bestmatch)
Option 5 - Search for Song/Album by Name
Option 6 - Search for Artist
Option 7 - Change Audio Bitrate (Selected: 48kbps)
Option 8 - Exit

: 
```
