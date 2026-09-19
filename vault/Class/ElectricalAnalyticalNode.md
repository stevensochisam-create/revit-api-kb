---
type: ElectricalAnalyticalNode
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 12
tags: [revit-api, class]
---

# ElectricalAnalyticalNode

`Autodesk.Revit.DB.Electrical.ElectricalAnalyticalNode` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanConnectToUpstreamNode | 2023 | `public bool CanConnectToUpstreamNode ( ElementId upstreamNodeId )` |
| Method | CanDisconnectFromUpstreamNode | 2023 | `public bool CanDisconnectFromUpstreamNode ( ElementId upstreamNodeId )` |
| Method | ConnectToUpstreamNode | 2023 | `public void ConnectToUpstreamNode ( ElementId upstreamNodeId )` |
| Method | Create | 2023 | `public static ElectricalAnalyticalNode Create ( Document document , ElectricalAnalyticalNodeType type , string name )` |
| Method | DisconnectFromUpstreamNode | 2023 | `public void DisconnectFromUpstreamNode ( ElementId upstreamNodeId )` |
| Method | GetAllDownstreamLoadIds | 2024 | `public ISet < ElementId > GetAllDownstreamLoadIds ()` |
| Method | GetAnalyticalPropertyData | 2023 | `public AnalyticalDistributionNodePropertyData GetAnalyticalPropertyData ()` |
| Method | GetDownstreamNodeIds | 2023 | `public IList < ElementId > GetDownstreamNodeIds ()` |
| Method | GetUpstreamNodeIds | 2023 | `public IList < ElementId > GetUpstreamNodeIds ()` |
| Property | NodeType | 2023 | `public ElectricalAnalyticalNodeType NodeType { get ; }` |
| Property | Parameter | — | `` |
| Property | TotalLoad | 2023 | `public double TotalLoad { get ; }` |