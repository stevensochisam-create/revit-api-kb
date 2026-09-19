---
type: ElectricalDemandFactorDefinition
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 13
tags: [revit-api, class]
---

# ElectricalDemandFactorDefinition

`Autodesk.Revit.DB.Electrical.ElectricalDemandFactorDefinition` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | ElectricalDemandFactorDefinition | 2011 | `public ElectricalDemandFactorDefinition ()` |
| Method | AddValue | 2011 | `public void AddValue ( ElectricalDemandFactorValue dfValue )` |
| Method | ClearValues | 2011 | `public void ClearValues ()` |
| Method | Create | 2011 | `public static ElectricalDemandFactorDefinition Create ( Document ADoc , string strName )` |
| Method | GetApplicableDemandFactor | 2011 | `public double GetApplicableDemandFactor ( double numberOrLoad )` |
| Method | GetValues | 2011 | `public ICollection < ElectricalDemandFactorValue > GetValues ()` |
| Method | GetValuesCount | 2011 | `public int GetValuesCount ()` |
| Method | RemoveValue | 2011 | `public void RemoveValue ( ElectricalDemandFactorValue dfValue )` |
| Method | SetValues | 2011 | `public void SetValues ( ICollection < ElectricalDemandFactorValue > values )` |
| Property | AdditionalLoad | 2011 | `public double AdditionalLoad { get ; set ; }` |
| Property | IncludeAdditionalLoad | 2011 | `public bool IncludeAdditionalLoad { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | RuleType | 2011 | `public ElectricalDemandFactorRule RuleType { get ; set ; }` |