---
num: 291
date: 2010-01-26
themes: [Transaction]
tags: [revit-api, tbc]
---

# Extra Transaction Required

<https://jeremytammik.github.io/tbc/a/0291_extra_transaction.htm>

```csharp
using RvtElement = Autodesk.Revit.Element; using CreationDocument = Autodesk.Revit.Creation.Document; public IExternalCommand.Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) { &nbsp; Application app = commandData.Application; &nbsp; Document doc = app.ActiveDocument; &nbsp; View view = commandData.View; &nbsp; &nbsp; ElementSet elemSet = view.Elements; &nbsp; &nbsp; IEnumerator elementEnumerator &nbsp; &nbsp; = elemSet.ForwardIterator(); &nbsp; &nbsp; while( elementEnumerator.MoveNext() ) &nbsp; { &nbsp; &nbsp; FamilyInstance fi = elementEnumerator.Current &nbsp; &nbsp; &nbsp; as FamilyInstance; &nbsp; &nbsp; &nbsp; if( null != fi ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; CurveArray curves = new CurveArray(); &nbsp; &nbsp; &nbsp; &nbsp; app.ActiveDocument.BeginTransaction(); &nbsp; &nbsp; &nbsp; &nbsp; // set the Vertical Projection &nbsp; &nbsp; &nbsp; &nbsp; Parameter p = fi.get_Parameter( &nbsp; &nbsp; &nbsp; &nbsp; BuiltInParameter.BEAM_V_JUSTIFICATION ); &nbsp; &nbsp; &nbsp; &nbsp; p.Set( 1 ); &nbsp; &nbsp; &nbsp; &nbsp; p = fi.get_Parameter( BuiltInParameter &nbsp; &nbsp; &nbsp; &nbsp; .STRUCTURAL_ANALYTICAL_PROJECT_MEMBER_PLANE ); &nbsp; &nbsp; &nbsp; &nbsp; if( p != null ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; ElementId elemId = p.AsElementId(); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; elemId.Value = -3; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; p.Set( ref elemId ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; // Vertical Projection modification ends here &nbsp; &nbsp; &nbsp; &nbsp; app.ActiveDocument.EndTransaction(); &nbsp; &nbsp; &nbsp; &nbsp; LocationCurve lc = fi.Location as LocationCurve; &nbsp; &nbsp; &nbsp; &nbsp; XYZ pointOnPlane = lc.Curve.get_EndPoint( 0 ); &nbsp; &nbsp; &nbsp; &nbsp; XYZ hostY = fi.FacingOrientation; &nbsp; &nbsp; &nbsp; XYZ hostX = fi.HandOrientation; &nbsp; &nbsp; &nbsp; XYZ hostZ = hostX.Cross( hostY ); &nbsp; &nbsp; &nbsp; &nbsp; curves = CreateRectangle( app, pointOnPlane, &nbsp; &nbsp; &nbsp; &nbsp; hostX, hostZ, 0.5, 0.5 ); &nbsp; &nbsp; &nbsp; &nbsp; Opening opening = doc.Create.NewOpening( fi, &nbsp; &nbsp; &nbsp; &nbsp; curves, CreationDocument.eRefFace.CenterY ); &nbsp; &nbsp; &nbsp; &nbsp; pointOnPlane = lc.Curve.get_EndPoint( 1 ); &nbsp; &nbsp; &nbsp; &nbsp; curves = CreateRectangle( app, pointOnPlane, &nbsp; &nbsp; &nbsp;
```
