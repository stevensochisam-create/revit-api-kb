---
num: 1172
date: 2014-06-24
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2015 Update Release 3

<https://jeremytammik.github.io/tbc/a/1172_2015_ur3.htm>

```csharp
&nbsp; XYZ origin = XYZ.Zero; &nbsp; XYZ baseVec = XYZ.BasisX; &nbsp; XYZ upVec = XYZ.BasisY; &nbsp; &nbsp; Transaction trans = new Transaction( doc ); &nbsp; trans.Start( &quot;Create text&quot; ); &nbsp; &nbsp; TextNote note = doc.Create.NewTextNote( &nbsp; &nbsp; view, origin, baseVec, upVec, 0.3, &nbsp; &nbsp; TextAlignFlags.TEF_ALIGN_BOTTOM | TextAlignFlags.TEF_ALIGN_LEFT, &nbsp; &nbsp; &quot;Why is this line too long for the text box!&quot; ); &nbsp; &nbsp; //doc.Regenerate(); &nbsp; //note.Width = 25; &nbsp; &nbsp; trans.Commit();
```
