---
num: 1410
date: 2016-03-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# Index, Debug, Curves, Distance, Deleting PrintSetup

<https://jeremytammik.github.io/tbc/a/1410_delete_print_setup.html>

```csharp
try { pMgr.PrintSetup.Delete(); pMgr.ViewSheetSetting.Delete(); } catch (Exception ex) { //Shows 'The print setup cannot be deleted' TaskDialog.Show("REVIT", ex.Message); }
```

```csharp
&nbsp; private void CleanUp( Document doc ) &nbsp; { &nbsp; &nbsp; var pMgr = doc.PrintManager; &nbsp; &nbsp; using( var trans = new Transaction( doc ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; trans.Start( &quot;CleanUp&quot; ); &nbsp; &nbsp; &nbsp; CleanUpTemporaryViewSheets( doc, pMgr ); &nbsp; &nbsp; &nbsp; CleanUpTemporaryPrintSettings( doc, pMgr ); &nbsp; &nbsp; &nbsp; trans.Commit(); &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; private void CleanUpTemporaryPrintSettings( &nbsp; &nbsp; Document doc, PrintManager pMgr ) &nbsp; { &nbsp; &nbsp; var printSetup = pMgr.PrintSetup; &nbsp; &nbsp; foreach( var printSettingsToDelete &nbsp; &nbsp; &nbsp; in ( from element &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; in new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( PrintSetting ) ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .ToElements() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; where element.Name.Contains( _tmpName ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; element.IsValidObject &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; select element as PrintSetting ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .ToList() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .Distinct( new EqualElementId() ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; printSetup.CurrentPrintSetting &nbsp; &nbsp; &nbsp; &nbsp; = pMgr.PrintSetup.InSession; &nbsp; &nbsp; &nbsp; &nbsp; printSetup.CurrentPrintSetting &nbsp; &nbsp; &nbsp; &nbsp; = printSettingsToDelete as PrintSetting; &nbsp; &nbsp; &nbsp; &nbsp; pMgr.PrintSetup.Delete(); &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; private void CleanUpTemporaryViewSheets( &nbsp; &nbsp; Document doc, PrintManager pMgr ) &nbsp; { &nbsp; &nbsp; var viewSheetSettings = pMgr.ViewSheetSetting; &nbsp; &nbsp; foreach( var viewSheetSetToDelete &nbsp; &nbsp; &nbsp; in ( from element &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; in new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( ViewSheetSet ) ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .ToElements() &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; where element.Name.Contains( _tmpName ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; element.IsValidObject &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; select element as ViewSheetSet ) &nbsp; &nbsp; &nbsp; 
```
