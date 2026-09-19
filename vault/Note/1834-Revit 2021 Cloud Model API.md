---
num: 1834
date: 2020-04-09
themes: [VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2021 Cloud Model API

<https://jeremytammik.github.io/tbc/a/1834_2021_cloud_model_api.html>

```csharp
{ "type": "hubs", "id": "b.6bdabd18-6096-492b-966e-86492a4bb660", "attributes": { "name": "Wookong_EU", "extension": { "type": "hubs:autodesk.bim360:Account", "version": "1.0", "schema": { "href": "https://developer.api.autodesk.com/schema/v1/versions/hubs:autodesk.bim360:Account-1.0" }, "data": {} }, "region": "EMEA" }, "links": { "self": { "href": "https://developer.api.autodesk.com/project/v1/hubs/b.6bdabd18-6096-492b-966e-86492a4bb660" } }, "relationships": { "projects": { "links": { "related": { "href": "http://developer.api.autodesk.com/dm/v1/hubs/b.6bdabd18-6096-492b-966e-86492a4bb660/projects" } } } } }
```

```csharp
"included": [ { "type": "versions", "id": "urn:adsk.wipbimemeastg:fs.file:vf.VFlOMhozRMac61hJ1JB_Nw?version=1", "attributes": { "name": "C4R_12_11_2019_10_01_14 AM_28.rvt", "displayName": "C4R_12_11_2019_10_01_14 AM_28.rvt", "createTime": "2019-12-11T10:01:44.0000000Z", "createUserId": "YZVYJQWWAJ89", "createUserName": "Phil Xia", "lastModifiedTime": "2019-12-11T10:01:47.0000000Z", "lastModifiedUserId": "YZVYJQWWAJ89", "lastModifiedUserName": "Phil Xia", "versionNumber": 1, "mimeType": "application/vnd.autodesk.r360", "extension": { "type": "versions:autodesk.bim360:C4RModel", "version": "1.1.0", "schema": { "href": "https://developer.api.autodesk.com/schema/v1/versions/versions:autodesk.bim360:C4RModel-1.1.0" }, "data": { "modelVersion": 3, "projectGuid": "fd1335eb-733b-480c-9d16-1a22e742ef70", "modelType": "singleuser", "latestEpisodeGuid": "11da0d90-e1bb-492a-b90e-f3759ca6ab39", "mimeType": "application/vnd.autodesk.r360", "modelGuid": "e5a59497-0d79-4df0-879d-396310288bb0", "processState": "PROCESSING_COMPLETE", "extractionState": "SKIPPED", "splittingState": "NOT_SPLIT", "revisionDisplayLabel": "1", "sourceFileName": "C4R_12_11_2019_10_01_14 AM_28.rvt" } } },
```

```csharp
Guid account = new Guid("a8d3b76e-cf23-4dd7-a090-9e893efcf949"); Guid project = new Guid("bf46f5e3-285e-496f-be03-b5b1f8b1e154"); string folder_id = "urn:adsk.wipemea:fs.folder:co.Jo68ieLRRcKvQr4fI2Q8uQ"; string model_name = "rac_advanced_sample_project.rvt"; currentDocument.SaveAsCloudModel( account, // BIM 360 account id project, // BIM 360 project id folder_id, // BIM 360 folder id model_name // model name );
```
