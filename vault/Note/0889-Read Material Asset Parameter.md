---
num: 889
date: 2013-01-30
themes: [Parameter]
tags: [revit-api, tbc]
---

# Read Material Asset Parameter

<https://jeremytammik.github.io/tbc/a/0889_read_material_asset.htm>

```csharp
public Result ReadMaterialParam( UIDocument uidoc ) { &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; Element e = null; &nbsp; &nbsp; Selection sel = uidoc.Selection; &nbsp; &nbsp; if( 1 == sel.Elements.Size ) &nbsp; { &nbsp; &nbsp; foreach( Element e2 in sel.Elements ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; e = e2; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; if( null == e ) &nbsp; { &nbsp; &nbsp; TaskDialog.Show( &quot;Error&quot;, &nbsp; &nbsp; &nbsp; &quot;Please select one single element.&quot; ); &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; &nbsp; Parameter paramMaterial = e.get_Parameter( &nbsp; &nbsp; BuiltInParameter.STRUCTURAL_MATERIAL_PARAM ); &nbsp; &nbsp; Material material = doc.GetElement( &nbsp; &nbsp; paramMaterial.AsElementId() ) as Material; &nbsp; &nbsp; PropertySetElement property = doc.GetElement( &nbsp; &nbsp; material.StructuralAssetId ) as PropertySetElement; &nbsp; &nbsp; Parameter paramTensionParallel &nbsp; &nbsp; = property.get_Parameter( BuiltInParameter &nbsp; &nbsp; &nbsp; .PHY_MATERIAL_PARAM_TENSION_PARALLEL ); &nbsp; &nbsp; TaskDialog.Show( &nbsp; &nbsp; &quot;PHY_MATERIAL_PARAM_TENSION_PARALLEL&quot;, &nbsp; &nbsp; paramTensionParallel.AsValueString() ); &nbsp; &nbsp; return Result.Succeeded; }
```
