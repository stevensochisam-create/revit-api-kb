---
num: 60
date: 2008-12-19
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# Linked Files

<https://jeremytammik.github.io/tbc/a/0060_linked_files.htm>

```csharp
Autodesk.Revit.Creation.Filter cf &nbsp; = app.Create.Filter; &nbsp; BuiltInCategory bic &nbsp; = BuiltInCategory.OST_RvtLinks; &nbsp; Filter f1 &nbsp; = cf.NewCategoryFilter( bic ); &nbsp; Filter f2 &nbsp; = cf.NewTypeFilter( typeof( Instance ) ); &nbsp; Filter f3 &nbsp; = cf.NewLogicAndFilter( f1, f2 ); &nbsp; List&lt;Element&gt; links = new List&lt;Element&gt;(); &nbsp; Document doc = app.ActiveDocument; doc.get_Elements( f3, links );
```

```csharp
BuiltInParameter bip &nbsp; = BuiltInParameter.ELEM_TYPE_PARAM; &nbsp; Document doc = app.ActiveDocument; ElementIterator it = doc.Elements; &nbsp; List&lt;Element&gt; links = new List&lt;Element&gt;(); &nbsp; while( it.MoveNext() ) { &nbsp; Instance inst = it.Current as Instance; &nbsp; if( null != inst ) &nbsp; { &nbsp; &nbsp; Parameter p = inst.get_Parameter( bip ); &nbsp; &nbsp; ElementId id = p.AsElementId(); &nbsp; &nbsp; Element e = doc.get_Element( ref id ); &nbsp; &nbsp; string n = e.Name; &nbsp; &nbsp; string s = n.Substring( n.Length - 4 ); &nbsp; &nbsp; if( s.ToLower().Equals( ".rvt" ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; links.Add( inst ); &nbsp; &nbsp; } &nbsp; } }
```

```csharp
DocumentSet docs = app.Documents; int n = docs.Size; &nbsp; Dictionary&lt;string, string&gt; dict &nbsp; = new Dictionary&lt;string, string&gt;( n ); &nbsp; foreach( Document doc in docs ) { &nbsp; string path = doc.PathName; &nbsp; int i = path.LastIndexOf( "\\" ) + 1; &nbsp; string name = path.Substring( i ); &nbsp; dict.Add( name, path ); }
```

```csharp
Application app = commandData.Application; &nbsp; Dictionary&lt;string, string&gt; dict &nbsp; = GetFilePaths( app ); &nbsp; List&lt;Element&gt; links &nbsp; = GetLinkedFiles( app ); &nbsp; int n = links.Count; Debug.WriteLine( string.Format( &nbsp; "There {0} {1} linked Revit model{2}.", &nbsp; (1 == n ? "is" : "are"), n, &nbsp; Util.PluralSuffix( n ) ) ); &nbsp; string name; char[] sep = new char[] { ':' }; string[] a; &nbsp; foreach( Element link in links ) { &nbsp; name = link.Name; &nbsp; a = name.Split( sep ); &nbsp; name = a[0].Trim(); &nbsp; &nbsp; Debug.WriteLine( string.Format( &nbsp; &nbsp; "Link '{0}' full path is '{1}'.", &nbsp; &nbsp; name, dict[name] ) ); } return CmdResult.Succeeded;
```

```csharp
There are 2 linked Revit models. Link 'roof.rvt' full path is 'C:\tmp\roof.rvt'. Link 'two_rooms.rvt' full path is 'C:\tmp\two_rooms.rvt'.
```
