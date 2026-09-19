---
num: 2020
date: 2023-12-21
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# Parameters and .NET Core Webinar

<https://jeremytammik.github.io/tbc/a/2020_net_core_webinar.html>

```csharp
import uuid yourGuid = str(uuid.uuid4()) # Your GUID will be like 8-4-4-4-12 yourGuid = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

```csharp
app = DocumentManager.Instance.CurrentUIApplication.Application yourSharedParamDefFile = r"yourDefinitionFile.txt" app.SharedParametersFilename = yourSharedParamDefFile sharedParametersFileName = app.OpenSharedParameterFile().Filename paraGroup = app.OpenSharedParameterFile().Groups.get_Item("YourParameterGroup") # verify in your Definition File the name of the Group under which you want to create the Shared Parameter newParaOptions = ExternalDefinitionCreationOptions("yourSharedParaName", ParameterType.Text) # Text, Integer, Number, Length, Area, Volume, etc. - look at the API for Parameter Type enumerations newParaOptions.UserModifiable = False # Users cannot modify it, only Revit API newParaOptions.Visible = False # Users cannot see it in the properties, but the parameter appears in schedules, etc. newParaOptions.GUID = Guid(yourGuid) # set the Guid createYourNewParameter = paraGroup.Definitions.Create(newParaOptions)
```
