---
num: 1137
date: 2014-04-16
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Migrating RoomEditorApp to Revit 2015

<https://jeremytammik.github.io/tbc/a/1137_roomeditorapp_2015.htm>

```csharp
&nbsp; List&lt;ElementId&gt; ids = null; &nbsp; &nbsp; Selection sel = uidoc.Selection; &nbsp; &nbsp; if( 0 &lt; sel.Elements.Size ) &nbsp; { &nbsp; &nbsp; foreach( Element e in sel.Elements ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( !( e is Room ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; Util.ErrorMsg( &quot;Please pre-select only room&quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + &quot; elements before running this command.&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; if( null == ids ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; ids = new List&lt;ElementId&gt;( 1 ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; ids.Add( e.Id ); &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; Selection sel = uidoc.Selection; &nbsp; &nbsp; ICollection&lt;ElementId&gt; ids = sel.GetElementIds(); &nbsp; &nbsp; if( 0 &lt; ids.Count ) &nbsp; { &nbsp; &nbsp; foreach( ElementId id in ids ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; if( !( doc.GetElement( id ) is Room ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; Util.ErrorMsg( &quot;Please pre-select only room&quot; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + &quot; elements before running this command.&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; foreach( View v in sheet.Views ) &nbsp; { &nbsp; &nbsp; GetViewTransform( v ); &nbsp; }
```

```csharp
&nbsp; foreach( View v in sheet.GetAllPlacedViews() &nbsp; &nbsp; .Select&lt;ElementId, View&gt;( id =&gt; &nbsp; &nbsp; &nbsp; doc.GetElement( id ) as View ) ) &nbsp; { &nbsp; &nbsp; GetViewTransform( v ); &nbsp; }
```

```csharp
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; standalone=&quot;no&quot;?&gt; &lt;Extensibility xmlns= &nbsp; &quot;http://schemas.microsoft.com/AutomationExtensibility&quot;&gt; &nbsp; &lt;HostApplication&gt; &nbsp; &nbsp; &lt;Name&gt;Microsoft Visual Studio Macros&lt;/Name&gt; &nbsp; &nbsp; &lt;Version&gt;11.0&lt;/Version&gt; &nbsp; &lt;/HostApplication&gt; &nbsp; &lt;HostApplication&gt; &nbsp; &nbsp; &lt;Name&gt;Microsoft Visual Studio&lt;/Name&gt; &nbsp; &nbsp; &lt;Version&gt;11.0&lt;/Version&gt; &nbsp; &lt;/HostApplication&gt; &nbsp; &lt;Addin&gt; &nbsp; &nbsp; &lt;FriendlyName&gt;CopySourceAsHtml&lt;/FriendlyName&gt; &nbsp; &nbsp; &lt;Description&gt; &nbsp; &nbsp; &nbsp; Adds support to Microsoft Visual Studio 2012 &nbsp; &nbsp; &nbsp; for copying source code, syntax highlighting, &nbsp; &nbsp; &nbsp; and line numbers as HTML. &nbsp; &nbsp; &lt;/Description&gt; &nbsp; &nbsp; &lt;Assembly&gt; &nbsp; &nbsp; &nbsp; JTLeigh.Tools.Development.CopySourceAsHtml, &nbsp; &nbsp; &nbsp; Version=3.0.3215.1, Culture=neutral, &nbsp; &nbsp; &nbsp; PublicKeyToken=bb2a58bdc03d2e14, &nbsp; &nbsp; &nbsp; processorArchitecture=MSIL &nbsp; &nbsp; &lt;/Assembly&gt; &nbsp; &nbsp; &lt;FullClassName&gt; &nbsp; &nbsp; &nbsp; JTLeigh.Tools.Development.CopySourceAsHtml.Connect &nbsp; &nbsp; &lt;/FullClassName&gt; &nbsp; &nbsp; &lt;LoadBehavior&gt;1&lt;/LoadBehavior&gt; &nbsp; &nbsp; &lt;CommandPreload&gt;0&lt;/CommandPreload&gt; &nbsp; &nbsp; &lt;CommandLineSafe&gt;0&lt;/CommandLineSafe&gt; &nbsp; &lt;/Addin&gt; &lt;/Extensibility&gt;
```
