---
type: SketchEditScope
namespace: Autodesk.Revit.DB
version: 2024
members: 6
tags: [revit-api, class]
---

# SketchEditScope

`Autodesk.Revit.DB.SketchEditScope` · Revit 2024 · 6 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | SketchEditScope | 2022 | `public SketchEditScope ( Document document , string transactionName )` |
| Method | IsElementWithoutSketch | 2023 | `public bool IsElementWithoutSketch ( ElementId elementId )` |
| Method | IsSketchEditingSupported | 2022 | `public bool IsSketchEditingSupported ( ElementId sketchId )` |
| Method | IsSketchEditingSupportedForSketchBasedElement | 2023 | `public bool IsSketchEditingSupportedForSketchBasedElement ( ElementId elemId )` |
| Method | Start | 2022 | `public void Start ( ElementId sketchId )` |
| Method | StartWithNewSketch | 2023 | `public void StartWithNewSketch ( ElementId elementId )` |