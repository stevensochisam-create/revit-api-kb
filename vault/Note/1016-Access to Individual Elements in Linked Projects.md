---
num: 1016
date: 2013-09-09
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# Access to Individual Elements in Linked Projects

<https://jeremytammik.github.io/tbc/a/1016_linked_project_element.htm>

```csharp
&nbsp; UIApplication uiapp = commandData.Application; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; Application app = uiapp.Application; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; FilteredElementCollector links &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfCategory( BuiltInCategory.OST_RvtLinks ); &nbsp; &nbsp; Debug.Print( &quot;\nLinks:\n&quot; ); &nbsp; &nbsp; string what; &nbsp; &nbsp; foreach( Element e in links ) &nbsp; { &nbsp; &nbsp; if( e is RevitLinkInstance ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; what = &quot;instance&quot;; &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Debug.Assert( e is RevitLinkType, &nbsp; &nbsp; &nbsp; &nbsp; &quot;expected all RvtLinks elements to &quot; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;be link type or link instance&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; what = &quot;type&quot;; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; Debug.Print( string.Format( &nbsp; &nbsp; &nbsp; &quot;Link {0} '{1}' &lt;{2}&gt;&quot;, &nbsp; &nbsp; &nbsp; what, e.Name, e.Id.IntegerValue ) ); &nbsp; } &nbsp; &nbsp; Debug.Print( &quot;\nDocuments and their elements:\n&quot; ); &nbsp; &nbsp; foreach( Document d in app.Documents ) &nbsp; { &nbsp; &nbsp; if( d.IsLinked ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Debug.Print( string.Format( &nbsp; &nbsp; &nbsp; &nbsp; &quot;Linked document '{0}':&quot;, &nbsp; &nbsp; &nbsp; &nbsp; d.Title ) ); &nbsp; &nbsp; &nbsp; &nbsp; FilteredElementCollector walls &nbsp; &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( d ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( Wall ) ); &nbsp; &nbsp; &nbsp; &nbsp; foreach( Element e in walls ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( string.Format( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;&nbsp; Element '{0}' &lt;{1}&gt;&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; e.Name, e.Id.IntegerValue ) ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; } &nbsp; return Result.Succeeded;
```

```csharp
Links: Link type 'a.rvt' &lt;193823&gt; Link instance 'a.rvt : 1 : location &lt;Not Shared&gt;' &lt;193824&gt; Link type 'b.rvt' &lt;193826&gt; Link instance 'b.rvt : 2 : location &lt;Not Shared&gt;' &lt;193827&gt; Link instance 'a.rvt : 3 : location &lt;Not Shared&gt;' &lt;193829&gt; Link instance 'b.rvt : 4 : location &lt;Not Shared&gt;' &lt;193841&gt; Documents and their elements: Linked document 'a.rvt': Element 'Generic - 200mm' &lt;193834&gt; Linked document 'b.rvt': Element 'Generic - 200mm' &lt;193842&gt;
```
