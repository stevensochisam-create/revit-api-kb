---
num: 1971
date: 2022-11-04
themes: [Units]
tags: [revit-api, tbc]
---

# Unit Test Your Revit Add-In

<https://jeremytammik.github.io/tbc/a/1971_unit_test.html>

```csharp
&nbsp;&nbsp;var&nbsp;allFabParts&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(document) &nbsp;&nbsp;&nbsp;&nbsp;.OfClass(typeof(FabricationPart)).Cast&lt;FabricationPart&gt;(); &nbsp;&nbsp;FabricationConfiguration&nbsp;fabConfig&nbsp;=&nbsp;FabricationConfiguration &nbsp;&nbsp;&nbsp;&nbsp;.GetFabricationConfiguration(document); &nbsp;&nbsp;var&nbsp;materialDetails&nbsp;=&nbsp;allFabParts &nbsp;&nbsp;&nbsp;&nbsp;.SelectMany(x&nbsp;=&gt;&nbsp;fabConfig.GetAllMaterials(x)) &nbsp;&nbsp;&nbsp;&nbsp;.Select(x&nbsp;=&gt;&nbsp;new&nbsp;{&nbsp;MatName&nbsp;=&nbsp;fabConfig.GetMaterialName(x),&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MatGroup&nbsp;=&nbsp;fabConfig.GetMaterialGroup(x)&nbsp;});
```

```csharp
&nbsp;&nbsp;[Fact] &nbsp;&nbsp;public&nbsp;void&nbsp;WallsHaveVolume() &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;testModel&nbsp;=&nbsp;GetTestModel(&quot;walls.rvt&quot;); &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;doc&nbsp;=&nbsp;xru.OpenDoc(testModel); &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;walls&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(doc).WhereElementIsNotElementType().OfCategory(BuiltInCategory.OST_Walls).ToElements(); &nbsp;&nbsp;&nbsp;&nbsp;foreach&nbsp;(var&nbsp;wall&nbsp;in&nbsp;walls) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;volumeParam&nbsp;=&nbsp;wall.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assert.NotNull(volumeParam); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assert.True(volumeParam.AsDouble()&nbsp;&gt;&nbsp;0); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;doc.Close(false); &nbsp;&nbsp;}
```
