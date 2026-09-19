---
type: ElementType
namespace: Autodesk.Revit.DB
version: 2024
members: 11
tags: [revit-api, class]
---

# ElementType

`Autodesk.Revit.DB.ElementType` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Duplicate | — | `public ElementType Duplicate ( string name )` |
| Method | GetPreviewImage | 2011 | `public virtual Bitmap GetPreviewImage ( Size size )` |
| Method | GetSimilarTypes | 2011 | `public ICollection < ElementId > GetSimilarTypes ()` |
| Method | IsSimilarType | 2011 | `public bool IsSimilarType ( ElementId typeId )` |
| Method | IsValidDefaultFamilyType | — | `public bool IsValidDefaultFamilyType ( ElementId familyCategoryId )` |
| Property | CanBeCopied | 2015 | `public bool CanBeCopied { get ; }` |
| Property | CanBeDeleted | 2015 | `public bool CanBeDeleted { get ; }` |
| Property | CanBeRenamed | 2015 | `public bool CanBeRenamed { get ; }` |
| Property | FamilyName | 2015 | `public string FamilyName { get ; }` |
| Property | Name | — | `public override string Name { set ; }` |
| Property | Parameter | — | `` |