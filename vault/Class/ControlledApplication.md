---
type: ControlledApplication
namespace: Autodesk.Revit.ApplicationServices
version: 2024
members: 56
tags: [revit-api, class]
---

# ControlledApplication

`Autodesk.Revit.ApplicationServices.ControlledApplication` · Revit 2024 · 56 members

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
| Event | ViewPrinted | 2010 | `public event EventHandler < ViewPrintedEventArgs > ViewPrinted` |
| Event | ViewPrinting | 2010 | `public event EventHandler < ViewPrintingEventArgs > ViewPrinting` |
| Event | WorksharedOperationProgressChanged | 2017 Subscription Update | `public event EventHandler < WorksharedOperationProgressChangedEventArgs > WorksharedOperationProgressChanged` |
| Method | GetFailureDefinitionRegistry | 2011 | `public static FailureDefinitionRegistry GetFailureDefinitionRegistry ()` |
| Method | GetLibraryPaths | 2012 | `public IDictionary < string , string > GetLibraryPaths ()` |
| Method | IsJournalPlaying | 2020 | `public bool IsJournalPlaying ()` |
| Method | OpenSharedParameterFile | — | `public DefinitionFile OpenSharedParameterFile ()` |
| Method | RegisterFailuresProcessor | — | `public static void RegisterFailuresProcessor ( IFailuresProcessor processor )` |
| Method | SetLibraryPaths | 2012 | `public void SetLibraryPaths ( IDictionary < string , string > paths )` |
| Method | WriteJournalComment | 2011 | `public void WriteJournalComment ( string comment , bool timeStamp )` |
| Property | ActiveAddInId | — | `public AddInId ActiveAddInId { get ; }` |
| Property | AllUsersAddinsLocation | 2014 | `public string AllUsersAddinsLocation { get ; }` |
| Property | Cities | — | `public CitySet Cities { get ; }` |
| Property | Create | — | `public Application Create { get ; }` |
| Property | CurrentUserAddinsLocation | 2014 | `public string CurrentUserAddinsLocation { get ; }` |
| Property | CurrentUsersAddinsDataFolderPath | 2019 | `public string CurrentUsersAddinsDataFolderPath { get ; }` |
| Property | CurrentUsersDataFolderPath | 2019 | `public string CurrentUsersDataFolderPath { get ; }` |
| Property | IsLateAddinLoading | — | `public bool IsLateAddinLoading { get ; }` |
| Property | Language | — | `public LanguageType Language { get ; }` |
| Property | Product | — | `public ProductType Product { get ; }` |
| Property | RecordingJournalFilename | — | `public string RecordingJournalFilename { get ; }` |
| Property | SharedParametersFilename | — | `public string SharedParametersFilename { get ; set ; }` |
| Property | SubVersionNumber | 2018 | `public string SubVersionNumber { get ; }` |
| Property | VersionBuild | — | `public string VersionBuild { get ; }` |
| Property | VersionName | — | `public string VersionName { get ; }` |
| Property | VersionNumber | — | `public string VersionNumber { get ; }` |