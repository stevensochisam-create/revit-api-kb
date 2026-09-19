---
num: 1507
date: 2016-12-12
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameter Definition Overview

<https://jeremytammik.github.io/tbc/a/1507_parameter_definition.html>

```csharp
public&nbsp;bool&nbsp;SetNewParameterToInstanceWall( &nbsp;&nbsp;UIApplication&nbsp;app, &nbsp;&nbsp;DefinitionFile&nbsp;myDefinitionFile&nbsp;) { &nbsp;&nbsp;//&nbsp;Create&nbsp;a&nbsp;new&nbsp;group&nbsp;in&nbsp;the&nbsp;shared&nbsp;parameters&nbsp;file &nbsp;&nbsp;DefinitionGroups&nbsp;myGroups&nbsp;=&nbsp;myDefinitionFile.Groups; &nbsp;&nbsp;DefinitionGroup&nbsp;myGroup&nbsp;=&nbsp;myGroups.Create(&nbsp;&quot;MyParameters&quot;&nbsp;); &nbsp;&nbsp;//&nbsp;Create&nbsp;an&nbsp;instance&nbsp;definition&nbsp;in&nbsp;definition&nbsp;group&nbsp;MyParameters &nbsp;&nbsp;ExternalDefinitionCreationOptions&nbsp;option &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ExternalDefinitionCreationOptions( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;Instance_ProductDate&quot;,&nbsp;ParameterType.Text&nbsp;); &nbsp;&nbsp;//&nbsp;Don&#39;t&nbsp;let&nbsp;the&nbsp;user&nbsp;modify&nbsp;the&nbsp;value,&nbsp;only&nbsp;the&nbsp;API &nbsp;&nbsp;option.UserModifiable&nbsp;=&nbsp;false; &nbsp;&nbsp;//&nbsp;Set&nbsp;tooltip &nbsp;&nbsp;option.Description&nbsp;=&nbsp;&quot;Wall&nbsp;product&nbsp;date&quot;; &nbsp;&nbsp;Definition&nbsp;myDefinition_ProductDate &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;myGroup.Definitions.Create(&nbsp;option&nbsp;); . . .
```

```csharp
&nbsp;&nbsp;bool&nbsp;dgMatchFound&nbsp;=&nbsp;false; &nbsp;&nbsp;foreach(&nbsp;DefinitionGroup&nbsp;dg&nbsp;in&nbsp;myGroups&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;dg.Name&nbsp;==&nbsp;myGroupName&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dgMatchFound&nbsp;=&nbsp;true; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;myGroup&nbsp;=&nbsp;dg; &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;} &nbsp;&nbsp;if(&nbsp;dgMatchFound&nbsp;==&nbsp;false&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;myGroup&nbsp;=&nbsp;myGroups.Create(&nbsp;myGroupName&nbsp;); &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;bool&nbsp;dMatchFound&nbsp;=&nbsp;false; &nbsp;&nbsp;foreach(&nbsp;Definition&nbsp;d&nbsp;in&nbsp;myGroup.Definitions&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;d.Name&nbsp;==&nbsp;newParameterName&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dMatchFound&nbsp;=&nbsp;true; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;myDefinition_ProductDate&nbsp;=&nbsp;d; &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;} &nbsp;&nbsp;if(&nbsp;!dMatchFound&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;myDefinition_ProductDate &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;myGroup.Definitions.Create(&nbsp;option&nbsp;); &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;DefinitionFile&nbsp;defFile&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;GetOrCreateSharedParamsFile(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ActiveUIDocument.Application.Application&nbsp;); &nbsp;&nbsp;bool&nbsp;AddParameterResult&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;SetNewParameterToInstanceWall(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ActiveUIDocument.Application,&nbsp;defFile&nbsp;); &nbsp;&nbsp;TaskDialog.Show(&nbsp;&quot;Did&nbsp;it&nbsp;work&quot;,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;AddParameterResult.ToString()&nbsp;);
```
