---
num: 556
date: 2011-03-18
themes: [Geometry]
tags: [revit-api, tbc]
---

# Toposurface Interior and Boundary Points

<https://jeremytammik.github.io/tbc/a/0556_toposurf_points.htm>

```csharp
/// &lt;summary&gt; /// For each point of the given mesh, /// determine how many triangles it belongs to. /// &lt;/summary&gt; void DetermineTriangleCountForPoints( Mesh mesh ) { &nbsp; int np = mesh.Vertices.Count; &nbsp; int nt = mesh.NumTriangles; &nbsp; &nbsp; Debug.Print( &quot;Mesh has {0} point{1} and {2} triangle{3}.&quot;, &nbsp; &nbsp; np, PluralSuffix( np ), nt, PluralSuffix( nt ) ); &nbsp; &nbsp; MapVertexToTriangleIndices map &nbsp; &nbsp; = new MapVertexToTriangleIndices(); &nbsp; &nbsp; for( int i = 0; i &lt; nt; ++i ) &nbsp; { &nbsp; &nbsp; MeshTriangle t = mesh.get_Triangle( i ); &nbsp; &nbsp; &nbsp; for( int j = 0; j &lt; 3; ++j ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; map.AddVertex( t.get_Vertex( j ), i ); &nbsp; &nbsp; } &nbsp; } &nbsp; List&lt;XYZ&gt; pts = new List&lt;XYZ&gt;( map.Keys ); &nbsp; pts.Sort( Compare ); &nbsp; &nbsp; foreach( XYZ p in pts ) &nbsp; { &nbsp; &nbsp; int n = map[p].Count; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;&nbsp; vertex {0} belongs to {1} triangle{2}&quot;, &nbsp; &nbsp; &nbsp; PointString( p ), n, PluralSuffix( n ) ); &nbsp; } }
```

```csharp
TopographySurface 128689: Mesh has 6 points and 5 triangles. (-35.952648163, -68.290878296, 0.000000000) belongs to 3 triangles and is therefore interior (-34.969902039, -57.134258270, 0.000000000) belongs to 1 triangle and is therefore exterior (-24.212404251, -76.898384094, 0.000000000) belongs to 2 triangles and is therefore exterior (-23.932262421, -60.340045929, 0.000000000) belongs to 3 triangles and is therefore interior (-23.100381851, -69.003776550, 0.000000000) belongs to 4 triangles and is therefore exterior (-14.513459206, -65.842926025, 0.000000000) belongs to 2 triangles and is therefore exterior
```

```csharp
public class MeshTriangleEdge { &nbsp; public XYZ A { get; set; } &nbsp; public XYZ B { get; set; } &nbsp; &nbsp; public MeshTriangleEdge( XYZ a, XYZ b ) &nbsp; { &nbsp; &nbsp; int d = Compare( a, b ); &nbsp; &nbsp; &nbsp; Debug.Assert( 0 != d, &quot;expected non-equal edge vertices&quot; ); &nbsp; &nbsp; &nbsp; A = ( 0 &lt; d ) ? a : b; &nbsp; &nbsp; B = ( 0 &lt; d ) ? b : a; &nbsp; } }
```

```csharp
/// &lt;summary&gt; /// Manage a mesh triangle edge by storing the /// index of the mesh vertex corresponing to /// the edge start and end point. /// For reliable comparison purposes, the /// lower index is always stored in A and /// the higher in B. /// &lt;/summary&gt; public class JtEdge { &nbsp; public int A { get; set; } &nbsp; public int B { get; set; } &nbsp; &nbsp; public JtEdge( int a, int b ) &nbsp; { &nbsp; &nbsp; Debug.Assert( a != b, &quot;expected non-equal edge vertices&quot; ); &nbsp; &nbsp; &nbsp; A = ( a &lt; b ) ? a : b; &nbsp; &nbsp; B = ( a &lt; b ) ? b : a; &nbsp; } }
```

```csharp
/// &lt;summary&gt; /// Map mesh triangle edges to a list of the /// indices of all the triangles they belong to. /// &lt;/summary&gt; class MapEdgeToTriangles &nbsp; : Dictionary&lt;JtEdge, List&lt;int&gt;&gt; { &nbsp; public MapEdgeToTriangles() &nbsp; &nbsp; : base( new JtEdgeEqualityComparer() ) &nbsp; { &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Add a new edge. &nbsp; /// If it is already known, append the triangle &nbsp; /// index of the current triangle. Otherwise, &nbsp; /// generate a new key for it. &nbsp; /// &lt;/summary&gt; &nbsp; public void AddEdge( &nbsp; &nbsp; JtEdge e, &nbsp; &nbsp; int triangleIndex ) &nbsp; { &nbsp; &nbsp; if( !ContainsKey( e ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Add( e, new List&lt;int&gt;( 2 ) ); &nbsp; &nbsp; } &nbsp; &nbsp; ( this )[e].Add( triangleIndex ); &nbsp; } }
```
