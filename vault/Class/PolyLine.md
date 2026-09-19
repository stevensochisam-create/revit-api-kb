---
type: PolyLine
namespace: Autodesk.Revit.DB
version: 2024
members: 8
tags: [revit-api, class]
---

# PolyLine

`Autodesk.Revit.DB.PolyLine` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Clone | — | `public PolyLine Clone ()` |
| Method | Create | — | `public static PolyLine Create ( IList < XYZ > coordinates )` |
| Method | Evaluate | — | `public XYZ Evaluate ( double param )` |
| Method | GetCoordinate | — | `public XYZ GetCoordinate ( int index )` |
| Method | GetCoordinates | — | `public IList < XYZ > GetCoordinates ()` |
| Method | GetOutline | — | `public Outline GetOutline ()` |
| Method | GetTransformed | — | `public PolyLine GetTransformed ( Transform transform )` |
| Property | NumberOfCoordinates | — | `public int NumberOfCoordinates { get ; }` |