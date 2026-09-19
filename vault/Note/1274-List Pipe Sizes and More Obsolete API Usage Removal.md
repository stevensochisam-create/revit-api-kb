---
num: 1274
date: 2015-02-02
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# List Pipe Sizes and More Obsolete API Usage Removal

<https://jeremytammik.github.io/tbc/a/1274_pipe_sizes.htm>

```csharp
&nbsp; const string _filename = &quot;C:/pipesizes.txt&quot;; &nbsp; &nbsp; string FootToMmString( double a ) &nbsp; { &nbsp; &nbsp; return Util.FootToMm( a ) &nbsp; &nbsp; &nbsp; .ToString( &quot;0.##&quot; ) &nbsp; &nbsp; &nbsp; .PadLeft( 8 ); &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// List all the pipe segment sizes in the given document. &nbsp; /// &lt;/summary&gt; &nbsp; /// &lt;param name=&quot;doc&quot;&gt;&lt;/param&gt; &nbsp; void GetPipeSegmentSizes( &nbsp; &nbsp; Document doc ) &nbsp; { &nbsp; &nbsp; FilteredElementCollector segments &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( Segment ) ); &nbsp; &nbsp; &nbsp; using( StreamWriter file = new StreamWriter( &nbsp; &nbsp; &nbsp; _filename, true ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( Segment segment in segments ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; file.WriteLine( segment.Name ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; foreach( MEPSize size in segment.GetSizes() ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; file.WriteLine( string.Format( &quot;&nbsp; {0} {1} {2}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; FootToMmString( size.NominalDiameter ), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; FootToMmString( size.InnerDiameter ), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; FootToMmString( size.OuterDiameter ) ) ); &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```
