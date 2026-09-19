---
type: UIDocument
namespace: Autodesk.Revit.UI
version: 2024
members: 25
tags: [revit-api, class]
---

# UIDocument

`Autodesk.Revit.UI.UIDocument` · Revit 2024 · 25 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | UIDocument | — | `public UIDocument ( Document document )` |
| Method | CanPlaceElementType | 2015 | `public bool CanPlaceElementType ( ElementType elementType )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetOpenUIViews | — | `public IList < UIView > GetOpenUIViews ()` |
| Method | GetPlacementTypes | 2017 | `public IList < FaceBasedPlacementType > GetPlacementTypes ( FamilySymbol familySymbol , View pDBView )` |
| Method | GetRevitUIFamilyLoadOptions | — | `public static IFamilyLoadOptions GetRevitUIFamilyLoadOptions ()` |
| Method | GetSketchGalleryOptions | 2017 | `public IList < SketchGalleryOptions > GetSketchGalleryOptions ( FamilySymbol familySymbol )` |
| Method | PostRequestForElementTypePlacement | 2015 | `public void PostRequestForElementTypePlacement ( ElementType elementType )` |
| Method | PromptForFamilyInstancePlacement | — | `` |
| Method | PromptToMatchElementType | 2015 | `public void PromptToMatchElementType ( ElementType elementType )` |
| Method | PromptToPlaceElementTypeOnLegendView | 2015 | `public void PromptToPlaceElementTypeOnLegendView ( ElementType elementType )` |
| Method | PromptToPlaceViewOnSheet | 2015 | `public void PromptToPlaceViewOnSheet ( View view , bool allowReplaceExistingSheetViewport )` |
| Method | RefreshActiveView | 2011 | `public void RefreshActiveView ()` |
| Method | RequestViewChange | 2015 | `public void RequestViewChange ( View view )` |
| Method | SaveAndClose | — | `public bool SaveAndClose ()` |
| Method | SaveAs | — | `` |
| Method | SaveAs | — | `public void SaveAs ()` |
| Method | ShowElements | — | `` |
| Method | UpdateAllOpenViews | 2018 | `public void UpdateAllOpenViews ()` |
| Property | ActiveGraphicalView | 2015 | `public View ActiveGraphicalView { get ; }` |
| Property | ActiveView | 2012 | `public View ActiveView { get ; set ; }` |
| Property | Application | — | `public UIApplication Application { get ; }` |
| Property | Document | — | `public Document Document { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Selection | — | `public Selection Selection { get ; }` |