---
num: 1458
date: 2016-08-17
themes: [Pitfall, Units]
tags: [revit-api, tbc]
---

# UnitUtils Converting Units for Unit Weight

<https://jeremytammik.github.io/tbc/a/1458_unitutils_weight.html>

```csharp
var parameterVaule = Parameter.AsDouble(); 7154.4631104000009 var converted = UnitUtils.ConvertFromInternalUnits(parameterVaule ,Autodesk.Revit.DB.DisplayUnitType.DUT_KILONEWTONS_PER_CUBIC_METER); 77.01 => This is a correct value. var converted2 = UnitUtils.ConvertFromInternalUnits(parameterVaule ,Autodesk.Revit.DB.DisplayUnitType.DUT_KILOGRAMS_PER_CUBIC_METER); 252657.48031496062 => ??? this not correct!
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Get&nbsp;the&nbsp;unit&nbsp;weight&nbsp;of&nbsp;a&nbsp;material. ///&nbsp;&lt;/summary&gt; internal&nbsp;static&nbsp;double&nbsp;GetMaterialEgenvekt(&nbsp; &nbsp;&nbsp;Document&nbsp;doc,&nbsp; &nbsp;&nbsp;ref&nbsp;string&nbsp;material,&nbsp; &nbsp;&nbsp;Element&nbsp;rebarelement&nbsp;) { &nbsp;&nbsp;var&nbsp;rType&nbsp;=&nbsp;rebarelement.Document.GetElement(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;rebarelement.GetTypeId()&nbsp;)&nbsp;as&nbsp;ElementType; &nbsp;&nbsp;var&nbsp;paramMaterial&nbsp;=&nbsp;rType.get_Parameter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.MATERIAL_ID_PARAM&nbsp;); &nbsp;&nbsp;var&nbsp;mat&nbsp;=&nbsp;doc.GetElement(&nbsp;paramMaterial &nbsp;&nbsp;&nbsp;&nbsp;.AsElementId()&nbsp;)&nbsp;as&nbsp;Material; &nbsp;&nbsp;double&nbsp;egenvekt&nbsp;=&nbsp;0; &nbsp;&nbsp;if(&nbsp;mat&nbsp;==&nbsp;null&nbsp;)&nbsp;return&nbsp;egenvekt; &nbsp;&nbsp;var&nbsp;property&nbsp;=&nbsp;doc.GetElement( &nbsp;&nbsp;&nbsp;&nbsp;mat.StructuralAssetId&nbsp;)&nbsp;as&nbsp;PropertySetElement; &nbsp;&nbsp;if(&nbsp;property&nbsp;!=&nbsp;null&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;unitWeightParam&nbsp;=&nbsp;property.get_Parameter( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.PHY_MATERIAL_PARAM_UNIT_WEIGHT&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Not&nbsp;In&nbsp;Use&nbsp;-&nbsp;gives&nbsp;wrong&nbsp;value&nbsp;in&nbsp;metric&nbsp;unit. &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;unitWeight&nbsp;=&nbsp;UnitUtils.ConvertFromInternalUnits(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unitWeightParam.AsDouble(),&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DisplayUnitType.DUT_KILOGRAMS_PER_CUBIC_METER&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Manual&nbsp;calculation.&nbsp;In&nbsp;use,&nbsp;and&nbsp;calculates&nbsp;correct. &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;egenvektFraMaterial&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;EgenVektFraNewtonPerSquareFootMeter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unitWeightParam.AsDouble()&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;!(&nbsp;egenvekt&nbsp;&gt;&nbsp;0&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;egenvekt&nbsp;=&nbsp;egenvektFraMaterial; &nbsp;&nbsp;} &nbsp;&nbsp;material&nbsp;=&nbsp;mat.Name; &nbsp;&nbsp;return&nbsp;egenvekt; }
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Calculate&nbsp;the&nbsp;unit&nbsp;weight&nbsp;from&nbsp;NewtonPerSquareFootMeter ///&nbsp;&lt;/summary&gt; double&nbsp;EgenVektFraNewtonPerSquareFootMeter(&nbsp; &nbsp;&nbsp;double&nbsp;unitweight&nbsp;) { &nbsp;&nbsp;double&nbsp;egenvekt&nbsp;=&nbsp;unitweight&nbsp;/&nbsp;9.81F; &nbsp;&nbsp;double&nbsp;meterPerFot&nbsp;=&nbsp;1000&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;GeoHelper.FootMillimeterKonstant; &nbsp;&nbsp;egenvekt&nbsp;=&nbsp;egenvekt&nbsp;*&nbsp;Math.Pow(&nbsp;meterPerFot,&nbsp;2&nbsp;); &nbsp;&nbsp;return&nbsp;egenvekt; }
```

```csharp
public&nbsp;static&nbsp;double&nbsp;FootMillimeterKonstant &nbsp;&nbsp;=&nbsp;Math.Round(&nbsp;304.8,&nbsp;1&nbsp;);
```

```csharp
// Does not work (different units: value in // UnitWeight units kg/(ft²·s²) displayed as // value in Density units kg/m³) var unitWeight = UnitUtils.ConvertFromInternalUnits( unitWeightParam.AsDouble(), DisplayUnitType.DUT_KILOGRAMS_PER_CUBIC_METER);
```
