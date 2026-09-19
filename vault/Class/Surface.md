---
type: Surface
namespace: Autodesk.Revit.DB
version: 2024
members: 6
tags: [revit-api, class]
---

# Surface

`Autodesk.Revit.DB.Surface` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetBoundingBoxUV | 2021 | `public BoundingBoxUV GetBoundingBoxUV ()` |
| Method | Project | 2018.1 | `public void Project ( XYZ point , out UV uv , out double distance )` |
| Method | ProjectWithGuessPoint | 2018.1 | `public void ProjectWithGuessPoint ( XYZ point , UV guessUV , out UV uv , out double distance )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | OrientationMatchesParametricOrientation | 2018 | `public bool OrientationMatchesParametricOrientation { get ; }` |