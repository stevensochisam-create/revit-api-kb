---
type: PartUtils
namespace: Autodesk.Revit.DB
version: 2024
members: 18
tags: [revit-api, class]
---

# PartUtils

`Autodesk.Revit.DB.PartUtils` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreElementsValidForCreateParts | 2012 | `public static bool AreElementsValidForCreateParts ( Document document , ICollection < ElementId > elementIds )` |
| Method | ArePartsValidForDivide | 2013 | `public static bool ArePartsValidForDivide ( Document document , ICollection < ElementId > elementIdsToDivide )` |
| Method | ArePartsValidForMerge | 2013 | `public static bool ArePartsValidForMerge ( Document document , ICollection < ElementId > partIds )` |
| Method | CreateMergedPart | 2013 | `public static PartMaker CreateMergedPart ( Document document , ICollection < ElementId > partIds )` |
| Method | CreateParts | — | `` |
| Method | DivideParts | 2012 | `public static PartMaker DivideParts ( Document document , ICollection < ElementId > elementIdsToDivide , ICollection < ElementId > intersectingReferenceIds , IList < Curve > curveArray , ElementId sketchPlaneId )` |
| Method | FindMergeableClusters | 2013 | `public static IList < ICollection < ElementId >> FindMergeableClusters ( Document doc , ICollection < ElementId > partIds )` |
| Method | GetAssociatedPartMaker | — | `` |
| Method | GetAssociatedParts | — | `` |
| Method | GetChainLengthToOriginal | 2013 | `public static int GetChainLengthToOriginal ( Part part )` |
| Method | GetMergedParts | 2013 | `public static ICollection < ElementId > GetMergedParts ( Part part )` |
| Method | GetPartMakerMethodToDivideVolumeFW | 2013 | `public static PartMakerMethodToDivideVolumes GetPartMakerMethodToDivideVolumeFW ( PartMaker partMaker )` |
| Method | GetSplittingCurves | — | `` |
| Method | GetSplittingElements | 2019.1 | `public static ISet < ElementId > GetSplittingElements ( Document document , ElementId partId )` |
| Method | HasAssociatedParts | — | `` |
| Method | IsMergedPart | 2013 | `public static bool IsMergedPart ( Part part )` |
| Method | IsPartDerivedFromLink | 2013 | `public static bool IsPartDerivedFromLink ( Part dPart )` |
| Method | IsValidForCreateParts | 2013 | `public static bool IsValidForCreateParts ( Document document , LinkElementId hostOrLinkElementId )` |