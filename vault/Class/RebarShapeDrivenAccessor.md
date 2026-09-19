---
type: RebarShapeDrivenAccessor
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 22
tags: [revit-api, class]
---

# RebarShapeDrivenAccessor

`Autodesk.Revit.DB.Structure.RebarShapeDrivenAccessor` · Revit 2024 · 22 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ComputeDrivingCurves | 2018 | `public IList < Curve > ComputeDrivingCurves ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FlipRebarSet | 2023.1 | `public void FlipRebarSet ()` |
| Method | GetBarPositionTransform | 2018 | `public Transform GetBarPositionTransform ( int barPositionIndex )` |
| Method | GetDistributionPath | 2018 | `public Line GetDistributionPath ()` |
| Method | ScaleToBox | 2018 | `public void ScaleToBox ( XYZ origin , XYZ xVec , XYZ yVec )` |
| Method | ScaleToBoxFor3D | 2018 | `public void ScaleToBoxFor3D ( XYZ origin , XYZ xVec , XYZ yVec , double height )` |
| Method | SetLayoutAsFixedNumber | 2018 | `public void SetLayoutAsFixedNumber ( int numberOfBarPositions , double arrayLength , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsMaximumSpacing | 2018 | `public void SetLayoutAsMaximumSpacing ( double spacing , double arrayLength , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsMinimumClearSpacing | 2018 | `public void SetLayoutAsMinimumClearSpacing ( double spacing , double arrayLength , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsNumberWithSpacing | 2018 | `public void SetLayoutAsNumberWithSpacing ( int numberOfBarPositions , double spacing , bool barsOnNormalSide , bool includeFirstBar , bool includeLastBar )` |
| Method | SetLayoutAsSingle | 2018 | `public void SetLayoutAsSingle ()` |
| Method | SetRebarShapeId | 2018 | `public void SetRebarShapeId ( ElementId shapeId )` |
| Property | ArrayLength | 2018 | `public double ArrayLength { get ; set ; }` |
| Property | BarsOnNormalSide | 2018 | `public bool BarsOnNormalSide { get ; set ; }` |
| Property | BaseFinishingTurns | 2018 | `public int BaseFinishingTurns { get ; set ; }` |
| Property | Height | 2018 | `public double Height { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MultiplanarDepth | 2018 | `public double MultiplanarDepth { get ; set ; }` |
| Property | Normal | 2018 | `public XYZ Normal { get ; }` |
| Property | Pitch | 2018 | `public double Pitch { get ; set ; }` |
| Property | TopFinishingTurns | 2018 | `public int TopFinishingTurns { get ; set ; }` |