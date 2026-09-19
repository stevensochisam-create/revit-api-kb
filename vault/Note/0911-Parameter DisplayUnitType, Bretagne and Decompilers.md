---
num: 911
date: 2013-03-19
themes: [Parameter, Pitfall]
tags: [revit-api, tbc]
---

# Parameter DisplayUnitType, Bretagne and Decompilers

<https://jeremytammik.github.io/tbc/a/0911_displayunittype.htm>

```csharp
public DisplayUnitType DisplayUnitType { &nbsp; get &nbsp; { &nbsp; &nbsp; Definition definition = this.Definition; &nbsp; &nbsp; ParamTypeSpec paramTypeSpec1; &nbsp; &nbsp; if ((ParamTypeEnum) *(int*) &nbsp; &nbsp; &nbsp; definition.getParamTypeSpec(&amp;paramTypeSpec1) &nbsp; &nbsp; &nbsp; != (ParamTypeEnum) 15) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; throw new Autodesk.Revit.Exceptions &nbsp; &nbsp; &nbsp; &nbsp; .InvalidOperationException(new FunctionId( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;n:\\build\\2013_ship_x64_inst_20120221_2030\\source\\api\\revitapi\\objects\\parameters\\APIParameter.cpp&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 581, &quot;Autodesk::Revit::DB::Parameter::DisplayUnitType::get&quot;), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; string.Empty); &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ParamTypeSpec paramTypeSpec2; &nbsp; &nbsp; &nbsp; return (DisplayUnitType) &nbsp; &nbsp; &nbsp; &nbsp; \u003CModule\u003E.FormatOptions\u002EgetDisplayUnits( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \u003CModule\u003E.AUnits\u002EgetFormatOptions( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \u003CModule\u003E.ADocument\u002EgetAUnits( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (ADocument*) *(long*) this.m_pCDA), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (UnitType.Enum) *(int*) ((IntPtr) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; definition.getParamTypeSpec(&amp;paramTypeSpec2) + 8L))); &nbsp; &nbsp; } &nbsp; } }
```

```csharp
&nbsp; default: &nbsp; &nbsp; parameterType = (ParameterType) ( &nbsp; &nbsp; &nbsp; ^(int&amp;) ((IntPtr) &amp;paramTypeSpec + 8) + 100); &nbsp; &nbsp; break;
```

```csharp
public static class ParameterExtensions { &nbsp; public static bool HasDisplayUnitType( &nbsp; &nbsp; this Parameter parameter ) &nbsp; { &nbsp; &nbsp; var parameterType = &nbsp; &nbsp; &nbsp; &nbsp; parameter.Definition.ParameterType; &nbsp; &nbsp; &nbsp; switch( parameterType ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; case ParameterType.Length: &nbsp; &nbsp; &nbsp; case ParameterType.Area: &nbsp; &nbsp; &nbsp; case ParameterType.Volume: &nbsp; &nbsp; &nbsp; case ParameterType.Angle: &nbsp; &nbsp; &nbsp; case ParameterType.Number: &nbsp; &nbsp; &nbsp; case ParameterType.Force: &nbsp; &nbsp; &nbsp; case ParameterType.LinearForce: &nbsp; &nbsp; &nbsp; case ParameterType.AreaForce: &nbsp; &nbsp; &nbsp; case ParameterType.Moment: &nbsp; &nbsp; &nbsp; &nbsp; return true; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; /* At the reflector I can see the following code &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; default: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; parameterType = (ParameterType) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (^(int&amp;) ((IntPtr) &amp;paramTypeSpec &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + 8) + 100); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; looking at the ParameterType enumeration &nbsp; &nbsp; &nbsp; &nbsp; suggests that every parameter type whose &nbsp; &nbsp; &nbsp; &nbsp; integer value is greater than 100 belongs &nbsp; &nbsp; &nbsp; &nbsp; to paramTypeSpec = 15 &nbsp; &nbsp; */ &nbsp; &nbsp; return 100 &lt; (int) parameterType; &nbsp; } }
```

```csharp
&nbsp; Reference r; &nbsp; &nbsp; try &nbsp; { &nbsp; &nbsp; r = uidoc.Selection.PickObject( &nbsp; &nbsp; &nbsp; ObjectType.Element ); &nbsp; } &nbsp; catch( OperationCanceledException ) &nbsp; { &nbsp; &nbsp; message = &quot;Cancelled&quot;; &nbsp; &nbsp; return Result.Cancelled; &nbsp; } &nbsp; &nbsp; var e = doc.GetElement( r.ElementId ); &nbsp; &nbsp; Stopwatch sw = Stopwatch.StartNew(); &nbsp; &nbsp; foreach( Parameter parameter in e.Parameters ) &nbsp; { &nbsp; &nbsp; try &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; DisplayUnitType dut = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; parameter.DisplayUnitType; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( dut.ToString() ); &nbsp; &nbsp; } &nbsp; &nbsp; catch( Autodesk.Revit.Exceptions &nbsp; &nbsp; &nbsp; .InvalidOperationException ) &nbsp; &nbsp; { &nbsp; &nbsp; } &nbsp; } &nbsp; sw.Stop(); &nbsp; &nbsp; TaskDialog.Show( &quot;Benchmark result&quot;, &nbsp; &nbsp; sw.Elapsed.ToString() );
```

```csharp
&nbsp; Reference r; &nbsp; &nbsp; try &nbsp; { &nbsp; &nbsp; r = uidoc.Selection.PickObject( &nbsp; &nbsp; &nbsp; ObjectType.Element ); &nbsp; } &nbsp; catch( OperationCanceledException ) &nbsp; { &nbsp; &nbsp; &nbsp; message = &quot;Canceled&quot;; &nbsp; &nbsp; return Result.Cancelled; &nbsp; } &nbsp; &nbsp; var e = doc.GetElement( r.ElementId ); &nbsp; &nbsp; Stopwatch sw = Stopwatch.StartNew(); &nbsp; &nbsp; foreach( Parameter parameter in e.Parameters ) &nbsp; { &nbsp; &nbsp; if( parameter.HasDisplayUnitType() ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; DisplayUnitType dut = &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; parameter.DisplayUnitType; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( dut.ToString() ); &nbsp; &nbsp; } &nbsp; } &nbsp; sw.Stop(); &nbsp; &nbsp; TaskDialog.Show( &quot;Benchmark result&quot;, &nbsp; &nbsp; sw.Elapsed.ToString() );
```
