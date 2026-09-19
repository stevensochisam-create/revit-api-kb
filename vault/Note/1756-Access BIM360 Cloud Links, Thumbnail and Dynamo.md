---
num: 1756
date: 2019-06-03
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Access BIM360 Cloud Links, Thumbnail and Dynamo

<https://jeremytammik.github.io/tbc/a/1756_bim360_links.html>

```csharp
import os.path as op import olefile def get_rvt_preview(rvt_file): if op.exists(rvt_file): if olefile.isOleFile(rvt_file): rvt_ole = olefile.OleFileIO(rvt_file) bfi = rvt_ole.openstream("RevitPreview4.0") readed = bfi.read() f = open('my_file.bmp', 'w+b') f.write(readed) f.close() else: print("file does not apper to be an ole file: {}".format(rvt_file)) else: print("file not found: {}".format(rvt_file))
```

```csharp
def get_rvt_preview(rvt_file, png_path): if op.exists(rvt_file): if olefile.isOleFile(rvt_file): # Open ole file rvt_ole = olefile.OleFileIO(rvt_file) bfi = rvt_ole.openstream("RevitPreview4.0") readed = bfi.read() # Find png signature readed_hex = readed.hex() pos = readed_hex.find('89504e470d0a1a0a') png_hex = readed_hex[pos:] data = bytes.fromhex(png_hex) # Save png file f = open(png_path, 'w+b') f.write(data) f.close() else: print("file does not apper to be an ole file: {}".format(rvt_file)) else: print("file not found: {}".format(rvt_file))
```
