---
num: 536
date: 2011-02-15
themes: [MEP]
tags: [revit-api, tbc]
---

# Create a Pipe Cap

<https://jeremytammik.github.io/tbc/a/0536_pipe_cap.htm>

```csharp
&nbsp; UIApplication uiapp = commandData.Application; &nbsp; Document rvtDoc = uiapp.ActiveUIDocument.Document; &nbsp; &nbsp; XYZ start = new XYZ( 0, 0, 0 ); &nbsp; XYZ end = new XYZ( 6, 0, 4 ); &nbsp; &nbsp; FilteredElementCollector collector &nbsp; &nbsp; = new FilteredElementCollector( rvtDoc ); &nbsp; &nbsp; collector.OfClass( typeof( ElementType ) ); &nbsp; &nbsp; PipeType pipeType = collector.FirstElement() &nbsp; &nbsp; as PipeType; &nbsp; &nbsp; Pipe pipe = rvtDoc.Create.NewPipe( &nbsp; &nbsp; start, end, pipeType ); &nbsp; &nbsp; pipe.get_Parameter( &nbsp; &nbsp; BuiltInParameter.RBS_PIPE_DIAMETER_PARAM ) &nbsp; &nbsp; .Set( 0.1667 ); // revise to 2&quot; dia pipe
```

```csharp
&nbsp; const string _libFolder = &quot;C:/Documents and Settings&quot; &nbsp; &nbsp; + &quot;/All Users/Application Data/Autodesk/RME 2011&quot; &nbsp; &nbsp; + &quot;/Metric Library/Pipe/Fittings/Generic&quot;; &nbsp; &nbsp; const string _rfaExtension = &quot;.rfa&quot;; &nbsp; const string _capFamilyName = &quot;M_Cap - Generic&quot;; &nbsp; const string _capSymbolName = &quot;Standard&quot;;
```

```csharp
&nbsp; UIApplication uiapp = commandData.Application; &nbsp; Document doc = uiapp.ActiveUIDocument.Document; &nbsp; &nbsp; PipeType pipeType &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; .OfClass( typeof( ElementType ) ) &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_PipeCurves ) &nbsp; &nbsp; .FirstElement() as PipeType; &nbsp; &nbsp; XYZ start = new XYZ( 0, 0, 0 ); &nbsp; XYZ end = new XYZ( 6, 0, 4 ); &nbsp; &nbsp; Transaction t = new Transaction( doc, &nbsp; &nbsp; &quot;Create Pipe Cap&quot; ); &nbsp; &nbsp; t.Start(); &nbsp; &nbsp; Pipe pipe = doc.Create.NewPipe( &nbsp; &nbsp; start, end, pipeType ); &nbsp; &nbsp; pipe.get_Parameter( &nbsp; &nbsp; BuiltInParameter.RBS_PIPE_DIAMETER_PARAM ) &nbsp; &nbsp; .Set( 0.1667 ); // revise to 2&quot; dia pipe &nbsp; &nbsp; // get cap symbol: &nbsp; &nbsp; List&lt;FamilySymbol&gt; symbols = new List&lt;FamilySymbol&gt;( &nbsp; &nbsp; new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_PipeFitting ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( FamilySymbol ) ) &nbsp; &nbsp; &nbsp; .OfType&lt;FamilySymbol&gt;() &nbsp; &nbsp; &nbsp; .Where&lt;FamilySymbol&gt;( s &nbsp; &nbsp; &nbsp; &nbsp; =&gt; s.Family.Name.Equals( _capFamilyName ) ) ); &nbsp; &nbsp; FamilySymbol capSymbol = null; &nbsp; &nbsp; if( 0 &lt; symbols.Count ) &nbsp; { &nbsp; &nbsp; capSymbol = symbols[0]; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; string filename = Path.Combine( _libFolder, &nbsp; &nbsp; &nbsp; _capFamilyName + _rfaExtension ); &nbsp; &nbsp; &nbsp; // requires a transaction, obviously: &nbsp; &nbsp; &nbsp; doc.LoadFamilySymbol( filename, _capSymbolName, &nbsp; &nbsp; &nbsp; out capSymbol ); &nbsp; } &nbsp; &nbsp; Debug.Assert( capSymbol.Family.Name.Equals( _capFamilyName ), &nbsp; &nbsp; &quot;expected cap pipe fitting to be of family &quot; + _capFamilyName ); &nbsp; &nbsp; FamilyInstance fi = doc.Create.NewFamilyInstance( &nbsp; &nbsp; end, capSymbol, StructuralType.NonStructural );
```

```csharp
&nbsp; // pick connector on cap: &nbsp; &nbsp; ConnectorSet connectors &nbsp; &nbsp; = fi.MEPModel.ConnectorManager.Connectors; &nbsp; &nbsp; Debug.Assert( 1 == connectors.Size, &nbsp; &nbsp; &quot;expected nly one connector on pipe cap element&quot; ); &nbsp; &nbsp; Connector cap_end = null; &nbsp; &nbsp; foreach( Connector c in connectors ) &nbsp; { &nbsp; &nbsp; cap_end = c; &nbsp; } &nbsp; &nbsp; // pick closest connector on pipe: &nbsp; &nbsp; connectors = pipe.ConnectorManager.Connectors; &nbsp; &nbsp; Connector pipe_end = null; &nbsp; &nbsp; // the order of connectors returned by the &nbsp; // connector manager may change, so we &nbsp; // always use a location (or even more &nbsp; // information if several connectors are &nbsp; // at the same location) to get the right &nbsp; // connector! &nbsp; &nbsp; double dist = double.MaxValue; &nbsp; &nbsp; foreach( Connector c in connectors ) &nbsp; { &nbsp; &nbsp; XYZ p = c.Origin; &nbsp; &nbsp; double d = p.DistanceTo( end ); &nbsp; &nbsp; &nbsp; if( d &lt; dist ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; dist = d; &nbsp; &nbsp; &nbsp; pipe_end = c; &nbsp; &nbsp; } &nbsp; &nbsp; break; &nbsp; } &nbsp; &nbsp; cap_end.ConnectTo( pipe_end ); &nbsp; &nbsp; t.Commit(); &nbsp; &nbsp; return Result.Succeeded;
```
