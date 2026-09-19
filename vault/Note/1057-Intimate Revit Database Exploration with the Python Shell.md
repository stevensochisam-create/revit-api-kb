---
num: 1057
date: 2013-11-13
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Intimate Revit Database Exploration with the Python Shell

<https://jeremytammik.github.io/tbc/a/1057_db_explor_python_sh.htm>

```csharp
print "Path:", doc.PathName if doc.GetWorksharingCentralModelPath() != None: print "Central model path:", ModelPathUtils.ConvertModelPathToUserVisiblePath(doc.GetWorksharingCentralModelPath()) else: print "The project is not work-sharing" print dir(uidoc) for elem in selection: print elem, elem.Id
```

```csharp
# these commands get executed in the current scope # of each new shell (but not for canned commands) import clr clr.AddReference('RevitAPI') clr.AddReference('RevitAPIUI') from Autodesk.Revit.DB import * from Autodesk.Revit.DB.Architecture import * from Autodesk.Revit.DB.Analysis import * uidoc = __revit__.ActiveUIDocument doc = __revit__.ActiveUIDocument.Document selection = list(__revit__.ActiveUIDocument.Selection.Elements) ...
```

```csharp
collector = FilteredElementCollector(doc) linkedElements = collector .OfClass(RevitLinkType).ToElements() for elem in linkedElements: efr = elem.GetExternalFileReference() print ModelPathUtils.ConvertModelPathToUserVisiblePath( efr.GetAbsolutePath()) print "---------"
```

```csharp
worksets = FilteredWorksetCollector( doc ) worksets.OfKind( WorksetKind.UserWorkset ); for elem in worksets: print elem.Name
```

```csharp
def FindElementsByWorkset(wId): worksetI = int(BuiltInParameter.ELEM_PARTITION_PARAM) # convert enumeration element to an integer worksetE = ElementId(worksetI) # and create element id from it provider = ParameterValueProvider(worksetE) # the parameter should be BuiltInParameter.ELEM_PARTITION_PARAM evaluator = FilterNumericEquals() # the value should be equal rule = FilterIntegerRule(provider, evaluator, wId) # to wId parafilter = ElementParameterFilter(rule); # create filter parameter collector = FilteredElementCollector(doc) # create collector collector.WherePasses(parafilter) # and filter elements # iterate through the elements for elem in collector: print "\t", elem.Id, elem.GetType().Name
```
