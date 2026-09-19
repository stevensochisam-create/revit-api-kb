---
type: PanelScheduleView
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 45
tags: [revit-api, class]
---

# PanelScheduleView

`Autodesk.Revit.DB.Electrical.PanelScheduleView` · Revit 2024 · 45 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddSpace | 2018 | `public void AddSpace ( int nRow , int nCol )` |
| Method | AddSpare | 2018 | `public void AddSpare ( int nRow , int nCol )` |
| Method | CanMoveSlotTo | — | `public bool CanMoveSlotTo ( int nMovingRow , int nMovingCol , int nToRow , int nToCol )` |
| Method | CreateInstanceView | — | `` |
| Method | GenerateInstanceFromTemplate | — | `public void GenerateInstanceFromTemplate ( ElementId templateId )` |
| Method | GetApparentPhaseValue | — | `public double GetApparentPhaseValue ( ElementId circuitId , ElementId apparentLoadParam )` |
| Method | GetCellsBySlotNumber | — | `public void GetCellsBySlotNumber ( int nSlotNumber , out IList < int > RowArr , out IList < int > ColArr )` |
| Method | GetCircuitByCell | — | `public ElectricalSystem GetCircuitByCell ( int nRow , int nCol )` |
| Method | GetCircuitIdByCell | — | `public ElementId GetCircuitIdByCell ( int nRow , int nCol )` |
| Method | GetCombinedParamValue | — | `public string GetCombinedParamValue ( SectionType sectionType , int nRow , int nCol )` |
| Method | GetLoadClassificationConnectedCurrent | — | `public string GetLoadClassificationConnectedCurrent ( int nRow , int nCol )` |
| Method | GetLoadClassificationConnectedLoad | — | `public string GetLoadClassificationConnectedLoad ( int nRow , int nCol )` |
| Method | GetLoadClassificationDemandCurrent | — | `public string GetLoadClassificationDemandCurrent ( int nRow , int nCol )` |
| Method | GetLoadClassificationDemandFactor | — | `public string GetLoadClassificationDemandFactor ( int nRow , int nCol )` |
| Method | GetLoadClassificationDemandLoad | — | `public string GetLoadClassificationDemandLoad ( int nRow , int nCol )` |
| Method | GetLoadClassificationId | — | `public ElementId GetLoadClassificationId ( int nRow )` |
| Method | GetLoadClassificationName | — | `public string GetLoadClassificationName ( int nRow , int nCol )` |
| Method | GetLoadClassificationParamValue | — | `public string GetLoadClassificationParamValue ( ElementId parameterId , int nRow , int nCol )` |
| Method | GetPanel | — | `public ElementId GetPanel ()` |
| Method | GetParamValue | — | `public string GetParamValue ( SectionType sectionType , int nRow , int nCol )` |
| Method | GetSectionData | — | `public TableSectionData GetSectionData ( SectionType sectionType )` |
| Method | GetSlotNumberByCell | — | `public int GetSlotNumberByCell ( int nRow , int nCol )` |
| Method | GetSpareCurrentValue | 2013 | `public double GetSpareCurrentValue ( int row , int column , ElementId idCurrentParameter )` |
| Method | GetSpareLoadValue | 2013 | `public double GetSpareLoadValue ( int row , int column , ElementId idLoadParameter )` |
| Method | GetTableData | — | `public PanelScheduleData GetTableData ()` |
| Method | GetTemplate | — | `public ElementId GetTemplate ()` |
| Method | IsCellInPhaseLoads | — | `public bool IsCellInPhaseLoads ( int nRow , int nCol )` |
| Method | IsColumnInLoadSummary | — | `public bool IsColumnInLoadSummary ( int nCol )` |
| Method | IsPanelScheduleTemplate | — | `public bool IsPanelScheduleTemplate ()` |
| Method | IsRowInCircuitTable | — | `public bool IsRowInCircuitTable ( int nRow )` |
| Method | IsSlotGrouped | — | `public int IsSlotGrouped ( int nRow , int nCol )` |
| Method | IsSlotLocked | — | `public bool IsSlotLocked ( int nRow , int nCol )` |
| Method | IsSpace | — | `public bool IsSpace ( int nRow , int nCol )` |
| Method | IsSpare | — | `public bool IsSpare ( int nRow , int nCol )` |
| Method | MoveSlotTo | — | `public void MoveSlotTo ( int nMovingRow , int nMovingCol , int nToRow , int nToCol )` |
| Method | Print | — | `` |
| Method | RemoveSpace | 2018 | `public void RemoveSpace ( int nRow , int nCol )` |
| Method | RemoveSpare | 2018 | `public void RemoveSpare ( int nRow , int nCol )` |
| Method | RenumberIndexes | 2021 | `public void RenumberIndexes ()` |
| Method | SetLockSlot | 2023 | `public void SetLockSlot ( int nRow , int nCol , bool bLock )` |
| Method | SetParamValue | — | `public bool SetParamValue ( SectionType sectionType , int nRow , int nCol , string sValue )` |
| Method | SetSpareCurrentValue | 2013 | `public void SetSpareCurrentValue ( int row , int column , ElementId idCurrentParameter , double value )` |
| Method | SetSpareLoadValue | 2013 | `public void SetSpareLoadValue ( int row , int column , ElementId idLoadParameter , double value )` |
| Method | SwitchPhases | 2021 | `public void SwitchPhases ( int nRow , int nCol )` |
| Property | Parameter | — | `` |