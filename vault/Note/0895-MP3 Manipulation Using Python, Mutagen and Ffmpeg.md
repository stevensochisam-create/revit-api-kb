---
num: 895
date: 2013-02-08
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# MP3 Manipulation Using Python, Mutagen and Ffmpeg

<https://jeremytammik.github.io/tbc/a/0895_mutagen_ffmpeg.htm>

```csharp
#!/usr/bin/python # # mp3swapartist.py # # swap mp3 artist and album artist tags # # I set up my whole music collection using a directory structure # based on artist/album/trackno - title. Now I realise that # album artist is the proper tag to use for that structure. # # Copyright (C) 2013 Jeremy Tammik # import glob, os, re, sys from mutagen.mp3 import MP3 from mutagen.id3 import TPE1, TPE2 def swap_artist( filepath ): "Swap mp3 artist and album artist tags." assert filepath.lower().endswith( '.mp3' ) try: audio = MP3( filepath ) old_artist = unicode( audio['TPE1'] ) assert 0 &lt; len( old_artist ) old_album_artist = '' if audio.has_key( 'TPE2' ): old_album_artist = unicode( audio['TPE2'] ) s = "original artist '%s', album artist '%s'" % (old_artist, old_album_artist) if 0 == len( old_album_artist ): # copy artist to album artist s += ' - added album artist' audio.tags.add( TPE2( encoding=3, text=old_artist ) ) audio.tags.save() elif old_artist != old_album_artist: # swap artist and album artist s += ' swapped' audio.tags.add( TPE2( encoding=3, text=old_artist ) ) audio.tags.add( TPE1( encoding=3, text=old_album_artist ) ) audio.tags.save() else: s += ' retained' print filepath + ':', s except StandardError, err: print 'Error:', str( err ), "in '%s'" % filepath def main(): "Walk a directory tree and swap all mp3 artist and album artist tags." dir = '.' for root, dirs, files in os.walk( dir ): for filename in files: if filename.lower().endswith( '.mp3' ): filepath = os.path.join( root, filename ) swap_artist( filepath ) if __name__ == "__main__": main()
```

```csharp
#!/usr/bin/env python # # songbird_to_m3u.py - convert the file tags exported by songbird to m3u playlist # # Artist, Album, Title --> # /m/Artist/Album/Track*Title.mp3 # # cat songbird_export.txt | songbird_to_m3u.py > songbird_export.m3u # import glob, os, sys nOk = 0 nFailed = 0 while True: try: line = raw_input() except: break a = line.split( ', ' ) if 3 != len(a): sys.stderr.write( line + '\n' ) nFailed += 1 continue p = '/m/' + a[0] + '/' + a[1] + '/*' + a[2] + '.mp3' a = glob.glob( p ) if 1 == len(a): print a[0] nOk += 1 else: sys.stderr.write( line + '\n' ) nFailed += 1 sys.stderr.write( '%s files passed, %s failed.\n' % (nOk, nFailed) )
```

```csharp
lrwxr-xr-x 1 root wheel 21 Nov 14 19:42 m -> /Users/tammikj/Music/
```

```csharp
audio = MP3( path ) seconds = audio.info.length
```

```csharp
#!/usr/bin/python # # mp3duration.py - retrieve the length of the tracks in the playlist and calculate the total # import glob, os, re, subprocess, sys from mutagen.mp3 import MP3 _find_duration = re.compile( '.*Duration: ([0-9:]+)', re.MULTILINE ) def min_sec_to_seconds( ms ): "Convert a minutes:seconds string representation to the appropriate time in seconds." a = ms.split(':') assert 2 == len( a ) return float(a[0]) * 60 + float(a[1]) def seconds_to_min_sec( secs ): "Return a minutes:seconds string representation of the given number of seconds." mins = int(secs) / 60 secs = int(secs - (mins * 60)) return "%d:%02d" % (mins, secs) def retrieve_length( playlist_filename ): "Determine length of tracks listed in the given input files (e.g. playlists)." print playlist_filename + ' duration:' if not os.path.exists( playlist_filename ): print "Error: specified playlist '%s' does not exist.\n" % playlist_filename raise SystemExit(1) f = open( playlist_filename ) lines = f.readlines() f.close() total_mutagen = 0.0 total_ffmpeg = 0.0 print '%8s%8s%8s %s' % ('mutagen', 'm:s', 'ffmpeg', 'track') for line in lines: path = line.strip() if not path or path[0] == '#': continue if not os.path.exists( path ): print "Error: specified music file '%s' does not exist.\n" % path raise SystemExit(2) audio = MP3( path ) seconds = audio.info.length ffmpeg = subprocess.check_output( 'ffmpeg -i "%s"; exit 0' % path, shell = True, stderr = subprocess.STDOUT ) match = _find_duration.search( ffmpeg ) if match: ffmpeg = match.group( 1 ) else: ffmpeg = '--' ffmpeg = ffmpeg.lstrip('0:') print '%8.1f%8s%8s %s' % (seconds, seconds_to_min_sec(seconds), ffmpeg, path ) total_mutagen += seconds total_ffmpeg += min_sec_to_seconds( ffmpeg ) s = '-' * 6 print '%8s%8s%8s %s' % (s, s, s, s ) print '%8.1f%8s%8s %s' % (total_mutagen, seconds_to_min_sec(total_mutagen), seconds_to_min_sec(total_ffmpeg), 'total' ) def main(): "Determine length of tracks listed in the given input files (e.g. playlists)." for pattern in sys.argv[1:]: filelist = glob.glob( pattern ) for filename in filelist: retrieve_length( filename ) if __name__ == '__main__': main()
```
