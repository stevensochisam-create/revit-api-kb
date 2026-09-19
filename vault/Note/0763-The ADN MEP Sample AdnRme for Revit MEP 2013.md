---
num: 763
date: 2012-05-09
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# The ADN MEP Sample AdnRme for Revit MEP 2013

<https://jeremytammik.github.io/tbc/a/0763_adnrme_mep_2013.htm>

```csharp
public Result OnStartup( UIControlledApplication a ) { &nbsp; // only create a new ribbon panel in Revit MEP: &nbsp; &nbsp; ProductType pt = a.ControlledApplication.Product; &nbsp; &nbsp; //if( ProductType.MEP == pt ) // 2012 &nbsp; &nbsp; if( ProductType.MEP == pt &nbsp; &nbsp; || ProductType.Revit == pt ) // 2013 &nbsp; { &nbsp; &nbsp; AddRibbonPanel( a ); &nbsp; &nbsp; return Result.Succeeded; &nbsp; } &nbsp; return Result.Cancelled; }
```
