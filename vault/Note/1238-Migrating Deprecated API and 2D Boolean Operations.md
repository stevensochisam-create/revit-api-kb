---
num: 1238
date: 2014-11-07
themes: [Geometry, Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Migrating Deprecated API and 2D Boolean Operations

<https://jeremytammik.github.io/tbc/a/1238_booleans_migration.htm>

```csharp
Family family = null; this.document.LoadFamily( path, out family ); FamilySymbol symbol = null; - foreach( FamilySymbol s in family.Symbols ) + //foreach( FamilySymbol s in family.Symbols ) // 2014 + foreach( ElementId id in family.GetFamilySymbolIds() ) // 2015 { - symbol = s; + symbol = document.GetElement( id ) as FamilySymbol; break; } symbols.Add( symbol );
```

```csharp
&nbsp; if( _modify_existing_marks ) &nbsp; { &nbsp; &nbsp; //ElementSet els = uidoc.Selection.Elements; // 2014 &nbsp; &nbsp; &nbsp; ICollection&lt;ElementId&gt; ids = uidoc.Selection.GetElementIds(); // 2015 &nbsp; &nbsp; &nbsp; //foreach( Element e in els ) // 2014 &nbsp; &nbsp; &nbsp; foreach( ElementId id in ids ) // 2015 &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Element e = doc.GetElement( id ); // 2015 &nbsp; &nbsp; &nbsp; &nbsp; if( e is FamilyInstance &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; null != e.Category &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; (int) BuiltInCategory.OST_Doors &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; == e.Category.Id.IntegerValue ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; e.get_Parameter( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInParameter.ALL_MODEL_MARK ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .Set( _the_answer ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ++n; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```
