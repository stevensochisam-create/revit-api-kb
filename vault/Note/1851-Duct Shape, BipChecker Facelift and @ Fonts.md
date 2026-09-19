---
num: 1851
date: 2020-06-22
themes: [Geometry, MEP]
tags: [revit-api, tbc]
---

# Duct Shape, BipChecker Facelift and @ Fonts

<https://jeremytammik.github.io/tbc/a/1851_bipch_mepshap_atfont.html>

```csharp
&nbsp;&nbsp;var&nbsp;fabPart&nbsp;=&nbsp;myElement&nbsp;as&nbsp;FabricationPart; &nbsp;&nbsp;foreach(&nbsp;Connector&nbsp;conn &nbsp;&nbsp;&nbsp;&nbsp;in&nbsp;fabPart.ConnectorManager.Connectors&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;shape&nbsp;=&nbsp;conn.Shape; &nbsp;&nbsp;}
```

```csharp
DuctType&nbsp;dt&nbsp;=&nbsp;doc.GetElement(&nbsp;tid&nbsp;) &nbsp;&nbsp;as&nbsp;DuctType; if(&nbsp;null&nbsp;!=&nbsp;dt&nbsp;) { &nbsp;&nbsp;if(&nbsp;HasInvalidElementIdValue(&nbsp;e,&nbsp;BuiltInParameter &nbsp;&nbsp;&nbsp;&nbsp;.RBS_CURVETYPE_MULTISHAPE_TRANSITION_OVALROUND_PARAM&nbsp;)&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;shape&nbsp;=&nbsp;&quot;rectangular&quot;; &nbsp;&nbsp;} &nbsp;&nbsp;else&nbsp;if(&nbsp;HasInvalidElementIdValue(&nbsp;e,&nbsp;BuiltInParameter &nbsp;&nbsp;&nbsp;&nbsp;.RBS_CURVETYPE_MULTISHAPE_TRANSITION_RECTOVAL_PARAM&nbsp;)&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;shape&nbsp;=&nbsp;&quot;round&quot;; &nbsp;&nbsp;} &nbsp;&nbsp;else&nbsp;if(&nbsp;HasInvalidElementIdValue(&nbsp;e,&nbsp;BuiltInParameter &nbsp;&nbsp;&nbsp;&nbsp;.RBS_CURVETYPE_MULTISHAPE_TRANSITION_PARAM&nbsp;)&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;shape&nbsp;=&nbsp;&quot;oval&quot;; &nbsp;&nbsp;} }
```

```csharp
&nbsp;&nbsp;public&nbsp;void&nbsp;GetAllInstalledFonts() &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;System.Drawing.Text.InstalledFontCollection&nbsp;ifc &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;System.Drawing.Text.InstalledFontCollection(); &nbsp;&nbsp;&nbsp;&nbsp;List&lt;string&gt;&nbsp;fontList&nbsp;=&nbsp;new&nbsp;List&lt;string&gt;(); &nbsp;&nbsp;&nbsp;&nbsp;//list&nbsp;of&nbsp;all&nbsp;font&nbsp;family&nbsp;names &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;var&nbsp;font&nbsp;in&nbsp;ifc.Families&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fontList.Add(&nbsp;font.Name&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;fontList.Sort(); &nbsp;&nbsp;&nbsp;&nbsp;TaskDialog.Show(&nbsp;&quot;Installed&nbsp;Fonts&quot;, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string.Join(&nbsp;Environment.NewLine,&nbsp;fontList&nbsp;)&nbsp;); &nbsp;&nbsp;}
```

```csharp
Private&nbsp;Function&nbsp;TObj70( &nbsp;&nbsp;ByVal&nbsp;commandData&nbsp;As&nbsp;Autodesk.Revit.UI.ExternalCommandData, &nbsp;&nbsp;ByRef&nbsp;message&nbsp;As&nbsp;String, &nbsp;&nbsp;ByVal&nbsp;elements&nbsp;As&nbsp;Autodesk.Revit.DB.ElementSet)&nbsp;As&nbsp;Result &nbsp;&nbsp;Dim&nbsp;FD&nbsp;As&nbsp;New&nbsp;Windows.Forms.FontDialog &nbsp;&nbsp;FD.ShowColor&nbsp;=&nbsp;False&nbsp;&#39;or&nbsp;True&nbsp;if&nbsp;you&nbsp;like &nbsp;&nbsp;FD.ShowEffects&nbsp;=&nbsp;False &nbsp;&nbsp;FD.MinSize&nbsp;=&nbsp;10 &nbsp;&nbsp;FD.MaxSize&nbsp;=&nbsp;10 &nbsp;&nbsp;FD.ShowEffects&nbsp;=&nbsp;False &nbsp;&nbsp;FD.AllowScriptChange&nbsp;=&nbsp;False &nbsp;&nbsp;FD.AllowSimulations&nbsp;=&nbsp;False &nbsp;&nbsp;FD.ShowDialog() &nbsp;&nbsp;Dim&nbsp;Nme&nbsp;As&nbsp;String&nbsp;=&nbsp;&quot;&quot; &nbsp;&nbsp;If&nbsp;FD.Font.GdiVerticalFont&nbsp;Then &nbsp;&nbsp;&nbsp;&nbsp;Nme&nbsp;=&nbsp;&quot;@&quot;&nbsp;&amp;&nbsp;FD.Font.Name &nbsp;&nbsp;Else &nbsp;&nbsp;&nbsp;&nbsp;Nme&nbsp;=&nbsp;FD.Font.Name &nbsp;&nbsp;End&nbsp;If &nbsp;&nbsp;TaskDialog.Show(&quot;Font&quot;,&nbsp;Nme) &nbsp;&nbsp;Return&nbsp;Result.Succeeded End&nbsp;Function
```
