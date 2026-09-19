---
num: 1337
date: 2015-06-30
themes: [Geometry]
tags: [revit-api, tbc]
---

# IFC GUID Access, Life Span and Cloning of Geometry

<https://jeremytammik.github.io/tbc/a/1337_lifespan_clone_face.htm>

```csharp
FaceCollection instantiate -Trans.Start Loop Walls/Floors Geometry (Solids) FaceCollection populate End Loop -Trans.End FaceCollection use (just read-only geom.access to faces)
```

```csharp
#615 = IFCWALLSTANDARDCASE( '3lDzp1LFjDqwXDAihsyNrA', #42, '\X2\6A196E9658C1\X0\:(P)PC200:1185289', $, '\X2\6A196E9658C1\X0\:(P)PC200:794115', #587, #613, '1185289' );
```

```csharp
&nbsp; IList&lt;Parameter&gt; ps = e.GetParameters( &quot;IfcGUID&quot; ); // or &nbsp; Parameter pGuid = e.LookupParameter( &quot;IfcGUID&quot; ); &nbsp; string ifc_guid = pGuid.AsString();
```

```csharp
&nbsp; Parameter pGuid = e.get_Parameter( BuiltInParameter.IFC_GUID ); &nbsp; string ifc_guid = pGuid.AsString();
```
