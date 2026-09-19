---
num: 655
date: 2011-09-26
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Python Shell for Revit 2012 and Vasari 2.1

<https://jeremytammik.github.io/tbc/a/0655_python_shell_2012.htm>

```csharp
&gt;&gt;&gt;clr.AddReference('RevitAPI') &nbsp; &gt;&gt;&gt;from Autodesk.Revit.DB import * &nbsp; &gt;&gt;&gt;doc = __revit__.ActiveUIDocument.Document &nbsp; &gt;&gt;&gt;doc.PathName 'C:\\Program Files\\Autodesk\\Revit Architecture 2012 \\Program\\Samples\\rac_basic_sample_project.rvt' &nbsp; &gt;&gt;&gt;iter = doc.WallTypes.ForwardIterator() &nbsp; &gt;&gt;&gt;iter.MoveNext() True &nbsp; &gt;&gt;&gt;wt = iter.Current &nbsp; &gt;&gt;&gt;wt &lt;Autodesk.Revit.DB.WallType object at 0x000000000000002B [Autodesk.Revit.DB.WallType]&gt; &nbsp; &gt;&gt;&gt;wt.Width 1.15625
```
