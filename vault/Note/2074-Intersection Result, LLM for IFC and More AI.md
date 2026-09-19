---
num: 2074
date: 2025-04-15
themes: [Geometry]
tags: [revit-api, tbc]
---

# Intersection Result, LLM for IFC and More AI

<https://jeremytammik.github.io/tbc/a/2074_intersect_result.html>

```csharp
--> Click for animation --> Intersection Result, LLM for IFC and More AI Today, we highlight one pure Revit API related topic, LLMs interacting with AutoCAD and IFC, and lots more AI-related news snippets: IntersectionResult properties LLM interaction with AutoCAD and IFC AI literature and roadmap Vibe coding parody Collapse of critical thinking IDA iterated distillation and amplification training A2A agent-to-agent protocol OpenAI GPT 4.1 + mini + nano IntersectionResult Properties The Revit API Curve Intersect method sports some quirks that prompted explanations in the past. Another one is discussed in the explanation why IntersectionResult parameter getter throws an InvalidOperationException: Question: I check the intersection of 2 line elements. I know for a fact that these 2 lines intersect: SetComparisonResult result = line1.Intersect(line2, out resultArray);
```

```csharp
IntersectionResult intResult = resultArray.get_Item(0);
```

```csharp
results = clr.Reference[DB.IntersectionResultArray]() t = DB.Transaction(doc, "Line Creation") t.Start() lineV = DB.Line.CreateBound(DB.XYZ(0,0,0), DB.XYZ(0,10,0)) lineH = DB.Line.CreateBound(DB.XYZ(-5,5,0), DB.XYZ(5,5,0)) doc.Create.NewDetailCurve(uidoc.ActiveView, lineV) doc.Create.NewDetailCurve(uidoc.ActiveView, lineH) result = lineV.Intersect(lineH, results) intResult = results.get_Item(0) # For example this works print("XYZPoint: {}".format(intResult.XYZPoint)) # But the following all fail print("Distance: {}".format(intResult.Distance)) print("EdgeObject: {}".format(intResult.EdgeObject)) print("EdgeParameter: {}".format(intResult.EdgeParameter)) print("Parameter: {}".format(intResult.Parameter)) t.Commit()
```

```csharp
results = clr.Reference[DB.IntersectionResultArray]() lineV = DB.Line.CreateBound(DB.XYZ(0,0,0), DB.XYZ(0,10,0)) lineH = DB.Line.CreateBound(DB.XYZ(-5,5,0), DB.XYZ(5,5,0)) result = lineV.Intersect(lineH, results) intResult = results.get_Item(0) # For example this works print("XYZPoint: {}".format(intResult.XYZPoint)) # But the following all fail print("Distance: {}".format(intResult.Distance)) print("EdgeObject: {}".format(intResult.EdgeObject)) print("EdgeParameter: {}".format(intResult.EdgeParameter)) print("Parameter: {}".format(intResult.Parameter))
```
