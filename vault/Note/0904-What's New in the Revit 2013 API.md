---
num: 904
date: 2013-03-04
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# What's New in the Revit 2013 API

<https://jeremytammik.github.io/tbc/a/0904_whats_new_2013.htm>

```csharp
&nbsp; Element level = doc.GetElement( &nbsp; &nbsp; uidoc.Selection.PickObject( &nbsp; &nbsp; &nbsp; ObjectType.Element ) ) as Level; &nbsp; &nbsp; IEnumerable&lt;ViewFamilyType&gt; viewFamilyTypes &nbsp; &nbsp; = from elem in new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( ViewFamilyType ) ) &nbsp; &nbsp; &nbsp; &nbsp; let type = elem as ViewFamilyType &nbsp; &nbsp; &nbsp; &nbsp; where type.ViewFamily == ViewFamily.CeilingPlan &nbsp; &nbsp; &nbsp; &nbsp; select type; &nbsp; &nbsp; ViewPlan ceilingPlan = ViewPlan.Create( &nbsp; &nbsp; doc, viewFamilyTypes.First().Id, level.Id ); &nbsp; &nbsp; ceilingPlan.Name = &quot;New Ceiling Plan for &quot; &nbsp; &nbsp; + level.Name; &nbsp; &nbsp; ceilingPlan.DetailLevel = ViewDetailLevel.Fine; &nbsp; &nbsp; // 3D views can be created with &nbsp; // View3D.CreateIsometric and &nbsp; // View3D.CreatePerspective. &nbsp; // The new ViewOrientation3D object is used to &nbsp; // get or set the orientation of 3D views. &nbsp; &nbsp; View3D view = View3D.CreateIsometric( &nbsp; &nbsp; doc, viewFamily3d ); &nbsp; &nbsp; XYZ eyePosition = new XYZ( 10, 10, 10 ); &nbsp; XYZ upDirection = new XYZ( -1, 0, 1 ); &nbsp; XYZ forwardDirection = new XYZ( 1, 0, 1 ); &nbsp; view.SetOrientation( new ViewOrientation3D( &nbsp; &nbsp; eyePosition, upDirection, forwardDirection ) );
```

```csharp
&nbsp; RenderingSettings renderingSettings &nbsp; &nbsp; = view3D.GetRenderingSettings(); &nbsp; &nbsp; Transaction newTran = new Transaction( &nbsp; &nbsp; doc, &quot;Change Rendering Settings&quot; ); &nbsp; &nbsp; newTran.Start(); &nbsp; &nbsp; renderingSettings.BackgroundStyle &nbsp; &nbsp; = BackgroundStyle.Image; &nbsp; &nbsp; view3D.SetRenderingSettings( renderingSettings ); &nbsp; &nbsp; newTran.Commit();
```
