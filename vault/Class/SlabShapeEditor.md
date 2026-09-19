---
type: SlabShapeEditor
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# SlabShapeEditor

`Autodesk.Revit.DB.SlabShapeEditor` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateCreasesFromFoldingLines | 2023 | `public void CreateCreasesFromFoldingLines ( Element hostObj , IList < Reference > references )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | DrawPoint | — | `public SlabShapeVertex DrawPoint ( XYZ location )` |
| Method | DrawSplitLine | — | `public SlabShapeCreaseArray DrawSplitLine ( SlabShapeVertex startVertex , SlabShapeVertex endVertex )` |
| Method | Enable | — | `public void Enable ()` |
| Method | ModifySubElement | — | `` |
| Method | PickSupport | — | `public void PickSupport ( Line gLine )` |
| Method | ResetSlabShape | — | `public void ResetSlabShape ()` |
| Property | IsEnabled | — | `public bool IsEnabled { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | SlabShapeCreases | — | `public SlabShapeCreaseArray SlabShapeCreases { get ; }` |
| Property | SlabShapeVertices | — | `public SlabShapeVertexArray SlabShapeVertices { get ; }` |