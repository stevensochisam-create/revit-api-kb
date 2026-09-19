---
num: 1764
date: 2019-07-24
themes: [Geometry]
tags: [revit-api, tbc]
---

# Roadmap, Rebar Curves, Wizard Zip and More

<https://jeremytammik.github.io/tbc/a/1764_rebar_curves_wizard_zip.html>

```csharp
Rebar.GetCenterlineCurves( bool adjustForSelfIntersection, bool suppressHooks, bool suppressBendRadius, MultiplanarOption multiplanarOption, int barPositionIndex);
```

```csharp
Rebar.GetShapeDrivenAccessor() .GetBarPositionTransform(i);
```

```csharp
Environment.GetFolderPath( Environment.SpecialFolder.ApplicationData ) + @"\AppData\Local\Temp\"
```

```csharp
Path.Combine( System.Environment.GetEnvironmentVariable( "LOCALAPPDATA" ), "Temp")
```
