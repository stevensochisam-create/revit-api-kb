---
type: StructuralConnectionHandler
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 19
tags: [revit-api, class]
---

# StructuralConnectionHandler

`Autodesk.Revit.DB.Structure.StructuralConnectionHandler` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddElementIds | 2017 | `public void AddElementIds ( IList < ElementId > elemIds )` |
| Method | AddReferences | 2017 | `public void AddReferences ( Document document , IList < Reference > picks )` |
| Method | Create | — | `` |
| Method | CreateGenericConnection | 2021 | `public static StructuralConnectionHandler CreateGenericConnection ( Document document , IList < ElementId > idsToConnect )` |
| Method | GetConnectedElementIds | 2017 | `public IList < ElementId > GetConnectedElementIds ()` |
| Method | GetInputPoint | 2017 | `public ConnectionInputPoint GetInputPoint ( Guid id )` |
| Method | GetInputPoints | 2017 | `public IList < ConnectionInputPoint > GetInputPoints ()` |
| Method | GetInputReferences | 2017 | `public IList < Reference > GetInputReferences ()` |
| Method | GetOrigin | 2017 | `public XYZ GetOrigin ()` |
| Method | IsCustom | 2019 | `public bool IsCustom ()` |
| Method | IsDetailed | 2017 | `public bool IsDetailed ()` |
| Method | RemoveElementIds | 2017 | `public void RemoveElementIds ( IList < ElementId > elemIds )` |
| Method | RemoveReferences | 2017 | `public void RemoveReferences ( IList < Reference > picks )` |
| Method | SetDefaultElementOrder | 2017 | `public void SetDefaultElementOrder ()` |
| Property | ApprovalTypeId | 2017 | `public ElementId ApprovalTypeId { get ; set ; }` |
| Property | CodeCheckingStatus | 2017 | `public StructuralConnectionCodeCheckingStatus CodeCheckingStatus { get ; set ; }` |
| Property | OverrideTypeParams | 2020 | `public bool OverrideTypeParams { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SingleElementEndIndex | 2017 | `public int SingleElementEndIndex { get ; set ; }` |