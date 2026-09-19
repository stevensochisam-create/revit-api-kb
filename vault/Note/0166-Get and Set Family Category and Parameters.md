---
num: 166
date: 2009-07-04
themes: [Parameter]
tags: [revit-api, tbc]
---

# Get and Set Family Category and Parameters

<https://jeremytammik.github.io/tbc/a/0166_family_category_param.htm>

```csharp
BuiltInParameter _bip = BuiltInParameter.OMNICLASS_CODE; &nbsp; public IExternalCommand.Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; Application app = commandData.Application; &nbsp; Document doc = app.ActiveDocument; &nbsp; &nbsp; if( !doc.IsFamilyDocument ) &nbsp; { &nbsp; &nbsp; message &nbsp; &nbsp; &nbsp; = &quot;Please run this command in a family document.&quot;; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; Family f = doc.OwnerFamily; &nbsp; &nbsp; Category c = f.FamilyCategory; &nbsp; &nbsp; Parameter p = f.get_Parameter( _bip ); &nbsp; &nbsp; &nbsp; Debug.Print( &nbsp; &nbsp; &nbsp; &quot;Category '{0}', OmniClassNumber {1}&quot;, &nbsp; &nbsp; &nbsp; c.Name, p.AsString() ); &nbsp; &nbsp; &nbsp; p.Set( &quot;Jeremy&quot; ); &nbsp; &nbsp; &nbsp; Debug.Print( &quot;Modified OmniClassNumber {0}&quot;, &nbsp; &nbsp; &nbsp; f.get_Parameter( _bip ).AsString() ); &nbsp; } &nbsp; return IExternalCommand.Result.Failed; }
```
