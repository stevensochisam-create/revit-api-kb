---
type: Connector
namespace: Autodesk.Revit.DB
version: 2024
members: 48
tags: [revit-api, class]
---

# Connector

`Autodesk.Revit.DB.Connector` · Revit 2024 · 48 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | ConnectTo | — | `public void ConnectTo ( Connector connector )` |
| Method | DisconnectFrom | — | `public void DisconnectFrom ( Connector connector )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetFabricationConnectorInfo | 2016 | `public FabricationConnectorInfo GetFabricationConnectorInfo ()` |
| Method | GetMEPConnectorInfo | 2016 | `public MEPConnectorInfo GetMEPConnectorInfo ()` |
| Method | IsConnectedTo | — | `public bool IsConnectedTo ( Connector connector )` |
| Property | AllRefs | — | `public ConnectorSet AllRefs { get ; }` |
| Property | AllowsSlopeAdjustments | 2015 | `public bool AllowsSlopeAdjustments { get ; }` |
| Property | Angle | — | `public double Angle { get ; set ; }` |
| Property | AssignedDuctFlowConfiguration | — | `public DuctFlowConfigurationType AssignedDuctFlowConfiguration { get ; }` |
| Property | AssignedDuctLossMethod | — | `public DuctLossMethodType AssignedDuctLossMethod { get ; }` |
| Property | AssignedFixtureUnits | — | `public double AssignedFixtureUnits { get ; set ; }` |
| Property | AssignedFlow | — | `public double AssignedFlow { get ; set ; }` |
| Property | AssignedFlowDirection | — | `public FlowDirectionType AssignedFlowDirection { get ; }` |
| Property | AssignedFlowFactor | — | `public double AssignedFlowFactor { get ; set ; }` |
| Property | AssignedKCoefficient | — | `public double AssignedKCoefficient { get ; set ; }` |
| Property | AssignedLossCoefficient | — | `public double AssignedLossCoefficient { get ; set ; }` |
| Property | AssignedPipeFlowConfiguration | — | `public PipeFlowConfigurationType AssignedPipeFlowConfiguration { get ; }` |
| Property | AssignedPipeLossMethod | — | `public PipeLossMethodType AssignedPipeLossMethod { get ; }` |
| Property | AssignedPressureDrop | — | `public double AssignedPressureDrop { get ; set ; }` |
| Property | Coefficient | — | `public double Coefficient { get ; }` |
| Property | ConnectorManager | — | `public ConnectorManager ConnectorManager { get ; }` |
| Property | ConnectorType | — | `public ConnectorType ConnectorType { get ; }` |
| Property | CoordinateSystem | — | `public virtual Transform CoordinateSystem { get ; }` |
| Property | Demand | — | `public double Demand { get ; }` |
| Property | Description | 2015 | `public string Description { get ; }` |
| Property | Direction | — | `public FlowDirectionType Direction { get ; }` |
| Property | Domain | — | `public virtual Domain Domain { get ; }` |
| Property | DuctSystemType | — | `public DuctSystemType DuctSystemType { get ; }` |
| Property | ElectricalSystemType | — | `public ElectricalSystemType ElectricalSystemType { get ; }` |
| Property | EngagementLength | — | `public double EngagementLength { get ; }` |
| Property | Flow | — | `public double Flow { get ; }` |
| Property | GasketLength | 2024 | `public double GasketLength { get ; }` |
| Property | Height | — | `public virtual double Height { get ; set ; }` |
| Property | Id | 2016 | `public int Id { get ; }` |
| Property | IsConnected | — | `public bool IsConnected { get ; }` |
| Property | IsMovable | — | `public bool IsMovable { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MEPSystem | — | `public MEPSystem MEPSystem { get ; }` |
| Property | Origin | — | `public virtual XYZ Origin { get ; set ; }` |
| Property | Owner | — | `public Element Owner { get ; }` |
| Property | PipeSystemType | — | `public PipeSystemType PipeSystemType { get ; }` |
| Property | PressureDrop | — | `public double PressureDrop { get ; }` |
| Property | Radius | — | `public virtual double Radius { get ; set ; }` |
| Property | Shape | — | `public virtual ConnectorProfileType Shape { get ; }` |
| Property | Utility | 2015 | `public bool Utility { get ; }` |
| Property | VelocityPressure | — | `public double VelocityPressure { get ; }` |
| Property | Width | — | `public virtual double Width { get ; set ; }` |