---
num: 1216
date: 2014-09-30
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2015 R2, UR4 and Dimension Prefix & Suffix

<https://jeremytammik.github.io/tbc/a/1216_2015_r2_and_ur4.htm>

```csharp
&nbsp; private bool CheckVal( string val ) &nbsp; { &nbsp; &nbsp; foreach( char c in val ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( !char.IsDigit( c ) &amp;&amp; c != '.' ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return false; &nbsp; } &nbsp; // . . . &nbsp; if( CheckVal( dimseg.ValueString ) ) &nbsp; { &nbsp; &nbsp; if( string.IsNullOrEmpty( txtPrefix.Text ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; txtPrefix.Text = dimseg.Prefix; &nbsp; &nbsp; } &nbsp; &nbsp; if( string.IsNullOrEmpty( txtSuffix.Text ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; txtSuffix.Text = dimseg.Suffix; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; foreach( DimensionSegment dimseg in dim.Segments ) &nbsp; { &nbsp; &nbsp; dimseg.Above = dimseg.Above; // Hello API, are you awake? &nbsp; &nbsp; &nbsp; if( string.IsNullOrEmpty( txtPrefix.Text ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; txtPrefix.Text = dimseg.Prefix; &nbsp; &nbsp; } &nbsp; &nbsp; if( string.IsNullOrEmpty( txtSuffix.Text ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; txtSuffix.Text = dimseg.Suffix; &nbsp; &nbsp; } &nbsp; }
```
