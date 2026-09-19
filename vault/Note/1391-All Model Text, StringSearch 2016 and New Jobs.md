---
num: 1391
date: 2016-01-07
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# All Model Text, StringSearch 2016 and New Jobs

<https://jeremytammik.github.io/tbc/a/1391_string_search_2016.html>

```csharp
FilteredElementCollector a = Util.GetElementsOfType( doc, typeof( TextElement ), BuiltInCategory.OST_TextNotes );
```

```csharp
&nbsp; List&lt;string&gt; testStrings = new FilteredElementCollector( doc ) &nbsp; &nbsp; .OfClass( typeof( TextNote ) ) &nbsp; &nbsp; .Cast&lt;TextNote&gt;() &nbsp; &nbsp; .Select&lt;TextNote, string&gt;( tn =&gt; tn.Text ) &nbsp; &nbsp; .ToList&lt;string&gt;();
```
