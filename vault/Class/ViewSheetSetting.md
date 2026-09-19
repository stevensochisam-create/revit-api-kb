---
type: ViewSheetSetting
namespace: Autodesk.Revit.DB
version: 2024
members: 8
tags: [revit-api, class]
---

# ViewSheetSetting

`Autodesk.Revit.DB.ViewSheetSetting` · Revit 2024 · 8 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Delete | — | `public bool Delete ()` |
| Method | Rename | — | `public bool Rename ( string newName )` |
| Method | Revert | — | `public void Revert ()` |
| Method | Save | — | `public bool Save ()` |
| Method | SaveAs | — | `public bool SaveAs ( string newName )` |
| Property | AvailableViews | — | `public ViewSet AvailableViews { get ; }` |
| Property | CurrentViewSheetSet | — | `public IViewSheetSet CurrentViewSheetSet { get ; set ; }` |
| Property | InSession | — | `public InSessionViewSheetSet InSession { get ; }` |