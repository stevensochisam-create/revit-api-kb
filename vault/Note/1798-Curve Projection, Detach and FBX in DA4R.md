---
num: 1798
date: 2019-11-12
themes: [Geometry]
tags: [revit-api, tbc]
---

# Curve Projection, Detach and FBX in DA4R

<https://jeremytammik.github.io/tbc/a/1798_da4r_curve_project.html>

```csharp
Autodesk.Revit.Exceptions.WrongUserException: The local file is not owned by the current user, who therefore is not allowed to modify it. at Autodesk.Revit.ApplicationServices.Application.OpenDocumentFile(String fileName) at DesignAutomationFramework.DesignAutomationData..ctor(Application revitApp, String mainModelPath)
```

```csharp
1,0,0,0 0,1,0,0 0,0,0,0 0,0,0,1 // for completeness
```

```csharp
&nbsp;&nbsp;static&nbsp;Curve&nbsp;Project( &nbsp;&nbsp;&nbsp;&nbsp;Autodesk.Revit.DB.NurbSpline&nbsp;nurbsSpline, &nbsp;&nbsp;&nbsp;&nbsp;Autodesk.Revit.DB.Plane&nbsp;plane&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;XYZ[]&nbsp;controlPoints&nbsp;=&nbsp;GeometryHelper.ProjectPoint( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nurbsSpline.CtrlPoints,&nbsp;plane&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;double[]&nbsp;knots&nbsp;=&nbsp;new&nbsp;double[&nbsp;nurbsSpline.Knots.Size&nbsp;]; &nbsp;&nbsp;&nbsp;&nbsp;for(&nbsp;int&nbsp;i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;knots.Length;&nbsp;i++&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;knots[&nbsp;i&nbsp;]&nbsp;=&nbsp;nurbsSpline.Knots.get_Item(&nbsp;i&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;double[]&nbsp;weights&nbsp;=&nbsp;new&nbsp;double[&nbsp;nurbsSpline.Weights.Size&nbsp;]; &nbsp;&nbsp;&nbsp;&nbsp;for(&nbsp;int&nbsp;i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;weights.Length;&nbsp;i++&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weights[&nbsp;i&nbsp;]&nbsp;=&nbsp;nurbsSpline.Weights.get_Item(&nbsp;i&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;NurbSpline.CreateCurve(&nbsp;nurbsSpline.Degree, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;knots,&nbsp;controlPoints,&nbsp;weights&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;static&nbsp;Curve&nbsp;Project( &nbsp;&nbsp;&nbsp;&nbsp;Autodesk.Revit.DB.HermiteSpline&nbsp;hermiteSpline, &nbsp;&nbsp;&nbsp;&nbsp;Autodesk.Revit.DB.Plane&nbsp;plane&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;XYZ[]&nbsp;tangents&nbsp;=&nbsp;GeometryHelper.ProjectVector( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hermiteSpline.Tangents,&nbsp;plane&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;XYZ[]&nbsp;controlPoints&nbsp;=&nbsp;GeometryHelper.ProjectPoint( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hermiteSpline.ControlPoints,&nbsp;plane&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;HermiteSplineTangents&nbsp;hermiteSplineTangents &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;HermiteSplineTangents() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;StartTangent&nbsp;=&nbsp;tangents[&nbsp;0&nbsp;].Normalize(), &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EndTangent&nbsp;=&nbsp;tangents[&nbsp;tangents.Length&nbsp;-&nbsp;1&nbsp;].Normalize() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}; &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;HermiteSpline.Create(&nbsp;
```
