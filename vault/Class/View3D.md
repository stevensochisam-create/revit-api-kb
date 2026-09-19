---
type: View3D
namespace: Autodesk.Revit.DB
version: 2024
members: 31
tags: [revit-api, class]
---

# View3D

`Autodesk.Revit.DB.View3D` · Revit 2024 · 31 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanResetCameraTarget | 2015 Subscription Update | `public bool CanResetCameraTarget ()` |
| Method | CanSaveOrientation | 2013 | `public bool CanSaveOrientation ()` |
| Method | CanToggleBetweenPerspectiveAndIsometric | 2015 Subscription Update | `public bool CanToggleBetweenPerspectiveAndIsometric ()` |
| Method | CreateIsometric | 2013 | `public static View3D CreateIsometric ( Document document , ElementId viewFamilyTypeId )` |
| Method | CreatePerspective | 2013 | `public static View3D CreatePerspective ( Document document , ElementId viewFamilyTypeId )` |
| Method | GetLevelsThatShowGrids | 2022 | `public ISet < ElementId > GetLevelsThatShowGrids ()` |
| Method | GetOrientation | 2013 | `public ViewOrientation3D GetOrientation ()` |
| Method | GetRenderingSettings | 2013 | `public RenderingSettings GetRenderingSettings ()` |
| Method | GetSavedOrientation | 2013 | `public ViewOrientation3D GetSavedOrientation ()` |
| Method | GetSectionBox | — | `public BoundingBoxXYZ GetSectionBox ()` |
| Method | HasBeenLocked | 2013 | `public bool HasBeenLocked ()` |
| Method | HideGridsOnLevel | 2022 | `public void HideGridsOnLevel ( ElementId levelId )` |
| Method | OrientTo | 2015 | `public void OrientTo ( XYZ forwardDirection )` |
| Method | Print | — | `` |
| Method | ResetCameraTarget | 2015 Subscription Update | `public void ResetCameraTarget ()` |
| Method | RestoreOrientationAndLock | 2013 | `public void RestoreOrientationAndLock ()` |
| Method | SaveOrientation | 2013 | `public void SaveOrientation ()` |
| Method | SaveOrientationAndLock | 2013 | `public void SaveOrientationAndLock ()` |
| Method | SetOrientation | 2013 | `public void SetOrientation ( ViewOrientation3D newViewOrientation3D )` |
| Method | SetRenderingSettings | 2013 | `public void SetRenderingSettings ( RenderingSettings settings )` |
| Method | SetSectionBox | — | `public void SetSectionBox ( BoundingBoxXYZ boundingBoxXYZ )` |
| Method | ShowGridsOnLevel | 2022 | `public void ShowGridsOnLevel ( ElementId levelId )` |
| Method | ShowGridsOnLevels | 2022 | `public void ShowGridsOnLevels ( ISet < ElementId > levelsIds )` |
| Method | ToggleToIsometric | 2015 Subscription Update | `public void ToggleToIsometric ()` |
| Method | ToggleToPerspective | 2015 Subscription Update | `public void ToggleToPerspective ()` |
| Method | Unlock | 2013 | `public void Unlock ()` |
| Property | IsLocked | 2013 | `public bool IsLocked { get ; }` |
| Property | IsPerspective | — | `public bool IsPerspective { get ; }` |
| Property | IsSectionBoxActive | — | `public bool IsSectionBoxActive { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | ProjectGridsOnSectionBox | 2022 | `public bool ProjectGridsOnSectionBox { get ; set ; }` |