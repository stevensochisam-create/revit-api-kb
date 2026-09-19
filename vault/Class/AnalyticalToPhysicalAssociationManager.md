---
type: AnalyticalToPhysicalAssociationManager
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 10
tags: [revit-api, class]
---

# AnalyticalToPhysicalAssociationManager

`Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager` · Revit 2024 · 10 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddAssociation | — | `` |
| Method | GetAnalyticalToPhysicalAssociationManager | 2023 | `public static AnalyticalToPhysicalAssociationManager GetAnalyticalToPhysicalAssociationManager ( Document doc )` |
| Method | GetAssociatedElementId | 2023 | `public ElementId GetAssociatedElementId ( ElementId elementId )` |
| Method | GetAssociatedElementIds | 2024 | `public ISet < ElementId > GetAssociatedElementIds ( ElementId elementId )` |
| Method | HasAssociation | 2023 | `public bool HasAssociation ( ElementId id )` |
| Method | IsAnalyticalElement | 2023 | `public static bool IsAnalyticalElement ( Document doc , ElementId id )` |
| Method | IsPhysicalElement | 2023 | `public static bool IsPhysicalElement ( Document doc , ElementId id )` |
| Method | RemoveAssociation | 2023 | `public void RemoveAssociation ( ElementId id )` |
| Property | EnableAssistedAssociation | 2023 | `public static bool EnableAssistedAssociation { get ; set ; }` |
| Property | Parameter | — | `` |