---
type: StructuralAsset
namespace: Autodesk.Revit.DB
version: 2024
members: 35
tags: [revit-api, class]
---

# StructuralAsset

`Autodesk.Revit.DB.StructuralAsset` · Revit 2024 · 35 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | StructuralAsset | 2013 | `public StructuralAsset ( string name , StructuralAssetClass structuralAssetClass )` |
| Method | Copy | 2013 | `public StructuralAsset Copy ()` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Equals | — | `` |
| Method | SetPoissonRatio | 2013 | `public void SetPoissonRatio ( double poissonRatio )` |
| Method | SetShearModulus | 2013 | `public void SetShearModulus ( double shearModulus )` |
| Method | SetThermalExpansionCoefficient | 2013 | `public void SetThermalExpansionCoefficient ( double thermalExpCoeff )` |
| Method | SetYoungModulus | 2013 | `public void SetYoungModulus ( double youngModulus )` |
| Property | Behavior | 2013 | `public StructuralBehavior Behavior { get ; set ; }` |
| Property | ConcreteBendingReinforcement | 2013 | `public double ConcreteBendingReinforcement { get ; set ; }` |
| Property | ConcreteCompression | 2013 | `public double ConcreteCompression { get ; set ; }` |
| Property | ConcreteShearReinforcement | 2013 | `public double ConcreteShearReinforcement { get ; set ; }` |
| Property | ConcreteShearStrengthReduction | 2013 | `public double ConcreteShearStrengthReduction { get ; set ; }` |
| Property | Density | 2013 | `public double Density { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Lightweight | 2013 | `public bool Lightweight { get ; set ; }` |
| Property | MetalReductionFactor | 2013 | `public double MetalReductionFactor { get ; set ; }` |
| Property | MetalResistanceCalculationStrength | 2013 | `public double MetalResistanceCalculationStrength { get ; set ; }` |
| Property | MetalThermallyTreated | 2021 | `public bool MetalThermallyTreated { get ; set ; }` |
| Property | MinimumTensileStrength | 2013 | `public double MinimumTensileStrength { get ; set ; }` |
| Property | MinimumYieldStress | 2013 | `public double MinimumYieldStress { get ; set ; }` |
| Property | Name | 2013 | `public string Name { get ; set ; }` |
| Property | PoissonRatio | 2013 | `public XYZ PoissonRatio { get ; set ; }` |
| Property | ShearModulus | 2013 | `public XYZ ShearModulus { get ; set ; }` |
| Property | StructuralAssetClass | 2013 | `public StructuralAssetClass StructuralAssetClass { get ; }` |
| Property | SubClass | 2013 | `public string SubClass { get ; set ; }` |
| Property | ThermalExpansionCoefficient | 2013 | `public XYZ ThermalExpansionCoefficient { get ; set ; }` |
| Property | WoodBendingStrength | 2013 | `public double WoodBendingStrength { get ; set ; }` |
| Property | WoodGrade | 2013 | `public string WoodGrade { get ; set ; }` |
| Property | WoodParallelCompressionStrength | 2013 | `public double WoodParallelCompressionStrength { get ; set ; }` |
| Property | WoodParallelShearStrength | 2013 | `public double WoodParallelShearStrength { get ; set ; }` |
| Property | WoodPerpendicularCompressionStrength | 2013 | `public double WoodPerpendicularCompressionStrength { get ; set ; }` |
| Property | WoodPerpendicularShearStrength | 2013 | `public double WoodPerpendicularShearStrength { get ; set ; }` |
| Property | WoodSpecies | 2013 | `public string WoodSpecies { get ; set ; }` |
| Property | YoungModulus | 2013 | `public XYZ YoungModulus { get ; set ; }` |