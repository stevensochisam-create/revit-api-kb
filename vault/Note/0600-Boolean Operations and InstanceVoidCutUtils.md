---
num: 600
date: 2011-06-20
themes: [Geometry]
tags: [revit-api, tbc]
---

# Boolean Operations and InstanceVoidCutUtils

<https://jeremytammik.github.io/tbc/a/0600_instance_void_cut.htm>

```csharp
&nbsp; Element element; &nbsp; FamilySymbol fs; &nbsp; &nbsp; // . . . &nbsp; &nbsp; PlanarFace planarFace = facesToAttach[i] &nbsp; &nbsp; as PlanarFace; &nbsp; &nbsp; // . . . &nbsp; &nbsp; XYZ xyzOrigin = planarFace.Origin; &nbsp; &nbsp; FamilyInstance cuttingInstance &nbsp; &nbsp; = _doc.Create.NewFamilyInstance( &nbsp; &nbsp; &nbsp; facesToAttach[i], xyzOrigin, vecY, fs ); &nbsp; &nbsp; Parameter parAngle3 = cuttingInstance &nbsp; &nbsp; .get_Parameter( &quot;A3&quot; ); &nbsp; &nbsp; Utils.ParameterSet( parAngle3, angles[i] ); &nbsp; &nbsp; InstanceVoidCutUtils.AddInstanceVoidCut( &nbsp; &nbsp; _doc, element, cuttingInstance );
```

```csharp
&nbsp; FamilySymbol polyRecessFamily; &nbsp; Wall wall; &nbsp; &nbsp; // . . . &nbsp; &nbsp; FamilyInstance recessElement &nbsp; &nbsp; = _doc.Create.NewFamilyInstance( &nbsp; &nbsp; &nbsp; face, pos, XYZ.Zero, polyRecessFamily ); &nbsp; &nbsp; recessElement.SetParameter( &quot;Countersinking&quot;, &nbsp; &nbsp; UnitConversion.ToFeet( recess.CounterSinking ) ); &nbsp; &nbsp; if( InstanceVoidCutUtils.CanBeCutWithVoid( wall ) ) &nbsp; { &nbsp; &nbsp; InstanceVoidCutUtils.AddInstanceVoidCut( &nbsp; &nbsp; &nbsp; _doc, wall, recessElement ); &nbsp; }
```
