---
num: 544
date: 2011-02-28
themes: [ElementId]
tags: [revit-api, tbc]
---

# Comparing Element Id for Equality

<https://jeremytammik.github.io/tbc/a/0544_element_id_equality.htm>

```csharp
&nbsp; bool equal = ( id.IntegerValue == id2.IntegerValue );
```

```csharp
&nbsp; public void IdTest( UIDocument doc ) &nbsp; { &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc.Document ) &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( Wall ) ); &nbsp; &nbsp; &nbsp; ElementId id = collector.ToElementIds().First(); &nbsp; &nbsp; &nbsp; Reference selRef = doc.Selection.PickObject( &nbsp; &nbsp; &nbsp; ObjectType.Element ); &nbsp; &nbsp; &nbsp; if( id == selRef.Element.Id ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; TaskDialog.Show( &quot;Same Wall&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &quot;Just saying...&quot; ); &nbsp; &nbsp; } &nbsp; }
```
