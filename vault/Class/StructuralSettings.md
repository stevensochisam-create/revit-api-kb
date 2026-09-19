---
type: StructuralSettings
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 19
tags: [revit-api, class]
---

# StructuralSettings

`Autodesk.Revit.DB.Structure.StructuralSettings` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetLoadForceVectorReprLine | 2024 | `public XYZ GetLoadForceVectorReprLine ( LoadType loadType , XYZ forceVector )` |
| Method | GetStructuralSettings | 2011 | `public static StructuralSettings GetStructuralSettings ( Document doc )` |
| Method | SetValuesForLoadsDisplayScaling | 2024 | `public void SetValuesForLoadsDisplayScaling ( double minimumLoadValue , double minimumForceLineLength , double maximumLoadValue , double maximumForceLineLength )` |
| Property | BoundaryConditionAreaAndLineSymbolSpacing | 2011 | `public double BoundaryConditionAreaAndLineSymbolSpacing { get ; set ; }` |
| Property | BoundaryConditionFamilySymbolFixed | 2011 | `public ElementId BoundaryConditionFamilySymbolFixed { get ; set ; }` |
| Property | BoundaryConditionFamilySymbolPinned | 2011 | `public ElementId BoundaryConditionFamilySymbolPinned { get ; set ; }` |
| Property | BoundaryConditionFamilySymbolRoller | 2011 | `public ElementId BoundaryConditionFamilySymbolRoller { get ; set ; }` |
| Property | BoundaryConditionFamilySymbolUserDefined | 2011 | `public ElementId BoundaryConditionFamilySymbolUserDefined { get ; set ; }` |
| Property | BraceAboveSymbol | 2011 | `public ElementId BraceAboveSymbol { get ; set ; }` |
| Property | BraceBelowSymbol | 2011 | `public ElementId BraceBelowSymbol { get ; set ; }` |
| Property | BraceParallelLineOffset | 2011 | `public double BraceParallelLineOffset { get ; set ; }` |
| Property | KickerBraceSymbol | 2011 | `public ElementId KickerBraceSymbol { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | ShowBraceAbove | 2011 | `public bool ShowBraceAbove { get ; set ; }` |
| Property | ShowBraceBelow | 2011 | `public bool ShowBraceBelow { get ; set ; }` |
| Property | SymbolicCutbackForBeamAndTruss | 2011 | `public double SymbolicCutbackForBeamAndTruss { get ; set ; }` |
| Property | SymbolicCutbackForBrace | 2011 | `public double SymbolicCutbackForBrace { get ; set ; }` |
| Property | SymbolicCutbackForColumn | 2011 | `public double SymbolicCutbackForColumn { get ; set ; }` |
| Property | UseLoadsDisplayScaling | 2024 | `public bool UseLoadsDisplayScaling { get ; set ; }` |