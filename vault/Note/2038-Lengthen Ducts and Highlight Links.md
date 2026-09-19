---
num: 2038
date: 2024-05-13
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# Lengthen Ducts and Highlight Links

<https://jeremytammik.github.io/tbc/a/2038_highlight_link.html>

```csharp
var linkedFaceReference = UiDoc.Selection.PickObject( Autodesk.Revit.UI.Selection.ObjectType.PointOnElement ); UiDoc.Selection.SetReferences([linkedFaceReference]);
```

```csharp
var pickedReference = UiDoc.Selection.PickObject( Autodesk.Revit.UI.Selection.ObjectType.PointOnElement ); // get Revit link Instance and its document var linkedRvtInstance = Doc.GetElement(pickedReference) as RevitLinkInstance; var linkedDoc = linkedRvtInstance.GetLinkDocument(); //get the Linked element from the linked document var linkedElement = linkedDoc.GetElement(pickedReference.LinkedElementId); // now create a reference from this element // -- this is a reference inside the linked document var reference = new Reference(linkedElement); // convert the reference to be readable from the current document reference = reference.CreateLinkReference(linkedRvtInstance); // now the linked element is highlighted UiDoc.Selection.SetReferences([reference]);
```

```csharp
UIDocument uiDoc = commandData.Application.ActiveUIDocument; Document doc = uiDoc.Document; Reference refer = uiDoc.Selection.PickObject(Autodesk.Revit.UI.Selection.ObjectType.Element); Duct duct = doc.GetElement(refer) as Duct; ///New Length Dimension double newLength = UnitUtils.ConvertToInternalUnits(10000,UnitTypeId.Millimeters); ///Calculating New Length LocationCurve curve = duct.Location as LocationCurve; XYZ p1 = curve.Curve.GetEndPoint(0); XYZ p2 = p1 + ((curve.Curve as Line).Direction * newLength); using (Transaction deleteDuctAndCreateNew = new Transaction(doc, "Delete Existing Duct and Create New")) { deleteDuctAndCreateNew.Start(); //Create New Duct Duct.Create(doc, duct.MEPSystem.GetTypeId(),duct.GetTypeId(), duct.ReferenceLevel.Id, p1, p2); doc.Delete(duct.Id); deleteDuctAndCreateNew.Commit(); }
```

```csharp
var locCurve = ductObject.Location as LocationCurve; locCurve.Curve = extendedCurve;
```

```csharp
Connector connector = getMyConnector(); double extendby = 1; // extend by 1 feet for example XYZ direction = ductCurve.Direction; // assuming the duct is linear curve connector.Origin = connector.Origin + direction * extendby;
```
