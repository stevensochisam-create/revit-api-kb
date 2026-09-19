---
type: ColumnAttachment
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# ColumnAttachment

`Autodesk.Revit.DB.ColumnAttachment` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddColumnAttachment | — | `public static void AddColumnAttachment ( Document doc , FamilyInstance column , Element target , int baseOrTop , ColumnAttachmentCutStyle cutColumnStyle , ColumnAttachmentJustification justification , double attachOffset` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetColumnAttachment | — | `` |
| Method | IsValidColumn | — | `public static bool IsValidColumn ( FamilyInstance familyInstance )` |
| Method | IsValidTarget | — | `` |
| Method | RemoveColumnAttachment | — | `` |
| Method | SetJustification | — | `public void SetJustification ( ColumnAttachmentJustification justification )` |
| Property | AttachOffset | — | `public double AttachOffset { get ; set ; }` |
| Property | BaseOrTop | — | `public int BaseOrTop { get ; }` |
| Property | CutStyle | — | `public ColumnAttachmentCutStyle CutStyle { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | Justification | — | `public ColumnAttachmentJustification Justification { get ; }` |
| Property | TargetId | — | `public ElementId TargetId { get ; }` |