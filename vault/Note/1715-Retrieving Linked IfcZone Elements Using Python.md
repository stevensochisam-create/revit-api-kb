---
num: 1715
date: 2019-01-15
themes: [DynamoPython, LinkedModel]
tags: [revit-api, tbc]
---

# Retrieving Linked IfcZone Elements Using Python

<https://jeremytammik.github.io/tbc/a/1715_list_ifc_zones_py.html>

```csharp
import clr import math clr.AddReference('RevitAPI') clr.AddReference('RevitAPIUI') from Autodesk.Revit.DB import * from Autodesk.Revit.DB.Architecture import * from Autodesk.Revit.DB.Analysis import * uidoc = __revit__.ActiveUIDocument doc = __revit__.ActiveUIDocument.Document app = doc.Application docs = app.Documents n = docs.Size print n, 'open documents:' for d in docs: s = d.PathName print s if s.endswith('.ifc.RVT'): ifcdoc = d print 'Linked-in IFC document:' print ifcdoc.PathName collector = FilteredElementCollector(ifcdoc).OfClass(clr.GetClrType(DirectShape)).OfCategory(BuiltInCategory.OST_GenericModel) print collector.GetElementCount(), 'generic model direct shape elements' def get_param(e,s): "Return string parameter value for given parameter name" ps = e.GetParameters(s) n = ps.Count assert(2 > n) if 0 < n: return ps[0].AsString() else: return None def is_zone(e): "Predicate returning True is e is an IfcZone" export_as = get_param(e,'IfcExportAs') return export_as and export_as == 'IfcZone' def zone_name(e): "Return IfcName of IfcZone element or None" if is_zone(e): return get_param(e,'IfcName') zone_names = [] for e in collector: if is_zone(e): zone_names.append(get_param(e,'IfcName')) zone_names.sort() n = len(zone_names) print n, 'zones:', zone_names
```

```csharp
2 open documents: C:\...\test\010-123xx3-arc-bat01-apt01_2_2018-12-27_1507_ifc_link_host.rvt C:\...\010-123xx3-arc-bat01-apt01_2_2018-12-27_1507.ifc.RVT Linked-in IFC document: C:\...\010-123xx3-arc-bat01-apt01_2_2018-12-27_1507.ifc.RVT 1012 generic model direct shape elements 25 zones: ['APT0101', 'APT0102', 'APT0103', 'APT0104', 'APT0105', 'APT0106', 'APT0201', 'APT0202', 'APT0203', ... 'APT0402', 'APT0403', 'APT0404', 'APT0405', 'APT0406', u'Par d\xe9faut:127272']
```
