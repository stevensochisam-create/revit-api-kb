---
num: 428
date: 2010-08-16
themes: [MEP]
tags: [revit-api, tbc]
---

# Flex Duct Start Tangent

<https://jeremytammik.github.io/tbc/a/0428_flex_duct_start_tangent.htm>

```csharp
&nbsp; FlexDuct flexDuct = doc.Create.NewFlexDuct( &nbsp; &nbsp; points, flexducttype );
```

```csharp
&nbsp; Family fittingFamily &nbsp; &nbsp; = lstElem.Where( e =&gt; e.Name == &quot;M_xyz&quot; ) &nbsp; &nbsp; .Select( e =&gt; e as Family ) &nbsp; &nbsp; .FirstOrDefault(); &nbsp; &nbsp; FamilySymbol fittingType = fittingFamily &nbsp; &nbsp; .Symbols &nbsp; &nbsp; .ToList() &nbsp; &nbsp; .First(); &nbsp; &nbsp; const double fitLen = 1.5; &nbsp; &nbsp; var vectDown &nbsp; &nbsp; = ( samplePoints[1] - samplePoints[0] ) &nbsp; &nbsp; &nbsp; .Normalize(); &nbsp; &nbsp; var fittPos = ptA - vectDown * fitLen; &nbsp; &nbsp; // vectAb is the vector pointing from &nbsp; // ptA(samplePoints[First]) to &nbsp; // ptB(samplePoints[Last]) &nbsp; &nbsp; //&nbsp; remove the z values (as the &nbsp; // flexDuct first tangent do) &nbsp; &nbsp; var vectAbHoriz = new XYZ( vectAb.X, vectAb.Y, 0 ); &nbsp; &nbsp; FamilyInstance fittingInstance &nbsp; &nbsp; = _doc.Create.NewFamilyInstance( &nbsp; &nbsp; &nbsp; fittPos, fittingType, &nbsp; &nbsp; &nbsp; StructuralType.NonStructural ); &nbsp; &nbsp; Line axis2 = _app.Create.NewLine( &nbsp; &nbsp; fittPos, vectDown.CrossProduct( XYZ.BasisZ ), &nbsp; &nbsp; false ); &nbsp; &nbsp; // rotate the fitting to the desired angle &nbsp; &nbsp; bool success = _doc.Rotate( fittingInstance, &nbsp; &nbsp; axis2, -vectDown.AngleTo( vectAbHoriz ) ); &nbsp; &nbsp; SortedList valuePairs = new SortedList(); &nbsp; &nbsp; valuePairs[&quot;xyz 01&quot;] = fitLen; &nbsp; &nbsp; ChangeParametersValue( fittingInstance, valuePairs ); &nbsp; &nbsp; FlexDuct flexDuct2 = CreateDuct( &nbsp; &nbsp; samplePoints, flexDuctType );
```
