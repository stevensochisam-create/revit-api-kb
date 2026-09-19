---
num: 1997
date: 2023-06-13
themes: [Geometry]
tags: [revit-api, tbc]
---

# BRepBuilder and Toposurface Interior

<https://jeremytammik.github.io/tbc/a/1997_sdk_brep.html>

```csharp
public class Test{ public Test(){} // Keep track of already created edges and their orientation struct BrepEdge { public BRepBuilderGeometryId id; public XYZ p1, p2; } List&lt;BrepEdge&gt; brep_edges = new List&lt;BrepEdge&gt;(); // add edge to face loop void AddEdgeToBREP( BRepBuilder brep, BRepBuilderGeometryId loop, XYZ a, XYZ b) { foreach(var be in brep_edges) { // ab is p1-p2 if(be.p1.DistanceTo(a) &lt; 1e-7 && be.p2.DistanceTo(b) &lt; 1e-7) { brep.AddCoEdge(loop, be.id, false);return; } // ab is p2-p1 (reversed edge) if(be.p1.DistanceTo(b) &lt; 1e-7 && be.p2.DistanceTo(a) &lt; 1e-7) { brep.AddCoEdge(loop, be.id, true); return; } } // must create a new edge BRepBuilderGeometryId edge = brep.AddEdge(BRepBuilderEdgeGeometry.Create(a, b)); brep.AddCoEdge(loop, edge, false); var bed = new BrepEdge(); bed.p1 = a; bed.p2 = b; bed.id = edge; brep_edges.Add(bed); } // add triangle face to solid private void AddTriangleToBREP( BRepBuilder brep, XYZ a, XYZ b, XYZ c ) { Plane plane = Plane.CreateByThreePoints(a, b, c); BRepBuilderGeometryId face = brep.AddFace(BRepBuilderSurfaceGeometry.Create(plane, null), true); var loop = brep.AddLoop(face); AddEdgeToBREP(brep, loop, a, b); AddEdgeToBREP(brep, loop, b, c); AddEdgeToBREP(brep, loop, c, a); brep.FinishLoop(loop); brep.FinishFace(face); } public void run() { BRepBuilder brep = new BRepBuilder(BRepType.Solid); var points = new List&lt;XYZ&gt;(4); points.Add(new XYZ(0, 0, 0)); // 0 origin points.Add(new XYZ(1, 0, 0)); // 1 right points.Add(new XYZ(0, 1, 0)); // 2 back points.Add(new XYZ(0, 0, 1)); // 3 top AddTriangleToBREP(brep, points[2], points[1], points[0]); // bottom face AddTriangleToBREP(brep, points[0], points[1], points[3]); // front face AddTriangleToBREP(brep, points[1], points[2], points[3]); // diagonal face AddTriangleToBREP(brep, points[2], points[0], points[3]); // left face var outcome = brep.Finish(); // &lt;&lt;&lt;&lt;&lt; Failure // throws: "This BRepBuilder object hasn't completed building data or was unsuccessful building it. // Built Geometry is unavailable. In order to access the built Geometry, // Finish() must be called first. That will set the state to completed." var res = brep.GetResult(); } }
```

```csharp
var shapeBuilder = TessellatedShapeCreatorUtils.Create( builder =&gt; { var points = new List&lt;XYZ&gt;(4); points.Add(new XYZ(0, 0, 0)); // 0 origin points.Add(new XYZ(1, 0, 0)); // 1 right points.Add(new XYZ(0, 1, 0)); // 2 back points.Add(new XYZ(0, 0, 1)); // 3 top var materialId = ElementId.InvalidElementId; // bottom face builder.AddFace(new TessellatedFace(new[] { points[2], points[1], points[0] }, materialId)); // front face builder.AddFace(new TessellatedFace(new[] { points[0], points[1], points[3] }, materialId)); // diagonal face builder.AddFace(new TessellatedFace(new[] { points[1], points[2], points[3] }, materialId)); // left face builder.AddFace(new TessellatedFace(new[] { points[2], points[0], points[3] }, materialId)); });
```

```csharp
public static class TessellatedShapeCreatorUtils { public static TessellatedShapeBuilderResult Create( Action&lt;TessellatedShapeBuilder&gt; actionBuilder) { TessellatedShapeBuilder builder = new TessellatedShapeBuilder(); builder.Target = TessellatedShapeBuilderTarget.AnyGeometry; builder.Fallback = TessellatedShapeBuilderFallback.Mesh; builder.OpenConnectedFaceSet(true); actionBuilder?.Invoke(builder); builder.CloseConnectedFaceSet(); builder.Build(); TessellatedShapeBuilderResult result = builder.GetBuildResult(); return result; } }
```
