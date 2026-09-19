---
type: PathReinforcement
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 20
tags: [revit-api, class]
---

# PathReinforcement

`Autodesk.Revit.DB.Structure.PathReinforcement` · Revit 2024 · 20 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ConvertRebarInSystemToRebars | 2022 | `public static IList < ElementId > ConvertRebarInSystemToRebars ( Document doc , PathReinforcement system )` |
| Method | Create | — | `` |
| Method | GetCurveElementIds | — | `public IList < ElementId > GetCurveElementIds ()` |
| Method | GetHostId | — | `public ElementId GetHostId ()` |
| Method | GetOrCreateDefaultRebarShape | 2016 | `public static ElementId GetOrCreateDefaultRebarShape ( Document document , ElementId rebarBarTypeId , ElementId startRebarHookTypeId , ElementId endRebarHookTypeId )` |
| Method | GetRebarInSystemIds | 2013 | `public IList < ElementId > GetRebarInSystemIds ()` |
| Method | IsAlternatingLayerEnabled | 2016 | `public bool IsAlternatingLayerEnabled ()` |
| Method | IsUnobscuredInView | 2014 | `public bool IsUnobscuredInView ( View view )` |
| Method | IsValidAlternatingBarOrientation | 2016 | `public bool IsValidAlternatingBarOrientation ( ReinforcementBarOrientation orientation )` |
| Method | IsValidPrimaryBarOrientation | 2016 | `public bool IsValidPrimaryBarOrientation ( ReinforcementBarOrientation orientation )` |
| Method | IsValidRebarShapeId | — | `public static bool IsValidRebarShapeId ( Document aDoc , ElementId elementId )` |
| Method | RemovePathReinforcementSystem | 2013 | `public static IList < ElementId > RemovePathReinforcementSystem ( Document doc , PathReinforcement system )` |
| Method | SetUnobscuredInView | 2014 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | AdditionalOffset | 2014 | `public double AdditionalOffset { get ; set ; }` |
| Property | AlternatingBarOrientation | 2016 | `public ReinforcementBarOrientation AlternatingBarOrientation { get ; set ; }` |
| Property | AlternatingBarShapeId | 2016 | `public ElementId AlternatingBarShapeId { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | PathReinforcementType | — | `public PathReinforcementType PathReinforcementType { get ; }` |
| Property | PrimaryBarOrientation | 2016 | `public ReinforcementBarOrientation PrimaryBarOrientation { get ; set ; }` |
| Property | PrimaryBarShapeId | 2016 | `public ElementId PrimaryBarShapeId { get ; set ; }` |