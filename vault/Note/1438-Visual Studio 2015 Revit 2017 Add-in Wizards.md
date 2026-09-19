---
num: 1438
date: 2016-05-13
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Visual Studio 2015 Revit 2017 Add-in Wizards

<https://jeremytammik.github.io/tbc/a/1438_addin_wizard_2017.html>

```csharp
$ cp Revit2017AddinWizardCs0.zip \ "/v/C/Users/tammikj/Documents/Visual Studio \ 2015/Templates/ProjectTemplates/Visual C#/" $ cp Revit2017AddinWizardVb0.zip \ "/v/C/Users/tammikj/Documents/Visual Studio \ 2015/Templates/ProjectTemplates/Visual Basic/"
```

```csharp
@echo off if exist cs (goto okcs) else (echo "No cs folder found." && goto exit) :okcs if exist vb (goto okvb) else (echo "No vb folder found." && goto exit) :okvb set "D=C:\Users\%USERNAME%\Documents\Visual Studio 2015\Templates\ProjectTemplates" set "F=%TEMP%\Revit2017AddinWizardCs0.zip" echo Creating C# wizard archive %F%... cd cs zip -r "%F%" * cd .. echo Copying C# wizard archive to %D%\Visual C#... copy "%F%" "%D%\Visual C#" set "F=%TEMP%\Revit2017AddinWizardVb0.zip" echo Creating VB wizard archive %F%... cd vb zip -r "%F%" * cd .. echo Copying VB wizard archive to %D%\Visual Basic... copy "%F%" "%D%\Visual Basic" :exit
```

```csharp
Y:\VisualStudioRevitAddinWizard &gt; install.bat Creating C# wizard archive C:\Users\tammikj\AppData\Local\Temp\Revit2017AddinWizardCs0.zip... updating: App.cs (deflated 54%) updating: Command.cs (deflated 59%) updating: Properties/ (stored 0%) updating: Properties/AssemblyInfo.cs (deflated 56%) updating: RegisterAddin.addin (deflated 66%) updating: TemplateIcon.ico (deflated 67%) updating: TemplateRevitCs.csproj (deflated 68%) updating: TemplateRevitCs.csproj.user (deflated 30%) updating: TemplateRevitCs.vstemplate (deflated 65%) Copying C# wizard archive to C:\Users\tammikj\Documents\Visual Studio 2015\Templates\ProjectTemplates\Visual C#... 1 file(s) copied. Creating VB wizard archive C:\Users\tammikj\AppData\Local\Temp\Revit2017AddinWizardVb0.zip... updating: AdskApplication.vb (deflated 68%) updating: AdskCommand.vb (deflated 58%) updating: My Project/ (stored 0%) updating: My Project/AssemblyInfo.vb (deflated 54%) updating: RegisterAddin.addin (deflated 66%) updating: TemplateIcon.ico (deflated 67%) updating: TemplateRevitVb.vbproj (deflated 72%) updating: TemplateRevitVb.vstemplate (deflated 62%) Copying VB wizard archive to C:\Users\tammikj\Documents\Visual Studio 2015\Templates\ProjectTemplates\Visual Basic... 1 file(s) copied. Y:\VisualStudioRevitAddinWizard &gt;
```
