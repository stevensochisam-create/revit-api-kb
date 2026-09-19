---
type: MEPSystem
namespace: Autodesk.Revit.DB
version: 2024
members: 21
tags: [revit-api, class]
---

# MEPSystem

`Autodesk.Revit.DB.MEPSystem` · Revit 2024 · 21 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Add | — | `public virtual void Add ( ConnectorSet connectors )` |
| Method | DivideSystem | 2014 | `public ICollection < ElementId > DivideSystem ( Document ADoc )` |
| Method | GetCriticalPathSectionNumbers | 2013 | `public IList < int > GetCriticalPathSectionNumbers ()` |
| Method | GetPhysicalNetworksNumber | 2014 | `public int GetPhysicalNetworksNumber ()` |
| Method | GetSectionByIndex | 2013 | `public MEPSection GetSectionByIndex ( int index )` |
| Method | GetSectionByNumber | 2013 | `public MEPSection GetSectionByNumber ( int sectionNumber )` |
| Method | IsSystemDividable | 2014 | `public bool IsSystemDividable ()` |
| Method | Remove | — | `` |
| Property | BaseEquipment | — | `public FamilyInstance BaseEquipment { get ; }` |
| Property | BaseEquipmentConnector | — | `public Connector BaseEquipmentConnector { get ; }` |
| Property | ConnectorManager | — | `public ConnectorManager ConnectorManager { get ; }` |
| Property | Elements | — | `public ElementSet Elements { get ; }` |
| Property | HasDesignParts | 2015 | `public bool HasDesignParts { get ; }` |
| Property | HasFabricationParts | 2015 | `public bool HasFabricationParts { get ; }` |
| Property | HasPlaceholders | 2015 | `public bool HasPlaceholders { get ; }` |
| Property | IsEmpty | 2011 | `public bool IsEmpty { get ; }` |
| Property | IsMultipleNetwork | 2014 | `public bool IsMultipleNetwork { get ; }` |
| Property | IsValid | 2011 | `public bool IsValid { get ; }` |
| Property | Parameter | — | `` |
| Property | PressureLossOfCriticalPath | 2013 | `public double PressureLossOfCriticalPath { get ; }` |
| Property | SectionsCount | 2013 | `public int SectionsCount { get ; }` |