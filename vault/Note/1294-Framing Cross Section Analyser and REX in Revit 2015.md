---
num: 1294
date: 2015-03-12
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Framing Cross Section Analyser and REX in Revit 2015

<https://jeremytammik.github.io/tbc/a/1294_framing_xsec_analyse.htm>

```csharp
&nbsp; AppDomain.CurrentDomain.AssemblyResolve &nbsp; &nbsp; += new ResolveEventHandler( OnAssemblyResolve );
```

```csharp
&nbsp; static System.Reflection.Assembly OnAssemblyResolve( &nbsp; &nbsp; object sender, &nbsp; &nbsp; ResolveEventArgs args ) &nbsp; { &nbsp; &nbsp; Assembly a = Assembly.GetExecutingAssembly(); &nbsp; &nbsp; &nbsp; return Autodesk.REX.Framework.REXAssemblies &nbsp; &nbsp; &nbsp; .Resolve( sender, args, &quot;2015&quot;, a ); &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Use REX to analyse element cross section. &nbsp; /// This requires a reference to &nbsp; /// REX.ContentGeneratorLT.dll and prior &nbsp; /// initialisation of the REX framework. &nbsp; /// The converter initialisation must reside in &nbsp; /// a different method than the subscription to &nbsp; /// the assembly resolver OnAssemblyResolve. &nbsp; /// &lt;/summary&gt; &nbsp; void RexXsecAnalyis( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; Element e ) &nbsp; { &nbsp; &nbsp; // Initialise converter &nbsp; &nbsp; &nbsp; RVTFamilyConverter rvt = new RVTFamilyConverter( &nbsp; &nbsp; &nbsp; commandData, true ); &nbsp; &nbsp; &nbsp; // Retrieve family type &nbsp; &nbsp; &nbsp; REXFamilyType fam = rvt.GetFamily( e, &nbsp; &nbsp; &nbsp; ECategoryType.SECTION_PARAM ); &nbsp; &nbsp; &nbsp; // Retrieve section data &nbsp; &nbsp; &nbsp; REXFamilyType_ParamSection paramSection = fam &nbsp; &nbsp; &nbsp; as REXFamilyType_ParamSection; &nbsp; &nbsp; &nbsp; REXSectionParamDescription parameters &nbsp; &nbsp; &nbsp; = paramSection.Parameters; &nbsp; &nbsp; &nbsp; // Extract dimensions, section type, tapered &nbsp; &nbsp; // predicate, etc. &nbsp; &nbsp; // If different start and end sections are &nbsp; &nbsp; // required, use DimensionsEnd as well. &nbsp; &nbsp; &nbsp; REXSectionParamDimensions dimensions = parameters &nbsp; &nbsp; &nbsp; .Dimensions; &nbsp; &nbsp; &nbsp; ESectionType sectionType = parameters &nbsp; &nbsp; &nbsp; .SectionType; &nbsp; &nbsp; &nbsp; bool tapered = parameters.Tapered; &nbsp; &nbsp; &nbsp; bool start = true; &nbsp; &nbsp; &nbsp; Contour_Section contour = parameters.GetContour( &nbsp; &nbsp; &nbsp; start ); &nbsp; &nbsp; &nbsp; List&lt;ContourCont&gt; shape = contour.Shape; &nbsp; &nbsp; &nbsp; Util.InfoMessage( string.Format( &nbsp; &nbsp; &nbsp; &quot;The selected structural framing element &quot; &nbsp; &nbsp; &nbsp; + &quot;cross section REX section type is &quot; &nbsp; &nbsp; &nbsp; + &quot;{0}.&quot;, sectionType ) ); &nbsp; }
```

```csharp
The selected structural framing element cross section section view cut plane face has 1 loop and is thus 'open'. The selected structural framing element cross section REX section type is I.
```

```csharp
'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Windows\Microsoft.Net\assembly\GAC_MSIL\Autodesk.REX.Framework\v4.0_2014.0.0.0__51e16e3b26b42eda\Autodesk.REX.Framework.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Windows\assembly\GAC_MSIL\Autodesk.Common.AResourcesControl\1.0.0.0__ff3304d4f320ee59\Autodesk.Common.AResourcesControl.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Components\AREXContentGenerator\REX.ContentGeneratorLT.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Windows\Microsoft.Net\assembly\GAC_MSIL\Autodesk.REX.Framework\v4.0_2015.0.0.0__51e16e3b26b42eda\Autodesk.REX.Framework.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Foundation\REX.Foundation.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Foundation\REX.Foundation.Forms.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Products\Revit\AREXRevitMngr.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Foundation\REX.Geometry.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\REX.Engine.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\REX.Preferences.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\REX.System.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\REX.UI.WPF.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\REX.UI.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\REX.UI.Forms.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\en-US\REX.UI.resources.dll' 'Revit.exe' (Managed (v4.0.30319)): Loaded 'C:\Program Files\Common Files\Autodesk Shared\Extensions 2015\Framework\Engine\en-US\REX.Sy
```
