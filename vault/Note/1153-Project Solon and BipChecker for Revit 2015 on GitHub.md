---
num: 1153
date: 2014-05-14
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Project Solon and BipChecker for Revit 2015 on GitHub

<https://jeremytammik.github.io/tbc/a/1153_bipchecker_2015_git.htm>

```csharp
&nbsp; public static Element &nbsp; &nbsp; GetSingleSelectedElementOrPrompt( &nbsp; &nbsp; &nbsp; UIDocument uidoc ) &nbsp; { &nbsp; &nbsp; Element e = null; &nbsp; &nbsp; ElementSet ss = uidoc.Selection.Elements; &nbsp; &nbsp; &nbsp; if( 1 == ss.Size ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ElementSetIterator iter = ss.ForwardIterator(); &nbsp; &nbsp; &nbsp; iter.MoveNext(); &nbsp; &nbsp; &nbsp; e = iter.Current as Element; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; // . . .
```

```csharp
&nbsp; &nbsp; ICollection&lt;ElementId&gt; ids &nbsp; &nbsp; &nbsp; = uidoc.Selection.GetElementIds(); &nbsp; &nbsp; &nbsp; if( 1 == ids.Count ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( ElementId id in ids ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; e = uidoc.Document.GetElement( id ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; }
```
