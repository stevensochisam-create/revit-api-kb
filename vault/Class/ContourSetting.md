---
type: ContourSetting
namespace: Autodesk.Revit.DB
version: 2024
members: 9
tags: [revit-api, class]
---

# ContourSetting

`Autodesk.Revit.DB.ContourSetting` · Revit 2024 · 9 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddContourRange | 2024 | `public ContourSettingItem AddContourRange ( double start , double stop , double step , ElementId subcategoryId )` |
| Method | AddSingleContour | 2024 | `public ContourSettingItem AddSingleContour ( double elevation , ElementId subcategoryId )` |
| Method | DisableItem | 2024 | `public void DisableItem ( ContourSettingItem item )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | EnableItem | 2024 | `public void EnableItem ( ContourSettingItem item )` |
| Method | GetContourSettingItems | 2024 | `public IList < ContourSettingItem > GetContourSettingItems ()` |
| Method | GetItemIndex | 2024 | `public int GetItemIndex ( ContourSettingItem item )` |
| Method | RemoveItem | 2024 | `public void RemoveItem ( ContourSettingItem item )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |