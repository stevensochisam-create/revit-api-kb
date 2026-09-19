---
type: IndependentTag
namespace: Autodesk.Revit.DB
version: 2024
members: 31
tags: [revit-api, class]
---

# IndependentTag

`Autodesk.Revit.DB.IndependentTag` · Revit 2024 · 31 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddReferences | 2022 | `public void AddReferences ( IList < Reference > referencesToTag )` |
| Method | CanLeaderEndConditionBeAssigned | — | `public bool CanLeaderEndConditionBeAssigned ( LeaderEndCondition leaderEndCondition )` |
| Method | Create | — | `` |
| Method | GetLeaderElbow | 2022 | `public XYZ GetLeaderElbow ( Reference referenceTagged )` |
| Method | GetLeaderEnd | 2022 | `public XYZ GetLeaderEnd ( Reference referenceTagged )` |
| Method | GetTaggedElementIds | 2022 | `public ICollection < LinkElementId > GetTaggedElementIds ()` |
| Method | GetTaggedLocalElementIds | 2022 | `public ISet < ElementId > GetTaggedLocalElementIds ()` |
| Method | GetTaggedLocalElements | 2022 | `public ICollection < Element > GetTaggedLocalElements ()` |
| Method | GetTaggedReferences | 2022 | `public IList < Reference > GetTaggedReferences ()` |
| Method | HasLeaderElbow | 2022 | `public bool HasLeaderElbow ( Reference referenceTagged )` |
| Method | HasTagBehavior | 2024 | `public bool HasTagBehavior ()` |
| Method | IsLeaderVisible | 2023 | `public bool IsLeaderVisible ( Reference referenceTagged )` |
| Method | IsTaggedOnSubelement | 2018 | `public bool IsTaggedOnSubelement ()` |
| Method | RemoveReferences | 2022 | `public void RemoveReferences ( IList < Reference > referencesToRemove )` |
| Method | SetIsLeaderVisible | 2023 | `public void SetIsLeaderVisible ( Reference referenceTagged , bool visible )` |
| Method | SetLeaderElbow | 2022 | `public void SetLeaderElbow ( Reference referenceTagged , XYZ elbowPosition )` |
| Method | SetLeaderEnd | 2022 | `public void SetLeaderEnd ( Reference referenceTagged , XYZ pointEnd )` |
| Property | HasLeader | — | `public bool HasLeader { get ; set ; }` |
| Property | IsMaterialTag | — | `public bool IsMaterialTag { get ; }` |
| Property | IsMulticategoryTag | — | `public bool IsMulticategoryTag { get ; }` |
| Property | IsOrphaned | — | `public bool IsOrphaned { get ; }` |
| Property | LeaderEndCondition | — | `public LeaderEndCondition LeaderEndCondition { get ; set ; }` |
| Property | LeadersPresentationMode | 2023 | `public LeadersPresentationMode LeadersPresentationMode { get ; set ; }` |
| Property | MergeElbows | 2023 | `public bool MergeElbows { get ; set ; }` |
| Property | MultiLeader | 2022 | `public bool MultiLeader { get ; }` |
| Property | MultiReferenceAnnotationId | — | `public ElementId MultiReferenceAnnotationId { get ; }` |
| Property | Parameter | — | `` |
| Property | RotationAngle | 2022 | `public double RotationAngle { get ; set ; }` |
| Property | TagHeadPosition | — | `public XYZ TagHeadPosition { get ; set ; }` |
| Property | TagOrientation | — | `public TagOrientation TagOrientation { get ; set ; }` |
| Property | TagText | — | `public string TagText { get ; }` |