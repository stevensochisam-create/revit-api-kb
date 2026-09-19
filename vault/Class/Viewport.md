---
type: Viewport
namespace: Autodesk.Revit.DB
version: 2024
members: 16
tags: [revit-api, class]
---

# Viewport

`Autodesk.Revit.DB.Viewport` · Revit 2024 · 16 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanAddViewToSheet | 2013 | `public static bool CanAddViewToSheet ( Document document , ElementId viewSheetId , ElementId viewId )` |
| Method | Create | 2013 | `public static Viewport Create ( Document document , ElementId viewSheetId , ElementId viewId , XYZ point )` |
| Method | GetBoxCenter | 2014 | `public XYZ GetBoxCenter ()` |
| Method | GetBoxOutline | 2013 | `public Outline GetBoxOutline ()` |
| Method | GetLabelOutline | 2013 | `public Outline GetLabelOutline ()` |
| Method | GetProjectionToSheetTransform | 2023 | `public Transform GetProjectionToSheetTransform ()` |
| Method | HasViewportTransforms | 2023 | `public bool HasViewportTransforms ()` |
| Method | IsViewIdValidForViewport | 2023 | `public bool IsViewIdValidForViewport ( ElementId viewId )` |
| Method | SetBoxCenter | 2014 | `public void SetBoxCenter ( XYZ newCenterPoint )` |
| Property | LabelLineLength | 2022 | `public double LabelLineLength { get ; set ; }` |
| Property | LabelOffset | 2022 | `public XYZ LabelOffset { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | Rotation | 2014 | `public ViewportRotation Rotation { get ; set ; }` |
| Property | SheetId | 2013 | `public ElementId SheetId { get ; }` |
| Property | ViewId | 2013 | `public ElementId ViewId { get ; set ; }` |
| Property | ViewportPositioning | 2023 | `public ViewportPositioning ViewportPositioning { get ; set ; }` |