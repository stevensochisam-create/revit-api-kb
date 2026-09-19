---
num: 898
date: 2013-02-13
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Eliminating Compiler Warnings and Deprecated Calls

<https://jeremytammik.github.io/tbc/a/0898_compiler_warnings.htm>

```csharp
C:\bc\BuildingCoder\BuildingCoder\CmdTransformedCoords.cs(67,41): warning CS0618: 'Autodesk.Revit.DB.GeometryElement.Objects' is obsolete: 'This property will be obsolete from 2013; Call GetEnumerator() instead.' C:\bc\BuildingCoder\BuildingCoder\CmdNestedInstanceGeo.cs(119,32): warning CS0618: 'Autodesk.Revit.DB.GeometryElement.Objects' is obsolete: 'This property will be obsolete from 2013; Call GetEnumerator() instead.' C:\bc\BuildingCoder\BuildingCoder\CmdLinkedFiles.cs(103,41): warning CS0618: 'Autodesk.Revit.DB.GeometryElement.Objects' is obsolete: 'This property will be obsolete from 2013; Call GetEnumerator() instead.' C:\bc\BuildingCoder\BuildingCoder\CmdSetTagType.cs(171,19): warning CS0618: 'Autodesk.Revit.Creation.Document.NewWall(Autodesk.Revit.DB.Curve, Autodesk.Revit.DB.Level, bool)' is obsolete: 'This method is obsolete in Revit 2013. Please call a static creation method of Wall class instead.' C:\bc\BuildingCoder\BuildingCoder\CmdCreateGableWall.cs(89,19): warning CS0618: 'Autodesk.Revit.Creation.Document.NewWall(Autodesk.Revit.DB.CurveArray, Autodesk.Revit.DB.WallType, Autodesk.Revit.DB.Level, bool, Autodesk.Revit.DB.XYZ)' is obsolete: 'This method is obsolete in Revit 2013. Please call a static creation method of Wall class instead.' C:\bc\BuildingCoder\BuildingCoder\CmdPlanTopology.cs(103,26): warning CS0618: 'Autodesk.Revit.DB.PlanTopology.Rooms' is obsolete: 'This property is obsolete in Revit 2013. Call GetRoomIds() instead.' C:\bc\BuildingCoder\BuildingCoder\CmdPressKeys.cs(222,19): warning CS0618: 'Autodesk.Revit.Creation.Document.NewWall(Autodesk.Revit.DB.Curve, Autodesk.Revit.DB.WallType, Autodesk.Revit.DB.Level, double, double, bool, bool)' is obsolete: 'This method is obsolete in Revit 2013. Please call a static creation method of Wall class instead.' C:\bc\BuildingCoder\BuildingCoder\CmdSlopedWall.cs(65,19): warning CS0618: 'Autodesk.Revit.Creation.Document.NewWall(Autodesk.Revit.DB.CurveArray, bool)' is obsolete: 'This method is obsolete in Revit 2013. Please call a static creation method of Wall class instead.' C:\bc\BuildingCoder\BuildingCoder\CmdSlopedWall.cs(140,19): warning CS0618: 'Autodesk.Revit.Creation.Document.NewWall(Autodesk.Revit.DB.CurveArray, Autodesk.Revit.DB.WallType, Autodesk.Revit.DB.Level, bool, Autodesk.Revit.DB.XYZ)' is obsolete: 'This method is obsolete in Revit 2013. Please call a static creation method 
```

```csharp
&nbsp; GeometryObjectArray objects = geoElem.Objects; &nbsp; &nbsp; n = objects.Size; &nbsp; &nbsp; // . . . &nbsp; &nbsp; foreach( GeometryObject obj in objects )
```

```csharp
&nbsp; n = geoElem.Count&lt;GeometryObject&gt;(); &nbsp; &nbsp; // . . . &nbsp; &nbsp; foreach( GeometryObject obj in geoElem )
```

```csharp
&nbsp; Wall wall = createDoc.NewWall( &nbsp; &nbsp; line, levelBottom, false );
```

```csharp
&nbsp; Wall wall = Wall.Create( &nbsp; &nbsp; doc, line, levelBottom.Id, false );
```
