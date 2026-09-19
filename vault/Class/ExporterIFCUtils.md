---
type: ExporterIFCUtils
namespace: Autodesk.Revit.DB.IFC
version: 2024
members: 61
tags: [revit-api, class]
---

# ExporterIFCUtils

`Autodesk.Revit.DB.IFC.ExporterIFCUtils` · Revit 2024 · 61 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddClippingsToBaseExtrusion | — | `public static IFCAnyHandle AddClippingsToBaseExtrusion ( ExporterIFC exporterIFC , Wall wall , XYZ setterOffset , IFCRange range , IFCRange zSpan , IFCAnyHandle baseBodyItemHandle , out IList < IFCExtrusionData > pCutPai` |
| Method | AddValueString | 2013 | `public static void AddValueString ( Element element , ElementId builtInParameter , string propertyValue )` |
| Method | AreSolidsEqual | 2013 | `public static bool AreSolidsEqual ( Solid first , Solid second , out Transform trf )` |
| Method | CanExportWallGeometryAsExtrusion | 2012 | `public static bool CanExportWallGeometryAsExtrusion ( Element element , IFCRange range , Curve curve )` |
| Method | CollectGeometryInfo | — | `` |
| Method | ComputeAreaOfCurveLoops | — | `public static double ComputeAreaOfCurveLoops ( IList < CurveLoop > curveLoops )` |
| Method | ComputeRoofProjectedArea | 2013 | `public static double ComputeRoofProjectedArea ( Element pElem )` |
| Method | ComputeSubcomponents | 2016 | `public static IList < HostObjectSubcomponentInfo > ComputeSubcomponents ( HostObject roofOrFloor )` |
| Method | CreateAlternateGUID | 2013 | `public static string CreateAlternateGUID ( Element pElement )` |
| Method | CreateGUID | 2013 | `public static string CreateGUID ()` |
| Method | CreateProjectLevelGUID | 2013 | `public static string CreateProjectLevelGUID ( Document document , IFCProjectLevelGUIDType guidType )` |
| Method | CreateSubElementGUID | 2013 | `public static string CreateSubElementGUID ( Element pElement , int subElementIndex )` |
| Method | EndExportInternal | 2013 | `public static void EndExportInternal ( ExporterIFC exporterIFC )` |
| Method | ExportExtrudedSlabOpenings | — | `public static void ExportExtrudedSlabOpenings ( ExporterIFC exporterIFC , Element pElem , IFCLevelInfo levelInfo , IFCAnyHandle localPlacementAny , IList < IFCAnyHandle > elementSlabAnyArr , IList < IList < CurveLoop >> ` |
| Method | ExportSlabAsExtrusion | — | `public static bool ExportSlabAsExtrusion ( ExporterIFC exporterIFC , Element pCeilingAndFloor , GeometryElement pGRep , IFCTransformSetter pTmpTrfSetter , IFCAnyHandle localPlacement , out IList < IFCAnyHandle > localPla` |
| Method | GetAttachedColumns | 2012 | `public static IList < FamilyInstance > GetAttachedColumns ( Wall pWallElem )` |
| Method | GetConnectedWalls | 2012 | `public static IList < IFCConnectedWallData > GetConnectedWalls ( Wall pWallElem , IFCConnectedWallDataLocation locaction )` |
| Method | GetDoor2DArcsFromFamily | 2014 | `public static IList < Arc > GetDoor2DArcsFromFamily ( Family pFam )` |
| Method | GetElevationProfile | 2012 | `public static IList < CurveLoop > GetElevationProfile ( Wall pVWall )` |
| Method | GetGeometryFromInplaceWall | 2012 | `public static GeometryElement GetGeometryFromInplaceWall ( FamilyInstance pFamInstWallElem )` |
| Method | GetGlobal2DDirectionHandles | 2012 | `public static IList < IFCAnyHandle > GetGlobal2DDirectionHandles ( bool positive )` |
| Method | GetGlobal2DOriginHandle | 2012 | `public static IFCAnyHandle GetGlobal2DOriginHandle ()` |
| Method | GetGlobal3DDirectionHandles | 2012 | `public static IList < IFCAnyHandle > GetGlobal3DDirectionHandles ( bool positive )` |
| Method | GetGlobal3DOriginHandle | 2012 | `public static IFCAnyHandle GetGlobal3DOriginHandle ()` |
| Method | GetIFCClassName | 2012 | `public static string GetIFCClassName ( Element element , ExporterIFC exporterIFC )` |
| Method | GetIFCClassNameByCategory | 2013 | `public static string GetIFCClassNameByCategory ( ElementId catId , ExporterIFC exporterIFC )` |
| Method | GetIFCType | 2012 | `public static string GetIFCType ( Element element , ExporterIFC exporterIFC )` |
| Method | GetInstanceCutoutFromWall | 2014 | `public static CurveLoop GetInstanceCutoutFromWall ( Document pADoc , Wall pVWall , FamilyInstance pFamInst , out XYZ pCutDir )` |
| Method | GetLegacyCurtainSubElements | 2013 | `public static ICollection < ElementId > GetLegacyCurtainSubElements ( Element element )` |
| Method | GetLegacyStairOrRampComponents | 2013 | `public static IFCLegacyStairOrRamp GetLegacyStairOrRampComponents ( ExporterIFC exporterIFC , Element element )` |
| Method | GetLegacyStairsProperties | 2013 | `public static void GetLegacyStairsProperties ( ExporterIFC exporterIFC , Element pElement , out int pNumRisers , out int pNumTreads , out double pRiserHeight , out double pTreadLength , out double pMinTreadLength , out d` |
| Method | GetLevelIdByHeight | 2014 | `public static ElementId GetLevelIdByHeight ( ExporterIFC exporterIFC , Element elem )` |
| Method | GetLoopsFromTopBottomFace | 2012 | `public static IList < CurveLoop > GetLoopsFromTopBottomFace ( ExporterIFC exporterIFC , Wall wall )` |
| Method | GetMinSymbolHeight | 2012 | `public static double GetMinSymbolHeight ( FamilySymbol symbol )` |
| Method | GetMinSymbolWidth | 2012 | `public static double GetMinSymbolWidth ( FamilySymbol symbol )` |
| Method | GetNumBuildingStoreys | 2013 | `public static int GetNumBuildingStoreys ( ExporterIFC exporterIFC )` |
| Method | GetOpeningData | 2017 | `public static IList < IFCOpeningData > GetOpeningData ( ExporterIFC exporterIFC , Element element , Transform lcs , IFCRange range )` |
| Method | GetOriginalSymbol | 2012 | `public static FamilySymbol GetOriginalSymbol ( FamilyInstance familyInstance )` |
| Method | GetRelativeLocalPlacementOffsetTransform | 2012 | `public static Transform GetRelativeLocalPlacementOffsetTransform ( IFCAnyHandle originalPlacement , IFCAnyHandle relativePlacement )` |
| Method | GetRoofComponents | 2014 | `public static RoofComponents GetRoofComponents ( ExporterIFC exporterIFC , RoofBase roof )` |
| Method | GetRoomBoundaryAsCurveLoopArray | 2012 | `public static IList < CurveLoop > GetRoomBoundaryAsCurveLoopArray ( SpatialElement spatialElement , SpatialElementBoundaryOptions options , bool cleanCurves )` |
| Method | GetTransformForDoorOrWindow | 2014 | `public static Transform GetTransformForDoorOrWindow ( FamilyInstance familyInstance , FamilySymbol familySymbol , bool flippedX , bool flippedY )` |
| Method | GetUnscaledTransform | 2012 | `public static Transform GetUnscaledTransform ( ExporterIFC exporterIFC , IFCAnyHandle placement )` |
| Method | GetUnscaledTransformWithoutFixOfDirection | 2012 | `public static Transform GetUnscaledTransformWithoutFixOfDirection ( ExporterIFC exporterIFC , IFCAnyHandle placement )` |
| Method | GetWallBaseOffset | 2012 | `public static double GetWallBaseOffset ( Wall wall )` |
| Method | GetWallTrimmedCurve | 2012 | `public static Curve GetWallTrimmedCurve ( Wall pVWall )` |
| Method | HasElevationProfile | 2012 | `public static bool HasElevationProfile ( Wall pVWall )` |
| Method | IsCurveFromOtherElementSketch | 2012 | `public static bool IsCurveFromOtherElementSketch ( CurveElement curveElement )` |
| Method | IsCurveLoopConvexWithOpenings | 2012 | `public static bool IsCurveLoopConvexWithOpenings ( CurveLoop inputCurveLoop , Wall wall , IFCRange range , out bool loopIsDegenerate )` |
| Method | IsWallBaseRectangular | 2012 | `public static bool IsWallBaseRectangular ( Wall wall , Curve curve )` |
| Method | IsWallCompletelyClipped | 2012 | `public static bool IsWallCompletelyClipped ( Wall pVWall , ExporterIFC exporterIFC , IFCRange range )` |
| Method | IsWallJoinedToTop | 2013 | `public static bool IsWallJoinedToTop ( Wall wall )` |
| Method | SetGlobal2DDirectionHandles | 2013 | `public static void SetGlobal2DDirectionHandles ( bool positive , IFCAnyHandle xDir , IFCAnyHandle yDir )` |
| Method | SetGlobal2DOriginHandle | 2013 | `public static void SetGlobal2DOriginHandle ( IFCAnyHandle origin )` |
| Method | SetGlobal3DDirectionHandles | 2013 | `public static void SetGlobal3DDirectionHandles ( bool positive , IFCAnyHandle xDir , IFCAnyHandle yDir , IFCAnyHandle zDir )` |
| Method | SetGlobal3DOriginHandle | 2013 | `public static void SetGlobal3DOriginHandle ( IFCAnyHandle origin )` |
| Method | SortCurveLoops | — | `public static IList < IList < CurveLoop >> SortCurveLoops ( IList < CurveLoop > loops )` |
| Method | TransformAndScalePoint | 2013 | `public static XYZ TransformAndScalePoint ( ExporterIFC exporterIFC , XYZ origPt )` |
| Method | TransformAndScaleVector | 2013 | `public static XYZ TransformAndScaleVector ( ExporterIFC exporterIFC , XYZ origVector )` |
| Method | UsesInstanceGeometry | 2012 | `public static bool UsesInstanceGeometry ( FamilyInstance familyInstance )` |
| Method | ValidateCurveLoops | — | `public static IList < CurveLoop > ValidateCurveLoops ( IList < CurveLoop > curveLoops , XYZ extrDirVec )` |