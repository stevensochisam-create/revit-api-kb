---
num: 106
date: 2009-02-27
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# List Linked Elements

<https://jeremytammik.github.io/tbc/a/0106_list_linked_elements.htm>

```csharp
public class ElementData { &nbsp; string _document; &nbsp; string _elementName; &nbsp; int _id; &nbsp; double _x; &nbsp; double _y; &nbsp; double _z; &nbsp; string _uniqueId; &nbsp; string _folder; &nbsp; &nbsp; public ElementData( &nbsp; &nbsp; string path, &nbsp; &nbsp; string elementName, &nbsp; &nbsp; int id, &nbsp; &nbsp; double x, &nbsp; &nbsp; double y, &nbsp; &nbsp; double z, &nbsp; &nbsp; string uniqueId ) &nbsp; { &nbsp; &nbsp; int i = path.LastIndexOf( "\\" ); &nbsp; &nbsp; _document = path.Substring( i + 1 ); &nbsp; &nbsp; _elementName = elementName; &nbsp; &nbsp; _id = id; &nbsp; &nbsp; _x = x; &nbsp; &nbsp; _y = y; &nbsp; &nbsp; _z = z; &nbsp; &nbsp; _uniqueId = uniqueId; &nbsp; &nbsp; _folder = path.Substring( 0, i ); &nbsp; } &nbsp; &nbsp; public string Document { &nbsp; &nbsp; get { return _document; } &nbsp; } &nbsp; public string Element { &nbsp; &nbsp; get { return _elementName; } &nbsp; } &nbsp; public int Id { &nbsp; &nbsp; get { return _id; } &nbsp; } &nbsp; public string X { &nbsp; &nbsp; get { return Util.RealString( _x ); } &nbsp; } &nbsp; public string Y { &nbsp; &nbsp; get { return Util.RealString( _y ); } &nbsp; } &nbsp; public string Z { &nbsp; &nbsp; get { return Util.RealString( _z ); } &nbsp; } &nbsp; public string UniqueId { &nbsp; &nbsp; get { return _uniqueId; } &nbsp; } &nbsp; public string Folder { &nbsp; &nbsp; get { return _folder; } &nbsp; } }
```

```csharp
public CmdLinkedFileElementsForm( &nbsp; List&lt;ElementData&gt; a ) { &nbsp; InitializeComponent(); &nbsp; dataGridView1.DataSource = a; }
```

```csharp
public List&lt;Element&gt; GetElements( &nbsp; BuiltInCategory bic, &nbsp; Type elemType, &nbsp; Application app, &nbsp; Document doc ) { &nbsp; CreationFilter cf = app.Create.Filter; &nbsp; Filter f1 = cf.NewCategoryFilter( bic ); &nbsp; Filter f2 = cf.NewTypeFilter( elemType ); &nbsp; Filter f3 = cf.NewLogicAndFilter( f1, f2 ); &nbsp; List&lt;Element&gt; elements = new List&lt;Element&gt;(); &nbsp; doc.get_Elements( f3, elements ); &nbsp; return elements; }
```

```csharp
&nbsp; List&lt;Element&gt; links = GetElements( &nbsp; &nbsp; BuiltInCategory.OST_RvtLinks, &nbsp; &nbsp; typeof( Instance ), app, doc );
```

```csharp
List&lt;ElementData&gt; data = new List&lt;ElementData&gt;(); Application app = commandData.Application; DocumentSet docs = app.Documents; foreach( Document doc in docs ) { &nbsp; List&lt;Element&gt; elements = GetElements( &nbsp; &nbsp; BuiltInCategory.OST_LightingFixtures, &nbsp; &nbsp; typeof( FamilyInstance ), app, doc ); &nbsp; &nbsp; foreach( FamilyInstance e in elements ) &nbsp; { &nbsp; &nbsp; string name = e.Name; &nbsp; &nbsp; LocationPoint lp = e.Location as LocationPoint; &nbsp; &nbsp; if( null != lp ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; XYZ p = lp.Point; &nbsp; &nbsp; &nbsp; data.Add( new ElementData( doc.PathName, e.Name, &nbsp; &nbsp; &nbsp; &nbsp; e.Id.Value, p.X, p.Y, p.Z, e.UniqueId ) ); &nbsp; &nbsp; } &nbsp; } } using( CmdLinkedFileElementsForm dlg = new CmdLinkedFileElementsForm( data ) ) { &nbsp; dlg.ShowDialog(); } return CmdResult.Cancelled;
```
