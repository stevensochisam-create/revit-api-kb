---
type: ItemFactoryBase
namespace: Autodesk.Revit.Creation
version: 2024
members: 12
tags: [revit-api, class]
---

# ItemFactoryBase

`Autodesk.Revit.Creation.ItemFactoryBase` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | NewAlignment | — | `public Dimension NewAlignment ( View view , Reference reference1 , Reference reference2 )` |
| Method | NewDetailCurve | — | `public DetailCurve NewDetailCurve ( View view , Curve geometryCurve )` |
| Method | NewDetailCurveArray | — | `public DetailCurveArray NewDetailCurveArray ( View view , CurveArray geometryCurveArray )` |
| Method | NewDimension | — | `` |
| Method | NewFamilyInstance | — | `` |
| Method | NewFamilyInstances2 | — | `public ICollection < ElementId > NewFamilyInstances2 ( List < FamilyInstanceCreationData > dataList )` |
| Method | NewGroup | — | `public Group NewGroup ( ICollection < ElementId > elementIds )` |
| Method | NewModelCurve | — | `public ModelCurve NewModelCurve ( Curve geometryCurve , SketchPlane sketchPlane )` |
| Method | NewModelCurveArray | — | `public ModelCurveArray NewModelCurveArray ( CurveArray geometryCurveArray , SketchPlane sketchPlane )` |
| Method | NewReferencePlane | — | `public ReferencePlane NewReferencePlane ( XYZ bubbleEnd , XYZ freeEnd , XYZ cutVec , View pView )` |
| Method | NewReferencePlane2 | — | `public ReferencePlane NewReferencePlane2 ( XYZ bubbleEnd , XYZ freeEnd , XYZ thirdPnt , View pView )` |
| Method | PlaceGroup | — | `public Group PlaceGroup ( XYZ location , GroupType groupType )` |