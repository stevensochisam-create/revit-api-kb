---
num: 713
date: 2012-01-30
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Eliminating Compiler Warnings and Deprecated Calls

<https://jeremytammik.github.io/tbc/a/0713_compiler_warnings.htm>

```csharp
C:\bc\BuildingCoder\BuildingCoder\CmdNewSpotElevation.cs(69,11): warning CS0618: 'Autodesk.Revit.DB.Document.FindReferencesByDirection(Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.View3D)' is obsolete: 'This method will be removed, use FindReferencesWithContextByDirection().' C:\bc\BuildingCoder\BuildingCoder\CmdNewSpotElevation.cs(86,14): warning CS0618: 'Autodesk.Revit.DB.Reference.ProximityParameter' is obsolete: 'Property will be removed. Use ReferenceByContext.ProximityParameter instead (after obtaining ReferenceWithContext from Document.FindReferencesWithContextByDirection())' C:\bc\BuildingCoder\BuildingCoder\CmdNewSpotElevation.cs(89,21): warning CS0618: 'Autodesk.Revit.DB.Reference.ProximityParameter' is obsolete: 'Property will be removed. Use ReferenceByContext.ProximityParameter instead (after obtaining ReferenceWithContext from Document.FindReferencesWithContextByDirection())' C:\bc\BuildingCoder\BuildingCoder\CmdDimensionWallsFindRefs.cs(239,14): warning CS0618: 'Autodesk.Revit.DB.Document.FindReferencesByDirection(Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.XYZ, Autodesk.Revit.DB.View3D)' is obsolete: 'This method will be removed, use FindReferencesWithContextByDirection().' C:\bc\BuildingCoder\BuildingCoder\CmdDimensionWallsFindRefs.cs(295,17): warning CS0618: 'Autodesk.Revit.DB.Reference.ProximityParameter' is obsolete: 'Property will be removed. Use ReferenceByContext.ProximityParameter instead (after obtaining ReferenceWithContext from Document.FindReferencesWithContextByDirection())' C:\bc\BuildingCoder\BuildingCoder\CmdDimensionWallsFindRefs.cs(305,19): warning CS0618: 'Autodesk.Revit.DB.Reference.ProximityParameter' is obsolete: 'Property will be removed. Use ReferenceByContext.ProximityParameter instead (after obtaining ReferenceWithContext from Document.FindReferencesWithContextByDirection())' C:\bc\BuildingCoder\BuildingCoder\CmdDimensionWallsFindRefs.cs(308,34): warning CS0618: 'Autodesk.Revit.DB.Reference.ProximityParameter' is obsolete: 'Property will be removed. Use ReferenceByContext.ProximityParameter instead (after obtaining ReferenceWithContext from Document.FindReferencesWithContextByDirection())' Compile complete -- 0 errors, 7 warnings
```

```csharp
&nbsp; ReferenceArray references &nbsp; &nbsp; = doc.FindReferencesByDirection( &nbsp; &nbsp; &nbsp; centerOfTopOfBox, viewDirection, view3D ); &nbsp; foreach( Reference r in references ) &nbsp; { &nbsp; &nbsp; Element re = doc.GetElement( r ); &nbsp; &nbsp; &nbsp; if( re.Id.IntegerValue == e.Id.IntegerValue &nbsp; &nbsp; &nbsp; &amp;&amp; r.ProximityParameter &lt; closest ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ret = r; &nbsp; &nbsp; &nbsp; closest = r.ProximityParameter; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; IList&lt;ReferenceWithContext&gt; references &nbsp; &nbsp; = doc.FindReferencesWithContextByDirection( &nbsp; &nbsp; &nbsp; centerOfTopOfBox, viewDirection, view3D ); &nbsp; foreach( ReferenceWithContext r in references ) &nbsp; { &nbsp; &nbsp; Element re = doc.GetElement( &nbsp; &nbsp; &nbsp; r.GetReference() ); &nbsp; &nbsp; &nbsp; if( re.Id.IntegerValue == e.Id.IntegerValue &nbsp; &nbsp; &nbsp; &amp;&amp; r.Proximity &lt; closest ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ret = r.GetReference(); &nbsp; &nbsp; &nbsp; closest = r.Proximity; &nbsp; &nbsp; } &nbsp; }
```
