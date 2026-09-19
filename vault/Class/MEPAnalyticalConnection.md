---
type: MEPAnalyticalConnection
namespace: Autodesk.Revit.DB
version: 2024
members: 5
tags: [revit-api, class]
---

# MEPAnalyticalConnection

`Autodesk.Revit.DB.MEPAnalyticalConnection` · Revit 2024 · 5 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanSupportAnalyticalConnection | 2018 | `public static bool CanSupportAnalyticalConnection ( Connector connector )` |
| Method | Create | 2018 | `public static MEPAnalyticalConnection Create ( Document doc , ElementId typeId , Connector startConnector , Connector endConnector )` |
| Method | CreateMultipleConnections | 2018 | `public static ISet < ElementId > CreateMultipleConnections ( Document doc , ElementId typeId , IList < Connector > equipmentOpenConnectors , IList < ElementId > curveIdsToConnect )` |
| Method | GetFlow | 2018 | `public double GetFlow ()` |
| Property | Parameter | — | `` |