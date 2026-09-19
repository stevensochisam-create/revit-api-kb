---
num: 1026
date: 2013-09-26
themes: [Geometry]
tags: [revit-api, tbc]
---

# Saving a Solid to a SAT File Implementation

<https://jeremytammik.github.io/tbc/a/1026_save_solid_to_file.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return the full path of the first file &nbsp; /// found matching the given filename pattern &nbsp; /// in a recursive search through all &nbsp; /// subdirectories of the given starting folder. &nbsp; /// &lt;/summary&gt; &nbsp; string DirSearch( &nbsp; &nbsp; string start_dir, &nbsp; &nbsp; string filename_pattern ) &nbsp; { &nbsp; &nbsp; foreach( string d in Directory.GetDirectories( &nbsp; &nbsp; &nbsp; start_dir ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( string f in Directory.GetFiles( &nbsp; &nbsp; &nbsp; &nbsp; d, filename_pattern ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; return f; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; string f2 = DirSearch( d, filename_pattern ); &nbsp; &nbsp; &nbsp; &nbsp; if( null != f2 ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; return f2; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return null; &nbsp; }
```

```csharp
&nbsp; // Search for the metric mass family template file &nbsp; &nbsp; string template_path = DirSearch( &nbsp; &nbsp; app.FamilyTemplatePath, &nbsp; &nbsp; &quot;Metric Mass.rft&quot; );
```
