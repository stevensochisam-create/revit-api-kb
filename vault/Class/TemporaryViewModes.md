---
type: TemporaryViewModes
namespace: Autodesk.Revit.DB
version: 2024
members: 18
tags: [revit-api, class]
---

# TemporaryViewModes

`Autodesk.Revit.DB.TemporaryViewModes` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | DeactivateAllModes | 2016 Subscription Update | `public void DeactivateAllModes ()` |
| Method | DeactivateMode | 2016 Subscription Update | `public void DeactivateMode ( TemporaryViewMode mode )` |
| Method | GetCaption | 2016 Subscription Update | `public string GetCaption ( TemporaryViewMode mode )` |
| Method | IsCustomized | 2020.1 | `public bool IsCustomized ()` |
| Method | IsModeActive | 2016 Subscription Update | `public bool IsModeActive ( TemporaryViewMode mode )` |
| Method | IsModeAvailable | 2016 Subscription Update | `public bool IsModeAvailable ( TemporaryViewMode mode )` |
| Method | IsModeEnabled | 2016 Subscription Update | `public bool IsModeEnabled ( TemporaryViewMode mode )` |
| Method | IsValidState | 2016 Subscription Update | `public bool IsValidState ( PreviewFamilyVisibilityMode state )` |
| Method | RemoveCustomization | 2020.1 | `public void RemoveCustomization ()` |
| Property | CustomColor | 2020.1 | `public Color CustomColor { get ; set ; }` |
| Property | CustomTitle | 2020.1 | `public string CustomTitle { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | PreviewFamilyVisibility | 2016 Subscription Update | `public PreviewFamilyVisibilityMode PreviewFamilyVisibility { get ; set ; }` |
| Property | PreviewFamilyVisibilityDefaultOnState | 2016 Subscription Update | `public static bool PreviewFamilyVisibilityDefaultOnState { get ; set ; }` |
| Property | PreviewFamilyVisibilityDefaultUncutState | 2016 Subscription Update | `public static bool PreviewFamilyVisibilityDefaultUncutState { get ; set ; }` |
| Property | RevealConstraints | 2016 Subscription Update | `public bool RevealConstraints { get ; set ; }` |
| Property | RevealHiddenElements | 2016 Subscription Update | `public bool RevealHiddenElements { get ; set ; }` |
| Property | WorksharingDisplay | 2016 Subscription Update | `public WorksharingDisplayMode WorksharingDisplay { get ; set ; }` |