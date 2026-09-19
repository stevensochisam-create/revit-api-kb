---
type: Application
namespace: Autodesk.Revit.Creation
version: 2024
members: 160
tags: [revit-api, class]
---

# Application

`Autodesk.Revit.Creation.Application` · Revit 2024 · 160 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Event | ApplicationInitialized | 2013 | `public event EventHandler < ApplicationInitializedEventArgs > ApplicationInitialized` |
| Event | DocumentChanged | 2011 | `public event EventHandler < DocumentChangedEventArgs > DocumentChanged` |
| Event | DocumentClosed | 2010 | `public event EventHandler < DocumentClosedEventArgs > DocumentClosed` |
| Event | DocumentClosing | 2010 | `public event EventHandler < DocumentClosingEventArgs > DocumentClosing` |
| Event | DocumentCreated | 2010 | `public event EventHandler < DocumentCreatedEventArgs > DocumentCreated` |
| Event | DocumentCreating | 2010 | `public event EventHandler < DocumentCreatingEventArgs > DocumentCreating` |
| Event | DocumentOpened | 2010 | `public event EventHandler < DocumentOpenedEventArgs > DocumentOpened` |
| Event | DocumentOpening | 2010 | `public event EventHandler < DocumentOpeningEventArgs > DocumentOpening` |
| Event | DocumentPrinted | 2010 | `public event EventHandler < DocumentPrintedEventArgs > DocumentPrinted` |
| Event | DocumentPrinting | 2010 | `public event EventHandler < DocumentPrintingEventArgs > DocumentPrinting` |
| Event | DocumentReloadedLatest | 2021 | `public event EventHandler < DocumentReloadedLatestEventArgs > DocumentReloadedLatest` |
| Event | DocumentReloadingLatest | 2021 | `public event EventHandler < DocumentReloadingLatestEventArgs > DocumentReloadingLatest` |
| Event | DocumentSaved | 2010 | `public event EventHandler < DocumentSavedEventArgs > DocumentSaved` |
| Event | DocumentSavedAs | 2010 | `public event EventHandler < DocumentSavedAsEventArgs > DocumentSavedAs` |
| Event | DocumentSaving | 2010 | `public event EventHandler < DocumentSavingEventArgs > DocumentSaving` |
| Event | DocumentSavingAs | 2010 | `public event EventHandler < DocumentSavingAsEventArgs > DocumentSavingAs` |
| Event | DocumentSynchronizedWithCentral | 2010 | `public event EventHandler < DocumentSynchronizedWithCentralEventArgs > DocumentSynchronizedWithCentral` |
| Event | DocumentSynchronizingWithCentral | 2010 | `public event EventHandler < DocumentSynchronizingWithCentralEventArgs > DocumentSynchronizingWithCentral` |
| Event | DocumentWorksharingEnabled | 2015 | `public event EventHandler < DocumentWorksharingEnabledEventArgs > DocumentWorksharingEnabled` |
| Event | ElementTypeDuplicated | 2015 | `public event EventHandler < ElementTypeDuplicatedEventArgs > ElementTypeDuplicated` |
| Event | ElementTypeDuplicating | 2015 | `public event EventHandler < ElementTypeDuplicatingEventArgs > ElementTypeDuplicating` |
| Event | FailuresProcessing | 2011 | `public event EventHandler < FailuresProcessingEventArgs > FailuresProcessing` |
| Event | FamilyLoadedIntoDocument | 2015 | `public event EventHandler < FamilyLoadedIntoDocumentEventArgs > FamilyLoadedIntoDocument` |
| Event | FamilyLoadingIntoDocument | 2015 | `public event EventHandler < FamilyLoadingIntoDocumentEventArgs > FamilyLoadingIntoDocument` |
| Event | FileExported | 2010 | `public event EventHandler < FileExportedEventArgs > FileExported` |
| Event | FileExporting | 2010 | `public event EventHandler < FileExportingEventArgs > FileExporting` |
| Event | FileImported | 2010 | `public event EventHandler < FileImportedEventArgs > FileImported` |
| Event | FileImporting | 2010 | `public event EventHandler < FileImportingEventArgs > FileImporting` |
| Event | LinkedResourceOpened | 2018 | `public event EventHandler < LinkedResourceOpenedEventArgs > LinkedResourceOpened` |
| Event | LinkedResourceOpening | 2018 | `public event EventHandler < LinkedResourceOpeningEventArgs > LinkedResourceOpening` |
| Event | ProgressChanged | 2013 | `public event EventHandler < ProgressChangedEventArgs > ProgressChanged` |
| Event | ViewExported | 2018 | `public event EventHandler < ViewExportedEventArgs > ViewExported` |
| Event | ViewExporting | 2018 | `public event EventHandler < ViewExportingEventArgs > ViewExporting` |
| Event | ViewPrinted | 2010 | `public event EventHandler < ViewPrintedEventArgs > ViewPrinted` |
| Event | ViewPrinting | 2010 | `public event EventHandler < ViewPrintingEventArgs > ViewPrinting` |
| Event | ViewsExportedByContext | 2021 | `public event EventHandler < ViewsExportedByContextEventArgs > ViewsExportedByContext` |
| Event | ViewsExportingByContext | 2021 | `public event EventHandler < ViewsExportingByContextEventArgs > ViewsExportingByContext` |
| Event | WorksharedOperationProgressChanged | 2017 Subscription Update | `public event EventHandler < WorksharedOperationProgressChangedEventArgs > WorksharedOperationProgressChanged` |
| Method | CopyModel | 2012 | `public void CopyModel ( ModelPath sourceModelPath , string destFilePath , bool overwrite )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | ExtractPartAtomFromFamilyFile | — | `public void ExtractPartAtomFromFamilyFile ( string familyFilePath , string xmlFilePath )` |
| Method | GetAssets | 2018.1 | `public IList < Asset > GetAssets ( AssetType assetType )` |
| Method | GetFailureDefinitionRegistry | 2011 | `public static FailureDefinitionRegistry GetFailureDefinitionRegistry ()` |
| Method | GetLibraryPaths | 2012 | `public IDictionary < string , string > GetLibraryPaths ()` |
| Method | GetRevitServerNetworkHosts | 2013 | `public IList < string > GetRevitServerNetworkHosts ()` |
| Method | GetSystemsAnalysisWorkflowNames | 2020.1 | `public IList < string > GetSystemsAnalysisWorkflowNames ()` |
| Method | GetSystemsAnalysisWorkflows | 2020.1 | `public IDictionary < string , string > GetSystemsAnalysisWorkflows ()` |
| Method | GetWorksharingCentralGUID | 2013 | `public Guid GetWorksharingCentralGUID ( ServerPath serverModelPath )` |
| Method | IsJournalPlaying | 2020 | `public bool IsJournalPlaying ()` |
| Method | IsValidThickness | 2015 | `public static bool IsValidThickness ( double thickness )` |
| Method | NewAreaCreationData | — | `public AreaCreationData NewAreaCreationData ( ViewPlan areaView , UV point )` |
| Method | NewBoundingBoxUV | — | `` |
| Method | NewBoundingBoxUV | — | `public BoundingBoxUV NewBoundingBoxUV ()` |
| Method | NewBoundingBoxXYZ | — | `public BoundingBoxXYZ NewBoundingBoxXYZ ()` |
| Method | NewCategorySet | — | `public CategorySet NewCategorySet ()` |
| Method | NewColor | — | `public Color NewColor ()` |
| Method | NewCombinableElementArray | — | `public CombinableElementArray NewCombinableElementArray ()` |
| Method | NewCurveArrArray | — | `public CurveArrArray NewCurveArrArray ()` |
| Method | NewCurveArray | — | `public CurveArray NewCurveArray ()` |
| Method | NewCurveLoopsProfile | — | `public CurveLoopsProfile NewCurveLoopsProfile ( CurveArrArray curveLoops )` |
| Method | NewDWFExportOptions | — | `public DWFExportOptions NewDWFExportOptions ()` |
| Method | NewDWFXExportOptions | — | `public DWFXExportOptions NewDWFXExportOptions ()` |
| Method | NewDoubleArray | — | `public DoubleArray NewDoubleArray ()` |
| Method | NewElementId | — | `public ElementId NewElementId ()` |
| Method | NewElementSet | — | `public ElementSet NewElementSet ()` |
| Method | NewFBXExportOptions | — | `public FBXExportOptions NewFBXExportOptions ()` |
| Method | NewFaceArray | — | `public FaceArray NewFaceArray ()` |
| Method | NewFamilyDocument | — | `public virtual Document NewFamilyDocument ( string templateFileName )` |
| Method | NewFamilyInstanceCreationData | — | `` |
| Method | NewFamilySymbolProfile | — | `public FamilySymbolProfile NewFamilySymbolProfile ( FamilySymbol familySymbol )` |
| Method | NewGBXMLImportOptions | — | `public GBXMLImportOptions NewGBXMLImportOptions ()` |
| Method | NewGeometryOptions | — | `public Options NewGeometryOptions ()` |
| Method | NewInstanceBinding | — | `` |
| Method | NewInstanceBinding | — | `public InstanceBinding NewInstanceBinding ()` |
| Method | NewIntersectionResultArray | — | `public IntersectionResultArray NewIntersectionResultArray ()` |
| Method | NewPointOnEdge | — | `public PointOnEdge NewPointOnEdge ( Reference edgeReference , PointLocationOnCurve locationOnCurve )` |
| Method | NewPointOnEdgeEdgeIntersection | — | `public PointOnEdgeEdgeIntersection NewPointOnEdgeEdgeIntersection ( Reference edgeReference1 , Reference edgeReference2 )` |
| Method | NewPointOnEdgeFaceIntersection | — | `public PointOnEdgeFaceIntersection NewPointOnEdgeFaceIntersection ( Reference edgeReference , Reference faceReference , bool orientWithEdge )` |
| Method | NewPointOnFace | — | `public PointOnFace NewPointOnFace ( Reference faceReference , UV uv )` |
| Method | NewPointOnPlane | — | `public PointOnPlane NewPointOnPlane ( Reference planeReference , UV position , UV xvec , double offset )` |
| Method | NewPointRelativeToPoint | 2013 | `public PointRelativeToPoint NewPointRelativeToPoint ( Reference hostPointReference )` |
| Method | NewProjectDocument | — | `` |
| Method | NewProjectPosition | — | `public ProjectPosition NewProjectPosition ( double ew , double ns , double elevation , double angle )` |
| Method | NewProjectTemplateDocument | — | `public virtual Document NewProjectTemplateDocument ( string templateFilename )` |
| Method | NewReferenceArray | — | `public ReferenceArray NewReferenceArray ()` |
| Method | NewReferencePointArray | — | `public ReferencePointArray NewReferencePointArray ()` |
| Method | NewSpaceSet | — | `public SpaceSet NewSpaceSet ()` |
| Method | NewTypeBinding | — | `` |
| Method | NewTypeBinding | — | `public TypeBinding NewTypeBinding ()` |
| Method | NewUV | — | `` |
| Method | NewUV | — | `public UV NewUV ()` |
| Method | NewVertexIndexPair | — | `public VertexIndexPair NewVertexIndexPair ( int iTop , int iBottom )` |
| Method | NewVertexIndexPairArray | — | `public VertexIndexPairArray NewVertexIndexPairArray ()` |
| Method | NewViewSet | — | `public ViewSet NewViewSet ()` |
| Method | NewXYZ | — | `` |
| Method | NewXYZ | — | `public XYZ NewXYZ ()` |
| Method | OpenDocumentFile | — | `` |
| Method | OpenIFCDocument | — | `` |
| Method | OpenSharedParameterFile | — | `public DefinitionFile OpenSharedParameterFile ()` |
| Method | PurgeReleasedAPIObjects | 2011 | `public void PurgeReleasedAPIObjects ()` |
| Method | RegisterFailuresProcessor | — | `public static void RegisterFailuresProcessor ( IFailuresProcessor processor )` |
| Method | SetLibraryPaths | 2012 | `public void SetLibraryPaths ( IDictionary < string , string > paths )` |
| Method | SetSystemsAnalysisWorkflows | 2020.1 | `public void SetSystemsAnalysisWorkflows ( IDictionary < string , string > paths )` |
| Method | UpdateRenderAppearanceLibrary | 2014 | `public void UpdateRenderAppearanceLibrary ()` |
| Method | WriteJournalComment | 2011 | `public void WriteJournalComment ( string comment , bool timeStamp )` |
| Property | ActiveAddInId | — | `public AddInId ActiveAddInId { get ; }` |
| Property | AllUsersAddinsLocation | 2014 | `public string AllUsersAddinsLocation { get ; }` |
| Property | AllowNavigationDuringRedraw | 2016 | `public bool AllowNavigationDuringRedraw { get ; set ; }` |
| Property | AngleTolerance | 2015 | `public double AngleTolerance { get ; }` |
| Property | BackgroundColor | 2016 | `public Color BackgroundColor { get ; set ; }` |
| Property | Cities | — | `public CitySet Cities { get ; }` |
| Property | Create | — | `public Application Create { get ; }` |
| Property | CurrentRevitServerAccelerator | 2013 | `public string CurrentRevitServerAccelerator { get ; set ; }` |
| Property | CurrentUserAddinsLocation | 2014 | `public string CurrentUserAddinsLocation { get ; }` |
| Property | CurrentUsersAddinsDataFolderPath | 2019 | `public string CurrentUsersAddinsDataFolderPath { get ; }` |
| Property | CurrentUsersDataFolderPath | 2019 | `public string CurrentUsersDataFolderPath { get ; }` |
| Property | DefaultIFCProjectTemplate | 2015 | `public string DefaultIFCProjectTemplate { get ; }` |
| Property | DefaultProjectTemplate | 2013 | `public string DefaultProjectTemplate { get ; }` |
| Property | DefaultViewDiscipline | 2013 | `public ViewDiscipline DefaultViewDiscipline { get ; set ; }` |
| Property | Documents | — | `public virtual DocumentSet Documents { get ; }` |
| Property | ExportIFCCategoryTable | 2015 | `public string ExportIFCCategoryTable { get ; }` |
| Property | FamilyTemplatePath | 2011 | `public string FamilyTemplatePath { get ; }` |
| Property | ImportIFCCategoryTable | 2015 | `public string ImportIFCCategoryTable { get ; }` |
| Property | IsArchitectureEnabled | 2013 | `public bool IsArchitectureEnabled { get ; set ; }` |
| Property | IsElectricalAnalysisEnabled | 2013 | `public bool IsElectricalAnalysisEnabled { get ; set ; }` |
| Property | IsElectricalEnabled | 2013 | `public bool IsElectricalEnabled { get ; set ; }` |
| Property | IsEnergyAnalysisEnabled | 2013 | `public bool IsEnergyAnalysisEnabled { get ; set ; }` |
| Property | IsInfrastructureEnabled | 2021.1 | `public bool IsInfrastructureEnabled { get ; set ; }` |
| Property | IsLoggedIn | 2016 | `public static bool IsLoggedIn { get ; }` |
| Property | IsMassingEnabled | 2013 | `public bool IsMassingEnabled { get ; set ; }` |
| Property | IsMechanicalAnalysisEnabled | 2013 | `public bool IsMechanicalAnalysisEnabled { get ; set ; }` |
| Property | IsMechanicalEnabled | 2013 | `public bool IsMechanicalEnabled { get ; set ; }` |
| Property | IsPipingAnalysisEnabled | 2013 | `public bool IsPipingAnalysisEnabled { get ; set ; }` |
| Property | IsPipingEnabled | 2013 | `public bool IsPipingEnabled { get ; set ; }` |
| Property | IsRouteAnalysisEnabled | 2020 | `public bool IsRouteAnalysisEnabled { get ; set ; }` |
| Property | IsStructuralAnalysisEnabled | 2013 | `public bool IsStructuralAnalysisEnabled { get ; set ; }` |
| Property | IsStructureEnabled | 2013 | `public bool IsStructureEnabled { get ; set ; }` |
| Property | IsSystemsEnabled | 2013 | `public bool IsSystemsEnabled { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Language | — | `public LanguageType Language { get ; }` |
| Property | LoginUserId | 2016 | `public string LoginUserId { get ; }` |
| Property | MinimumThickness | 2015 | `public static double MinimumThickness { get ; }` |
| Property | PointCloudsRootPath | 2016 | `public string PointCloudsRootPath { get ; }` |
| Property | Product | — | `public ProductType Product { get ; }` |
| Property | RecordingJournalFilename | — | `public string RecordingJournalFilename { get ; }` |
| Property | SharedParametersFilename | — | `public string SharedParametersFilename { get ; set ; }` |
| Property | ShortCurveTolerance | 2014 | `public double ShortCurveTolerance { get ; }` |
| Property | ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects | 2023 | `public bool ShowGraphicalOpenEndsAreaBasedLoadBoundaryDisconnects { get ; set ; }` |
| Property | ShowGraphicalWarningCableTrayConduitDisconnects | 2012 | `public bool ShowGraphicalWarningCableTrayConduitDisconnects { get ; set ; }` |
| Property | ShowGraphicalWarningDuctDisconnects | 2012 | `public bool ShowGraphicalWarningDuctDisconnects { get ; set ; }` |
| Property | ShowGraphicalWarningElectricalDisconnects | 2012 | `public bool ShowGraphicalWarningElectricalDisconnects { get ; set ; }` |
| Property | ShowGraphicalWarningHangerDisconnects | 2016 | `public bool ShowGraphicalWarningHangerDisconnects { get ; set ; }` |
| Property | ShowGraphicalWarningPipeDisconnects | 2012 | `public bool ShowGraphicalWarningPipeDisconnects { get ; set ; }` |
| Property | SubVersionNumber | 2018 | `public string SubVersionNumber { get ; }` |
| Property | SystemsAnalysisWorkfilesRootPath | 2020 | `public string SystemsAnalysisWorkfilesRootPath { get ; }` |
| Property | Username | 2012 | `public string Username { get ; }` |
| Property | VersionBuild | — | `public string VersionBuild { get ; }` |
| Property | VersionName | — | `public string VersionName { get ; }` |
| Property | VersionNumber | — | `public string VersionNumber { get ; }` |
| Property | VertexTolerance | 2012 | `public double VertexTolerance { get ; }` |