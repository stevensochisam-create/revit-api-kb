---
num: 840
date: 2012-10-10
themes: [Geometry]
tags: [revit-api, tbc]
---

# UIView, Windows Coordinates, ReferenceIntersector and My Own Tooltip

<https://jeremytammik.github.io/tbc/a/0840_wincoord_tooltip.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Singleton external application class instance. &nbsp; /// &lt;/summary&gt; &nbsp; internal static App _app = null; &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Provide access to singleton class instance. &nbsp; /// &lt;/summary&gt; &nbsp; public static App Instance &nbsp; { &nbsp; &nbsp; get { return _app; } &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// The tooltip form to display. &nbsp; /// &lt;/summary&gt; &nbsp; internal static JtTooltipForm2 _form = null; &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Dispose and null out form. &nbsp; /// Return true if it was previously not disposed. &nbsp; /// &lt;/summary&gt; &nbsp; static bool CloseForm() &nbsp; { &nbsp; &nbsp; bool rc = _form != null; &nbsp; &nbsp; &nbsp; if( rc ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( !_form.IsDisposed ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; _form.Dispose(); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; _form = null; &nbsp; &nbsp; } &nbsp; &nbsp; return rc; &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Create and show the form, &nbsp; /// unless it already exists. &nbsp; /// &lt;/summary&gt; &nbsp; /// &lt;remarks&gt; &nbsp; /// The external command invokes &nbsp; /// this on end-user request. &nbsp; /// &lt;/remarks&gt; &nbsp; public void ShowForm( UIApplication uiapp ) &nbsp; { &nbsp; &nbsp; // If we do not have a form yet, create and show it &nbsp; &nbsp; &nbsp; if( _form == null || _form.IsDisposed ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // Instantiate JtTooltipForm to use &nbsp; &nbsp; &nbsp; // the designer generated form. &nbsp; &nbsp; &nbsp; &nbsp; _form = new JtTooltipForm2(); &nbsp; &nbsp; &nbsp; &nbsp; _form.Show(); &nbsp; &nbsp; &nbsp; &nbsp; // If we have a form, we need Idling too &nbsp; &nbsp; &nbsp; &nbsp; uiapp.Idling += IdlingHandler; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Hide the form. &nbsp; /// &lt;/summary&gt; &nbsp; /// &lt;remarks&gt; &nbsp; /// The external command invokes &nbsp; /// this on end-user request. &nbsp; /// &lt;/remarks&gt; &nbsp; public void HideForm( UIApplication uiapp ) &nbsp; { &nbsp; &nbsp; if( CloseForm() ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // If the form was showing, we had subscribed &nbsp; &nbsp; &nbsp; &nbsp; uiapp.Idling -= IdlingHandler; &nbsp; &nbsp; } &nbsp; } &nbsp; &nbsp; public Result OnStartup( UIControlledApplication a ) &nbsp
```

```csharp
/// &lt;summary&gt; /// Return currently active UIView or null. /// &lt;/summary&gt; static UIView GetActiveUiView( &nbsp; UIDocument uidoc ) { &nbsp; Document doc = uidoc.Document; &nbsp; View view = doc.ActiveView; &nbsp; IList&lt;UIView&gt; uiviews = uidoc.GetOpenUIViews(); &nbsp; UIView uiview = null; &nbsp; &nbsp; foreach( UIView uv in uiviews ) &nbsp; { &nbsp; &nbsp; if( uv.ViewId.Equals( view.Id ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; uiview = uv; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; } &nbsp; } &nbsp; return uiview; }
```

```csharp
/// &lt;summary&gt; /// Return the 3D view named &quot;{3D}&quot;. /// &lt;/summary&gt; View3D GetView3d( Document doc ) { &nbsp; return new FilteredElementCollector( doc ) &nbsp; &nbsp; .OfClass( typeof( View3D ) ) &nbsp; &nbsp; .Cast&lt;View3D&gt;() &nbsp; &nbsp; .FirstOrDefault&lt;View3D&gt;( &nbsp; &nbsp; &nbsp; v =&gt; v.Name.Equals( &quot;{3D}&quot; ) ); }
```

```csharp
/// &lt;summary&gt; /// Return a string describing the given element: /// .NET type name, /// category name, /// family and symbol name for a family instance, /// element id and element name. /// &lt;/summary&gt; static string ElementDescription( &nbsp; Element e ) { &nbsp; if( null == e ) &nbsp; { &nbsp; &nbsp; return &quot;&lt;null&gt;&quot;; &nbsp; } &nbsp; &nbsp; // For a wall, the element name equals the &nbsp; // wall type name, which is equivalent to the &nbsp; // family name ... &nbsp; &nbsp; FamilyInstance fi = e as FamilyInstance; &nbsp; &nbsp; string typeName = e.GetType().Name; &nbsp; &nbsp; string categoryName = ( null == e.Category ) &nbsp; &nbsp; ? string.Empty &nbsp; &nbsp; : e.Category.Name + &quot; &quot;; &nbsp; &nbsp; string familyName = ( null == fi ) &nbsp; &nbsp; ? string.Empty &nbsp; &nbsp; : fi.Symbol.Family.Name + &quot; &quot;; &nbsp; &nbsp; string symbolName = ( null == fi &nbsp; &nbsp; || e.Name.Equals( fi.Symbol.Name ) ) &nbsp; &nbsp; &nbsp; ? string.Empty &nbsp; &nbsp; &nbsp; : fi.Symbol.Name + &quot; &quot;; &nbsp; &nbsp; return string.Format( &quot;{0} {1}{2}{3}&lt;{4} {5}&gt;&quot;, &nbsp; &nbsp; typeName, categoryName, familyName, &nbsp; &nbsp; symbolName, e.Id.IntegerValue, e.Name ); }
```

```csharp
&nbsp; Point p = System.Windows.Forms.Cursor.Position;
```
