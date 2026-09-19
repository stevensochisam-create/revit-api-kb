---
num: 2061
date: 2025-01-02
themes: [Units]
tags: [revit-api, tbc]
---

# Back Again to Unit Test, Icons, Viewports and More

<https://jeremytammik.github.io/tbc/a/2061_unittest_viewports.html>

```csharp
// Retrieve all viewport types (family symbols) in the project FilteredElementCollector collector = new FilteredElementCollector(doc) .OfClass(typeof(FamilySymbol)) .OfCategory(BuiltInCategory.OST_ViewportLabel); string targetViewportTypeName = "Title, No Scale, Line"; FamilySymbol targetViewportType = collector .Cast&lt;FamilySymbol&gt;() .FirstOrDefault(fs => fs.Name.Equals(targetViewportTypeName, StringComparison.OrdinalIgnoreCase)); if (targetViewportType == null) { TaskDialog.Show("Error", "The specified viewport type was not found."); return; }
```

```csharp
FilteredElementCollector viewportCollector = new FilteredElementCollector(doc) .OfClass(typeof(Viewport)); using (Transaction trans = new Transaction(doc, "Change Viewport Types")) { try { trans.Start(); foreach (Viewport viewport in viewportCollector.Cast&lt;Viewport&gt;()) { Autodesk.Revit.DB.View view = doc.GetElement(viewport.ViewId) as Autodesk.Revit.DB.View; // Example: Update only viewports associated with Drafting Views if (view != null && view.ViewType == ViewType.DraftingView) { viewport.ChangeTypeId(targetViewportType.Id); } } trans.Commit(); } catch (Exception ex) { trans.RollBack(); TaskDialog.Show("Error", $"An error occurred: {ex.Message}"); } }
```

```csharp
FilteredElementCollector collector = new FilteredElementCollector(doc) .OfClass(typeof(FamilySymbol)) .OfCategory(BuiltInCategory.OST_ViewportLabel); StringBuilder viewportTypeNames = new StringBuilder("Available Viewport Types:\n"); foreach (FamilySymbol type in collector.Cast&lt;FamilySymbol&gt;()) { viewportTypeNames.AppendLine(type.Name); } TaskDialog.Show("Viewport Types", viewportTypeNames.ToString());
```

```csharp
// create filterRule to be used in collection var rule = ParameterFilterRuleFactory.CreateGreaterOrEqualRule( new ElementId(BuiltInParameter.VIEWPORT_ATTR_SHOW_EXTENSION_LINE), 0 ); // define which type name you are looking for var nameRule = ParameterFilterRuleFactory.CreateEqualsRule( new ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME), "Titre sans ligne" ); // get all elements that comply to this rule var viewPortTypes = new FilteredElementCollector(doc) .WhereElementIsElementType() .OfCategory(BuiltInCategory.INVALID) .WherePasses(new ElementParameterFilter(rule)) .WherePasses(new ElementParameterFilter(nameRule)) .ToElementIds(); // should be only one result var viewPortTypeId = viewPortTypes.FirstOrDefault(); if (viewPortTypeId != null) { var vp = ... ; // the viewport you need to change Trans.Start(); vp.ChangeTypeId(viewPortTypeId); Trans.Commit(); }
```
