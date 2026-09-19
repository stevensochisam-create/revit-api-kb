---
type: Floor
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# Floor

`Autodesk.Revit.DB.Floor` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | — | `` |
| Method | GetDefaultFloorType | 2022 | `public static ElementId GetDefaultFloorType ( Document document , bool isFoundation )` |
| Method | GetNormalAtVerticalProjectionPoint | — | `public XYZ GetNormalAtVerticalProjectionPoint ( XYZ modelLocation , FloorFace floorFace )` |
| Method | GetSlabShapeEditor | — | `public SlabShapeEditor GetSlabShapeEditor ()` |
| Method | GetSpanDirectionSymbolIds | 2013 | `public ICollection < ElementId > GetSpanDirectionSymbolIds ()` |
| Method | GetVerticalProjectionPoint | — | `public XYZ GetVerticalProjectionPoint ( XYZ modelLocation , FloorFace floorFace )` |
| Property | FloorType | — | `public FloorType FloorType { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | SketchId | 2022 | `public ElementId SketchId { get ; }` |
| Property | SlabShapeEditor | — | `[ ObsoleteAttribute ("This method is deprecated in Revit 2024 and may be removed in a future version of Revit. Use GetSlabShapeEditor() instead.")] public SlabShapeEditor SlabShapeEditor { get ; }` |
| Property | SpanDirectionAngle | — | `public double SpanDirectionAngle { get ; set ; }` |