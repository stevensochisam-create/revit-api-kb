---
type: ElectricalSetting
namespace: Autodesk.Revit.DB.Electrical
version: 2024
members: 27
tags: [revit-api, class]
---

# ElectricalSetting

`Autodesk.Revit.DB.Electrical.ElectricalSetting` · Revit 2024 · 27 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddDistributionSysType | — | `public DistributionSysType AddDistributionSysType ( string name , ElectricalPhase phase , ElectricalPhaseConfiguration phaseConfig , int numWire , VoltageType volLineToLine , VoltageType volLineToGround )` |
| Method | AddVoltageType | — | `public VoltageType AddVoltageType ( string name , double actualValue , double minValue , double maxValue )` |
| Method | AddWireMaterialType | — | `public WireMaterialType AddWireMaterialType ( string name , WireMaterialType baseMaterial )` |
| Method | AddWireType | — | `public WireType AddWireType ( string name , WireMaterialType materialType , TemperatureRatingType temperatureRating , InsulationType insulation , WireSize maxSize , double neutralMultiplier , bool neutralRequired , Neutr` |
| Method | GetCircuitNamingSchemeSettings | 2021 | `public static CircuitNamingSchemeSettings GetCircuitNamingSchemeSettings ( Document cda )` |
| Method | GetElectricalSettings | 2014 | `public static ElectricalSetting GetElectricalSettings ( Document document )` |
| Method | GetSpecificFittingAngleStatus | 2014 | `public bool GetSpecificFittingAngleStatus ( double angle )` |
| Method | GetSpecificFittingAngles | 2014 | `public IList < double > GetSpecificFittingAngles ()` |
| Method | IsValidSpecificFittingAngle | 2014 | `public bool IsValidSpecificFittingAngle ( double angle )` |
| Method | RemoveDistributionSysType | — | `public void RemoveDistributionSysType ( DistributionSysType distributionSysType )` |
| Method | RemoveVoltageType | — | `public void RemoveVoltageType ( VoltageType voltageType )` |
| Method | RemoveWireMaterialType | — | `public void RemoveWireMaterialType ( WireMaterialType materialType )` |
| Method | RemoveWireType | — | `public void RemoveWireType ( WireType wireType )` |
| Method | SetSpecificFittingAngleStatus | 2014 | `public void SetSpecificFittingAngleStatus ( double angle , bool bStatus )` |
| Property | CircuitLoadCalculationMethod | 2017 | `public CircuitLoadCalculationMethod CircuitLoadCalculationMethod { get ; set ; }` |
| Property | CircuitNamePhaseA | 2015 Subscription Update | `public string CircuitNamePhaseA { get ; set ; }` |
| Property | CircuitNamePhaseB | 2015 Subscription Update | `public string CircuitNamePhaseB { get ; set ; }` |
| Property | CircuitNamePhaseC | 2015 Subscription Update | `public string CircuitNamePhaseC { get ; set ; }` |
| Property | CircuitPathOffset | 2011 | `public double CircuitPathOffset { get ; set ; }` |
| Property | CircuitRating | 2011 | `public double CircuitRating { get ; set ; }` |
| Property | CircuitSequence | 2015 Subscription Update | `public CircuitSequence CircuitSequence { get ; set ; }` |
| Property | DistributionSysTypes | — | `public DistributionSysTypeSet DistributionSysTypes { get ; }` |
| Property | Parameter | — | `` |
| Property | VoltageTypes | — | `public VoltageTypeSet VoltageTypes { get ; }` |
| Property | WireConduitTypes | — | `public WireConduitTypeSet WireConduitTypes { get ; }` |
| Property | WireMaterialTypes | — | `public WireMaterialTypeSet WireMaterialTypes { get ; }` |
| Property | WireTypes | — | `public WireTypeSet WireTypes { get ; }` |