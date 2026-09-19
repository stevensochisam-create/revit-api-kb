---
type: RebarHostData
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 18
tags: [revit-api, class]
---

# RebarHostData

`Autodesk.Revit.DB.Structure.RebarHostData` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetAreaReinforcementsInHost | 2012 | `public IList < AreaReinforcement > GetAreaReinforcementsInHost ()` |
| Method | GetCommonCoverType | 2012 | `public RebarCoverType GetCommonCoverType ()` |
| Method | GetCoverType | — | `public RebarCoverType GetCoverType ( Reference face )` |
| Method | GetExposedFaces | 2012 | `public IList < Reference > GetExposedFaces ()` |
| Method | GetFabricAreasInHost | 2013 | `public IList < FabricArea > GetFabricAreasInHost ()` |
| Method | GetFabricSheetsInHost | 2015 | `public IList < FabricSheet > GetFabricSheetsInHost ()` |
| Method | GetPathReinforcementsInHost | 2012 | `public IList < PathReinforcement > GetPathReinforcementsInHost ()` |
| Method | GetRebarContainersInHost | 2016 | `public IList < RebarContainer > GetRebarContainersInHost ()` |
| Method | GetRebarHostData | — | `public static RebarHostData GetRebarHostData ( Element host )` |
| Method | GetRebarsInHost | 2012 | `public IList < Rebar > GetRebarsInHost ()` |
| Method | IsFaceExposed | 2012 | `public bool IsFaceExposed ( Reference face )` |
| Method | IsReferenceContainedByAValidHost | 2023 | `public static bool IsReferenceContainedByAValidHost ( Document doc , Reference reference )` |
| Method | IsValidHost | — | `` |
| Method | IsValidHost | 2012 | `public bool IsValidHost ()` |
| Method | SetCommonCoverType | 2012 | `public void SetCommonCoverType ( RebarCoverType coverType )` |
| Method | SetCoverType | — | `public void SetCoverType ( Reference face , RebarCoverType coverType )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |