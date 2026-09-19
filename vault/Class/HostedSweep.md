---
type: HostedSweep
namespace: Autodesk.Revit.DB
version: 2024
members: 14
tags: [revit-api, class]
---

# HostedSweep

`Autodesk.Revit.DB.HostedSweep` · Revit 2024 · 14 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddSegment | — | `public abstract void AddSegment ( Reference targetRef )` |
| Method | GetEndPointParameter | — | `public double GetEndPointParameter ( Reference targetRef , int endIdx )` |
| Method | HorizontalFlip | — | `public void HorizontalFlip ()` |
| Method | RemoveSegment | — | `public void RemoveSegment ( Reference targetRef )` |
| Method | SetEndPointParameter | — | `public bool SetEndPointParameter ( Reference targetRef , int endIdx , double param )` |
| Method | VerticalFlip | — | `public void VerticalFlip ()` |
| Property | Angle | — | `public double Angle { get ; set ; }` |
| Property | HorizontalFlipped | — | `public bool HorizontalFlipped { get ; }` |
| Property | HorizontalOffset | — | `public double HorizontalOffset { get ; set ; }` |
| Property | Length | — | `public double Length { get ; }` |
| Property | Parameter | — | `` |
| Property | ReferenceCurve | — | `public Curve this [ Reference targetRef ] { get ; }` |
| Property | VerticalFlipped | — | `public bool VerticalFlipped { get ; }` |
| Property | VerticalOffset | — | `public double VerticalOffset { get ; set ; }` |