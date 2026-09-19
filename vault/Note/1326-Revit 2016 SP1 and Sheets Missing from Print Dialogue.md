---
num: 1326
date: 2015-06-01
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2016 SP1 and Sheets Missing from Print Dialogue

<https://jeremytammik.github.io/tbc/a/1326_2016_sp1_print_sheets.htm>

```csharp
&nbsp; public void viewsheet( UIDocument uidoc ) &nbsp; { &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; FilteredElementCollector filteredElementCollector &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; &nbsp; filteredElementCollector.OfClass( &nbsp; &nbsp; &nbsp; typeof( ViewSheet ) ); &nbsp; &nbsp; &nbsp; ViewSheetSetting viewSheetSetting &nbsp; &nbsp; &nbsp; = doc.PrintManager.ViewSheetSetting; &nbsp; &nbsp; &nbsp; Transaction tr = new Transaction( doc, &quot;test&quot; ); &nbsp; &nbsp; tr.Start(); &nbsp; &nbsp; try &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( ViewSheet vs in filteredElementCollector ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; MessageBox.Show( vs.SheetNumber + &quot; + &quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + vs.CanBePrinted.ToString() ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; viewSheetSetting.AvailableViews.Insert( vs ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; tr.Commit(); &nbsp; &nbsp; } &nbsp; &nbsp; catch( Exception ex ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; MessageBox.Show( ex.ToString() ); &nbsp; &nbsp; &nbsp; tr.RollBack(); &nbsp; &nbsp; } &nbsp; &nbsp; foreach( Autodesk.Revit.DB.View view in &nbsp; &nbsp; &nbsp; viewSheetSetting.AvailableViews ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; MessageBox.Show( view.Name + &quot; + &quot; &nbsp; &nbsp; &nbsp; &nbsp; + view.CanBePrinted.ToString() ); &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; Public Sub TwoTrans_placeholderToReal(doc As Document) &nbsp; &nbsp; &nbsp; Dim fec As FilteredElementCollector = &nbsp; &nbsp; &nbsp; New FilteredElementCollector(doc) &nbsp; &nbsp; &nbsp; fec.OfCategory(BuiltInCategory.OST_TitleBlocks) &nbsp; &nbsp; &nbsp; Dim NumSheets As Integer = 10 &nbsp; &nbsp; Dim SheetsCreated(NumSheets) As ViewSheet &nbsp; &nbsp; &nbsp; 'Dim SheetSubTransaction As Transaction &nbsp; &nbsp; &nbsp; Using SheetSubTransaction As New Transaction(doc) &nbsp; &nbsp; &nbsp; SheetSubTransaction.Start(&quot;Create Placeholders&quot;) &nbsp; &nbsp; &nbsp; For ii = 1 To NumSheets &nbsp; &nbsp; &nbsp; &nbsp; SheetsCreated(ii) = ViewSheet.CreatePlaceholder(doc) &nbsp; &nbsp; &nbsp; &nbsp; SheetsCreated(ii).Name = &quot;Sheet&quot; &amp; ii 'NewSheetsToCreate.Name &nbsp; &nbsp; &nbsp; &nbsp; SheetsCreated(ii).SheetNumber = ii &amp; &quot;Number&quot; 'NewSheetsToCreate.Number &nbsp; &nbsp; &nbsp; Next &nbsp; &nbsp; &nbsp; SheetSubTransaction.Commit() &nbsp; &nbsp; End Using &nbsp; &nbsp; &nbsp; Using ConvertPlaceholderTransaction As New Transaction(doc) &nbsp; &nbsp; &nbsp; ConvertPlaceholderTransaction.Start(&quot;Convert to Real Sheets&quot;) &nbsp; &nbsp; &nbsp; For ii = 1 To NumSheets &nbsp; &nbsp; &nbsp; &nbsp; SheetsCreated(ii).ConvertToRealSheet(fec.FirstElementId()) &nbsp; &nbsp; &nbsp; Next &nbsp; &nbsp; &nbsp; ConvertPlaceholderTransaction.Commit() &nbsp; &nbsp; End Using &nbsp; &nbsp; End Sub
```
