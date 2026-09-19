---
type: AreaReinforcement
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 23
tags: [revit-api, class]
---

# AreaReinforcement

`Autodesk.Revit.DB.Structure.AreaReinforcement` · Revit 2024 · 23 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ConvertRebarInSystemToRebars | 2022 | `public static IList < ElementId > ConvertRebarInSystemToRebars ( Document doc , AreaReinforcement system )` |
| Method | Create | — | `` |
| Method | GetBoundaryCurveIds | 2015 | `public IList < ElementId > GetBoundaryCurveIds ()` |
| Method | GetHostId | — | `public ElementId GetHostId ()` |
| Method | GetLayerDirection | 2022 | `public XYZ GetLayerDirection ( AreaReinforcementLayerType layer )` |
| Method | GetLineFromLayerAtIndex | 2022 | `public Line GetLineFromLayerAtIndex ( AreaReinforcementLayerType layer , int linePositionIndex )` |
| Method | GetMovedLineTransform | 2022 | `public Transform GetMovedLineTransform ( AreaReinforcementLayerType layer , int linePositionIndex )` |
| Method | GetNumberOfLines | 2022 | `public int GetNumberOfLines ( AreaReinforcementLayerType layer )` |
| Method | GetRebarInSystemIds | 2013 | `public IList < ElementId > GetRebarInSystemIds ()` |
| Method | IsLayerActive | 2022 | `public bool IsLayerActive ( AreaReinforcementLayerType layer )` |
| Method | IsLineIncluded | 2022 | `public bool IsLineIncluded ( AreaReinforcementLayerType layer , int linePositionIndex )` |
| Method | IsUnobscuredInView | 2014 | `public bool IsUnobscuredInView ( View view )` |
| Method | MoveLine | 2022 | `public void MoveLine ( XYZ translation , AreaReinforcementLayerType layer , int linePositionIndex )` |
| Method | RemoveAreaReinforcementSystem | 2013 | `public static IList < ElementId > RemoveAreaReinforcementSystem ( Document doc , AreaReinforcement system )` |
| Method | ResetMovedLineTransform | 2022 | `public void ResetMovedLineTransform ( AreaReinforcementLayerType layer , int linePositionIndex )` |
| Method | SetLayerActive | 2022 | `public void SetLayerActive ( bool active , AreaReinforcementLayerType layer )` |
| Method | SetLineIncluded | 2022 | `public void SetLineIncluded ( bool include , AreaReinforcementLayerType layer , int linePositionIndex )` |
| Method | SetUnobscuredInView | 2014 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | AdditionalBottomCoverOffset | 2013 | `public double AdditionalBottomCoverOffset { get ; set ; }` |
| Property | AdditionalTopCoverOffset | 2013 | `public double AdditionalTopCoverOffset { get ; set ; }` |
| Property | AreaReinforcementType | — | `public AreaReinforcementType AreaReinforcementType { get ; }` |
| Property | Direction | — | `public XYZ Direction { get ; }` |
| Property | Parameter | — | `` |