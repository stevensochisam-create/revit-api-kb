---
type: FilteredElementCollector
namespace: Autodesk.Revit.DB
version: 2024
members: 26
tags: [revit-api, class]
---

# FilteredElementCollector

`Autodesk.Revit.DB.FilteredElementCollector` · Revit 2024 · 26 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | FilteredElementCollector | — | `` |
| Method | ContainedInDesignOption | 2011 | `public FilteredElementCollector ContainedInDesignOption ( ElementId designOptionId )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | Excluding | 2011 | `public FilteredElementCollector Excluding ( ICollection < ElementId > idsToExclude )` |
| Method | FirstElement | 2011 | `public Element FirstElement ()` |
| Method | FirstElementId | 2011 | `public ElementId FirstElementId ()` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetElementCount | 2011 | `public int GetElementCount ()` |
| Method | GetElementIdIterator | 2011 | `public FilteredElementIdIterator GetElementIdIterator ()` |
| Method | GetElementIterator | 2011 | `public FilteredElementIterator GetElementIterator ()` |
| Method | GetEnumerator | — | `public virtual IEnumerator < Element > GetEnumerator ()` |
| Method | IntersectWith | 2011 | `public FilteredElementCollector IntersectWith ( FilteredElementCollector other )` |
| Method | IsViewValidForElementIteration | 2011 | `public static bool IsViewValidForElementIteration ( Document document , ElementId viewId )` |
| Method | OfCategory | — | `public FilteredElementCollector OfCategory ( BuiltInCategory category )` |
| Method | OfCategoryId | 2011 | `public FilteredElementCollector OfCategoryId ( ElementId categoryId )` |
| Method | OfClass | 2011 | `public FilteredElementCollector OfClass ( Type type )` |
| Method | OwnedByView | 2011 | `public FilteredElementCollector OwnedByView ( ElementId viewId )` |
| Method | ToElementIds | 2011 | `public ICollection < ElementId > ToElementIds ()` |
| Method | ToElements | 2011 | `public IList < Element > ToElements ()` |
| Method | UnionWith | 2011 | `public FilteredElementCollector UnionWith ( FilteredElementCollector other )` |
| Method | WhereElementIsCurveDriven | 2011 | `public FilteredElementCollector WhereElementIsCurveDriven ()` |
| Method | WhereElementIsElementType | 2011 | `public FilteredElementCollector WhereElementIsElementType ()` |
| Method | WhereElementIsNotElementType | 2011 | `public FilteredElementCollector WhereElementIsNotElementType ()` |
| Method | WhereElementIsViewIndependent | 2011 | `public FilteredElementCollector WhereElementIsViewIndependent ()` |
| Method | WherePasses | 2011 | `public FilteredElementCollector WherePasses ( ElementFilter filter )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |