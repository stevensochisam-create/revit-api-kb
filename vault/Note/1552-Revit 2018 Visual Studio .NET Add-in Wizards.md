---
num: 1552
date: 2017-04-27
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2018 Visual Studio .NET Add-in Wizards

<https://jeremytammik.github.io/tbc/a/1552_addin_wizard_2018.html>

```csharp
$ cp Revit2018AddinWizardCs0.zip \ "/v/C/Users/tammikj/Documents/Visual Studio \ 2015/Templates/ProjectTemplates/Visual C#/" $ cp Revit2018AddinWizardVb0.zip \ "/v/C/Users/tammikj/Documents/Visual Studio \ 2015/Templates/ProjectTemplates/Visual Basic/"
```

```csharp
@echo off if exist cs (goto okcs) else (echo "No cs folder found." && goto exit) :okcs if exist vb (goto okvb) else (echo "No vb folder found." && goto exit) :okvb set "D=C:\Users\%USERNAME%\Documents\Visual Studio 2015\Templates\ProjectTemplates" set "F=%TEMP%\Revit2018AddinWizardCs0.zip" echo Creating C# wizard archive %F%... cd cs zip -r "%F%" * cd .. echo Copying C# wizard archive to %D%\Visual C#... copy "%F%" "%D%\Visual C#" set "F=%TEMP%\Revit2018AddinWizardVb0.zip" echo Creating VB wizard archive %F%... cd vb zip -r "%F%" * cd .. echo Copying VB wizard archive to %D%\Visual Basic... copy "%F%" "%D%\Visual Basic" :exit
```

```csharp
C:\a\vs\VisualStudioRevitAddinWizard &gt; install.bat Creating C# wizard archive C:\Users\tammikj\AppData\Local\Temp\Revit2018AddinWizardCs0.zip... updating: App.cs (deflated 54%) updating: Command.cs (deflated 59%) updating: Properties/ (stored 0%) updating: Properties/AssemblyInfo.cs (deflated 56%) updating: RegisterAddin.addin (deflated 66%) updating: TemplateIcon.ico (deflated 67%) updating: TemplateRevitCs.csproj (deflated 69%) updating: TemplateRevitCs.csproj.user (deflated 30%) updating: TemplateRevitCs.vstemplate (deflated 65%) Copying C# wizard archive to C:\Users\tammikj\Documents\Visual Studio 2015\Templates\ProjectTemplates\Visual C#... 1 file(s) copied. Creating VB wizard archive C:\Users\tammikj\AppData\Local\Temp\Revit2018AddinWizardVb0.zip... updating: AdskApplication.vb (deflated 68%) updating: AdskCommand.vb (deflated 58%) updating: My Project/ (stored 0%) updating: My Project/AssemblyInfo.vb (deflated 54%) updating: RegisterAddin.addin (deflated 66%) updating: TemplateIcon.ico (deflated 67%) updating: TemplateRevitVb.vbproj (deflated 72%) updating: TemplateRevitVb.vstemplate (deflated 62%) Copying VB wizard archive to C:\Users\tammikj\Documents\Visual Studio 2015\Templates\ProjectTemplates\Visual Basic... 1 file(s) copied.
```
