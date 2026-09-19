---
num: 380
date: 2010-06-04
themes: [Geometry]
tags: [revit-api, tbc]
---

# Display Webcam Image on Building Element Face

<https://jeremytammik.github.io/tbc/a/0380_revitwebcam.htm>

```csharp
&nbsp; Reference r = uidoc.Selection.PickObject( &nbsp; &nbsp; ObjectType.Face, &nbsp; &nbsp; new BimElementFilter(), &nbsp; &nbsp; _prompt ); &nbsp; _faceReference = r;
```

```csharp
class BimElementFilter : ISelectionFilter { &nbsp; public bool AllowElement( Element e ) &nbsp; { &nbsp; &nbsp; return null != e.Category &nbsp; &nbsp; &nbsp; &amp;&amp; e.Category.HasMaterialQuantities; &nbsp; } &nbsp; &nbsp; public bool AllowReference( Reference r, XYZ p ) &nbsp; { &nbsp; &nbsp; return true; &nbsp; } }
```

```csharp
&nbsp; SpatialFieldManager sfm &nbsp; &nbsp; = SpatialFieldManager.GetSpatialFieldManager( &nbsp; &nbsp; &nbsp; view ); &nbsp; &nbsp; if( null != sfm &amp;&amp; 0 &lt; _sfp_index ) &nbsp; { &nbsp; &nbsp; sfm.RemoveSpatialFieldPrimitive( &nbsp; &nbsp; &nbsp; _sfp_index ); &nbsp; &nbsp; &nbsp; _sfp_index = -1; &nbsp; }
```

```csharp
void SetAnalysisDisplayStyle( Document doc ) { &nbsp; AnalysisDisplayStyle analysisDisplayStyle; &nbsp; &nbsp; const string styleName &nbsp; &nbsp; = &quot;Revit Webcam Display Style&quot;; &nbsp; &nbsp; // extract existing display styles with specific name &nbsp; &nbsp; FilteredElementCollector a &nbsp; &nbsp; = new FilteredElementCollector( doc ); &nbsp; &nbsp; IList&lt;Element&gt; elements = a &nbsp; &nbsp; .OfClass( typeof( AnalysisDisplayStyle ) ) &nbsp; &nbsp; .Where( x =&gt; x.Name.Equals( styleName ) ) &nbsp; &nbsp; .Cast&lt;Element&gt;() &nbsp; &nbsp; .ToList(); &nbsp; &nbsp; if( 0 &lt; elements.Count ) &nbsp; { &nbsp; &nbsp; // use the existing display style &nbsp; &nbsp; &nbsp; analysisDisplayStyle = elements[0] &nbsp; &nbsp; &nbsp; as AnalysisDisplayStyle; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; // create new display style: &nbsp; &nbsp; &nbsp; // coloured surface settings: &nbsp; &nbsp; &nbsp; AnalysisDisplayColoredSurfaceSettings &nbsp; &nbsp; &nbsp; coloredSurfaceSettings &nbsp; &nbsp; &nbsp; &nbsp; = new AnalysisDisplayColoredSurfaceSettings(); &nbsp; &nbsp; &nbsp; coloredSurfaceSettings.ShowGridLines = false; &nbsp; &nbsp; &nbsp; // color settings: &nbsp; &nbsp; &nbsp; AnalysisDisplayColorSettings colorSettings &nbsp; &nbsp; &nbsp; = new AnalysisDisplayColorSettings(); &nbsp; &nbsp; &nbsp; colorSettings.MaxColor = new Color( 255, 255, 255 ); &nbsp; &nbsp; colorSettings.MinColor = new Color( 0, 0, 0 ); &nbsp; &nbsp; &nbsp; // legend settings: &nbsp; &nbsp; &nbsp; AnalysisDisplayLegendSettings legendSettings &nbsp; &nbsp; &nbsp; = new AnalysisDisplayLegendSettings(); &nbsp; &nbsp; &nbsp; legendSettings.NumberOfSteps = 10; &nbsp; &nbsp; legendSettings.Rounding = 0.05; &nbsp; &nbsp; legendSettings.ShowDataDescription = false; &nbsp; &nbsp; legendSettings.ShowLegend = true; &nbsp; &nbsp; &nbsp; // extract legend text: &nbsp; &nbsp; &nbsp; a = new FilteredElementCollector( doc ); &nbsp; &nbsp; &nbsp; elements = a &nbsp; &nbsp; &nbsp; .OfClass( typeof( TextNoteType ) ) &nbsp; &nbsp; &nbsp; .Where( x =&gt; x.Name == &quot;LegendText&quot; ) &nbsp; &nbsp; &nbsp; .Cast&lt;Element&gt;() &nbsp; &nbsp; &nbsp; .ToList(); &nbsp; &nbsp; &nbsp; if( 0 &lt; elements.Count ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // if LegendText exists, use it for this display style &nbsp; &nbsp; &nbsp; &nbsp; TextNoteType textType = elements[0] as TextNoteType; &nbsp; &nbsp
```

```csharp
&nbsp; uiapp.Idling &nbsp; &nbsp; += new EventHandler&lt;IdlingEventArgs&gt;( &nbsp; &nbsp; &nbsp; OnIdling );
```
