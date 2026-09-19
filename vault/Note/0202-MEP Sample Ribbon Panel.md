---
num: 202
date: 2009-08-14
themes: [MEP]
tags: [revit-api, tbc]
---

# MEP Sample Ribbon Panel

<https://jeremytammik.github.io/tbc/a/0202_mep_ribbon_panel.htm>

```csharp
private static void AddMenu( ControlledApplication app ) { &nbsp; const string m = &quot;mep.Cmd&quot;; // namespace and command prefix &nbsp; string path = System.Reflection.Assembly.GetExecutingAssembly().Location; &nbsp; Autodesk.Revit.MenuItem rootMenu = app.CreateTopMenu( &quot;ME&amp;P API Samples&quot; ); &nbsp; MenuItem.MenuType mt = MenuItem.MenuType.BasicMenu; &nbsp; rootMenu.Append( mt, &quot;&amp;Assign flow to terminals&quot;, path, m + &quot;AssignFlowToTerminals&quot; ); &nbsp; rootMenu.Append( mt, &quot;&amp;Change size&quot;, path, m + &quot;ChangeSize&quot; ); &nbsp; rootMenu.Append( mt, &quot;&amp;Populate CFM per SF on spaces&quot;, path, m + &quot;PopulateCfmPerSf&quot; ); &nbsp; rootMenu.Append( mt, &quot;&amp;Reset demo&quot;, path, m + &quot;ResetDemo&quot; ); &nbsp; rootMenu.Append( MenuItem.MenuType.SeparatorMenu ); &nbsp; rootMenu.Append( mt, &quot;Electrical &amp;System Browser&quot;, path, m + &quot;ElectricalSystemBrowser&quot; ); &nbsp; rootMenu.Append( mt, &quot;Electrical &amp;Hierarchy&quot;, path, m + &quot;ElectricalHierarchy&quot; ); &nbsp; rootMenu.Append( mt, &quot;Electrical Hierarchy &amp;2&quot;, path, m + &quot;ElectricalHierarchy2&quot; ); &nbsp; rootMenu.Append( mt, &quot;&amp;Unhosted elements&quot;, path, m + &quot;UnhostedElements&quot; ); &nbsp; rootMenu.Append( MenuItem.MenuType.SeparatorMenu ); &nbsp; rootMenu.Append( mt, &quot;A&amp;bout...&quot;, path, m + &quot;About&quot; ); }
```

```csharp
static void AddRibbonPanel( &nbsp; ControlledApplication a ) { &nbsp; const string m = &quot;mep.Cmd&quot;; // namespace and command prefix &nbsp; string path = Assembly.GetExecutingAssembly().Location; &nbsp; &nbsp; string[] text = new string[] { &nbsp; &nbsp; &quot;Assign flow to terminals&quot;, &nbsp; &nbsp; &quot;Change size&quot;, &nbsp; &nbsp; &quot;Populate CFM per SF on spaces&quot;, &nbsp; &nbsp; &quot;Reset demo&quot;, &nbsp; &nbsp; &quot;Electrical System Browser&quot;, &nbsp; &nbsp; &quot;Electrical Hierarchy&quot;, &nbsp; &nbsp; &quot;Electrical Hierarchy 2&quot;, &nbsp; &nbsp; &quot;Unhosted elements&quot;, &nbsp; &nbsp; &quot;About...&quot; &nbsp; }; &nbsp; &nbsp; string[] classNameStem = new string[] { &nbsp; &nbsp; &quot;AssignFlowToTerminals&quot;, &nbsp; &nbsp; &quot;ChangeSize&quot;, &nbsp; &nbsp; &quot;PopulateCfmPerSf&quot;, &nbsp; &nbsp; &quot;ResetDemo&quot;, &nbsp; &nbsp; &quot;ElectricalSystemBrowser&quot;, &nbsp; &nbsp; &quot;ElectricalHierarchy&quot;, &nbsp; &nbsp; &quot;ElectricalHierarchy2&quot;, &nbsp; &nbsp; &quot;UnhostedElements&quot;, &nbsp; &nbsp; &quot;About&quot; &nbsp; }; &nbsp; // &nbsp; // create three stacked buttons for the &nbsp; // HVAC, electrical and about commands respectively: &nbsp; // &nbsp; RibbonPanel panel = a.CreateRibbonPanel( &nbsp; &nbsp; &quot;MEP Sample&quot; ); &nbsp; &nbsp; PulldownButtonData d1 = new PulldownButtonData( &nbsp; &nbsp; &quot;Hvac&quot;, &quot;HVAC&quot; ); &nbsp; &nbsp; d1.ToolTip = &quot;HVAC Commands&quot;; &nbsp; &nbsp; PulldownButtonData d2 = new PulldownButtonData( &nbsp; &nbsp; &quot;Electrical&quot;, &quot;Electrical&quot; ); &nbsp; &nbsp; d2.ToolTip = &quot;Electrical Commands&quot;; &nbsp; &nbsp; PushButtonData d3 = new PushButtonData( &nbsp; &nbsp; classNameStem[8], text[8], path, m + classNameStem[8] ); &nbsp; &nbsp; d3.ToolTip = &quot;About the HVAC and Electrical MEP Sample.&quot;; &nbsp; &nbsp; List&lt;RibbonItem&gt; ribbonItems = panel.AddStackedButtons( &nbsp; &nbsp; d1, d2, d3 ); &nbsp; // &nbsp; // add subitems to the HVAC and electrical pulldown buttons: &nbsp; // &nbsp; PulldownButton pulldown; &nbsp; PushButton pb; &nbsp; int j; &nbsp; &nbsp; for( int i = 0; i &lt; 8; ++i ) &nbsp; { &nbsp; &nbsp; j = i &lt; 4 ? 0 : 1; &nbsp; &nbsp; pulldown = ribbonItems[j] as PulldownButton; &nbsp; &nbsp; &nbsp; pb = pulldown.AddItem( text[i], path, &nbsp; &nbsp; &nbsp; m + c
```

```csharp
internal static System.Drawing.Bitmap door_button { get { object obj = ResourceManager.GetObject( "door_button", resourceCulture); return ((System.Drawing.Bitmap)(obj)); } }
```

```csharp
static void Main( string[] args ) { &nbsp; Bitmap a = Resource1.Image1; &nbsp; &nbsp; MemoryStream ms = new MemoryStream(); &nbsp; a.Save( ms, ImageFormat.Png ); &nbsp; &nbsp; BitmapImage b = new BitmapImage(); &nbsp; b.BeginInit(); &nbsp; b.StreamSource = ms; &nbsp; b.EndInit(); }
```
