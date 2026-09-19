---
num: 1773
date: 2019-09-02
themes: [Geometry]
tags: [revit-api, tbc]
---

# Face Intersect Face is Unbounded

<https://jeremytammik.github.io/tbc/a/1773_face_intersect_face.html>

```csharp
&nbsp;&nbsp;public&nbsp;Result&nbsp;Execute( &nbsp;&nbsp;&nbsp;&nbsp;ExternalCommandData&nbsp;commandData, &nbsp;&nbsp;&nbsp;&nbsp;ref&nbsp;string&nbsp;message, &nbsp;&nbsp;&nbsp;&nbsp;ElementSet&nbsp;elements&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;list&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;commandData.Application.ActiveUIDocument.Document,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;commandData.View.Id&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Where(&nbsp;e&nbsp;=&gt;&nbsp;e&nbsp;is&nbsp;Wall&nbsp;||&nbsp;e&nbsp;is&nbsp;Floor&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;var&nbsp;f1&nbsp;in&nbsp;list.First() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.get_Geometry(&nbsp;new&nbsp;Options()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfType&lt;Solid&gt;().First() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Faces.OfType&lt;Face&gt;()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;var&nbsp;f2&nbsp;in&nbsp;list.Last() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.get_Geometry(&nbsp;new&nbsp;Options()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfType&lt;Solid&gt;().First() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Faces.OfType&lt;Face&gt;()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;f1.Intersect(&nbsp;f2&nbsp;)&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==&nbsp;FaceIntersectionFaceResult.Intersecting&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;System.Windows.Forms.MessageBox.Show( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;Intersects&quot;,&nbsp;&quot;Continue&quot;, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System.Windows.Forms.MessageBoxButtons.OKCancel, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System.Windows.Forms.MessageBoxIcon.Exclamation&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;==&nbsp;System.Windows.Forms.DialogResult.Cancel&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&
```

```csharp
Floor has 7 faces. Wall has 6 faces. 38 face-face intersections.
```
