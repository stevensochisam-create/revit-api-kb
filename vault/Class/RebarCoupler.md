---
type: RebarCoupler
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 11
tags: [revit-api, class]
---

# RebarCoupler

`Autodesk.Revit.DB.Structure.RebarCoupler` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CouplerLinkTwoBars | 2017 | `public bool CouplerLinkTwoBars ()` |
| Method | Create | 2017 | `public static RebarCoupler Create ( Document doc , ElementId typeId , ReinforcementData pFirstData , ReinforcementData pSecondData , out RebarCouplerError error )` |
| Method | GetCoupledReinforcementData | 2017 | `public IList < ReinforcementData > GetCoupledReinforcementData ()` |
| Method | GetCouplerPositionTransform | 2017 | `public Transform GetCouplerPositionTransform ( int couplerPositionIndex )` |
| Method | GetCouplerQuantity | 2017 | `public int GetCouplerQuantity ()` |
| Method | GetPointsForPlacement | 2017 | `public IList < XYZ > GetPointsForPlacement ()` |
| Method | IsUnobscuredInView | 2018.3 | `public bool IsUnobscuredInView ( View view )` |
| Method | SetUnobscuredInView | 2018.3 | `public void SetUnobscuredInView ( View view , bool unobscured )` |
| Property | CouplerMark | 2017 | `public string CouplerMark { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RotationAngle | 2023 | `public double RotationAngle { get ; set ; }` |