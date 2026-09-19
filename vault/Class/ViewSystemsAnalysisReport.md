---
type: ViewSystemsAnalysisReport
namespace: Autodesk.Revit.DB.Analysis
version: 2024
members: 13
tags: [revit-api, class]
---

# ViewSystemsAnalysisReport

`Autodesk.Revit.DB.Analysis.ViewSystemsAnalysisReport` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CancelSystemsAnalysis | 2023 | `public static void CancelSystemsAnalysis ( Document document , ElementId reportElement )` |
| Method | Create | 2020.1 | `public static ViewSystemsAnalysisReport Create ( Document document , string viewName )` |
| Method | GetLatestSystemsAnalysisReport | 2020.1 | `public static ElementId GetLatestSystemsAnalysisReport ( Document document )` |
| Method | GetReportContent | 2020.1 | `public string GetReportContent ()` |
| Method | IsAnalysisCompleted | 2020.1 | `public bool IsAnalysisCompleted ()` |
| Method | Print | — | `` |
| Method | RequestSystemsAnalysis | 2020.1 | `public void RequestSystemsAnalysis ( SystemsAnalysisOptions options )` |
| Property | AnalysisDateAndTime | 2020.1 | `public DateTime AnalysisDateAndTime { get ; }` |
| Property | Parameter | — | `` |
| Property | ReportStyle | 2022 | `public SystemsAnalysisReportStyle ReportStyle { get ; set ; }` |
| Property | SystemsAnalysisOutputFolder | 2020.1 | `public string SystemsAnalysisOutputFolder { get ; }` |
| Property | SystemsAnalysisWorkflowFile | 2020.1 | `public string SystemsAnalysisWorkflowFile { get ; }` |
| Property | WeatherFile | 2020.1 | `public string WeatherFile { get ; }` |