---
type: Reference
namespace: Autodesk.Revit.DB
version: 2024
members: 12
tags: [revit-api, class]
---

# Reference

`Autodesk.Revit.DB.Reference` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | Reference | 2011 | `public Reference ( Element element )` |
| Method | Contains | 2018 | `public bool Contains ( Reference reference )` |
| Method | ConvertToStableRepresentation | — | `public string ConvertToStableRepresentation ( Document document )` |
| Method | CreateLinkReference | 2014 | `public Reference CreateLinkReference ( RevitLinkInstance revitLinkInstance )` |
| Method | CreateReferenceInLink | 2014 | `public Reference CreateReferenceInLink ()` |
| Method | EqualTo | 2018 | `public bool EqualTo ( Reference reference )` |
| Method | ParseFromStableRepresentation | — | `public static Reference ParseFromStableRepresentation ( Document document , string representation )` |
| Property | ElementId | 2012 | `public ElementId ElementId { get ; }` |
| Property | ElementReferenceType | — | `public ElementReferenceType ElementReferenceType { get ; }` |
| Property | GlobalPoint | — | `public XYZ GlobalPoint { get ; }` |
| Property | LinkedElementId | 2014 | `public ElementId LinkedElementId { get ; }` |
| Property | UVPoint | — | `public UV UVPoint { get ; }` |