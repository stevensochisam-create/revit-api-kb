---
num: 290
date: 2010-01-25
themes: [Geometry]
tags: [revit-api, tbc]
---

# Transformations

<https://jeremytammik.github.io/tbc/a/0290_abg07_transform.htm>

```csharp
protected XYZ GetWindowDirection( FamilyInstance window ) { &nbsp; Options options = new Options(); &nbsp; &nbsp; // Extract the geometry of the window. &nbsp; &nbsp; Autodesk.Revit.Geometry.Element geomElem &nbsp; &nbsp; = window.get_Geometry( options ); &nbsp; &nbsp; foreach( GeometryObject geomObj in geomElem.Objects ) &nbsp; { &nbsp; &nbsp; // We expect there to be one main Instance &nbsp; &nbsp; // in each window.&nbsp; Ignore the rest of the geometry. &nbsp; &nbsp; &nbsp; Instance instance = geomObj as Instance; &nbsp; &nbsp; if( instance != null ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // Obtain the Instance transform and the &nbsp; &nbsp; &nbsp; // nominal facing direction (Y-direction). &nbsp; &nbsp; &nbsp; &nbsp; Transform t = instance.Transform; &nbsp; &nbsp; &nbsp; &nbsp; XYZ facingDirection = t.BasisY; &nbsp; &nbsp; &nbsp; &nbsp; // If the window is flipped in one direction, &nbsp; &nbsp; &nbsp; // but not the other, the transform is left handed.&nbsp; &nbsp; &nbsp; &nbsp; // The Y direction needs to be reversed to &nbsp; &nbsp; &nbsp; // obtain the facing direction. &nbsp; &nbsp; &nbsp; &nbsp; if( ( window.FacingFlipped &amp;&amp; !window.HandFlipped ) &nbsp; &nbsp; &nbsp; &nbsp; || ( !window.FacingFlipped &amp;&amp; window.HandFlipped ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; facingDirection = -facingDirection; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; // Because the need to perform this operation &nbsp; &nbsp; &nbsp; // on instances is so common, the Revit API exposes &nbsp; &nbsp; &nbsp; // this calculation directly as the FacingOrientation &nbsp; &nbsp; &nbsp; // property as shown in GetWindowDirectionAlternate() &nbsp; &nbsp; &nbsp; &nbsp; return facingDirection; &nbsp; &nbsp; } &nbsp; } &nbsp; return XYZ.BasisZ; }
```

```csharp
protected XYZ GetWindowDirectionAlternate( &nbsp; FamilyInstance window ) { &nbsp; return window.FacingOrientation; }
```
