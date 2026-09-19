---
type: UIApplication
namespace: Autodesk.Revit.UI
version: 2024
members: 40
tags: [revit-api, class]
---

# UIApplication

`Autodesk.Revit.UI.UIApplication` · Revit 2024 · 40 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | UIApplication | — | `public UIApplication ( Application revitApp )` |
| Event | ApplicationClosing | 2010 | `public event EventHandler < ApplicationClosingEventArgs > ApplicationClosing` |
| Event | DialogBoxShowing | 2010 | `public event EventHandler < DialogBoxShowingEventArgs > DialogBoxShowing` |
| Event | DisplayingOptionsDialog | 2013 | `public event EventHandler < DisplayingOptionsDialogEventArgs > DisplayingOptionsDialog` |
| Event | DockableFrameFocusChanged | 2015 | `public event EventHandler < DockableFrameFocusChangedEventArgs > DockableFrameFocusChanged` |
| Event | DockableFrameVisibilityChanged | 2015 | `public event EventHandler < DockableFrameVisibilityChangedEventArgs > DockableFrameVisibilityChanged` |
| Event | FabricationPartBrowserChanged | 2017 | `public event EventHandler < FabricationPartBrowserChangedEventArgs > FabricationPartBrowserChanged` |
| Event | FormulaEditing | — | `public event EventHandler < FormulaEditingEventArgs > FormulaEditing` |
| Event | Idling | 2010 | `public event EventHandler < IdlingEventArgs > Idling` |
| Event | SelectionChanged | 2023 | `public event EventHandler < SelectionChangedEventArgs > SelectionChanged` |
| Event | ThemeChanged | 2024 | `public event EventHandler < ThemeChangedEventArgs > ThemeChanged` |
| Event | TransferredProjectStandards | 2017.2 | `public event EventHandler < TransferredProjectStandardsEventArgs > TransferredProjectStandards` |
| Event | TransferringProjectStandards | 2017.2 | `public event EventHandler < TransferringProjectStandardsEventArgs > TransferringProjectStandards` |
| Event | ViewActivated | 2010 | `public event EventHandler < ViewActivatedEventArgs > ViewActivated` |
| Event | ViewActivating | 2010 | `public event EventHandler < ViewActivatingEventArgs > ViewActivating` |
| Method | CanPostCommand | 2014 | `public bool CanPostCommand ( RevitCommandId commandId )` |
| Method | CreateAddInCommandBinding | 2013 | `public AddInCommandBinding CreateAddInCommandBinding ( RevitCommandId revitCommandId )` |
| Method | CreateRibbonPanel | — | `` |
| Method | CreateRibbonTab | — | `public virtual void CreateRibbonTab ( string tabName )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | DoDragDrop | — | `` |
| Method | GetDockablePane | 2014 | `public DockablePane GetDockablePane ( DockablePaneId id )` |
| Method | GetRibbonPanels | — | `` |
| Method | GetRibbonPanels | — | `public virtual List < RibbonPanel > GetRibbonPanels ()` |
| Method | LoadAddIn | 2014 | `public void LoadAddIn ( string fileName )` |
| Method | LoadPackageContents | 2014 | `public void LoadPackageContents ( string packageContentsPath )` |
| Method | OpenAndActivateDocument | — | `` |
| Method | PostCommand | 2014 | `public void PostCommand ( RevitCommandId commandId )` |
| Method | RegisterDockablePane | 2014 | `public void RegisterDockablePane ( DockablePaneId id , string title , IDockablePaneProvider provider )` |
| Method | RemoveAddInCommandBinding | 2013 | `public void RemoveAddInCommandBinding ( RevitCommandId revitCommandId )` |
| Property | ActiveAddInId | — | `public AddInId ActiveAddInId { get ; }` |
| Property | ActiveUIDocument | — | `public virtual UIDocument ActiveUIDocument { get ; }` |
| Property | Application | — | `public Application Application { get ; }` |
| Property | DrawingAreaExtents | 2011 | `public virtual Rectangle DrawingAreaExtents { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | IsViewerModeActive | 2019.1 | `public bool IsViewerModeActive { get ; }` |
| Property | LoadedApplications | — | `public virtual ExternalApplicationArray LoadedApplications { get ; }` |
| Property | MainWindowExtents | 2011 | `public virtual Rectangle MainWindowExtents { get ; }` |
| Property | MainWindowHandle | 2019 | `public virtual IntPtr MainWindowHandle { get ; }` |
| Property | ProductIsRS | 2019 | `public bool ProductIsRS { get ; }` |