---
num: 1054
date: 2013-11-08
themes: [MEP]
tags: [revit-api, tbc]
---

# User MEP Calculation Sample on GitHub

<https://jeremytammik.github.io/tbc/a/1054_mep_calculation.htm>

```csharp
&nbsp; xmlFileName = System.IO.Path.GetDirectoryName( &nbsp; &nbsp; PressureLossReportHelper.instance.Doc &nbsp; &nbsp; &nbsp; .Application.RecordingJournalFilename ); &nbsp; &nbsp; if( xmlFileName != null &amp;&amp; xmlFileName.Length &gt; 0 ) &nbsp; &nbsp; xmlFileName = xmlFileName &nbsp; &nbsp; &nbsp; + &quot;\\UserPressureLossReport&quot; &nbsp; &nbsp; &nbsp; + DateTime.Now.Millisecond.ToString() + &quot;.xml&quot;; &nbsp; &nbsp; string strPath = typeof( &nbsp; &nbsp; UserPressureLossReport.WholeReportSettingsDlg ) &nbsp; &nbsp; &nbsp; .Assembly.Location; &nbsp; &nbsp; xsltFileName = Path.Combine( &nbsp; &nbsp; Path.GetDirectoryName( Path.GetDirectoryName( &nbsp; &nbsp; &nbsp; strPath ) ), &nbsp; &nbsp; &quot;output&quot;, &quot;UserPressureLossReport.xslt&quot; ); &nbsp; &nbsp; xmlWriter = XmlWriter.Create( xmlFileName );
```

```csharp
&nbsp; // Check if the xslt file exists &nbsp; &nbsp; if (!File.Exists(writer.XsltFileName)) &nbsp; { &nbsp; &nbsp; string subMsg = ReportResource.xsltFileSubMsg &nbsp; &nbsp; &nbsp; .Replace(&quot;%FULLPATH%&quot;, writer.XsltFileName ); &nbsp; &nbsp; &nbsp; UIHelperFunctions.postWarning( &nbsp; &nbsp; &nbsp; ReportResource.htmlGenerateTitle, &nbsp; &nbsp; &nbsp; ReportResource.xsltFileMsg, subMsg ); &nbsp; &nbsp; &nbsp; return false; &nbsp; }
```

```csharp
C:\a\vs\UserMepCalculation\output &gt; ren PressureLossReport.xslt UserPressureLossReport.xslt
```
