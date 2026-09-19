---
num: 1243
date: 2014-11-14
themes: [Geometry, Pitfall]
tags: [revit-api, tbc]
---

# Futureproofing and Determining Intersecting Elements

<https://jeremytammik.github.io/tbc/a/1243_future_proof.htm>

```csharp
&nbsp; // Find intersections between family instances and a selected element&nbsp; &nbsp; &nbsp; Reference Reference = uidoc.Selection.PickObject( &nbsp; &nbsp; ObjectType.Element, &quot;Select element that will &quot; &nbsp; &nbsp; + &quot;be checked for intersection with all family &quot; &nbsp; &nbsp; + &quot;instances&quot; ); &nbsp; &nbsp; Element e = doc.GetElement( reference ); &nbsp; &nbsp; GeometryElement geomElement = e.get_Geometry( &nbsp; &nbsp; new Options() ); &nbsp; &nbsp; Solid solid = null; &nbsp; foreach( GeometryObject geomObj in geomElement ) &nbsp; { &nbsp; &nbsp; solid = geomObj as Solid; &nbsp; &nbsp; if( solid = !null ) break; &nbsp; } &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( FamilyInstance ) ) &nbsp; &nbsp; &nbsp; .WherePasses( new ElementIntersectsSolidFilter( &nbsp; &nbsp; &nbsp; &nbsp; solid ) ); &nbsp; &nbsp; TaskDialog.Show( &quot;Revit&quot;, collector.Count() + &nbsp; &nbsp; &quot;Family instances intersect with selected element (&quot; &nbsp; &nbsp; + element.Category.Name + &quot;ID:&quot; + element.Id + &quot;)&quot; );
```

```csharp
/// &lt;summary&gt; /// Retrieve all family instances intersecting a /// given BIM element, e.g. all columns /// intersecting a wall. /// &lt;/summary&gt; void GetInstancesIntersectingElement( Element e ) { &nbsp; Document doc = e.Document; &nbsp; &nbsp; Solid solid = e.get_Geometry( new Options() ) &nbsp; &nbsp; .OfType&lt;Solid&gt;() &nbsp; &nbsp; .Where&lt;Solid&gt;( s =&gt; null != s &amp;&amp; !s.Edges.IsEmpty ) &nbsp; &nbsp; .FirstOrDefault(); &nbsp; &nbsp; FilteredElementCollector intersectingInstances &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( FamilyInstance ) ) &nbsp; &nbsp; &nbsp; .WherePasses( new ElementIntersectsSolidFilter( solid ) ); &nbsp; &nbsp; int n = intersectingInstances.Count&lt;Element&gt;(); &nbsp; &nbsp; string result = string.Format( &nbsp; &nbsp; &quot;{0} family instance{1} intersect{2} the &quot; &nbsp; &nbsp; + &quot;selected element {3}{4}&quot;, &nbsp; &nbsp; n, Util.PluralSuffix( n ), &nbsp; &nbsp; ( 1 == n ? &quot;s&quot; : &quot;&quot; ), &nbsp; &nbsp; Util.ElementDescription( e ), &nbsp; &nbsp; Util.DotOrColon( n ) ); &nbsp; &nbsp; string id_list = 0 == n &nbsp; &nbsp; ? string.Empty &nbsp; &nbsp; : string.Join( &quot;, &quot;, &nbsp; &nbsp; &nbsp; &nbsp; intersectingInstances &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .Select&lt;Element, string&gt;( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x =&gt; x.Id.IntegerValue.ToString() ) ) &nbsp; &nbsp; &nbsp; + &quot;.&quot;; &nbsp; &nbsp; Util.InfoMsg2( result, id_list ); }
```

```csharp
&nbsp; Element wall = Util.SelectSingleElementOfType( &nbsp; &nbsp; uidoc, typeof( Wall ), &quot;a wall&quot;, true ); &nbsp; &nbsp; GetInstancesIntersectingElement( wall );
```

```csharp
&nbsp; Solid solid = e.get_Geometry( new Options() ) &nbsp; &nbsp; .OfType&lt;Solid&gt;() &nbsp; &nbsp; .Where&lt;Solid&gt;( s =&gt; null != s &amp;&amp; !s.Edges.IsEmpty ) &nbsp; &nbsp; .FirstOrDefault(); &nbsp; &nbsp; FilteredElementCollector intersectingInstances &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( FamilyInstance ) ) &nbsp; &nbsp; &nbsp; .WherePasses( new ElementIntersectsSolidFilter( &nbsp; &nbsp; &nbsp; &nbsp; solid ) ); &nbsp; &nbsp; int n1 = intersectingInstances.Count&lt;Element&gt;(); &nbsp; &nbsp; intersectingInstances &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( FamilyInstance ) ) &nbsp; &nbsp; &nbsp; .WherePasses( new ElementIntersectsElementFilter( &nbsp; &nbsp; &nbsp; &nbsp; e ) ); &nbsp; &nbsp; int n = intersectingInstances.Count&lt;Element&gt;(); &nbsp; &nbsp; Debug.Assert( n.Equals( n1 ), &nbsp; &nbsp; &quot;expected solid intersection to equal element intersection&quot; );
```
