---
type: SolidSolidCutUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# SolidSolidCutUtils

`Autodesk.Revit.DB.SolidSolidCutUtils` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddCutBetweenSolids | — | `` |
| Method | CanElementCutElement | 2011 | `public static bool CanElementCutElement ( Element cuttingElement , Element cutElement , out CutFailureReason reason )` |
| Method | CutExistsBetweenElements | 2011 | `public static bool CutExistsBetweenElements ( Element first , Element second , out bool firstCutsSecond )` |
| Method | GetCuttingSolids | 2011 | `public static ICollection < ElementId > GetCuttingSolids ( Element element )` |
| Method | GetSolidsBeingCut | 2011 | `public static ICollection < ElementId > GetSolidsBeingCut ( Element element )` |
| Method | IsAllowedForSolidCut | 2011 | `public static bool IsAllowedForSolidCut ( Element element )` |
| Method | IsElementFromAppropriateContext | 2011 | `public static bool IsElementFromAppropriateContext ( Element element )` |
| Method | RemoveCutBetweenSolids | 2011 | `public static void RemoveCutBetweenSolids ( Document document , Element first , Element second )` |
| Method | SplitFacesOfCuttingSolid | 2011 | `public static void SplitFacesOfCuttingSolid ( Element first , Element second , bool split )` |