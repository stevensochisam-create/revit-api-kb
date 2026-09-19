---
num: 1863
date: 2020-09-09
themes: [Parameter]
tags: [revit-api, tbc]
---

# Optimising Parameters and Full-Text Search

<https://jeremytammik.github.io/tbc/a/1863_param_optimise_tbcfts.html>

```csharp
class&nbsp;IdForSynchro { &nbsp;&nbsp;public&nbsp;ElementId&nbsp;RevitId&nbsp;{&nbsp;get;&nbsp;set;&nbsp;} &nbsp;&nbsp;public&nbsp;int&nbsp;Param1&nbsp;{&nbsp;get;&nbsp;set;&nbsp;} &nbsp;&nbsp;public&nbsp;string&nbsp;Param2&nbsp;{&nbsp;get;&nbsp;set;&nbsp;} &nbsp;&nbsp;public&nbsp;double&nbsp;Param3&nbsp;{&nbsp;get;&nbsp;set;&nbsp;} } void&nbsp;modifyParameterValues(&nbsp;Document&nbsp;doc,&nbsp;IList&lt;IdForSynchro&gt;&nbsp;data&nbsp;) { &nbsp;&nbsp;using(&nbsp;Transaction&nbsp;tr&nbsp;=&nbsp;new&nbsp;Transaction(&nbsp;doc&nbsp;)&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;Guid&nbsp;guid1&nbsp;=&nbsp;Guid.Empty; &nbsp;&nbsp;&nbsp;&nbsp;Guid&nbsp;guid2&nbsp;=&nbsp;Guid.Empty; &nbsp;&nbsp;&nbsp;&nbsp;Guid&nbsp;guid3&nbsp;=&nbsp;Guid.Empty; &nbsp;&nbsp;&nbsp;&nbsp;tr.Start(&nbsp;&quot;synchro&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;IdForSynchro&nbsp;d&nbsp;in&nbsp;data&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Element&nbsp;e&nbsp;=&nbsp;doc.GetElement(&nbsp;d.RevitId&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;Guid.Empty&nbsp;==&nbsp;guid1&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;guid1&nbsp;=&nbsp;e.LookupParameter(&nbsp;&quot;PLUGIN_PARAM1&quot;&nbsp;).GUID; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;guid2&nbsp;=&nbsp;e.LookupParameter(&nbsp;&quot;PLUGIN_PARAM2&quot;&nbsp;).GUID; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;guid3&nbsp;=&nbsp;e.LookupParameter(&nbsp;&quot;PLUGIN_PARAM3&quot;&nbsp;).GUID; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.get_Parameter(&nbsp;guid1&nbsp;).Set(&nbsp;d.Param1&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.get_Parameter(&nbsp;guid2&nbsp;).Set(&nbsp;d.Param2&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.get_Parameter(&nbsp;guid3&nbsp;).Set(&nbsp;d.Param3&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;tr.Commit(); &nbsp;&nbsp;} }
```

```csharp
/a/src/go/tbcfts $ ./tbcfts -q "dabble" 2020/09/09 10:31:40 Starting tbcfts, p=/a/doc/revit/tbc/git/a, q=dabble 2020/09/09 10:31:41 Loaded 1863 documents in 377.397917ms 2020/09/09 10:31:44 Indexed 1863 documents in 2.876775333s 2020/09/09 10:31:44 Search for 'dabble' found 5 documents in 9.703µs 2020/09/09 10:31:44 582 [Wiki API Help, View Event and Structural Material Type](0582_api_wiki_help_view_mat.htm 2020/09/09 10:31:44 906 [Export Wall Parts Individually to DXF](0906_export_wall_part_dxf.htm 2020/09/09 10:31:44 961 [Super Insane MP3 and Songbird Playlist Exporter](0961_songbird_to_m3u.htm 2020/09/09 10:31:44 1008 [Open MEP Connector Warning](1527_mep_connector_number.html 2020/09/09 10:31:44 1863 [Optimising Parameters and Full-Text Search](http thebuildingcoder.typepad.com not yet published)
```
