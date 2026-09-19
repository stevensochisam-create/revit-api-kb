---
type: Truss
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 12
tags: [revit-api, class]
---

# Truss

`Autodesk.Revit.DB.Structure.Truss` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AttachChord | 2011 | `public void AttachChord ( Element attachToElement , TrussChordLocation location , bool forceRemoveSketch )` |
| Method | Create | 2014 | `public static Truss Create ( Document document , ElementId trussTypeId , ElementId sketchPlaneId , Curve curve )` |
| Method | DetachChord | 2011 | `public void DetachChord ( TrussChordLocation location )` |
| Method | DropTruss | 2011 | `public static void DropTruss ( Truss truss )` |
| Method | GetTrussMemberInfo | — | `public TrussMemberInfo GetTrussMemberInfo ( ElementId elemId )` |
| Method | RemoveProfile | — | `public void RemoveProfile ()` |
| Method | SetProfile | — | `public void SetProfile ( CurveArray topChords , CurveArray bottomChords )` |
| Method | TogglePinMember | — | `public void TogglePinMember ( ElementId elemId )` |
| Property | Curves | — | `public CurveArray Curves { get ; }` |
| Property | Members | — | `public ICollection < ElementId > Members { get ; }` |
| Property | Parameter | — | `` |
| Property | TrussType | — | `public TrussType TrussType { get ; set ; }` |