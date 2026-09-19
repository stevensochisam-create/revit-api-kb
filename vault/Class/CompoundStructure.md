---
type: CompoundStructure
namespace: Autodesk.Revit.DB
version: 2024
members: 78
tags: [revit-api, class]
---

# CompoundStructure

`Autodesk.Revit.DB.CompoundStructure` · Revit 2024 · 78 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddWallSweep | — | `public void AddWallSweep ( WallSweepInfo wallSweepInfo )` |
| Method | AssociateRegionWithLayer | — | `public void AssociateRegionWithLayer ( int regionId , int layerIdx )` |
| Method | CanLayerBeStructuralMaterial | 2016 | `public bool CanLayerBeStructuralMaterial ( int layerIndex )` |
| Method | CanLayerBeVariable | 2016 | `public bool CanLayerBeVariable ( int variableLayerIndex )` |
| Method | CanLayerWidthBeNonZero | — | `public bool CanLayerWidthBeNonZero ( int layerIdx )` |
| Method | CanSplitAndMergeRegionsBeUsed | — | `public bool CanSplitAndMergeRegionsBeUsed ()` |
| Method | ChangeRegionWidth | — | `public bool ChangeRegionWidth ( int regionId , double newWidth )` |
| Method | ClearWallSweeps | — | `public void ClearWallSweeps ( WallSweepType wallSweepType )` |
| Method | CreateSimpleCompoundStructure | — | `public static CompoundStructure CreateSimpleCompoundStructure ( IList < CompoundStructureLayer > layers )` |
| Method | CreateSingleLayerCompoundStructure | — | `` |
| Method | DeleteLayer | — | `public bool DeleteLayer ( int layerIdx )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FindEnclosingRegionAndSegments | — | `public int FindEnclosingRegionAndSegments ( UV gridUV , RectangularGridSegmentOrientation splitDirection , out int segmentId1 , out int segmentId2 )` |
| Method | GetAdjacentRegions | — | `public IList < int > GetAdjacentRegions ( int segmentId )` |
| Method | GetCoreBoundaryLayerIndex | — | `public int GetCoreBoundaryLayerIndex ( ShellLayerType shellLayerType )` |
| Method | GetDeckEmbeddingType | — | `public StructDeckEmbeddingType GetDeckEmbeddingType ( int layerIdx )` |
| Method | GetDeckProfileId | — | `public ElementId GetDeckProfileId ( int layerIdx )` |
| Method | GetExtendableRegionIds | — | `public IList < int > GetExtendableRegionIds ( bool top )` |
| Method | GetFirstCoreLayerIndex | — | `public int GetFirstCoreLayerIndex ()` |
| Method | GetLastCoreLayerIndex | — | `public int GetLastCoreLayerIndex ()` |
| Method | GetLayerAssociatedToRegion | — | `public int GetLayerAssociatedToRegion ( int regionId )` |
| Method | GetLayerFunction | — | `public MaterialFunctionAssignment GetLayerFunction ( int layerIdx )` |
| Method | GetLayerWidth | — | `public double GetLayerWidth ( int layerIdx )` |
| Method | GetLayers | — | `public IList < CompoundStructureLayer > GetLayers ()` |
| Method | GetMaterialId | — | `public ElementId GetMaterialId ( int layerIdx )` |
| Method | GetMinimumLayerThickness | — | `public static double GetMinimumLayerThickness ()` |
| Method | GetNumberOfShellLayers | — | `public int GetNumberOfShellLayers ( ShellLayerType shellLayerType )` |
| Method | GetOffsetForLocationLine | — | `public double GetOffsetForLocationLine ( WallLocationLine wallLocationLine )` |
| Method | GetPreviousNonZeroLayerIndex | — | `public int GetPreviousNonZeroLayerIndex ( int thisIdx )` |
| Method | GetRegionEnvelope | — | `public BoundingBoxUV GetRegionEnvelope ( int regionId )` |
| Method | GetRegionIds | — | `public IList < int > GetRegionIds ()` |
| Method | GetRegionsAlongLevel | — | `public IList < int > GetRegionsAlongLevel ( double height )` |
| Method | GetRegionsAssociatedToLayer | — | `public IList < int > GetRegionsAssociatedToLayer ( int layerIdx )` |
| Method | GetSegmentCoordinate | — | `public double GetSegmentCoordinate ( int segmentId )` |
| Method | GetSegmentEndPoints | — | `public void GetSegmentEndPoints ( int segmentId , int regionId , out UV end1 , out UV end2 )` |
| Method | GetSegmentIds | — | `public IList < int > GetSegmentIds ()` |
| Method | GetSegmentOrientation | — | `public RectangularGridSegmentOrientation GetSegmentOrientation ( int segmentId )` |
| Method | GetSimpleCompoundStructure | — | `public CompoundStructure GetSimpleCompoundStructure ( double wallHeight , double distAboveBase )` |
| Method | GetWallSweepsInfo | — | `public IList < WallSweepInfo > GetWallSweepsInfo ( WallSweepType wallSweepType )` |
| Method | GetWidth | — | `` |
| Method | GetWidth | — | `public double GetWidth ()` |
| Method | IsCoreLayer | — | `public bool IsCoreLayer ( int layerIdx )` |
| Method | IsEqual | — | `public bool IsEqual ( CompoundStructure otherStructure )` |
| Method | IsLayerValid | — | `public bool IsLayerValid ( int layerIdx , CompoundStructureLayer layer )` |
| Method | IsRectangularRegion | — | `public bool IsRectangularRegion ( int regionId )` |
| Method | IsSimpleRegion | — | `public bool IsSimpleRegion ( int regionId )` |
| Method | IsStructuralDeck | — | `public bool IsStructuralDeck ( int layerIdx )` |
| Method | IsValid | — | `public bool IsValid ( Document doc , out IDictionary < int , CompoundStructureError > errMap , out IDictionary < int , int > twoLayerErrorsMap )` |
| Method | IsValidRegionId | — | `public bool IsValidRegionId ( int regionId )` |
| Method | IsValidSampleHeight | — | `public bool IsValidSampleHeight ( double height )` |
| Method | IsValidSegmentId | — | `public bool IsValidSegmentId ( int segmentId )` |
| Method | IsVerticallyHomogeneous | — | `public bool IsVerticallyHomogeneous ()` |
| Method | MergeRegionsAdjacentToSegment | — | `public int MergeRegionsAdjacentToSegment ( int segmentId , int layerIdxForMergedRegion )` |
| Method | ParticipatesInWrapping | — | `public bool ParticipatesInWrapping ( int layerIdx )` |
| Method | RemoveWallSweep | — | `public void RemoveWallSweep ( WallSweepType wallSweepType , int id )` |
| Method | SetDeckEmbeddingType | — | `public void SetDeckEmbeddingType ( int layerIdx , StructDeckEmbeddingType embedType )` |
| Method | SetDeckProfileId | — | `public void SetDeckProfileId ( int layerIdx , ElementId profileId )` |
| Method | SetExtendableRegionIds | — | `public void SetExtendableRegionIds ( bool top , IList < int > regionIds )` |
| Method | SetLayer | — | `public void SetLayer ( int layerIdx , CompoundStructureLayer layer )` |
| Method | SetLayerFunction | — | `public void SetLayerFunction ( int layerIdx , MaterialFunctionAssignment function )` |
| Method | SetLayerWidth | — | `public void SetLayerWidth ( int layerIdx , double width )` |
| Method | SetLayers | — | `public void SetLayers ( IList < CompoundStructureLayer > layers )` |
| Method | SetMaterialId | — | `public void SetMaterialId ( int layerIdx , ElementId materialId )` |
| Method | SetNumberOfShellLayers | — | `public void SetNumberOfShellLayers ( ShellLayerType shellLayerType , int numLayers )` |
| Method | SetParticipatesInWrapping | — | `public void SetParticipatesInWrapping ( int layerIdx , bool participatesInWrapping )` |
| Method | SplitRegion | — | `` |
| Property | CutoffHeight | — | `public double CutoffHeight { get ; set ; }` |
| Property | EndCap | — | `public EndCapCondition EndCap { get ; set ; }` |
| Property | HasStructuralDeck | — | `public bool HasStructuralDeck { get ; }` |
| Property | IsEmpty | — | `public bool IsEmpty { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | IsVerticallyCompound | — | `public bool IsVerticallyCompound { get ; }` |
| Property | LayerCount | — | `public int LayerCount { get ; }` |
| Property | MinimumSampleHeight | — | `public double MinimumSampleHeight { get ; }` |
| Property | OpeningWrapping | — | `public OpeningWrappingCondition OpeningWrapping { get ; set ; }` |
| Property | SampleHeight | — | `public double SampleHeight { get ; set ; }` |
| Property | StructuralMaterialIndex | — | `public int StructuralMaterialIndex { get ; set ; }` |
| Property | VariableLayerIndex | — | `public int VariableLayerIndex { get ; set ; }` |