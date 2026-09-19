---
num: 1871
date: 2020-10-21
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# FireRevit, Deprecated API and Elbow Centre Point

<https://jeremytammik.github.io/tbc/a/1871_elbow_centre.html>

```csharp
case&nbsp;StorageType.Double: &nbsp;&nbsp;double?&nbsp;nullable&nbsp;=&nbsp;t.AsDouble(&nbsp;fp&nbsp;); &nbsp;&nbsp;if(&nbsp;nullable.HasValue&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;DisplayUnitType&nbsp;displayUnitType&nbsp;=&nbsp;fp.DisplayUnitType; &nbsp;&nbsp;&nbsp;&nbsp;value&nbsp;=&nbsp;UnitUtils.ConvertFromInternalUnits(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nullable.Value,&nbsp;displayUnitType&nbsp;).ToString(); &nbsp;&nbsp;&nbsp;&nbsp;break; &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;//&nbsp;Pre&nbsp;2021 &nbsp;&nbsp;DisplayUnitType&nbsp;displayUnitType&nbsp;=&nbsp;fp.DisplayUnitType; &nbsp;&nbsp;value&nbsp;=&nbsp;UnitUtils.ConvertFromInternalUnits(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;nullable.Value,&nbsp;displayUnitType&nbsp;).ToString(); &nbsp;&nbsp;//2021 &nbsp;&nbsp;ForgeTypeId&nbsp;forgeTypeId&nbsp;=&nbsp;fp.GetUnitTypeId(); &nbsp;&nbsp;value&nbsp;=&nbsp;UnitUtils.ConvertFromInternalUnits(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;nullable.Value,&nbsp;forgeTypeId&nbsp;).ToString();
```

```csharp
&nbsp;&nbsp;static&nbsp;public&nbsp;XYZ&nbsp;GetCenterofElbow(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;FamilyInstance&nbsp;selectedDuct&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;XYZ&nbsp;output&nbsp;=&nbsp;null; &nbsp;&nbsp;&nbsp;&nbsp;List&lt;Connector&gt;&nbsp;allConnectors&nbsp;=&nbsp;selectedDuct.MEPModel &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.ConnectorManager.Connectors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;Connector&gt;().ToList(); &nbsp;&nbsp;&nbsp;&nbsp;Connector&nbsp;connectorA&nbsp;=&nbsp;allConnectors[&nbsp;0&nbsp;]; &nbsp;&nbsp;&nbsp;&nbsp;Connector&nbsp;connectorB&nbsp;=&nbsp;allConnectors[&nbsp;0&nbsp;]; &nbsp;&nbsp;&nbsp;&nbsp;GeometryElement&nbsp;geometryElement&nbsp;=&nbsp;selectedDuct &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.get_Geometry(&nbsp;new&nbsp;Options()&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;List&lt;GeometryInstance&gt;&nbsp;ginsList&nbsp;=&nbsp;selectedDuct &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.get_Geometry(&nbsp;new&nbsp;Options()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Where(&nbsp;o&nbsp;=&gt;&nbsp;o&nbsp;is&nbsp;GeometryInstance&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;GeometryInstance&gt;() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.ToList(); &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;GeometryInstance&nbsp;gins&nbsp;in&nbsp;ginsList&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;GeometryObject&nbsp;ge&nbsp;in&nbsp;gins.GetInstanceGeometry()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;try &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arc&nbsp;centerArc&nbsp;=&nbsp;ge&nbsp;as&nbsp;Arc; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output&nbsp;=&nbsp;centerArc.Center; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;catch(&nbsp;Exception&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;output; &nbsp;&nbsp;}
```
