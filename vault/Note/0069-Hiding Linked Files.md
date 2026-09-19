---
num: 69
date: 2009-01-14
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# Hiding Linked Files

<https://jeremytammik.github.io/tbc/a/0069_hiding_linked_files.htm>

```csharp
Document doc = app.ActiveDocument; Categories categories = doc.Settings.Categories; &nbsp; // get category for linked files Category linkedRevitCat &nbsp; = categories.get_Item( &nbsp; &nbsp; BuiltInCategory.OST_RvtLinks ); &nbsp; // loop through all categories in document foreach( Category c in categories ) { &nbsp; // if they end with dwg or rvt toggle &nbsp; // their current visibility in current view &nbsp; if( c.Name.ToLower().EndsWith( ".dwg" ) &nbsp; &nbsp; || c.Name.ToLower().Contains( ".rvt" ) &nbsp; &nbsp; || c.Name.ToLower().EndsWith( ".dwf" ) &nbsp; &nbsp; || c.Name.ToLower().EndsWith( ".dxf" ) &nbsp; &nbsp; || c.Name.ToLower().EndsWith( ".dwfx" ) &nbsp; &nbsp; || ( linkedRevitCat != null &nbsp; &nbsp; &nbsp; &amp;&amp; c.Id.Equals( linkedRevitCat.Id ) ) ) &nbsp; { &nbsp; &nbsp; // toggle visibility &nbsp; &nbsp; doc.ActiveView.setVisibility( c, &nbsp; &nbsp; &nbsp; !c.get_Visible( doc.ActiveView ) ); &nbsp; } }
```

```csharp
&nbsp; BuiltInCategory bic = BuiltInCategory.OST_RvtLinks; &nbsp; ElementIterator i = doc.Elements; &nbsp; Element e; &nbsp; while( i.MoveNext() ) &nbsp; { &nbsp; &nbsp; e = i.Current as Element; &nbsp; &nbsp; if( e.Name.Contains( ".rvt" ) &nbsp; &nbsp; &nbsp; &amp;&amp; e.Category != null &nbsp; &nbsp; &nbsp; &amp;&amp; e.Category.Id.Value.Equals( (int) bic ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; } &nbsp; }
```

```csharp
Instance rvtLinkInst = . . . // retrieve revit link instance bool canHidden = rvtLInkInst.CanBeHidden( view ); // this always returns false elems.Insert( rvtLinkInst ); // insert instance into element set view.Hide( elems ); // this throws an exception
```
