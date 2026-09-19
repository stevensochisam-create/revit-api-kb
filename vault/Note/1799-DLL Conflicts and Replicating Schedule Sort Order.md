---
num: 1799
date: 2019-11-19
themes: [Schedule]
tags: [revit-api, tbc]
---

# DLL Conflicts and Replicating Schedule Sort Order

<https://jeremytammik.github.io/tbc/a/1799_dll_hell_schedule_sort.html>

```csharp
&nbsp;&nbsp;ElementCategoryFilter&nbsp;filter&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;ElementCategoryFilter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BuiltInCategory.OST_StructuralColumns&nbsp;); &nbsp;&nbsp;StructuralMaterialTypeFilter&nbsp;filter_mat&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;StructuralMaterialTypeFilter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;StructuralMaterialType.Concrete&nbsp;); &nbsp;&nbsp;IList&lt;Element&gt;&nbsp;columns&nbsp;=&nbsp;collector &nbsp;&nbsp;&nbsp;&nbsp;.WherePasses(&nbsp;filter&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.WherePasses(&nbsp;filter_mat&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;.ToElements(); &nbsp;&nbsp;List&lt;XYZ&gt;&nbsp;locations&nbsp;=&nbsp;new&nbsp;List&lt;XYZ&gt;(); &nbsp;&nbsp;List&lt;string&gt;&nbsp;colmarks&nbsp;=&nbsp;new&nbsp;List&lt;string&gt;(); &nbsp;&nbsp;foreach(&nbsp;Element&nbsp;ele&nbsp;in&nbsp;columns&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;string&nbsp;colmark&nbsp;=&nbsp;ele.get_Parameter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.COLUMN_LOCATION_MARK&nbsp;).AsString(); &nbsp;&nbsp;&nbsp;&nbsp;colmarks.Add(&nbsp;colmark&nbsp;); &nbsp;&nbsp;} &nbsp;&nbsp;colmarks.Sort();
```

```csharp
List&lt;Element&gt;&nbsp;sortedElements&nbsp;=&nbsp;columns &nbsp;&nbsp;.OrderBy(&nbsp;x&nbsp;=&gt;&nbsp;x.get_Parameter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.COLUMN_LOCATION_MARK&nbsp;).AsString()&nbsp;) &nbsp;&nbsp;.ToList();
```

```csharp
List&lt;FamilyInstance&gt;&nbsp;GetSortedColumns(&nbsp;Document&nbsp;doc&nbsp;) { &nbsp;&nbsp;List&lt;FamilyInstance&gt;&nbsp;colums &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfCategory(&nbsp;BuiltInCategory.OST_StructuralColumns&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.OfClass(&nbsp;typeof(&nbsp;FamilyInstance&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.Cast&lt;FamilyInstance&gt;() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.ToList(); &nbsp;&nbsp;colums.Sort(&nbsp;new&nbsp;ColumnMarkComparer()&nbsp;); &nbsp;&nbsp;return&nbsp;colums; }
```

```csharp
public&nbsp;static&nbsp;class&nbsp;Extensions { &nbsp;&nbsp;public&nbsp;static&nbsp;string&nbsp;GetColumnLocationMark(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;this&nbsp;FamilyInstance&nbsp;f&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;Parameter&nbsp;p&nbsp;=&nbsp;f.get_Parameter(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.COLUMN_LOCATION_MARK&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;return(&nbsp;p&nbsp;==&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;?&nbsp;string.Empty &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;p.AsString(); &nbsp;&nbsp;} }
```
