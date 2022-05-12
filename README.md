# natsuka
a single file application giving you the ability to download music from spotify with id3 data
## credits
JoshuaDoes (for the API endpoint)

Skylar Bleed (for helping with several initial changes)

## current features:
**1: single song download support**
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
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


Press enter to exit.
```

**2: multiple song download support**
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
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

Press enter to exit.

```

**3: album download support** (**NOTE: can download multi disc albums**)
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
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

Press enter to exit.
```

**4: playlist download support** (currently unimplemented but planned for the future)

<br/>

**5: downloading song/album by search query**
#### option 1: download song by query
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
Option 6 - Exit

: 5
Input song name
: 16
Result number: 1
Song: 16
Song creator: Highly Suspect
Song Album: MCID
Song Album URI: spotify:album:16ah4zHJlxx3wjRFg3nkSl

Result number: 2
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue
Song Album URI: spotify:album:3r46DPIQeBQbjvjjV5mXGg

Result number: 3
Song: Sixteen Tons
Song creator: Tennessee Ernie Ford
Song Album: Vintage Collections
Song Album URI: spotify:album:5qWqMyXJ9uOCl6vEIVKqBD

Result number: 4
Song: 16 Lines
Song creator: Lil Peep
Song Album: Come Over When You're Sober, Pt. 2
Song Album URI: spotify:album:52JymrguPgkmmwLaWIusst

Result number: 5
Song: Dos Mil 16
Song creator: Bad Bunny
Song Album: Un Verano Sin Ti
Song Album URI: spotify:album:3RQQmkQEvNCY4prGKE6oc5

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


Press enter to exit.
```

#### option 2: download album by query
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
Option 6 - Exit

: 5
Input song name
: 16
Result number: 1
Song: 16
Song creator: Highly Suspect
Song Album: MCID
Song Album URI: spotify:album:16ah4zHJlxx3wjRFg3nkSl

Result number: 2
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue
Song Album URI: spotify:album:3r46DPIQeBQbjvjjV5mXGg

Result number: 3
Song: Sixteen Tons
Song creator: Tennessee Ernie Ford
Song Album: Vintage Collections
Song Album URI: spotify:album:5qWqMyXJ9uOCl6vEIVKqBD

Result number: 4
Song: 16 Lines
Song creator: Lil Peep
Song Album: Come Over When You're Sober, Pt. 2
Song Album URI: spotify:album:52JymrguPgkmmwLaWIusst

Result number: 5
Song: Dos Mil 16
Song creator: Bad Bunny
Song Album: Un Verano Sin Ti
Song Album URI: spotify:album:3RQQmkQEvNCY4prGKE6oc5

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

Press enter to exit.
```

**note: the more specific your search query is, the better the chance of finding the song**
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Search for Song/Album By Name
Option 6 - Exit

: 5
Input song name
: 16 baby keem
Result number: 1
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue
Song Album URI: spotify:album:3r46DPIQeBQbjvjjV5mXGg

Result number: 2
Song: 16
Song creator: Baby Keem
Song Album: The Melodic Blue
Song Album URI: spotify:album:7n23fjZTviIUnHyvZGQjni

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


Press enter to exit.
```


## future goals
add album art to tracks.

implement playlist downloading
