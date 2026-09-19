---
num: 2001
date: 2023-07-18
themes: [Geometry]
tags: [revit-api, tbc]
---

# Bounding Boxes Axis Alignment and Transformation

<https://jeremytammik.github.io/tbc/a/2001_boundingbox.html>

```csharp
public static List&lt;Parameter&gt; GetBuiltinParameters( Document document) { const BindingFlags bindingFlags = BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.DeclaredOnly; var documentType = typeof(Document); var parameterType = typeof(Parameter); var assembly = Assembly.GetAssembly(parameterType); var aDocumentType = assembly.GetType("ADocument"); var elementIdType = assembly.GetType("ElementId"); var elementIdIdType = elementIdType.GetField("&lt;alignment member&gt;", bindingFlags)!; var getADocumentType = documentType.GetMethod("getADocument", bindingFlags)!; var parameterCtorType = parameterType.GetConstructor(bindingFlags, null, new[] {aDocumentType.MakePointerType(), elementIdType.MakePointerType()}, null)!; var builtinParameters = Enum.GetValues(typeof(BuiltInParameter)); var parameters = new List&lt;Parameter&gt;(builtinParameters.Length); foreach (BuiltInParameter builtinParameter in builtinParameters) { var elementId = Activator.CreateInstance(elementIdType); elementIdIdType.SetValue(elementId, builtinParameter); var handle = GCHandle.Alloc(elementId); var elementIdPointer = GCHandle.ToIntPtr(handle); Marshal.StructureToPtr(elementId, elementIdPointer, true); var parameter = (Parameter) parameterCtorType.Invoke( new[] {getADocumentType.Invoke(document, null), elementIdPointer}); parameters.Add(parameter); handle.Free(); } return parameters; }
```

```csharp
public static List&lt;Category&gt; GetBuiltinCategories( Document document) { const BindingFlags bindingFlags = BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.DeclaredOnly; var documentType = typeof(Document); var categoryType = typeof(Category); var assembly = Assembly.GetAssembly(categoryType); var aDocumentType = assembly.GetType("ADocument"); var elementIdType = assembly.GetType("ElementId"); var elementIdIdType = elementIdType.GetField("&lt;alignment member&gt;", bindingFlags)!; var getADocumentType = documentType.GetMethod("getADocument", bindingFlags)!; var categoryCtorType = categoryType.GetConstructor(bindingFlags, null, new[] {aDocumentType.MakePointerType(), elementIdType.MakePointerType()}, null)!; var builtInCategories = Enum.GetValues(typeof(BuiltInCategory)); var categories = new List&lt;Category&gt;(builtInCategories.Length); foreach (BuiltInCategory builtInCategory in builtInCategories) { var elementId = Activator.CreateInstance(elementIdType); elementIdIdType.SetValue(elementId, builtInCategory); var handle = GCHandle.Alloc(elementId); var elementIdPointer = GCHandle.ToIntPtr(handle); Marshal.StructureToPtr(elementId, elementIdPointer, true); var category = (Category) categoryCtorType.Invoke( new[] {getADocumentType.Invoke(document, null), elementIdPointer}); categories.Add(category); handle.Free(); } return categories; }
```

```csharp
# get the elements bounding box s_BBox = element.get_BoundingBox(doc.ActiveView) # apply the link documents transform s_BBox_min = link_trans.OfPoint(s_BBox.Min) s_BBox_max = link_trans.OfPoint(s_BBox.Max) # make the outline new_outline = Outline(s_BBox_min, s_BBox_max) # make the filter bb_filter = BoundingBoxIntersectsFilter(new_outline)
```

```csharp
/// &lt;summary&gt; /// Expand the given bounding box to include /// and contain the given point. /// &lt;/summary&gt; public static void ExpandToContain( this BoundingBoxXYZ bb, XYZ p) { bb.Min = new XYZ(Math.Min(bb.Min.X, p.X), Math.Min(bb.Min.Y, p.Y), Math.Min(bb.Min.Z, p.Z)); bb.Max = new XYZ(Math.Max(bb.Max.X, p.X), Math.Max(bb.Max.Y, p.Y), Math.Max(bb.Max.Z, p.Z)); }
```
