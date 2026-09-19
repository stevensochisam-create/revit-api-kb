---
num: 1679
date: 2018-09-04
themes: [Geometry, Pitfall]
tags: [revit-api, tbc]
---

# Reference Intersector and Deleting Reference Planes

<https://jeremytammik.github.io/tbc/a/1679_delete_unused_ref_plane.html>

```csharp
&nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;Return&nbsp;reference&nbsp;to&nbsp;ceiling&nbsp;face&nbsp;to&nbsp;place&nbsp; &nbsp;&nbsp;///&nbsp;lighting&nbsp;fixture&nbsp;above&nbsp;a&nbsp;given&nbsp;point. &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;Reference&nbsp;GetCeilingReferenceAbove(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;View3D&nbsp;view,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;XYZ&nbsp;p&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;ElementClassFilter&nbsp;filter&nbsp;=&nbsp;new&nbsp;ElementClassFilter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;typeof(&nbsp;Ceiling&nbsp;)&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;ReferenceIntersector&nbsp;refIntersector&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ReferenceIntersector(&nbsp;filter,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FindReferenceTarget.Face,&nbsp;view&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;refIntersector.FindReferencesInRevitLinks&nbsp;=&nbsp;true; &nbsp;&nbsp;&nbsp;&nbsp;ReferenceWithContext&nbsp;rwc&nbsp;=&nbsp;refIntersector.FindNearest(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p,&nbsp;XYZ.BasisZ&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;Reference&nbsp;r&nbsp;=&nbsp;(null&nbsp;==&nbsp;rwc)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?&nbsp;null&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;rwc.GetReference(); &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;null&nbsp;==&nbsp;r&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System.Windows.MessageBox.Show(&nbsp;&quot;no&nbsp;intersecting&nbsp;geometry&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;r; &nbsp;&nbsp;}
```

```csharp
&nbsp;&nbsp;void&nbsp;TestGetCeilingReferenceAbove(&nbsp;Document&nbsp;doc&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;View3D&nbsp;view&nbsp;=&nbsp;doc.GetElement(&nbsp;new&nbsp;ElementId(&nbsp;147335&nbsp;)&nbsp;)&nbsp;as&nbsp;View3D; &nbsp;&nbsp;&nbsp;&nbsp;Space&nbsp;space&nbsp;=&nbsp;doc.GetElement(&nbsp;new&nbsp;ElementId(&nbsp;151759&nbsp;)&nbsp;)&nbsp;as&nbsp;Space; &nbsp;&nbsp;&nbsp;&nbsp;XYZ&nbsp;center&nbsp;=&nbsp;(&nbsp;(LocationPoint)&nbsp;space.Location&nbsp;).Point; &nbsp;&nbsp;&nbsp;&nbsp;Reference&nbsp;r&nbsp;=&nbsp;GetCeilingReferenceAbove(&nbsp;view,&nbsp;center&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Populate&nbsp;these&nbsp;as&nbsp;needed: &nbsp;&nbsp;&nbsp;&nbsp;XYZ&nbsp;startPoint&nbsp;=&nbsp;null; &nbsp;&nbsp;&nbsp;&nbsp;FamilySymbol&nbsp;sym&nbsp;=&nbsp;null; &nbsp;&nbsp;&nbsp;&nbsp;doc.Create.NewFamilyInstance(&nbsp;r,&nbsp;startPoint,&nbsp;XYZ.BasisY,&nbsp;sym&nbsp;); &nbsp;&nbsp;}
```
