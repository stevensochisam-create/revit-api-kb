---
type: Document
namespace: Autodesk.Revit.DB
version: 2024
members: 160
tags: [revit-api, class]
---

# Document

`Autodesk.Revit.DB.Document` · Revit 2024 · 160 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Event | DocumentClosing | 2010 | `public event EventHandler < DocumentClosingEventArgs > DocumentClosing` |
| Event | DocumentPrinted | 2010 | `public event EventHandler < DocumentPrintedEventArgs > DocumentPrinted` |
| Event | DocumentPrinting | 2010 | `public event EventHandler < DocumentPrintingEventArgs > DocumentPrinting` |
| Event | DocumentSaved | 2010 | `public event EventHandler < DocumentSavedEventArgs > DocumentSaved` |
| Event | DocumentSavedAs | 2010 | `public event EventHandler < DocumentSavedAsEventArgs > DocumentSavedAs` |
| Event | DocumentSaving | 2010 | `public event EventHandler < DocumentSavingEventArgs > DocumentSaving` |
| Event | DocumentSavingAs | 2010 | `public event EventHandler < DocumentSavingAsEventArgs > DocumentSavingAs` |
| Event | ViewPrinted | 2010 | `public event EventHandler < ViewPrintedEventArgs > ViewPrinted` |
| Event | ViewPrinting | 2010 | `public event EventHandler < ViewPrintingEventArgs > ViewPrinting` |
| Method | AcquireCoordinates | 2018 | `public void AcquireCoordinates ( ElementId linkInstanceId )` |
| Method | AutoJoinElements | — | `public void AutoJoinElements ()` |
| Method | CanEnableCloudWorksharing | 2019.2 | `public bool CanEnableCloudWorksharing ()` |
| Method | CanEnableWorksharing | 2015 | `public bool CanEnableWorksharing ()` |
| Method | Close | — | `` |
| Method | Close | — | `public bool Close ()` |
| Method | CombineElements | — | `public GeomCombination CombineElements ( CombinableElementArray members )` |
| Method | ConvertDetailToModelCurves | — | `public ModelCurveArray ConvertDetailToModelCurves ( View view , DetailCurveArray detailCurves )` |
| Method | ConvertModelToDetailCurves | — | `public DetailCurveArray ConvertModelToDetailCurves ( View view , ModelCurveArray modelCurves )` |
| Method | ConvertModelToSymbolicCurves | — | `public SymbolicCurveArray ConvertModelToSymbolicCurves ( View view , ModelCurveArray modelCurves )` |
| Method | ConvertSymbolicToModelCurves | — | `public ModelCurveArray ConvertSymbolicToModelCurves ( View view , SymbolicCurveArray symbolicCurve )` |
| Method | Delete | — | `` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | EditFamily | — | `public Document EditFamily ( Family loadedFamily )` |
| Method | EnableCloudWorksharing | 2019.2 | `public void EnableCloudWorksharing ()` |
| Method | EnableWorksharing | 2014 | `public void EnableWorksharing ( string worksetNameGridLevel , string worksetName )` |
| Method | Equals | — | `public override bool Equals ( Object obj )` |
| Method | EraseSchemaAndAllEntities | 2021 | `public void EraseSchemaAndAllEntities ( Schema schema )` |
| Method | Export | — | `` |
| Method | ExportImage | 2011 | `public void ExportImage ( ImageExportOptions options )` |
| Method | GetAllUnusedElements | 2024 | `public ISet < ElementId > GetAllUnusedElements ( ISet < ElementId > categories )` |
| Method | GetChangedElements | 2023 | `public DocumentDifference GetChangedElements ( Guid baseVersionGUID )` |
| Method | GetCloudFolderId | 2022 | `public string GetCloudFolderId ( bool forceRefresh )` |
| Method | GetCloudModelPath | 2019.1 | `public ModelPath GetCloudModelPath ()` |
| Method | GetCloudModelUrn | 2022 | `public string GetCloudModelUrn ()` |
| Method | GetDefaultElementTypeId | 2015 | `public ElementId GetDefaultElementTypeId ( ElementTypeGroup defaultTypeId )` |
| Method | GetDefaultFamilyTypeId | 2015 | `public ElementId GetDefaultFamilyTypeId ( ElementId familyCategoryId )` |
| Method | GetDocumentPreviewSettings | — | `public DocumentPreviewSettings GetDocumentPreviewSettings ()` |
| Method | GetDocumentVersion | 2015 | `public static DocumentVersion GetDocumentVersion ( Document doc )` |
| Method | GetElement | — | `` |
| Method | GetHashCode | — | `public override int GetHashCode ()` |
| Method | GetHubId | 2022 | `public string GetHubId ()` |
| Method | GetPaintedMaterial | 2014 | `public ElementId GetPaintedMaterial ( ElementId elementId , Face face )` |
| Method | GetPrintSettingIds | — | `public ICollection < ElementId > GetPrintSettingIds ()` |
| Method | GetProjectId | 2022 | `public string GetProjectId ()` |
| Method | GetRoomAtPoint | — | `` |
| Method | GetSpaceAtPoint | — | `` |
| Method | GetSubelement | — | `` |
| Method | GetTypeOfStorage | 2022 | `public StorageType GetTypeOfStorage ( ForgeTypeId parameterTypeId )` |
| Method | GetUnits | 2014 | `public Units GetUnits ()` |
| Method | GetUnusedElements | 2024 | `public ISet < ElementId > GetUnusedElements ( ISet < ElementId > categories )` |
| Method | GetWarnings | 2018 | `public IList < FailureMessage > GetWarnings ()` |
| Method | GetWorksetId | — | `public WorksetId GetWorksetId ( ElementId id )` |
| Method | GetWorksetTable | — | `public WorksetTable GetWorksetTable ()` |
| Method | GetWorksharingCentralModelPath | 2013 | `public ModelPath GetWorksharingCentralModelPath ()` |
| Method | HasAllChangesFromCentral | 2014 | `public bool HasAllChangesFromCentral ()` |
| Method | Import | — | `` |
| Method | IsBackgroundCalculationInProgress | 2019.1 | `public bool IsBackgroundCalculationInProgress ()` |
| Method | IsDefaultElementTypeIdValid | 2015 | `public bool IsDefaultElementTypeIdValid ( ElementTypeGroup defaultTypeId , ElementId typeId )` |
| Method | IsDefaultFamilyTypeIdValid | 2015 | `public bool IsDefaultFamilyTypeIdValid ( ElementId familyCategoryId , ElementId familyTypeId )` |
| Method | IsPainted | 2014 | `public bool IsPainted ( ElementId elementId , Face face )` |
| Method | IsValidVersionGUID | 2023 | `public static bool IsValidVersionGUID ( Document document , Guid versionGUID )` |
| Method | Link | — | `` |
| Method | LoadFamily | — | `` |
| Method | LoadFamilySymbol | — | `` |
| Method | MakeTransientElements | — | `public void MakeTransientElements ( ITransientElementMaker maker )` |
| Method | NewArea | — | `public Area NewArea ( ViewPlan areaView , UV point )` |
| Method | NewAreaBoundaryConditions | — | `` |
| Method | NewAreaBoundaryLine | — | `public ModelCurve NewAreaBoundaryLine ( SketchPlane sketchPlane , Curve geometryCurve , ViewPlan areaView )` |
| Method | NewAreaTag | — | `public AreaTag NewAreaTag ( ViewPlan areaView , Area room , UV point )` |
| Method | NewAreas | — | `public ElementSet NewAreas ( List < AreaCreationData > dataList )` |
| Method | NewCrossFitting | — | `public FamilyInstance NewCrossFitting ( Connector connector1 , Connector connector2 , Connector connector3 , Connector connector4 )` |
| Method | NewCurtainSystem | — | `public CurtainSystem NewCurtainSystem ( FaceArray faces , CurtainSystemType curtainSystemType )` |
| Method | NewCurtainSystem2 | — | `public ICollection < ElementId > NewCurtainSystem2 ( ReferenceArray faces , CurtainSystemType curtainSystemType )` |
| Method | NewDimension | — | `` |
| Method | NewElbowFitting | — | `public FamilyInstance NewElbowFitting ( Connector connector1 , Connector connector2 )` |
| Method | NewExtrusionRoof | — | `public ExtrusionRoof NewExtrusionRoof ( CurveArray profile , ReferencePlane refPlane , Level level , RoofType roofType , double extrusionStart , double extrusionEnd )` |
| Method | NewFamilyInstance | — | `` |
| Method | NewFascia | — | `` |
| Method | NewFlexDuct | — | `` |
| Method | NewFlexPipe | — | `` |
| Method | NewFootPrintRoof | — | `public FootPrintRoof NewFootPrintRoof ( CurveArray footPrint , Level level , RoofType roofType , out ModelCurveArray footPrintToModelCurvesMapping )` |
| Method | NewGutter | — | `` |
| Method | NewLineBoundaryConditions | — | `` |
| Method | NewMechanicalSystem | — | `public MechanicalSystem NewMechanicalSystem ( Connector baseEquipmentConnector , ConnectorSet connectors , DuctSystemType ductSystemType )` |
| Method | NewOpening | — | `` |
| Method | NewPipingSystem | — | `public PipingSystem NewPipingSystem ( Connector baseEquipmentConnector , ConnectorSet connectors , PipeSystemType pipingSystemType )` |
| Method | NewPointBoundaryConditions | — | `public BoundaryConditions NewPointBoundaryConditions ( Reference reference , TranslationRotationValue X_Translation , double X_TranslationSpringModulus , TranslationRotationValue Y_Translation , double Y_TranslationSprin` |
| Method | NewRoom | — | `` |
| Method | NewRoomBoundaryLines | — | `public ModelCurveArray NewRoomBoundaryLines ( SketchPlane sketchPlane , CurveArray curves , View view )` |
| Method | NewRoomTag | 2014 | `public RoomTag NewRoomTag ( LinkElementId roomId , UV point , ElementId viewId )` |
| Method | NewRooms2 | — | `` |
| Method | NewSlabEdge | — | `` |
| Method | NewSpace | — | `` |
| Method | NewSpaceBoundaryLines | — | `public ModelCurveArray NewSpaceBoundaryLines ( SketchPlane sketchPlane , CurveArray curves , View view )` |
| Method | NewSpaceTag | — | `public SpaceTag NewSpaceTag ( Space space , UV point , View view )` |
| Method | NewSpaces2 | — | `` |
| Method | NewSpotCoordinate | — | `public SpotDimension NewSpotCoordinate ( View view , Reference reference , XYZ origin , XYZ bend , XYZ end , XYZ refPt , bool hasLeader )` |
| Method | NewSpotElevation | — | `public SpotDimension NewSpotElevation ( View view , Reference reference , XYZ origin , XYZ bend , XYZ end , XYZ refPt , bool hasLeader )` |
| Method | NewTakeoffFitting | — | `public FamilyInstance NewTakeoffFitting ( Connector connector , MEPCurve curve )` |
| Method | NewTeeFitting | — | `public FamilyInstance NewTeeFitting ( Connector connector1 , Connector connector2 , Connector connector3 )` |
| Method | NewTransitionFitting | — | `public FamilyInstance NewTransitionFitting ( Connector connector1 , Connector connector2 )` |
| Method | NewUnionFitting | — | `public FamilyInstance NewUnionFitting ( Connector connector1 , Connector connector2 )` |
| Method | NewZone | — | `public Zone NewZone ( Level level , Phase phase )` |
| Method | Paint | — | `` |
| Method | PostFailure | 2011 | `public FailureMessageKey PostFailure ( FailureMessage failure )` |
| Method | Print | — | `` |
| Method | PublishCoordinates | 2018 | `public void PublishCoordinates ( LinkElementId locationId )` |
| Method | Regenerate | — | `public void Regenerate ()` |
| Method | ReloadLatest | 2014 | `public void ReloadLatest ( ReloadLatestOptions reloadOptions )` |
| Method | RemovePaint | 2014 | `public void RemovePaint ( ElementId elementId , Face face )` |
| Method | ResetSharedCoordinates | 2021.1 | `public void ResetSharedCoordinates ()` |
| Method | Save | — | `` |
| Method | Save | 2014 | `public void Save ()` |
| Method | SaveAs | — | `` |
| Method | SaveAsCloudModel | 2021 | `public void SaveAsCloudModel ( Guid accountId , Guid projectId , string folderId , string modelName )` |
| Method | SaveCloudModel | 2019.2 | `public void SaveCloudModel ()` |
| Method | SaveToProjectAsImage | 2011 | `public ElementId SaveToProjectAsImage ( ImageExportOptions options )` |
| Method | SeparateElements | — | `public void SeparateElements ( CombinableElementArray members )` |
| Method | SetDefaultElementTypeId | 2015 | `public void SetDefaultElementTypeId ( ElementTypeGroup defaultTypeId , ElementId typeId )` |
| Method | SetDefaultFamilyTypeId | 2015 | `public void SetDefaultFamilyTypeId ( ElementId familyCategoryId , ElementId familyTypeId )` |
| Method | SetUnits | 2014 | `public void SetUnits ( Units units )` |
| Method | SynchronizeWithCentral | 2014 | `public void SynchronizeWithCentral ( TransactWithCentralOptions transactOptions , SynchronizeWithCentralOptions syncOptions )` |
| Method | UnpostFailure | 2011 | `public void UnpostFailure ( FailureMessageKey messageKey )` |
| Property | ActiveProjectLocation | — | `public ProjectLocation ActiveProjectLocation { get ; set ; }` |
| Property | ActiveView | — | `public View ActiveView { get ; }` |
| Property | Application | — | `public Application Application { get ; }` |
| Property | Create | — | `public Document Create { get ; }` |
| Property | CreationGUID | 2024 | `public Guid CreationGUID { get ; }` |
| Property | DisplayUnitSystem | — | `public DisplayUnit DisplayUnitSystem { get ; }` |
| Property | FamilyCreate | — | `public FamilyItemFactory FamilyCreate { get ; }` |
| Property | FamilyManager | — | `public FamilyManager FamilyManager { get ; }` |
| Property | IsDetached | 2015 | `public bool IsDetached { get ; }` |
| Property | IsFamilyDocument | — | `public bool IsFamilyDocument { get ; }` |
| Property | IsLinked | 2014 | `public bool IsLinked { get ; }` |
| Property | IsModelInCloud | 2019.1 | `public bool IsModelInCloud { get ; }` |
| Property | IsModifiable | — | `public bool IsModifiable { get ; }` |
| Property | IsModified | — | `public bool IsModified { get ; }` |
| Property | IsReadOnly | — | `public bool IsReadOnly { get ; }` |
| Property | IsReadOnlyFile | — | `public bool IsReadOnlyFile { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | IsWorkshared | — | `public bool IsWorkshared { get ; }` |
| Property | MassDisplayTemporaryOverride | — | `public MassDisplayTemporaryOverrideType MassDisplayTemporaryOverride { get ; set ; }` |
| Property | MullionTypes | — | `public MullionTypeSet MullionTypes { get ; }` |
| Property | OwnerFamily | — | `public Family OwnerFamily { get ; }` |
| Property | PanelTypes | — | `public PanelTypeSet PanelTypes { get ; }` |
| Property | ParameterBindings | — | `public BindingMap ParameterBindings { get ; }` |
| Property | PathName | — | `public string PathName { get ; }` |
| Property | Phases | — | `public PhaseArray Phases { get ; }` |
| Property | PlanTopologies | — | `` |
| Property | PlanTopologies | — | `public PlanTopologySet PlanTopologies { get ; }` |
| Property | PlanTopology | — | `` |
| Property | PrintManager | — | `public PrintManager PrintManager { get ; }` |
| Property | ProjectInformation | — | `public ProjectInfo ProjectInformation { get ; }` |
| Property | ProjectLocations | — | `public ProjectLocationSet ProjectLocations { get ; }` |
| Property | ReactionsAreUpToDate | — | `public bool ReactionsAreUpToDate { get ; }` |
| Property | Settings | — | `public Settings Settings { get ; }` |
| Property | SiteLocation | — | `public SiteLocation SiteLocation { get ; }` |
| Property | Title | — | `public string Title { get ; }` |
| Property | TypeOfStorage | — | `public StorageType this [ BuiltInParameter A_0 ] { get ; }` |
| Property | WorksharingCentralGUID | 2013 | `public Guid WorksharingCentralGUID { get ; }` |