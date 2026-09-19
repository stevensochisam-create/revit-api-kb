---
num: 337
date: 2010-04-09
themes: [Geometry]
tags: [revit-api, tbc]
---

# Beam Requires Curve

<https://jeremytammik.github.io/tbc/a/0337_beam_requires_curve.htm>

```csharp
&nbsp; Level level; &nbsp; FamilySymbol symbol; &nbsp; double x1, y1, x2, y2; &nbsp; XYZ p = new XYZ( x1, y1, level.Elevation ); &nbsp; XYZ q = new XYZ( x2, y2, level.Elevation ); &nbsp; &nbsp; Autodesk.Revit.DB.Structure.StructuralType st &nbsp; &nbsp; = Autodesk.Revit.DB.Structure.StructuralType.Beam; &nbsp; &nbsp; FamilyInstance beam = doc.Create.NewFamilyInstance( &nbsp; &nbsp; p, symbol, level, st ); &nbsp; &nbsp; LocationCurve beamCurve = beam.Location &nbsp; &nbsp; as LocationCurve; &nbsp; &nbsp; if( null != beamCurve ) &nbsp; { &nbsp; &nbsp; Line line = app.Create.NewLineBound( p, q ); &nbsp; &nbsp; beamCurve.Curve = line; &nbsp; }
```

```csharp
&nbsp; Curve useCurve = app.Create.NewLineBound( p, q ); &nbsp; beam = doc.Create.NewFamilyInstance( &nbsp; &nbsp; useCurve, symbol, level, st );
```
