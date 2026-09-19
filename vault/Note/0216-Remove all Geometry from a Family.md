---
num: 216
date: 2009-09-07
themes: [Geometry]
tags: [revit-api, tbc]
---

# Remove all Geometry from a Family

<https://jeremytammik.github.io/tbc/a/0216_remove_geometry_rfa.htm>

```csharp
public IExternalCommand.Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; Application app = commandData.Application; &nbsp; Document doc = app.ActiveDocument; &nbsp; &nbsp; ElementIterator it = doc.Elements; &nbsp; Options opt = app.Create.NewGeometryOptions(); &nbsp; List&lt;Element&gt; a = new List&lt;Element&gt;(); &nbsp; &nbsp; while( it.MoveNext() ) &nbsp; { &nbsp; &nbsp; Element e = it.Current as Element; &nbsp; &nbsp; &nbsp; if( null != e.get_Geometry( opt ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; a.Add( e ); &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; int n = a.Count; &nbsp; Debug.Print( &nbsp; &nbsp; &quot;{0} element{1} have non-null geometry{2}&quot;, &nbsp; &nbsp; n, &nbsp; &nbsp; ( 1 == n ? &quot;&quot; : &quot;s&quot; ), &nbsp; &nbsp; ( 0 == n ? &quot;.&quot; : &quot;:&quot; ) ); &nbsp; &nbsp; ElementSet els = new ElementSet(); &nbsp; &nbsp; foreach( Element e in a ) &nbsp; { &nbsp; &nbsp; string cat = (null == e.Category) &nbsp; &nbsp; &nbsp; ? &quot;&lt;null&gt;&quot; &nbsp; &nbsp; &nbsp; : e.Category.Name; &nbsp; &nbsp; &nbsp; Debug.Print( &nbsp; &nbsp; &nbsp; &quot;Category={0}; Name={1}; Id={2}; Type={3}&quot;, &nbsp; &nbsp; &nbsp; cat, &nbsp; &nbsp; &nbsp; e.Name, &nbsp; &nbsp; &nbsp; e.Id.Value.ToString(), &nbsp; &nbsp; &nbsp; e.GetType().Name ); &nbsp; &nbsp; &nbsp; if( null == e.Category ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; els.Insert( e ); &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; ElementIdSet ids = doc.Delete( els ); &nbsp; &nbsp; n = (null == ids) ? 0 : ids.Size; &nbsp; &nbsp; Debug.Print( &quot;{0} element{1} deleted.&quot;, &nbsp; &nbsp; n, &nbsp; &nbsp; ( 1 == n ? &quot;&quot; : &quot;s&quot; ) ); &nbsp; &nbsp; return IExternalCommand.Result.Succeeded; }
```

```csharp
2 elements have non-null geometry: Category=; Name=Extrusion; Id=105; Type=Extrusion Category=Cameras; Name=View 1; Id=427; Type=Element 13 elements deleted.
```
