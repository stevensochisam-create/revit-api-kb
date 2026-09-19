---
type: ElementTransformUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# ElementTransformUtils

`Autodesk.Revit.DB.ElementTransformUtils` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanMirrorElement | 2012 | `public static bool CanMirrorElement ( Document ADoc , ElementId elemId )` |
| Method | CanMirrorElements | 2012 | `public static bool CanMirrorElements ( Document ADoc , ICollection < ElementId > elemIds )` |
| Method | CopyElement | 2012 | `public static ICollection < ElementId > CopyElement ( Document document , ElementId elementToCopy , XYZ translation )` |
| Method | CopyElements | — | `` |
| Method | GetTransformFromViewToView | 2014 | `public static Transform GetTransformFromViewToView ( View sourceView , View destinationView )` |
| Method | MirrorElement | 2012 | `public static void MirrorElement ( Document document , ElementId elementToMirror , Plane plane )` |
| Method | MirrorElements | 2016 | `public static IList < ElementId > MirrorElements ( Document document , ICollection < ElementId > elementsToMirror , Plane plane , bool mirrorCopies )` |
| Method | MoveElement | 2012 | `public static void MoveElement ( Document document , ElementId elementToMove , XYZ translation )` |
| Method | MoveElements | 2012 | `public static void MoveElements ( Document document , ICollection < ElementId > elementsToMove , XYZ translation )` |
| Method | RotateElement | 2012 | `public static void RotateElement ( Document document , ElementId elementToRotate , Line axis , double angle )` |
| Method | RotateElements | 2012 | `public static void RotateElements ( Document document , ICollection < ElementId > elementsToRotate , Line axis , double angle )` |