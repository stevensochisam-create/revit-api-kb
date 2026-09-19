---
num: 882
date: 2013-01-14
themes: [Units]
tags: [revit-api, tbc]
---

# Revit 2013 Unit Conversion Utility

<https://jeremytammik.github.io/tbc/a/0882_unit_conversion.htm>

```csharp
&nbsp; if( null == _Parameter ) &nbsp; { &nbsp; &nbsp; // Create a new parameter &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; _Parameter &nbsp; &nbsp; &nbsp; &nbsp; = _DbDocument.FamilyManager.AddParameter( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; parameterTypeToCreate.ToString(), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; BuiltInParameterGroup.INVALID, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; parameterTypeToCreate, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; false ); &nbsp; &nbsp; } &nbsp; &nbsp; catch( Exception ex ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; TaskDialog.Show( &quot;Error&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &quot;Cannot create parameter '&quot; &nbsp; &nbsp; &nbsp; &nbsp; + parameterTypeToCreate.ToString() &nbsp; &nbsp; &nbsp; &nbsp; + &quot;' with parameter type '&quot; &nbsp; &nbsp; &nbsp; &nbsp; + parameterTypeToCreate &nbsp; &nbsp; &nbsp; &nbsp; + &quot;' because of exception\n&quot; &nbsp; &nbsp; &nbsp; &nbsp; + ex.Message.ToString() ); &nbsp; &nbsp; &nbsp; &nbsp; return; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; public static bool canGetFormatOptions( &nbsp; &nbsp; Document doc, &nbsp; &nbsp; FamilyParameter familyParameter ) &nbsp; { &nbsp; &nbsp; try &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; UnitType parameterUnitType &nbsp; &nbsp; &nbsp; &nbsp; = ConvertParameterTypeToUnitType( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; familyParameter.Definition.ParameterType ); &nbsp; &nbsp; &nbsp; &nbsp; doc.ProjectUnit.get_FormatOptions( &nbsp; &nbsp; &nbsp; &nbsp; parameterUnitType ); &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; } &nbsp; &nbsp; catch &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return false; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; if( !canGetFormatOptions( &nbsp; &nbsp; famDoc, familyParameter ) ) &nbsp; { &nbsp; &nbsp; TaskDialog.Show( &quot;Error&quot;, &nbsp; &nbsp; &nbsp; &quot;Cannot set parameter value.\nUnit Type &quot; &nbsp; &nbsp; &nbsp; + ConvertParameterTypeToUnitType( &nbsp; &nbsp; &nbsp; &nbsp; familyParameter.Definition.ParameterType ) &nbsp; &nbsp; &nbsp; + &quot; is not supported in Revit &quot; &nbsp; &nbsp; &nbsp; + famDoc.Application.Product.ToString() ); &nbsp; }
```
