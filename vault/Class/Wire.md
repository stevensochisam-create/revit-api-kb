---
type: Wire
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 16
tags: [revit-api, class]
---

# Wire

`Autodesk.Revit.DB.Electrical.Wire` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AppendVertex | 2015 | `public void AppendVertex ( XYZ vertexPoint )` |
| Method | AreVertexPointsValid | 2015 | `public static bool AreVertexPointsValid ( IList < XYZ > vertexPoints , Connector startConnector , Connector endConnector )` |
| Method | ConnectTo | 2015 | `public void ConnectTo ( Connector startConnectorTo , Connector endConnectorTo )` |
| Method | Create | 2015 | `public static Wire Create ( Document document , ElementId wireTypeId , ElementId viewId , WiringType wiringType , IList < XYZ > vertexPoints , Connector startConnectorTo , Connector endConnectorTo )` |
| Method | GetMEPSystems | 2016 Subscription Update | `public IList < ElementId > GetMEPSystems ()` |
| Method | GetVertex | 2015 | `public XYZ GetVertex ( int index )` |
| Method | InsertVertex | 2015 | `public void InsertVertex ( int index , XYZ vertexPoint )` |
| Method | IsVertexPointValid | 2015 | `public bool IsVertexPointValid ( XYZ vertexPoint )` |
| Method | RemoveVertex | 2015 | `public void RemoveVertex ( int index )` |
| Method | SetVertex | 2015 | `public void SetVertex ( int index , XYZ vertexPoint )` |
| Property | GroundConductorNum | — | `public int GroundConductorNum { get ; set ; }` |
| Property | HotConductorNum | — | `public int HotConductorNum { get ; set ; }` |
| Property | NeutralConductorNum | — | `public int NeutralConductorNum { get ; set ; }` |
| Property | NumberOfVertices | 2015 | `public int NumberOfVertices { get ; }` |
| Property | Parameter | — | `` |
| Property | WiringType | — | `public WiringType WiringType { get ; set ; }` |