---
num: 891
date: 2013-02-01
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameters versus Properties

<https://jeremytammik.github.io/tbc/a/0891_prop_versus_param.htm>

```csharp
&nbsp; Material material = null; &nbsp; &nbsp; foreach( Material mat in e.Materials ) &nbsp; { &nbsp; &nbsp; material = mat; &nbsp; &nbsp; break; &nbsp; } &nbsp; PropertySetElement pse = doc.GetElement( &nbsp; &nbsp; material.StructuralAssetId ) &nbsp; &nbsp; &nbsp; as PropertySetElement; &nbsp; &nbsp; StructuralAsset asset = pse.GetStructuralAsset(); &nbsp; &nbsp; double a = asset.WoodBendingStrength; &nbsp; double b = asset.WoodParallelCompressionStrength; &nbsp; double c = asset.WoodParallelShearStrength; &nbsp; double d = asset.WoodPerpendicularCompressionStrength; &nbsp; double f = asset.WoodPerpendicularShearStrength; &nbsp; // ... and lots of other properties ...
```

```csharp
public static class ElementExtensions { &nbsp; public static Material material( this Element e ) &nbsp; { &nbsp; &nbsp; foreach( Material m in e.Materials ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return m; &nbsp; &nbsp; } &nbsp; &nbsp; return null; &nbsp; } }
```

```csharp
&nbsp; Material material2 = e.material();
```

```csharp
&nbsp; Material material3 &nbsp; &nbsp; = ElementExtensions.material( e );
```

```csharp
&nbsp; ElementId typeId = viewport.GetTypeId(); &nbsp; &nbsp; ViewType viewtype = doc.GetElement( typeId ) &nbsp; &nbsp; as ViewType; &nbsp; &nbsp; Parameter withLine = viewtype.get_Parameter( &nbsp; &nbsp; BuiltInParameter &nbsp; &nbsp; &nbsp; .VIEWPORT_ATTR_SHOW_EXTENSION_LINE ); &nbsp; &nbsp; withLine.Set( 0 ); // No Line &nbsp; withLine.Set( 1 ); // Has Line
```
