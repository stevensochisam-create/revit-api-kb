---
num: 1919
date: 2021-09-24
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# Snooping Parts, C# Templates and Python Topics

<https://jeremytammik.github.io/tbc/a/1919_py_cs_template.html>

```csharp
from RevitServices.Persistence import DocumentManager doc = DocumentManager.Instance.CurrentDBDocument uiapp = DocumentManager.Instance.CurrentUIApplication uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
```

```csharp
&nbsp;&nbsp;public&nbsp;Result&nbsp;Execute( &nbsp;&nbsp;&nbsp;&nbsp;ExternalCommandData&nbsp;commandData, &nbsp;&nbsp;&nbsp;&nbsp;ref&nbsp;string&nbsp;message, &nbsp;&nbsp;&nbsp;&nbsp;ElementSet&nbsp;elements&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;UIApplication&nbsp;_revit&nbsp;=&nbsp;commandData.Application; &nbsp;&nbsp;&nbsp;&nbsp;UIDocument&nbsp;uidoc&nbsp;=&nbsp;_revit.ActiveUIDocument; &nbsp;&nbsp;&nbsp;&nbsp;Document&nbsp;doc&nbsp;=&nbsp;uidoc.Document; &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;flags&nbsp;=&nbsp;new&nbsp;Dictionary&lt;string,&nbsp;object&gt;()&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{&nbsp;&quot;Frames&quot;,&nbsp;true&nbsp;}, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{&nbsp;&quot;FullFrames&quot;,&nbsp;true&nbsp;}&nbsp;}; &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;py&nbsp;=&nbsp;IronPython.Hosting.Python.CreateEngine(&nbsp;flags&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;scope&nbsp;=&nbsp;IronPython.Hosting.Python.CreateModule(&nbsp;py,&nbsp;&quot;__main__&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;scope.SetVariable(&nbsp;&quot;__commandData__&quot;,&nbsp;commandData&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;add&nbsp;special&nbsp;variable:&nbsp;__revit__&nbsp;to&nbsp;be&nbsp;globally&nbsp;visible&nbsp;everywhere: &nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;builtin&nbsp;=&nbsp;IronPython.Hosting.Python.GetBuiltinModule(&nbsp;py&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;builtin.SetVariable(&nbsp;&quot;__revit__&quot;,&nbsp;_revit&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;py.Runtime.LoadAssembly(&nbsp;typeof(&nbsp;Autodesk.Revit.DB.Document&nbsp;).Assembly&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;py.Runtime.LoadAssembly(&nbsp;typeof(&nbsp;Autodesk.Revit.UI.TaskDialog&nbsp;).Assembly&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;try &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;py.ExecuteFile(&nbsp;&quot;totalSelectedVolume.py&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;catch(&nbsp;Exception&nbsp;ex&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TaskDialog&nbsp;myDialog&nbsp;=&nbsp;new&nbsp;TaskDialog(&nbsp;&quot;IronPython&nbsp;Error&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;myDialog.MainInstruction&nbsp;=&nbsp;&quot;Couldn&#39;t&nbsp;execute&nbsp;IronPython&nbsp;script&nbsp;totalSelectedVolume.py:&nbsp;&quot;; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;myDialog.ExpandedContent&nbsp;=&nbsp;ex.Message; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;myDialog.Show(); &n
```
