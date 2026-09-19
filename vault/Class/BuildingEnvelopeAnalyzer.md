---
type: BuildingEnvelopeAnalyzer
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 6
tags: [revit-api, class]
---

# BuildingEnvelopeAnalyzer

`Autodesk.Revit.DB.Analysis.BuildingEnvelopeAnalyzer` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2015 | `public static BuildingEnvelopeAnalyzer Create ( Document document , BuildingEnvelopeAnalyzerOptions options )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetBoundingElements | 2015 | `public IList < LinkElementId > GetBoundingElements ()` |
| Method | GetBoundingElementsForSpaceVolume | 2015 | `public IList < LinkElementId > GetBoundingElementsForSpaceVolume ( int spaceVolume )` |
| Method | GetCenterPointsForConnectedGridCellsInSpaceVolume | 2015 | `public IList < XYZ > GetCenterPointsForConnectedGridCellsInSpaceVolume ( int spaceVolume )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |