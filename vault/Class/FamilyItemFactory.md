---
type: FamilyItemFactory
namespace: Autodesk.Revit.Creation
version: 2024
members: 24
tags: [revit-api, class]
---

# FamilyItemFactory

`Autodesk.Revit.Creation.FamilyItemFactory` · Revit 2024 · 24 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | NewAngularDimension | — | `` |
| Method | NewArcLengthDimension | — | `` |
| Method | NewBlend | — | `public Blend NewBlend ( bool isSolid , CurveArray profile1 , CurveArray profile2 , SketchPlane sketchPlane )` |
| Method | NewControl | — | `public Control NewControl ( ControlShape controlShape , View view , XYZ origin )` |
| Method | NewCurveByPoints | — | `public CurveByPoints NewCurveByPoints ( ReferencePointArray points )` |
| Method | NewDiameterDimension | — | `public Dimension NewDiameterDimension ( View view , Reference arcRef , XYZ origin )` |
| Method | NewDimension | — | `` |
| Method | NewExtrusion | — | `public Extrusion NewExtrusion ( bool isSolid , CurveArrArray profile , SketchPlane sketchPlane , double end )` |
| Method | NewExtrusionForm | — | `public Form NewExtrusionForm ( bool isSolid , ReferenceArray profile , XYZ direction )` |
| Method | NewFamilyInstance | — | `` |
| Method | NewFormByCap | — | `public Form NewFormByCap ( bool isSolid , ReferenceArray profile )` |
| Method | NewFormByThickenSingleSurface | — | `public Form NewFormByThickenSingleSurface ( bool isSolid , Form singleSurfaceForm , XYZ thickenDir )` |
| Method | NewLinearDimension | — | `` |
| Method | NewLoftForm | — | `public Form NewLoftForm ( bool isSolid , ReferenceArrayArray profiles )` |
| Method | NewModelText | — | `public ModelText NewModelText ( string text , ModelTextType modelTextType , SketchPlane sketchPlane , XYZ position , HorizontalAlign horizontalAlign , double depth )` |
| Method | NewOpening | — | `public Opening NewOpening ( Element host , CurveArray profile )` |
| Method | NewRadialDimension | — | `` |
| Method | NewReferencePoint | — | `` |
| Method | NewRevolution | — | `public Revolution NewRevolution ( bool isSolid , CurveArrArray profile , SketchPlane sketchPlane , Line axis , double startAngle , double endAngle )` |
| Method | NewRevolveForms | — | `public FormArray NewRevolveForms ( bool isSolid , ReferenceArray profile , Reference axis , double startAngle , double endAngle )` |
| Method | NewSweep | — | `` |
| Method | NewSweptBlend | — | `` |
| Method | NewSweptBlendForm | — | `public Form NewSweptBlendForm ( bool isSolid , ReferenceArray path , ReferenceArrayArray profiles )` |
| Method | NewSymbolicCurve | — | `public SymbolicCurve NewSymbolicCurve ( Curve curve , SketchPlane sketchPlane )` |