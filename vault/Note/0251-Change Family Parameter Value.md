---
num: 251
date: 2009-11-23
themes: [Parameter]
tags: [revit-api, tbc]
---

# Change Family Parameter Value

<https://jeremytammik.github.io/tbc/a/0251_change_family_param_value.htm>

```csharp
void addParameters() { &nbsp; FamilyManager mgr = _rvtDoc.FamilyManager; &nbsp; &nbsp; // API parameter group for Dimension is PG_GEOMETRY: &nbsp; // &nbsp; FamilyParameter paramTw = mgr.AddParameter( &nbsp; &nbsp; &quot;Tw&quot;, BuiltInParameterGroup.PG_GEOMETRY, &nbsp; &nbsp; ParameterType.Length, false ); &nbsp; &nbsp; FamilyParameter paramTd = mgr.AddParameter( &nbsp; &nbsp; &quot;Td&quot;, BuiltInParameterGroup.PG_GEOMETRY, &nbsp; &nbsp; ParameterType.Length, false ); &nbsp; &nbsp; // set initial values: &nbsp; // &nbsp; double tw = mmToFeet( 150.0 ); &nbsp; double td = mmToFeet( 150.0 ); &nbsp; mgr.Set( paramTw, tw ); &nbsp; mgr.Set( paramTd, td ); }
```

```csharp
&nbsp; FamilyParameter paramDan = mgr.AddParameter( &nbsp; &nbsp; &quot;Dan&quot;, BuiltInParameterGroup.PG_TEXT, &nbsp; &nbsp; ParameterType.YesNo, true ); &nbsp; &nbsp; mgr.Set( paramDan, 0 );
```
