---
type: View
namespace: Autodesk.Revit.DB
version: 2024
members: 139
tags: [revit-api, class]
---

# View

`Autodesk.Revit.DB.View` · Revit 2024 · 139 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddFilter | 2014 | `public void AddFilter ( ElementId filterElementId )` |
| Method | AllowsAnalysisDisplay | 2015 | `public bool AllowsAnalysisDisplay ()` |
| Method | ApplyViewTemplateParameters | 2013 | `public void ApplyViewTemplateParameters ( View otherView )` |
| Method | AreGraphicsOverridesAllowed | — | `public bool AreGraphicsOverridesAllowed ()` |
| Method | CanApplyColorFillScheme | 2022 | `public bool CanApplyColorFillScheme ( ElementId categoryId , ElementId schemeId )` |
| Method | CanCategoryBeHidden | 2014 | `public bool CanCategoryBeHidden ( ElementId elementId )` |
| Method | CanCategoryBeHiddenTemporary | 2013 | `public bool CanCategoryBeHiddenTemporary ( ElementId elementId )` |
| Method | CanEnableTemporaryViewPropertiesMode | 2014 | `public bool CanEnableTemporaryViewPropertiesMode ()` |
| Method | CanModifyDetailLevel | 2013 | `public bool CanModifyDetailLevel ()` |
| Method | CanModifyDisplayStyle | 2013 | `public bool CanModifyDisplayStyle ()` |
| Method | CanModifyViewDiscipline | 2013 | `public bool CanModifyViewDiscipline ()` |
| Method | CanUseDepthCueing | 2017 | `public bool CanUseDepthCueing ()` |
| Method | CanUseTemporaryVisibilityModes | 2013 | `public bool CanUseTemporaryVisibilityModes ()` |
| Method | CanViewBeDuplicated | 2013 | `public bool CanViewBeDuplicated ( ViewDuplicateOption duplicateOption )` |
| Method | ConvertTemporaryHideIsolateToPermanent | 2013 | `public void ConvertTemporaryHideIsolateToPermanent ()` |
| Method | ConvertToIndependent | 2016 | `public void ConvertToIndependent ()` |
| Method | CreateViewTemplate | 2020 | `public View CreateViewTemplate ()` |
| Method | DisableTemporaryViewMode | 2013 | `public void DisableTemporaryViewMode ( TemporaryViewMode mode )` |
| Method | Duplicate | 2013 | `public ElementId Duplicate ( ViewDuplicateOption duplicateOption )` |
| Method | EnableRevealHiddenMode | 2013 | `public void EnableRevealHiddenMode ()` |
| Method | EnableTemporaryViewPropertiesMode | 2014 | `public bool EnableTemporaryViewPropertiesMode ( ElementId viewTemplateId )` |
| Method | GetBackground | 2014 | `public ViewDisplayBackground GetBackground ()` |
| Method | GetCalloutParentId | 2022 | `public ElementId GetCalloutParentId ()` |
| Method | GetCategoryHidden | 2017 | `public bool GetCategoryHidden ( ElementId categoryId )` |
| Method | GetCategoryOverrides | 2014 | `public OverrideGraphicSettings GetCategoryOverrides ( ElementId categoryId )` |
| Method | GetColorFillSchemeId | 2022 | `public ElementId GetColorFillSchemeId ( ElementId categoryId )` |
| Method | GetCropRegionShapeManager | 2014 | `public ViewCropRegionShapeManager GetCropRegionShapeManager ()` |
| Method | GetCropRegionShapeManagerForReferenceCallout | 2014 | `public static ViewCropRegionShapeManager GetCropRegionShapeManagerForReferenceCallout ( Document doc , ElementId callout )` |
| Method | GetDependentViewIds | 2013 | `public ICollection < ElementId > GetDependentViewIds ()` |
| Method | GetDepthCueing | 2017 | `public ViewDisplayDepthCueing GetDepthCueing ()` |
| Method | GetDirectContext3DHandleOverrides | 2018 | `public DirectContext3DHandleOverrides GetDirectContext3DHandleOverrides ()` |
| Method | GetElementOverrides | 2014 | `public OverrideGraphicSettings GetElementOverrides ( ElementId elementId )` |
| Method | GetFilterOverrides | 2014 | `public OverrideGraphicSettings GetFilterOverrides ( ElementId filterElementId )` |
| Method | GetFilterVisibility | 2014 | `public bool GetFilterVisibility ( ElementId filterElementId )` |
| Method | GetFilters | 2014 | `public ICollection < ElementId > GetFilters ()` |
| Method | GetIsFilterEnabled | 2021 | `public bool GetIsFilterEnabled ( ElementId filterElementId )` |
| Method | GetLinkOverrides | 2024 | `public RevitLinkGraphicsSettings GetLinkOverrides ( ElementId linkId )` |
| Method | GetModelToProjectionTransforms | 2023 | `public IList < TransformWithBoundary > GetModelToProjectionTransforms ()` |
| Method | GetNonControlledTemplateParameterIds | 2013 | `public ICollection < ElementId > GetNonControlledTemplateParameterIds ()` |
| Method | GetOrderedFilters | 2021 | `public IList < ElementId > GetOrderedFilters ()` |
| Method | GetPlacementOnSheetStatus | 2023 | `public ViewPlacementOnSheetStatus GetPlacementOnSheetStatus ()` |
| Method | GetPointCloudOverrides | 2014 | `public PointCloudOverrides GetPointCloudOverrides ()` |
| Method | GetPrimaryViewId | 2013 | `public ElementId GetPrimaryViewId ()` |
| Method | GetReferenceCallouts | 2014 | `public ICollection < ElementId > GetReferenceCallouts ()` |
| Method | GetReferenceElevations | 2014 | `public ICollection < ElementId > GetReferenceElevations ()` |
| Method | GetReferenceSections | 2014 | `public ICollection < ElementId > GetReferenceSections ()` |
| Method | GetSketchyLines | 2015 | `public ViewDisplaySketchyLines GetSketchyLines ()` |
| Method | GetTemplateParameterIds | 2013 | `public IList < ElementId > GetTemplateParameterIds ()` |
| Method | GetTemporaryViewPropertiesId | 2014 | `public ElementId GetTemporaryViewPropertiesId ()` |
| Method | GetTemporaryViewPropertiesName | 2014 | `public string GetTemporaryViewPropertiesName ()` |
| Method | GetViewDisplayModel | 2015 | `public ViewDisplayModel GetViewDisplayModel ()` |
| Method | GetWorksetVisibility | 2012 | `public WorksetVisibility GetWorksetVisibility ( WorksetId worksetId )` |
| Method | GetWorksharingDisplayMode | — | `public WorksharingDisplayMode GetWorksharingDisplayMode ()` |
| Method | HasDetailLevel | 2013 | `public bool HasDetailLevel ()` |
| Method | HasDisplayStyle | 2013 | `public bool HasDisplayStyle ()` |
| Method | HasViewDiscipline | 2013 | `public bool HasViewDiscipline ()` |
| Method | HasViewTransforms | 2023 | `public bool HasViewTransforms ()` |
| Method | HideActiveWorkPlane | 2011 | `public void HideActiveWorkPlane ()` |
| Method | HideCategoriesTemporary | 2013 | `public void HideCategoriesTemporary ( ICollection < ElementId > elementIds )` |
| Method | HideCategoryTemporary | 2013 | `public void HideCategoryTemporary ( ElementId elementId )` |
| Method | HideElementTemporary | 2013 | `public void HideElementTemporary ( ElementId elementId )` |
| Method | HideElements | — | `public void HideElements ( ICollection < ElementId > elementIdSet )` |
| Method | HideElementsTemporary | 2013 | `public void HideElementsTemporary ( ICollection < ElementId > elementIdSet )` |
| Method | IsCategoryOverridable | 2014 | `public bool IsCategoryOverridable ( ElementId categoryId )` |
| Method | IsElementVisibleInTemporaryViewMode | 2012 | `public bool IsElementVisibleInTemporaryViewMode ( TemporaryViewMode mode , ElementId id )` |
| Method | IsFilterApplied | 2014 | `public bool IsFilterApplied ( ElementId filterElementId )` |
| Method | IsInTemporaryViewMode | 2012 | `public bool IsInTemporaryViewMode ( TemporaryViewMode mode )` |
| Method | IsTemporaryHideIsolateActive | 2013 | `public bool IsTemporaryHideIsolateActive ()` |
| Method | IsTemporaryViewPropertiesModeEnabled | 2014 | `public bool IsTemporaryViewPropertiesModeEnabled ()` |
| Method | IsValidViewScale | — | `public static bool IsValidViewScale ( int viewScale )` |
| Method | IsValidViewTemplate | 2013 | `public bool IsValidViewTemplate ( ElementId templateId )` |
| Method | IsViewValidForTemplateCreation | 2020 | `public bool IsViewValidForTemplateCreation ()` |
| Method | IsWorksetVisible | 2012 | `public bool IsWorksetVisible ( WorksetId worksetId )` |
| Method | IsolateCategoriesTemporary | 2013 | `public void IsolateCategoriesTemporary ( ICollection < ElementId > elementIds )` |
| Method | IsolateCategoryTemporary | 2013 | `public void IsolateCategoryTemporary ( ElementId elementId )` |
| Method | IsolateElementTemporary | 2013 | `public void IsolateElementTemporary ( ElementId elementId )` |
| Method | IsolateElementsTemporary | 2013 | `public void IsolateElementsTemporary ( ICollection < ElementId > elementIds )` |
| Method | Print | — | `` |
| Method | Print | — | `public void Print ()` |
| Method | RemoveCalloutParent | — | `public void RemoveCalloutParent ()` |
| Method | RemoveFilter | 2014 | `public void RemoveFilter ( ElementId filterElementId )` |
| Method | RemoveLinkOverrides | 2024 | `public void RemoveLinkOverrides ( ElementId linkId )` |
| Method | RestoreCalloutParent | — | `public void RestoreCalloutParent ()` |
| Method | SetBackground | 2014 | `public void SetBackground ( ViewDisplayBackground background )` |
| Method | SetCategoryHidden | 2017 | `public void SetCategoryHidden ( ElementId categoryId , bool hide )` |
| Method | SetCategoryOverrides | 2014 | `public void SetCategoryOverrides ( ElementId categoryId , OverrideGraphicSettings overrideGraphicSettings )` |
| Method | SetColorFillSchemeId | 2022 | `public void SetColorFillSchemeId ( ElementId categoryId , ElementId schemeId )` |
| Method | SetDepthCueing | 2017 | `public void SetDepthCueing ( ViewDisplayDepthCueing depthCueing )` |
| Method | SetElementOverrides | 2014 | `public void SetElementOverrides ( ElementId elementId , OverrideGraphicSettings overrideGraphicSettings )` |
| Method | SetFilterOverrides | 2014 | `public void SetFilterOverrides ( ElementId filterElementId , OverrideGraphicSettings overrideGraphicSettings )` |
| Method | SetFilterVisibility | 2014 | `public void SetFilterVisibility ( ElementId filterElementId , bool visibility )` |
| Method | SetIsFilterEnabled | 2021 | `public void SetIsFilterEnabled ( ElementId filterElementId , bool enable )` |
| Method | SetLinkOverrides | 2024 | `public void SetLinkOverrides ( ElementId linkId , RevitLinkGraphicsSettings linkDisplaySettings )` |
| Method | SetNonControlledTemplateParameterIds | 2013 | `public void SetNonControlledTemplateParameterIds ( ICollection < ElementId > newSet )` |
| Method | SetSketchyLines | 2015 | `public void SetSketchyLines ( ViewDisplaySketchyLines sketchyLines )` |
| Method | SetViewDisplayModel | 2015 | `public void SetViewDisplayModel ( ViewDisplayModel viewDisplayModel )` |
| Method | SetWorksetVisibility | 2012 | `public void SetWorksetVisibility ( WorksetId worksetId , WorksetVisibility visible )` |
| Method | SetWorksharingDisplayMode | — | `public void SetWorksharingDisplayMode ( WorksharingDisplayMode displayMode )` |
| Method | ShowActiveWorkPlane | 2011 | `public void ShowActiveWorkPlane ()` |
| Method | SupportedColorFillCategoryIds | 2022 | `public ICollection < ElementId > SupportedColorFillCategoryIds ()` |
| Method | SupportsRevealConstraints | 2016 | `public bool SupportsRevealConstraints ()` |
| Method | SupportsWorksharingDisplayMode | — | `public bool SupportsWorksharingDisplayMode ( WorksharingDisplayMode mode )` |
| Method | UnhideElements | — | `public void UnhideElements ( ICollection < ElementId > elementIdSet )` |
| Property | AnalysisDisplayStyleId | 2011 | `public ElementId AnalysisDisplayStyleId { get ; set ; }` |
| Property | AreAnalyticalModelCategoriesHidden | 2014 | `public bool AreAnalyticalModelCategoriesHidden { get ; set ; }` |
| Property | AreAnnotationCategoriesHidden | 2014 | `public bool AreAnnotationCategoriesHidden { get ; set ; }` |
| Property | AreCoordinationModelHandlesHidden | 2018 | `public bool AreCoordinationModelHandlesHidden { get ; set ; }` |
| Property | AreImportCategoriesHidden | 2014 | `public bool AreImportCategoriesHidden { get ; set ; }` |
| Property | AreModelCategoriesHidden | 2014 | `public bool AreModelCategoriesHidden { get ; set ; }` |
| Property | ArePointCloudsHidden | 2014 | `public bool ArePointCloudsHidden { get ; set ; }` |
| Property | AssociatedAssemblyInstanceId | — | `public ElementId AssociatedAssemblyInstanceId { get ; }` |
| Property | CanBePrinted | — | `public bool CanBePrinted { get ; }` |
| Property | CropBox | — | `public BoundingBoxXYZ CropBox { get ; set ; }` |
| Property | CropBoxActive | — | `public bool CropBoxActive { get ; set ; }` |
| Property | CropBoxVisible | — | `public bool CropBoxVisible { get ; set ; }` |
| Property | DetailLevel | 2013 | `public ViewDetailLevel DetailLevel { get ; set ; }` |
| Property | Discipline | 2013 | `public ViewDiscipline Discipline { get ; set ; }` |
| Property | DisplayStyle | 2013 | `public DisplayStyle DisplayStyle { get ; set ; }` |
| Property | GenLevel | — | `public Level GenLevel { get ; }` |
| Property | IsAssemblyView | 2015 | `public bool IsAssemblyView { get ; }` |
| Property | IsCallout | 2022 | `public bool IsCallout { get ; }` |
| Property | IsTemplate | 2011 | `public bool IsTemplate { get ; }` |
| Property | Origin | — | `public XYZ Origin { get ; }` |
| Property | Outline | — | `public BoundingBoxUV Outline { get ; }` |
| Property | Parameter | — | `` |
| Property | PartsVisibility | — | `public PartsVisibility PartsVisibility { get ; set ; }` |
| Property | RevealConstraintsMode | 2016 | `public bool RevealConstraintsMode { get ; set ; }` |
| Property | RightDirection | — | `public XYZ RightDirection { get ; }` |
| Property | Scale | — | `public int Scale { get ; set ; }` |
| Property | ShadowIntensity | 2014 | `public int ShadowIntensity { get ; set ; }` |
| Property | SketchPlane | — | `public SketchPlane SketchPlane { get ; set ; }` |
| Property | SunAndShadowSettings | 2011 | `public SunAndShadowSettings SunAndShadowSettings { get ; }` |
| Property | SunlightIntensity | 2014 | `public int SunlightIntensity { get ; set ; }` |
| Property | TemporaryViewModes | 2016 Subscription Update | `public TemporaryViewModes TemporaryViewModes { get ; }` |
| Property | Title | 2015 | `public string Title { get ; }` |
| Property | UpDirection | — | `public XYZ UpDirection { get ; }` |
| Property | ViewDirection | — | `public XYZ ViewDirection { get ; }` |
| Property | ViewTemplateId | 2013 | `public ElementId ViewTemplateId { get ; set ; }` |
| Property | ViewType | — | `public ViewType ViewType { get ; }` |