---
num: 1312
date: 2015-04-27
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Add-in Migration to Revit 2016 and Updated Wizards

<https://jeremytammik.github.io/tbc/a/1312_addin_wizard_2016.htm>

```csharp
&nbsp; TextNoteOptions tno = new TextNoteOptions(); &nbsp; tno.TypeId = TextTypeID; &nbsp; tno.Rotation = 0; &nbsp; tno.KeepRotatedTextReadable = false; &nbsp; tno.HorizontalAlignment = HorizontalTextAlignment.Left; &nbsp; tno.VerticalAlignment = VerticalTextAlignment.Bottom; &nbsp; TextNote tn = TextNote.Create( _ &nbsp; &nbsp; CurrentDoc, CurrentView.Id, InsertionPoint, _ &nbsp; &nbsp; LineWidth, &quot;Test&quot;, tno); &nbsp; tn.VerticalAlignment = VerticalTextAlignment.Bottom;
```

```csharp
$ cp /a/doc/revit/tbc/zip/Revit2016AddinWizardCs0.zip \ "/v/C/Users/tammikj/Documents/Visual Studio \ 2012/Templates/ProjectTemplates/Visual C#" $ cp /a/doc/revit/tbc/zip/Revit2016AddinWizardVb0.zip \ "/v/C/Users/tammikj/Documents/Visual Studio \ 2012/Templates/ProjectTemplates/Visual Basic"
```
