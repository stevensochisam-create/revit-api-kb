---
num: 1436
date: 2016-05-03
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# The Building Coder Samples 2017

<https://jeremytammik.github.io/tbc/a/1436_tbc_samples_2017.html>

```csharp
CurveArray&nbsp;curves&nbsp;=&nbsp;creapp.NewCurveArray(); foreach(&nbsp;Curve&nbsp;curve&nbsp;in&nbsp;curveLoop2&nbsp;) { &nbsp;&nbsp;curves.Append(&nbsp;curve.CreateTransformed(&nbsp;offset&nbsp;)&nbsp;); } //&nbsp;Create&nbsp;model&nbsp;lines&nbsp;for&nbsp;an&nbsp;curve&nbsp;loop. Plane&nbsp;plane&nbsp;=&nbsp;creapp.NewPlane(&nbsp;curves&nbsp;);&nbsp;//&nbsp;2016
```

```csharp
Plane&nbsp;plane&nbsp;=&nbsp;curveLoop2.GetPlane();&nbsp;//&nbsp;2017
```

```csharp
view.SetVisibility(&nbsp;catHosts,&nbsp;false&nbsp;);&nbsp;//&nbsp;2016 view.SetCategoryHidden(&nbsp;catHosts.Id,&nbsp;true&nbsp;);&nbsp;//&nbsp;2017
```

```csharp
DirectShape&nbsp;ds&nbsp;=&nbsp;DirectShape.CreateElement( &nbsp;&nbsp;doc,&nbsp;e.Category.Id, &nbsp;&nbsp;_direct_shape_appGUID, &nbsp;&nbsp;appDataGUID&nbsp;);&nbsp;//&nbsp;2016 DirectShape&nbsp;ds&nbsp;=&nbsp;DirectShape.CreateElement( &nbsp;&nbsp;doc,&nbsp;e.Category.Id&nbsp;);&nbsp;//2017 ds.ApplicationId&nbsp;=&nbsp;_direct_shape_appGUID;&nbsp;//&nbsp;2017 ds.ApplicationDataId&nbsp;=&nbsp;appDataGUID∫∫;&nbsp;//&nbsp;2017
```
