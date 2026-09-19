---
type: Category
namespace: Autodesk.Revit.DB
version: 2024
members: 28
tags: [revit-api, class]
---

# Category

`Autodesk.Revit.DB.Category` · Revit 2024 · 28 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | GetBuiltInCategory | 2022 | `public static BuiltInCategory GetBuiltInCategory ( ForgeTypeId categoryTypeId )` |
| Method | GetBuiltInCategoryTypeId | 2022 | `public static ForgeTypeId GetBuiltInCategoryTypeId ( BuiltInCategory categoryId )` |
| Method | GetCategory | — | `` |
| Method | GetGraphicsStyle | — | `public GraphicsStyle GetGraphicsStyle ( GraphicsStyleType graphicsStyleType )` |
| Method | GetHashCode | — | `public override int GetHashCode ()` |
| Method | GetLinePatternId | 2017 | `public ElementId GetLinePatternId ( GraphicsStyleType graphicsStyleType )` |
| Method | GetLineWeight | — | `public Nullable < int > GetLineWeight ( GraphicsStyleType graphicsStyleType )` |
| Method | IsBuiltInCategory | 2022 | `public static bool IsBuiltInCategory ( ForgeTypeId categoryTypeId )` |
| Method | IsBuiltInCategoryValid | 2020 | `public static bool IsBuiltInCategoryValid ( BuiltInCategory builtInCategory )` |
| Method | SetLinePatternId | 2017 | `public void SetLinePatternId ( ElementId linePatternId , GraphicsStyleType graphicsStyleType )` |
| Method | SetLineWeight | — | `public void SetLineWeight ( int lineWeight , GraphicsStyleType graphicsStyleType )` |
| Property | AllowsBoundParameters | — | `public bool AllowsBoundParameters { get ; }` |
| Property | AllowsVisibilityControl | — | `public bool this [ View view ] { get ; }` |
| Property | BuiltInCategory | 2023 | `public BuiltInCategory BuiltInCategory { get ; }` |
| Property | CanAddSubcategory | — | `public bool CanAddSubcategory { get ; }` |
| Property | CategoryType | 2015 | `public CategoryType CategoryType { get ; }` |
| Property | HasMaterialQuantities | — | `public bool HasMaterialQuantities { get ; }` |
| Property | Id | — | `public ElementId Id { get ; }` |
| Property | IsCuttable | — | `public bool IsCuttable { get ; }` |
| Property | IsTagCategory | 2015 | `public bool IsTagCategory { get ; }` |
| Property | IsValid | 2023.1 | `public bool IsValid { get ; }` |
| Property | IsVisibleInUI | 2020 | `public bool IsVisibleInUI { get ; }` |
| Property | LineColor | — | `public Color LineColor { get ; set ; }` |
| Property | Material | — | `public Material Material { get ; set ; }` |
| Property | Name | — | `public string Name { get ; }` |
| Property | Parent | — | `public Category Parent { get ; }` |
| Property | SubCategories | — | `public CategoryNameMap SubCategories { get ; }` |
| Property | Visible | — | `public bool this [ View view ] { get ; set ; }` |