---
num: 1430
date: 2016-04-25
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Room Editor &ndash; First Revit 2017 Addin Migration

<https://jeremytammik.github.io/tbc/a/1430_room_editor_2017.html>

```csharp
warning CS0618: 'Plane.Plane(XYZ, XYZ, XYZ)' is obsolete: This method is obsolete in Revit 2017. Please use Plane.CreateByOriginAndBasis() instead.
```

```csharp
Plane&nbsp;plane&nbsp;=&nbsp;new&nbsp;Plane( XYZ.BasisX, &nbsp;&nbsp;XYZ.BasisY,&nbsp;XYZ.Zero);&nbsp;//&nbsp;2016
```

```csharp
Plane&nbsp;plane&nbsp;=&nbsp;Plane.CreateByOriginAndBasis( &nbsp;&nbsp;XYZ.Zero,&nbsp;XYZ.BasisX,&nbsp;XYZ.BasisY&nbsp;);&nbsp;//&nbsp;2017
```
