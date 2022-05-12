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
Option 3 - Download Album              (Doesn't currently work)
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Exit

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
Option 3 - Download Album              (Doesn't currently work)
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Exit

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

**3: album download support**
```
natsuka - wip spotify downloader
Thanks to JoshuaDoes for making this possible.

What would you like to do today?

Option 1 - Download a single track
Option 2 - Download multiple tracks
Option 3 - Download Album
Option 4 - Download Playlist           (Doesn't currently work)
Option 5 - Exit

: 3
Enter the album's URL
: https://open.spotify.com/album/5k1geNqLd4yHzyg5L6XF2z?si=i18yaK1cTESTw1zg3uBoqA
5k1geNqLd4yHzyg5L6XF2z
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

## future goals
add album art to tracks.

add the ability to search for a specific song and download it
