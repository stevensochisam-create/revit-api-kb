---
type: RebarShapeDefinitionBySegments
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 17
tags: [revit-api, class]
---

# RebarShapeDefinitionBySegments

`Autodesk.Revit.DB.Structure.RebarShapeDefinitionBySegments` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | RebarShapeDefinitionBySegments | — | `public RebarShapeDefinitionBySegments ( Document doc , int numberOfSegments )` |
| Method | AddBendDefaultRadius | — | `public void AddBendDefaultRadius ( int vertexIndex , RebarShapeVertexTurn turn , RebarShapeBendAngle angle )` |
| Method | AddBendVariableRadius | — | `public void AddBendVariableRadius ( int vertexIndex , RebarShapeVertexTurn turn , RebarShapeBendAngle angle , ElementId paramId , bool measureIncludingBarThickness )` |
| Method | AddConstraintParallelToSegment | — | `public void AddConstraintParallelToSegment ( int iSegment , ElementId paramId , bool measureToOutsideOfBend0 , bool measureToOutsideOfBend1 )` |
| Method | AddConstraintToSegment | — | `public void AddConstraintToSegment ( int iSegment , ElementId paramId , double constraintDirCoordX , double constraintDirCoordY , int signOfZCoordOfCrossProductOfConstraintDirBySegmentDir , bool measureToOutsideOfBend0 ,` |
| Method | AddListeningDimensionBendToBend | — | `public void AddListeningDimensionBendToBend ( ElementId paramId , double constraintDirCoordX , double constraintDirCoordY , int iSegment0 , int iEnd0 , int iSegment1 , int iEnd1 )` |
| Method | AddListeningDimensionSegmentToBend | — | `public void AddListeningDimensionSegmentToBend ( ElementId paramId , double constraintDirCoordX , double constraintDirCoordY , int iSegment0 , int iSegment1 , int iEnd1 )` |
| Method | AddListeningDimensionSegmentToSegment | — | `public void AddListeningDimensionSegmentToSegment ( ElementId paramId , double constraintDirCoordX , double constraintDirCoordY , int iSegment0 , int iSegment1 )` |
| Method | GetSegment | 2012 | `public RebarShapeSegment GetSegment ( int segmentIndex )` |
| Method | GetVertex | 2012 | `public RebarShapeVertex GetVertex ( int vertexIndex )` |
| Method | RemoveParameterFromSegment | — | `public void RemoveParameterFromSegment ( int iSegment , ElementId paramId )` |
| Method | SetSegmentAs180DegreeBend | — | `` |
| Method | SetSegmentFixedDirection | — | `public void SetSegmentFixedDirection ( int iSegment , double vecCoordX , double vecCoordY )` |
| Method | SetSegmentVariableDirection | — | `public void SetSegmentVariableDirection ( int iSegment )` |
| Property | MajorSegmentIndex | 2012 | `public int MajorSegmentIndex { get ; set ; }` |
| Property | NumberOfSegments | — | `public int NumberOfSegments { get ; }` |
| Property | NumberOfVertices | 2012 | `public int NumberOfVertices { get ; }` |