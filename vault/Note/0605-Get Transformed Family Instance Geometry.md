---
num: 605
date: 2011-06-28
themes: [Geometry]
tags: [revit-api, tbc]
---

# Get Transformed Family Instance Geometry

<https://jeremytammik.github.io/tbc/a/0605_transformed_geo.htm>

```csharp
protected Mesh fetchSomeMesh( &nbsp; GeometryElement gElem, &nbsp; Transform transform ) { &nbsp; // Apply transformation and seek for Meshes &nbsp; &nbsp; GeometryElement transformed &nbsp; &nbsp; = gElem.GetTransformed( transform ); &nbsp; &nbsp; foreach( GeometryObject obj in transformed.Objects ) &nbsp; { &nbsp; &nbsp; Mesh gMesh = obj as Mesh; &nbsp; &nbsp; if( null != gMesh ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return gMesh; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; // Loop and seek for geometry instances &nbsp; &nbsp; foreach( GeometryObject obj in gElem.Objects ) &nbsp; { &nbsp; &nbsp; GeometryInstance gInstance &nbsp; &nbsp; &nbsp; = obj as GeometryInstance; &nbsp; &nbsp; &nbsp; if( null != gInstance ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // If it's GeometryInstance, combine &nbsp; &nbsp; &nbsp; // transformations and go recursive &nbsp; &nbsp; &nbsp; &nbsp; Transform combinedTransform = gInstance &nbsp; &nbsp; &nbsp; &nbsp; .Transform.Multiply( transform ); &nbsp; &nbsp; &nbsp; &nbsp; return fetchSomeMesh( &nbsp; &nbsp; &nbsp; &nbsp; gInstance.SymbolGeometry, &nbsp; &nbsp; &nbsp; &nbsp; combinedTransform ); &nbsp; &nbsp; } &nbsp; } &nbsp; return null; }
```

```csharp
void checkLinkedDwg( Element linked ) { &nbsp; Instance inst = linked as Instance; &nbsp; Transform transform = inst.GetTransform(); &nbsp; &nbsp; Options opt = new Options(); &nbsp; opt.View = _doc.ActiveView; &nbsp; &nbsp; GeometryElement gElem = inst.get_Geometry( opt ); &nbsp; &nbsp; Debug.Print( &quot;Point without Transformation: &quot; &nbsp; &nbsp; + fetchSomeMesh( gElem ).Vertices[0].ToString() ); &nbsp; &nbsp; XYZ vertex = fetchSomeMesh( gElem, transform ).Vertices[0]; &nbsp; Debug.Print( &quot;Point when Transformed: &quot; + vertex.ToString() ); &nbsp; &nbsp; Debug.Print( &quot;Point when Transformed + inverse: &quot; &nbsp; &nbsp; + transform.Inverse.OfPoint( vertex ).ToString() ); }
```

```csharp
Point without Transformation: (0.0, 0.0, 0.0) Point when Transformed: (2379.1, 1307.1, 0.0) Point when Transformed + inverse: (1203.5, 662.6, 0.0)
```

```csharp
protected Mesh fetchSomeMeshTransformed( &nbsp; GeometryElement gElem ) { &nbsp; // Apply transformation and seek for Meshes &nbsp; &nbsp; GeometryElement transformed &nbsp; &nbsp; = gElem.GetTransformed( Transform.Identity ); &nbsp; &nbsp; foreach( GeometryObject obj in transformed.Objects ) &nbsp; { &nbsp; &nbsp; Mesh gMesh = obj as Mesh; &nbsp; &nbsp; if( null != gMesh ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return gMesh; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; // Loop and seek for geometry instances &nbsp; &nbsp; foreach( GeometryObject obj in gElem.Objects ) &nbsp; { &nbsp; &nbsp; GeometryInstance gInstance &nbsp; &nbsp; &nbsp; = obj as GeometryInstance; &nbsp; &nbsp; &nbsp; if( null != gInstance ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return fetchSomeMeshTransformed( &nbsp; &nbsp; &nbsp; &nbsp; gInstance.SymbolGeometry ); &nbsp; &nbsp; } &nbsp; } &nbsp; return null; }
```

```csharp
&nbsp; Debug.Print( &quot;Point without Transformation: &quot; &nbsp; &nbsp; + fetchSomeMesh( gElem ).Vertices[0].ToString() ); &nbsp; &nbsp; XYZ vertex = fetchSomeMesh( gElem, transform ).Vertices[0]; &nbsp; Debug.Print( &quot;Point when Transformed: &quot; + vertex.ToString() ); &nbsp; &nbsp; Debug.Print( &quot;Point when Transformed + inverse: &quot; &nbsp; &nbsp; + transform.Inverse.OfPoint( vertex ).ToString() ); &nbsp; &nbsp; Debug.Print( &quot;Point with ID Transformation: &quot; &nbsp; &nbsp; + fetchSomeMeshTransformed( gElem ).Vertices[0].ToString() ); &nbsp;
```
