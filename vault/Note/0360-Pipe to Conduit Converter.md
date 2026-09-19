---
num: 360
date: 2010-05-07
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# Pipe to Conduit Converter

<https://jeremytammik.github.io/tbc/a/0360_p2c.htm>

```csharp
#region Namespaces using System; using System.Diagnostics; using System.Collections.Generic; using Autodesk.Revit.Attributes; using Autodesk.Revit.DB; using Autodesk.Revit.DB.Electrical; using Autodesk.Revit.DB.Plumbing; using Autodesk.Revit.UI; using Autodesk.Revit.UI.Selection; using InvalidOperationException &nbsp; = Autodesk.Revit.Exceptions &nbsp; &nbsp; .InvalidOperationException; #endregion // Namespaces
```

```csharp
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt; &lt;RevitAddIn&gt; &nbsp; &lt;AddIn Type=&quot;Command&quot;&gt; &nbsp; &nbsp; &lt;Text&gt;Convert Pipes to Conduits&lt;/Text&gt; &nbsp; &nbsp; &lt;Description&gt;Convert Pipes to Conduits&lt;/Description&gt; &nbsp; &nbsp; &lt;Assembly&gt;C:\src\p2c\p2c\bin\Debug\p2c.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;FullClassName&gt;p2c.Command&lt;/FullClassName&gt; &nbsp; &nbsp; &lt;ClientId&gt;835d6ad1-1a99-4039-95dc-e752ff635928&lt;/ClientId&gt; &nbsp; &lt;/AddIn&gt; &lt;/RevitAddIn&gt;
```

```csharp
&nbsp; [Transaction(TransactionMode.Automatic)] &nbsp; [Regeneration(RegenerationOption.Manual)] &nbsp; public class Command : IExternalCommand &nbsp; { &nbsp; &nbsp; public Result Execute( &nbsp; &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; &nbsp; ref string message, &nbsp; &nbsp; &nbsp; ElementSet elements ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Result result = Result.Failed; &nbsp; &nbsp; &nbsp; &nbsp; UIApplication app = commandData.Application; &nbsp; &nbsp; &nbsp; UIDocument uidoc = app.ActiveUIDocument; &nbsp; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; &nbsp; try &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; // ... main implementation goes here ... &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; result = Result.Succeeded; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; catch( InvalidOperationException ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; // selection cancelled &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; result = Result.Cancelled; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; catch( Exception ex ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; // if any error occurs, display error &nbsp; &nbsp; &nbsp; &nbsp; // information and return failed &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; message = ex.Message; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; return result; &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; const string _caption = &quot;Pipe to Conduit Converter&quot;; &nbsp; &nbsp; #region Formatting and message handlers &nbsp; /// &lt;summary&gt; &nbsp; /// MessageBox or Revit TaskDialog &nbsp; /// wrapper for informational message. &nbsp; /// &lt;/summary&gt; &nbsp; public static void InfoMsg( string msg ) &nbsp; { &nbsp; &nbsp; Debug.WriteLine( msg ); &nbsp; &nbsp; &nbsp; TaskDialog.Show( _caption, msg, &nbsp; &nbsp; &nbsp; TaskDialogCommonButtons.Ok ); &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// MessageBox or Revit TaskDialog &nbsp; /// wrapper for error message. &nbsp; /// &lt;/summary&gt; &nbsp; public static void ErrorMsg( string msg ) &nbsp; { &nbsp; &nbsp; Debug.WriteLine( msg ); &nbsp; &nbsp; &nbsp; TaskDialog d = new TaskDialog( _caption ); &nbsp; &nbsp; d.MainIcon = TaskDialogIcon.TaskDialogIconWarning; &nbsp; &nbsp; d.MainInstruction = msg; &nbsp; &nbsp; d.Show(); &nbsp; } &nbsp; #endregion // Message handlers
```

```csharp
public class PipeFilter : ISelectionFilter { &nbsp; const BuiltInCategory _bic = BuiltInCategory.OST_PipeCurves; &nbsp; &nbsp; public bool AllowElement( Element e ) &nbsp; { &nbsp; &nbsp; return null != e.Category &nbsp; &nbsp; &nbsp; &amp;&amp; e.Category.Id.IntegerValue == ( int ) _bic; &nbsp; } &nbsp; &nbsp; public bool AllowReference( Reference r, XYZ p ) &nbsp; { &nbsp; &nbsp; return true; &nbsp; } }
```
