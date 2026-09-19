---
num: 245
date: 2009-11-09
themes: [Parameter]
tags: [revit-api, tbc]
---

# Family Parameter Value

<https://jeremytammik.github.io/tbc/a/0245_family_param_value.htm>

```csharp
Application app = commandData.Application; Document doc = app.ActiveDocument; if( !doc.IsFamilyDocument ) { &nbsp; message = &nbsp; &nbsp; &quot;Please run this command in a family document.&quot;; } else
```

```csharp
FamilyManager mgr = doc.FamilyManager; &nbsp; int n = mgr.Parameters.Size; &nbsp; Debug.Print( &nbsp; &quot;\nFamily {0} has {1} parameter{2}.&quot;, &nbsp; doc.Title, n, Util.PluralSuffix( n ) ); &nbsp; Dictionary&lt;string, FamilyParameter&gt; fps &nbsp; = new Dictionary&lt;string, FamilyParameter&gt;( n ); &nbsp; foreach( FamilyParameter fp in mgr.Parameters ) { &nbsp; string name = fp.Definition.Name; &nbsp; fps.Add( name, fp ); } List&lt;string&gt; keys = new List&lt;string&gt;( fps.Keys ); keys.Sort();
```

```csharp
static string FamilyParamValueString( &nbsp; FamilyType t, &nbsp; FamilyParameter fp, &nbsp; Document doc ) { &nbsp; string value = t.AsValueString( fp ); &nbsp; switch( fp.StorageType ) &nbsp; { &nbsp; &nbsp; case StorageType.Double: &nbsp; &nbsp; &nbsp; value = Util.RealString( &nbsp; &nbsp; &nbsp; &nbsp; ( double ) t.AsDouble( fp ) ) &nbsp; &nbsp; &nbsp; &nbsp; + &quot; (double)&quot;; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; case StorageType.ElementId: &nbsp; &nbsp; &nbsp; ElementId id = t.AsElementId( fp ); &nbsp; &nbsp; &nbsp; Element e = doc.get_Element( ref id ); &nbsp; &nbsp; &nbsp; value = id.Value.ToString() + &quot; (&quot; &nbsp; &nbsp; &nbsp; &nbsp; + Util.ElementDescription( e ) + &quot;)&quot;; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; case StorageType.Integer: &nbsp; &nbsp; &nbsp; value = t.AsInteger( fp ).ToString() &nbsp; &nbsp; &nbsp; &nbsp; + &quot; (int)&quot;; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; case StorageType.String: &nbsp; &nbsp; &nbsp; value = &quot;'&quot; + t.AsString( fp ) &nbsp; &nbsp; &nbsp; &nbsp; + &quot;' (string)&quot;; &nbsp; &nbsp; &nbsp; break; &nbsp; } &nbsp; return value; }
```

```csharp
n = mgr.Types.Size; &nbsp; Debug.Print( &nbsp; &quot;Family {0} has {1} type{2}{3}&quot;, &nbsp; doc.Title, &nbsp; n, &nbsp; Util.PluralSuffix( n ), &nbsp; Util.DotOrColon( n ) ); &nbsp; foreach( FamilyType t in mgr.Types ) { &nbsp; string name = t.Name; &nbsp; Debug.Print( &quot;&nbsp; {0}:&quot;, name ); &nbsp; foreach( string key in keys ) &nbsp; { &nbsp; &nbsp; FamilyParameter fp = fps[key]; &nbsp; &nbsp; if( t.HasValue( fp ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; string value &nbsp; &nbsp; &nbsp; &nbsp; = FamilyParamValueString( t, fp, doc ); &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;&nbsp; &nbsp; {0} = {1}&quot;, key, value ); &nbsp; &nbsp; } &nbsp; } }
```

```csharp
Family Family1 has 13 parameters. Family Family1 has 5 types: : ColumnFinish = -1 () Depth = 1.97 (double) Td = 0.49 (double) Tw = 0.49 (double) Width = 1.97 (double) 1000x300: ColumnFinish = -1 () Depth = 0.98 (double) Td = 0.25 (double) Tw = 0.82 (double) Width = 3.28 (double) 600x900: ColumnFinish = -1 () Depth = 2.95 (double) Td = 0.74 (double) Tw = 0.49 (double) Width = 1.97 (double) Glass: ColumnFinish = 574 (Materials ) Depth = 1.97 (double) Td = 0.49 (double) Tw = 0.49 (double) Width = 1.97 (double) 600x600: ColumnFinish = -1 () Depth = 1.97 (double) Td = 0.49 (double) Tw = 0.49 (double) Width = 1.97 (double)
```
