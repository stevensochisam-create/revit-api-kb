---
num: 1974
date: 2022-11-29
themes: [ElementId, Pitfall]
tags: [revit-api, tbc]
---

# 64-Bit Element Ids, Maybe?

<https://jeremytammik.github.io/tbc/a/1974_64_bit_element_id.html>

```csharp
&nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;This&nbsp;macro&nbsp;gets&nbsp;the&nbsp;header&nbsp;text&nbsp;of&nbsp;the&nbsp;active&nbsp;Schedule&nbsp;View &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;public&nbsp;void&nbsp;ScheduleHeader() &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;UIDocument&nbsp;uidoc&nbsp;=&nbsp;this.ActiveUIDocument; &nbsp;&nbsp;&nbsp;&nbsp;Document&nbsp;doc&nbsp;=&nbsp;uidoc.Document; &nbsp;&nbsp;&nbsp;&nbsp;ViewSchedule&nbsp;mySchedule&nbsp;=&nbsp;uidoc.ActiveView&nbsp;as&nbsp;ViewSchedule; &nbsp;&nbsp;&nbsp;&nbsp;TableData&nbsp;myTableData&nbsp;=&nbsp;mySchedule.GetTableData(); &nbsp;&nbsp;&nbsp;&nbsp;TableSectionData&nbsp;myData&nbsp;=&nbsp;myTableData.GetSectionData(SectionType.Header); &nbsp;&nbsp;&nbsp;&nbsp;TaskDialog.Show(&quot;Header&nbsp;Info&quot;,&nbsp;&quot;The&nbsp;Header&nbsp;Text&nbsp;is:&nbsp;\n&quot;&nbsp;+&nbsp;myData.GetCellText(0,&nbsp;0)); &nbsp;&nbsp;}
```
