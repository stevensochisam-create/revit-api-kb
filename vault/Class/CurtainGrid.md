---
type: CurtainGrid
namespace: Autodesk.Revit.DB
version: 2024
members: 20
tags: [revit-api, class]
---

# CurtainGrid

`Autodesk.Revit.DB.CurtainGrid` · Revit 2024 · 20 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddGridLine | — | `public CurtainGridLine AddGridLine ( bool isUGridLine , XYZ position , bool oneSegmentOnly )` |
| Method | ChangePanelType | — | `public Element ChangePanelType ( Element panel , ElementType newSymbol )` |
| Method | GetCell | — | `public CurtainCell GetCell ( ElementId uGridLineId , ElementId vGridLineId )` |
| Method | GetCurtainCells | — | `public ICollection < CurtainCell > GetCurtainCells ()` |
| Method | GetMullionIds | — | `public ICollection < ElementId > GetMullionIds ()` |
| Method | GetPanel | — | `public Panel GetPanel ( ElementId uGridLineId , ElementId vGridLineId )` |
| Method | GetPanelIds | — | `public ICollection < ElementId > GetPanelIds ()` |
| Method | GetUGridLineIds | — | `public ICollection < ElementId > GetUGridLineIds ()` |
| Method | GetUnlockedMullionIds | — | `public ICollection < ElementId > GetUnlockedMullionIds ()` |
| Method | GetUnlockedPanelIds | — | `public ICollection < ElementId > GetUnlockedPanelIds ()` |
| Method | GetVGridLineIds | — | `public ICollection < ElementId > GetVGridLineIds ()` |
| Property | Grid1Angle | — | `public double Grid1Angle { get ; set ; }` |
| Property | Grid1Justification | — | `public CurtainGridAlignType Grid1Justification { get ; set ; }` |
| Property | Grid1Offset | — | `public double Grid1Offset { get ; set ; }` |
| Property | Grid2Angle | — | `public double Grid2Angle { get ; set ; }` |
| Property | Grid2Justification | — | `public CurtainGridAlignType Grid2Justification { get ; set ; }` |
| Property | Grid2Offset | — | `public double Grid2Offset { get ; set ; }` |
| Property | NumPanels | — | `public int NumPanels { get ; }` |
| Property | NumULines | — | `public int NumULines { get ; }` |
| Property | NumVLines | — | `public int NumVLines { get ; }` |