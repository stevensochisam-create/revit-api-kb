---
type: TransmissionData
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# TransmissionData

`Autodesk.Revit.DB.TransmissionData` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | TransmissionData | 2012 | `public TransmissionData ( TransmissionData other )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | DocumentIsNotTransmitted | 2012 | `public static bool DocumentIsNotTransmitted ( ModelPath filePath )` |
| Method | GetAllExternalFileReferenceIds | 2012 | `public ICollection < ElementId > GetAllExternalFileReferenceIds ()` |
| Method | GetDesiredReferenceData | 2012 | `public ExternalFileReference GetDesiredReferenceData ( ElementId elemId )` |
| Method | GetLastSavedReferenceData | 2012 | `public ExternalFileReference GetLastSavedReferenceData ( ElementId elemId )` |
| Method | IsDocumentTransmitted | 2012 | `public static bool IsDocumentTransmitted ( ModelPath filePath )` |
| Method | ReadTransmissionData | 2012 | `public static TransmissionData ReadTransmissionData ( ModelPath path )` |
| Method | SetDesiredReferenceData | 2012 | `public void SetDesiredReferenceData ( ElementId elemId , ModelPath path , PathType pathType , bool shouldLoad )` |
| Method | WriteTransmissionData | 2012 | `public static void WriteTransmissionData ( ModelPath path , TransmissionData data )` |
| Property | IsTransmitted | 2012 | `public bool IsTransmitted { get ; set ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | UserData | 2012 | `public string UserData { get ; set ; }` |
| Property | Version | 2012 | `public int Version { get ; }` |