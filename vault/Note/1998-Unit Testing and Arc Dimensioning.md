---
num: 1998
date: 2023-06-20
themes: [Units]
tags: [revit-api, tbc]
---

# Unit Testing and Arc Dimensioning

<https://jeremytammik.github.io/tbc/a/1998_unittest_arcdim.html>

```csharp
arc = Arc.Create(p - vw2, p + vh2, p + vw2); curve = doc.Create.NewModelCurve( arc, sketchPlane); arc = Arc.Create(p + vw2, p - vh2, p - vw2); curve = doc.Create.NewModelCurve(arc, sketchPlane);
```

```csharp
arc = Arc.Create(p - vw2, p + vh2, p + vw2); curve = doc.Create.NewModelCurve( arc, sketchPlane); // Vertical ra.Clear(); ra.Append(mc_front_left.GeometryCurve.GetEndPointReference(0)); ra.Append(curve.GeometryCurve.GetEndPointReference(0)); ra.Append(curve.GeometryCurve.GetEndPointReference(1)); ra.Append(mc_front_left.GeometryCurve.GetEndPointReference(1)); doc.Create.NewDimension(viewForDimension, Line.CreateUnbound(pVert, vz), ra); // Horizontal ra.Clear(); ra.Append(ductEdgeForDimHor.GeometryCurve.GetEndPointReference(0)); ra.Append(curve.GeometryCurve.GetEndPointReference(0)); ra.Append(curve.GeometryCurve.GetEndPointReference(1)); ra.Append(ductEdgeForDimHor.GeometryCurve.GetEndPointReference(1)); doc.Create.NewDimension(viewForDimension, Line.CreateUnbound(pHor, vHor), ra);
```

```csharp
arc = Arc.Create(p - vw2, p + vh2, p + vw2); curve = doc.Create.NewModelCurve( arc, sketchPlane); Reference r1 = curve.GeometryCurve.GetEndPointReference(0); arc = Arc.Create(p + vw2, p - vh2, p - vw2); curve = doc.Create.NewModelCurve(arc, sketchPlane); Reference r2 = curve.GeometryCurve.GetEndPointReference(0); // Vertical ra.Clear(); ra.Append(mc_front_left.GeometryCurve.GetEndPointReference(0)); ra.Append(r1); ra.Append(r2); ra.Append(mc_front_left.GeometryCurve.GetEndPointReference(1)); doc.Create.NewDimension(viewForDimension, Line.CreateUnbound(pVert, vz), ra); // Horizontal ra.Clear(); ra.Append(ductEdgeForDimHor.GeometryCurve.GetEndPointReference(0)); ra.Append(r1); ra.Append(r2); ra.Append(ductEdgeForDimHor.GeometryCurve.GetEndPointReference(1)); doc.Create.NewDimension(viewForDimension, Line.CreateUnbound(pHor, vHor), ra);
```

```csharp
arc = Arc.Create(p - vw2, p + vh2, p + vw2); curve = doc.Create.NewModelCurve( arc, sketchPlane); Reference a0r0 = curve.GeometryCurve.GetEndPointReference(0); Reference a0r1 = curve.GeometryCurve.GetEndPointReference(1); arc = Arc.Create(p + vw2, p - vh2, p - vw2); curve = doc.Create.NewModelCurve(arc, sketchPlane); Reference a1r0 = curve.GeometryCurve.GetEndPointReference(0); Reference a1r1 = curve.GeometryCurve.GetEndPointReference(1); // Vertical ra.Clear(); ra.Append(mc_front_left.GeometryCurve.GetEndPointReference(0)); ra.Append(a0r0); ra.Append(a1r0); ra.Append(mc_front_left.GeometryCurve.GetEndPointReference(1)); doc.Create.NewDimension(viewForDimension, Line.CreateUnbound(pVert, vz), ra); // Horizontal ra.Clear(); ra.Append(ductEdgeForDimHor.GeometryCurve.GetEndPointReference(0)); ra.Append(a0r1); ra.Append(a1r1); ra.Append(ductEdgeForDimHor.GeometryCurve.GetEndPointReference(1)); doc.Create.NewDimension(viewForDimension, Line.CreateUnbound(pHor, vHor), ra);
```
