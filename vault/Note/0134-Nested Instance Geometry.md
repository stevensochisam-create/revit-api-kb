---
num: 134
date: 2009-05-06
themes: [Geometry]
tags: [revit-api, tbc]
---

# Nested Instance Geometry

<https://jeremytammik.github.io/tbc/a/0134_nested_instance_geo.htm>

```csharp
F } +-- C0 } +-- F1 } } } +-- C1 } } } +-- C2 } +-- F2 } +-- C3 } +-- C4
```

```csharp
class XyzEqualityComparer : IEqualityComparer&lt;XYZ&gt; { &nbsp; public bool Equals( XYZ p, XYZ q ) &nbsp; { &nbsp; &nbsp; return p.AlmostEqual( q ); &nbsp; } &nbsp; &nbsp; public int GetHashCode( XYZ p ) &nbsp; { &nbsp; &nbsp; return Util.PointString( p ).GetHashCode(); &nbsp; } }
```

```csharp
const double _eps = 1.0e-9; &nbsp; public static bool IsZero( double a ) { &nbsp; return _eps &gt; Math.Abs( a ); } &nbsp; public static bool IsEqual( double a, double b ) { &nbsp; return IsZero( b - a ); } &nbsp; public static int Compare( double a, double b ) { &nbsp; return IsEqual( a, b ) ? 0 : ( a &lt; b ? -1 : 1 ); } &nbsp; public static int Compare( XYZ p, XYZ q ) { &nbsp; int diff = Compare( p.X, q.X ); &nbsp; if( 0 == diff ) { &nbsp; &nbsp; diff = Compare( p.Y, q.Y ); &nbsp; &nbsp; if( 0 == diff ) { &nbsp; &nbsp; &nbsp; diff = Compare( p.Z, q.Z ); &nbsp; &nbsp; } &nbsp; } &nbsp; return diff; }
```

```csharp
static void GetVertices( XYZArray vertices, Solid s ) { &nbsp; Debug.Assert( 0 &lt; s.Edges.Size, &nbsp; &nbsp; "expected a non-empty solid" ); &nbsp; &nbsp; Dictionary&lt;XYZ, int&gt; a &nbsp; &nbsp; = new Dictionary&lt;XYZ, int&gt;( &nbsp; &nbsp; &nbsp; new XyzEqualityComparer() ); &nbsp; &nbsp; foreach( Face f in s.Faces ) &nbsp; { &nbsp; &nbsp; Mesh m = f.Triangulate(); &nbsp; &nbsp; foreach( XYZ p in m.Vertices ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( !a.ContainsKey( p ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; a.Add( p, 1 ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; else &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &plusmn;&plusmn;a[p]; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; List&lt;XYZ&gt; keys = new List&lt;XYZ&gt;( a.Keys ); &nbsp; &nbsp; Debug.Assert( 8 == keys.Count, &nbsp; &nbsp; "expected eight vertices for a rectangular column" ); &nbsp; &nbsp; keys.Sort( Util.Compare ); &nbsp; &nbsp; foreach( XYZ p in keys ) &nbsp; { &nbsp; &nbsp; Debug.Assert( 3 == a[p], &nbsp; &nbsp; &nbsp; "expected every vertex of solid to appear in exactly three faces" ); &nbsp; &nbsp; &nbsp; vertices.Append( p ); &nbsp; } }
```

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; &nbsp; List&lt;RvtElement&gt; a = new List&lt;RvtElement&gt;(); &nbsp; if( !Util.GetSelectedElementsOrAll( a, doc, &nbsp; typeof( FamilyInstance ) ) ) { &nbsp; Selection sel = doc.Selection; &nbsp; message = ( 0 &lt; sel.Elements.Size ) &nbsp; &nbsp; ? "Please select some family instances." &nbsp; &nbsp; : "No family instances found."; &nbsp; return CmdResult.Failed; } FamilyInstance inst = a[0] as FamilyInstance; &nbsp; Options opts = app.Create.NewGeometryOptions(); GeoElement geoElement = inst.get_Geometry( opts ); &nbsp; GeometryObjectArray a1 = geoElement.Objects; int n = a1.Size; &nbsp; Debug.Print( &nbsp; "Family instance geometry has {0} geometry object{1}{2}", &nbsp; n, Util.PluralSuffix( n ), Util.DotOrColon( n ) ); &nbsp; int i = 0; foreach( GeometryObject o1 in a1 ) { &nbsp; GeoInstance geoInstance = o1 as GeoInstance; &nbsp; if( null != geoInstance ) &nbsp; { &nbsp; &nbsp; GeoElement symbolGeo = geoInstance.SymbolGeometry; &nbsp; &nbsp; GeometryObjectArray a2 = symbolGeo.Objects; &nbsp; &nbsp; foreach( GeometryObject o2 in a2 ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Solid s = o2 as Solid; &nbsp; &nbsp; &nbsp; if( null != s &amp;&amp; 0 &lt; s.Edges.Size ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; XYZArray vertices = app.Create.NewXYZArray(); &nbsp; &nbsp; &nbsp; &nbsp; GetVertices( vertices, s ); &nbsp; &nbsp; &nbsp; &nbsp; n = vertices.Size; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( "Solid {0} has {1} vertices{2} {3}", &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; i++, n, Util.DotOrColon( n ), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Util.PointArrayString( vertices ) ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } } ElementSet components = inst.Symbol.Family.Components; n = components.Size; &nbsp; Debug.Print( &nbsp; "Family instance symbol family has {0} component{1}{2}", &nbsp; n, Util.PluralSuffix( n ), Util.DotOrColon( n ) ); &nbsp; foreach( RvtElement e in components ) { &nbsp; LocationPoint lp = e.Location as LocationPoint; &nbsp; Debug.Print( "{0} at {1}", &nbsp; &nbsp; Util.ElementDescription( e ), &nbsp; &nbsp; Util.PointString( lp.Point ) ); } return CmdResult.Failed;
```
