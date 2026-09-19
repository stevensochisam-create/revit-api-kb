---
type: AnalyticalMember
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 15
tags: [revit-api, class]
---

# AnalyticalMember

`Autodesk.Revit.DB.Structure.AnalyticalMember` · Revit 2024 · 15 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2023 | `public static AnalyticalMember Create ( Document aDoc , Curve curve )` |
| Method | FlipCurve | 2023 | `public void FlipCurve ()` |
| Method | GetMemberForces | 2023 | `public IList < MemberForces > GetMemberForces ()` |
| Method | GetReleaseConditions | 2023 | `public IList < ReleaseConditions > GetReleaseConditions ()` |
| Method | GetReleaseType | 2023 | `public ReleaseType GetReleaseType ( bool start )` |
| Method | IsValidCurve | 2023 | `public static bool IsValidCurve ( Curve curve )` |
| Method | IsValidSectionTypeId | 2023 | `public bool IsValidSectionTypeId ( ElementId familySymbolId )` |
| Method | SetCurve | 2023 | `public void SetCurve ( Curve curve )` |
| Method | SetMemberForces | — | `` |
| Method | SetReleaseConditions | 2023 | `public void SetReleaseConditions ( ReleaseConditions releaseConditions )` |
| Method | SetReleaseType | 2023 | `public void SetReleaseType ( bool start , ReleaseType releaseType )` |
| Property | CrossSectionRotation | 2023 | `public double CrossSectionRotation { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SectionTypeId | 2023 | `public ElementId SectionTypeId { get ; set ; }` |
| Property | StructuralSectionShape | 2023 | `public StructuralSectionShape StructuralSectionShape { get ; }` |