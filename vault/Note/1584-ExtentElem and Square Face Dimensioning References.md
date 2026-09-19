---
num: 1584
date: 2017-09-12
themes: [Geometry]
tags: [revit-api, tbc]
---

# ExtentElem and Square Face Dimensioning References

<https://jeremytammik.github.io/tbc/a/1584_dim_inst_face.html>

```csharp
&nbsp;&nbsp;var&nbsp;collector&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;doc,&nbsp;legendView.Id&nbsp;); &nbsp;&nbsp;var&nbsp;elementsIds&nbsp;=&nbsp;collector &nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;.ToElementIds(); &nbsp;&nbsp;ElementTransformUtils.CopyElements(&nbsp;legendView,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;elementsIds,&nbsp;destLegendView,&nbsp;Transform.Identity,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;CopyPasteOptions()&nbsp;);
```

```csharp
&nbsp;&nbsp;var&nbsp;elementsIds&nbsp;=&nbsp;collector &nbsp;&nbsp;&nbsp;&nbsp;.WhereElementIsNotElementType() &nbsp;&nbsp;&nbsp;&nbsp;.Where(&nbsp;x&nbsp;=&gt;&nbsp;x.Category&nbsp;!=&nbsp;null&nbsp;)&nbsp;//&nbsp;I&nbsp;don't&nbsp;want&nbsp;to&nbsp;use&nbsp;name,&nbsp;but&nbsp;I've&nbsp;found&nbsp;that&nbsp;all&nbsp;other&nbsp;use&nbsp;elements&nbsp;in&nbsp;legend&nbsp;view&nbsp;has&nbsp;category &nbsp;&nbsp;&nbsp;&nbsp;.Select(&nbsp;x&nbsp;=&gt;&nbsp;x.Id&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;.ToList();
```

```csharp
# Dynamo import clr clr.AddReference('RevitAPI') clr.AddReference('RevitAPIUI') from Autodesk.Revit.DB import * from Autodesk.Revit.UI import * clr.AddReference("RevitServices") import RevitServices from RevitServices.Persistence import DocumentManager from RevitServices.Transactions import TransactionManager doc = DocumentManager.Instance.CurrentDBDocument uiapp = DocumentManager.Instance.CurrentUIApplication app = uiapp.Application uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument #The inputs to this node will be stored as a list in the IN variables. dataEnteringNode = IN selobject = UnwrapElement(IN[0]) # Object to select #Get user to pick a face selob = uidoc.Selection.PickObject(Selection.ObjectType.PointOnElement, "Pick something now") #Get Id of element thats picked selobid = selob.ElementId #Get element thats picked getob = doc.GetElement(selobid) #Get face thats picked getface = getob.GetGeometryObjectFromReference(selob) #Get edges of face (returns a list the first object is the list of edges) edgeloops = getface.EdgeLoops #Select the first edge dimedge1 = edgeloops[0][0] #Select the third edge (the one opposite the first) dimedge2 = edgeloops[0][2] #Obtain a reference of the first edge edgeref1 = dimedge1.Reference #Obtain a reference of the thord edge edgeref2 = dimedge2.Reference #Assign your output to the OUT variable. OUT = [selob, selobid, getob, getface, edgeloops, dimedge1, dimedge2, edgeref1, edgeref2]
```
