---
num: 665
date: 2011-10-14
themes: [MEP]
tags: [revit-api, tbc]
---

# Retrieving Duct and Pipe Endpoints

<https://jeremytammik.github.io/tbc/a/0665_retrieve_duct_endpoint.htm>

```csharp
public Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; UIApplication uiapp = commandData.Application; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; FilteredElementCollector a &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( Duct ) ); &nbsp; &nbsp; int nDucts = 0; &nbsp; int nCurves = 0; &nbsp; &nbsp; foreach( Duct d in a ) &nbsp; { &nbsp; &nbsp; ++nDucts; &nbsp; &nbsp; &nbsp; LocationCurve lc = d.Location as LocationCurve; &nbsp; &nbsp; &nbsp; Debug.Assert( null != lc, &nbsp; &nbsp; &nbsp; &quot;expected duct to have valid location curve&quot; ); &nbsp; &nbsp; &nbsp; if( null != lc ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ++nCurves; &nbsp; &nbsp; &nbsp; &nbsp; Curve c = lc.Curve; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;Duct {0} from {1} to {2}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; d.Id.IntegerValue, &nbsp; &nbsp; &nbsp; &nbsp; PointString( c.get_EndPoint( 0 ) ), &nbsp; &nbsp; &nbsp; &nbsp; PointString( c.get_EndPoint( 1 ) ) ); &nbsp; &nbsp; } &nbsp; } &nbsp; Debug.Print( &nbsp; &nbsp; &quot;{0} duct{1} analysed, and {2} curve{3} listed.&quot;, &nbsp; &nbsp; nDucts, PluralSuffix( nDucts ), &nbsp; &nbsp; nCurves, PluralSuffix( nCurves ) ); &nbsp; &nbsp; return Result.Succeeded; }
```

```csharp
Duct 392168 from (60.53,121.53,10.32) to (60.53,110.24,10.32) Duct 392170 from (28.59,119.19,10.32) to (28.59,110.24,10.32) Duct 392174 from (39.29,113.74,10.32) to (39.29,110.57,10.32) . . . Duct 686628 from (-39.04,21.2,16.84) to (-39.04,21.2,49.52) Duct 712063 from (115.66,-11.57,10.38) to (115.66,-15,10.38) 727 ducts analysed, and 727 curves listed.
```
