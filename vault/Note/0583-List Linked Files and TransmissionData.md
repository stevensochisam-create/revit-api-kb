---
num: 583
date: 2011-05-19
themes: [LinkedModel]
tags: [revit-api, tbc]
---

# List Linked Files and TransmissionData

<https://jeremytammik.github.io/tbc/a/0583_list_links.htm>

```csharp
/// &lt;summary&gt; /// List all DWG, RVT and other links of a given document. /// &lt;/summary&gt; void ListLinks( ModelPath location ) { &nbsp; string path = ModelPathUtils &nbsp; &nbsp; .ConvertModelPathToUserVisiblePath( location ); &nbsp; &nbsp; string content = string.Format( &nbsp; &nbsp; &quot;The document at '{0}' &quot;, &nbsp; &nbsp; path ); &nbsp; &nbsp; List&lt;string&gt; links = null; &nbsp; &nbsp; // access transmission data in the given Revit file &nbsp; &nbsp; TransmissionData transData = TransmissionData &nbsp; &nbsp; .ReadTransmissionData( location ); &nbsp; &nbsp; if( transData == null ) &nbsp; { &nbsp; &nbsp; content += &quot;does not have any transmission data&quot;; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; // collect all (immediate) external references in the model &nbsp; &nbsp; &nbsp; ICollection&lt;ElementId&gt; externalReferences &nbsp; &nbsp; &nbsp; = transData.GetAllExternalFileReferenceIds(); &nbsp; &nbsp; &nbsp; int n = externalReferences.Count; &nbsp; &nbsp; &nbsp; content += string.Format( &nbsp; &nbsp; &nbsp; &quot;has {0} external reference{1}{2}&quot;, &nbsp; &nbsp; &nbsp; n, PluralSuffix( n ), DotOrColon( n ) ); &nbsp; &nbsp; &nbsp; links = new List&lt;string&gt;( n ); &nbsp; &nbsp; &nbsp; // find every reference that is a link &nbsp; &nbsp; &nbsp; foreach( ElementId refId in externalReferences ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; ExternalFileReference extRef &nbsp; &nbsp; &nbsp; &nbsp; = transData.GetLastSavedReferenceData( refId ); &nbsp; &nbsp; &nbsp; &nbsp; links.Add( string.Format( &quot;{0} {1}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; extRef.ExternalFileReferenceType, &nbsp; &nbsp; &nbsp; &nbsp; ModelPathUtils.ConvertModelPathToUserVisiblePath( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; extRef.GetPath() ) ) ); &nbsp; &nbsp; } &nbsp; } &nbsp; Debug.Print( content ); &nbsp; &nbsp; TaskDialog dlg = new TaskDialog( &quot;List Links&quot; ); &nbsp; &nbsp; dlg.MainInstruction = content; &nbsp; &nbsp; if( null != links &amp;&amp; 0 &lt; links.Count ) &nbsp; { &nbsp; &nbsp; string s = string.Join( &quot;&nbsp; \r\n&quot;, &nbsp; &nbsp; &nbsp; links.ToArray() ); &nbsp; &nbsp; &nbsp; Debug.Print( s ); &nbsp; &nbsp; &nbsp; dlg.MainContent = s; &nbsp; } &nbsp; dlg.Show(); }
```

```csharp
public Result Execute( &nbsp; ExternalCommandData commandData, &nbsp; ref string message, &nbsp; ElementSet elements ) { &nbsp; View view = commandData.View; &nbsp; &nbsp; if( null == view ) &nbsp; { &nbsp; &nbsp; message = &quot;Please run this command in an active document.&quot;; &nbsp; &nbsp; return Result.Failed; &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; Document doc = view.Document; &nbsp; &nbsp; &nbsp; ModelPath modelPath = ModelPathUtils &nbsp; &nbsp; &nbsp; .ConvertUserVisiblePathToModelPath( &nbsp; &nbsp; &nbsp; &nbsp; doc.PathName ); &nbsp; &nbsp; &nbsp; ListLinks( modelPath ); &nbsp; &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```

```csharp
The document at 'C:\tmp\linked_file2.rvt' has 3 external references: KeynoteTable RevitKeynotes_Metric.txt RevitLink walls.rvt CADLink TestHouse.dwg
```
