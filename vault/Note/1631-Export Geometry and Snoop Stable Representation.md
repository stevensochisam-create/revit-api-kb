---
num: 1631
date: 2018-03-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# Export Geometry and Snoop Stable Representation

<https://jeremytammik.github.io/tbc/a/1631_snoop_stable_rep.html>

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Project&nbsp;given&nbsp;3D&nbsp;XYZ&nbsp;point&nbsp;onto&nbsp;plane. ///&nbsp;&lt;/summary&gt; public&nbsp;static&nbsp;XYZ&nbsp;ProjectOnto( &nbsp;&nbsp;this&nbsp;Plane&nbsp;plane, &nbsp;&nbsp;XYZ&nbsp;p&nbsp;) { &nbsp;&nbsp;double&nbsp;d&nbsp;=&nbsp;plane.SignedDistanceTo(&nbsp;p&nbsp;); &nbsp;&nbsp;//XYZ&nbsp;q&nbsp;=&nbsp;p&nbsp;+&nbsp;d&nbsp;*&nbsp;plane.Normal;&nbsp;//&nbsp;wrong&nbsp;according&nbsp;to&nbsp;Ruslan&nbsp;Hanza&nbsp;and&nbsp;Alexander&nbsp;Pekshev&nbsp;in&nbsp;their&nbsp;comments&nbsp;1202_plane_proj_pick.htm#comment-3765750464 &nbsp;&nbsp;XYZ&nbsp;q&nbsp;=&nbsp;p&nbsp;-&nbsp;d&nbsp;*&nbsp;plane.Normal; &nbsp;&nbsp;Debug.Assert( &nbsp;&nbsp;&nbsp;&nbsp;Util.IsZero(&nbsp;plane.SignedDistanceTo(&nbsp;q&nbsp;)&nbsp;), &nbsp;&nbsp;&nbsp;&nbsp;&quot;expected&nbsp;point&nbsp;on&nbsp;plane&nbsp;to&nbsp;have&nbsp;zero&nbsp;distance&nbsp;to&nbsp;plane&quot;&nbsp;); &nbsp;&nbsp;return&nbsp;q; }
```

```csharp
&nbsp;&nbsp;//&nbsp;setup&nbsp;export&nbsp;folder &nbsp;&nbsp;ExportGeometryToXml.FolderName&nbsp;=&nbsp;@&nbsp;&quot;C:\Temp&quot;;
```

```csharp
&nbsp;&nbsp;List&lt;Wall&gt;&nbsp;wallsToExport&nbsp;=&nbsp;new&nbsp;List&lt;Wall&gt;(); &nbsp;&nbsp;foreach(&nbsp;Reference&nbsp;reference&nbsp;in&nbsp;selectionResult&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;Wall&nbsp;wall&nbsp;=&nbsp;(Wall)&nbsp;doc.GetElement(&nbsp;reference&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;wallsToExport.Add(&nbsp;wall&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;ExportGeometryToXml.ExportWallsByFaces(&nbsp;wallsToExport,&nbsp;&quot;walls&quot;&nbsp;);
```

```csharp
&nbsp;&nbsp;List&lt;FamilyInstance&gt;&nbsp;familyInstances&nbsp;=&nbsp;new&nbsp;List&lt;FamilyInstance&gt;(); &nbsp;&nbsp;foreach(&nbsp;Reference&nbsp;reference&nbsp;in&nbsp;selectionResult&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;Element&nbsp;el&nbsp;=&nbsp;doc.GetElement(&nbsp;reference&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;el&nbsp;is&nbsp;FamilyInstance&nbsp;familyInstance) &nbsp;&nbsp;&nbsp;&nbsp;familyInstances.Add(&nbsp;familyInstance&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;ExportGeometryToXml.ExportFamilyInstancesByFaces(&nbsp;familyInstances,&nbsp;&quot;families&quot;,&nbsp;false&nbsp;);
```
