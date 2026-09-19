---
num: 280
date: 2010-01-12
themes: [Geometry]
tags: [revit-api, tbc]
---

# Import LandXML Surface

<https://jeremytammik.github.io/tbc/a/0280_landxml.htm>

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; &nbsp; W.OpenFileDialog dlg = new W.OpenFileDialog(); &nbsp; dlg.Filter = &quot;LandXML files (*.xml)|*.xml&quot;; &nbsp; dlg.Title = &quot;Import LandXML and &quot; &nbsp; + &quot;Create TopographySurface&quot;; &nbsp; if( dlg.ShowDialog() != W.DialogResult.OK ) { &nbsp; return CmdResult.Cancelled; } &nbsp; XmlDocument xmlDoc = new XmlDocument(); xmlDoc.Load( dlg.FileName ); &nbsp; XmlNodeList pnts &nbsp; = xmlDoc.GetElementsByTagName( &quot;Pnts&quot; ); &nbsp; char[] separator = new char[] { ' ' }; double x = 0, y = 0, z = 0; XYZ xyz; &nbsp; XYZArray pts = app.Create.NewXYZArray(); &nbsp; for( int k = 0; k &lt; pnts.Count; ++k ) { &nbsp; for( int i = 0; &nbsp; &nbsp; i &lt; pnts[k].ChildNodes.Count; ++i ) &nbsp; { &nbsp; &nbsp; int j = 1; &nbsp; &nbsp; &nbsp; string text = pnts[k].ChildNodes[i].InnerText; &nbsp; &nbsp; string[] coords = text.Split( separator ); &nbsp; &nbsp; &nbsp; foreach( string coord in coords ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; switch( j ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; case 1: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x = Double.Parse( coord ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; case 2: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; y = Double.Parse( coord ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; case 3: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; z = Double.Parse( coord ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; &nbsp; default: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; j++; &nbsp; &nbsp; } &nbsp; &nbsp; xyz = new XYZ( x, y, z ); &nbsp; &nbsp; pts.Append( xyz ); &nbsp; } } &nbsp; TopographySurface surface &nbsp; = doc.Create.NewTopographySurface( pts ); &nbsp; return CmdResult.Succeeded;
```
