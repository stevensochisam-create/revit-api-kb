---
type: RebarConstraint
namespace: Autodesk.Revit.DB.Structure
version: 2024
members: 45
tags: [revit-api, class]
---

# RebarConstraint

`Autodesk.Revit.DB.Structure.RebarConstraint` · Revit 2024 · 45 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AreGeometryTargetsTheSame | 2014 | `public bool AreGeometryTargetsTheSame ( RebarConstraint otherConstraint )` |
| Method | ConstrainsRebarEnds | 2020.1 | `public bool ConstrainsRebarEnds ()` |
| Method | Create | 2018 | `public static RebarConstraint Create ( RebarConstrainedHandle handle , IList < Reference > targetReferences , bool isConstraintToCover , double offsetValue )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | FlipHandleOverTarget | 2020.1 | `public void FlipHandleOverTarget ()` |
| Method | GetConstraintType | 2014 | `public RebarConstraintType GetConstraintType ()` |
| Method | GetCustomHandleTag | 2018 | `public int GetCustomHandleTag ()` |
| Method | GetDistanceToTargetCover | 2016 | `public double GetDistanceToTargetCover ()` |
| Method | GetDistanceToTargetHostFace | 2014 | `public double GetDistanceToTargetHostFace ()` |
| Method | GetDistanceToTargetRebar | 2020.1 | `public double GetDistanceToTargetRebar ()` |
| Method | GetPositiveOffsetDirectionForToOtherRebarConstraint | 2024 | `public XYZ GetPositiveOffsetDirectionForToOtherRebarConstraint ()` |
| Method | GetRebarConstraintTargetHostFaceType | — | `` |
| Method | GetRebarConstraintTargetHostFaceType | 2014 | `public RebarConstraintTargetHostFaceType GetRebarConstraintTargetHostFaceType ()` |
| Method | GetTargetCoverType | 2018 | `public RebarCoverType GetTargetCoverType ( int targetIndex )` |
| Method | GetTargetElement | — | `` |
| Method | GetTargetElement | 2014 | `public Element GetTargetElement ()` |
| Method | GetTargetHostFaceAndTransform | 2018 | `public Face GetTargetHostFaceAndTransform ( int targetIndex , Transform faceTransform )` |
| Method | GetTargetHostFaceReference | — | `` |
| Method | GetTargetHostFaceReference | 2014 | `public Reference GetTargetHostFaceReference ()` |
| Method | GetTargetRebarAngleOnBarOrHookBend | 2014 | `public int GetTargetRebarAngleOnBarOrHookBend ()` |
| Method | GetTargetRebarBendNumber | 2014 | `public int GetTargetRebarBendNumber ()` |
| Method | GetTargetRebarConstraintType | 2014 | `public TargetRebarConstraintType GetTargetRebarConstraintType ()` |
| Method | GetTargetRebarEdgeNumber | 2014 | `public int GetTargetRebarEdgeNumber ()` |
| Method | GetTargetRebarHookBarEnd | 2014 | `public int GetTargetRebarHookBarEnd ()` |
| Method | HasAnEdgeNumber | 2014 | `public bool HasAnEdgeNumber ()` |
| Method | IsBindingHandleWithTarget | 2020.1 | `public bool IsBindingHandleWithTarget ()` |
| Method | IsEqual | 2014 | `public bool IsEqual ( RebarConstraint other )` |
| Method | IsFixedDistanceToHostFace | 2014 | `public bool IsFixedDistanceToHostFace ()` |
| Method | IsReferenceValidForConstraint | 2019.1 | `public bool IsReferenceValidForConstraint ( Reference targetReference )` |
| Method | IsToCover | 2014 | `public bool IsToCover ()` |
| Method | IsToHostFaceOrCover | 2014 | `public bool IsToHostFaceOrCover ()` |
| Method | IsToOtherRebar | 2014 | `public bool IsToOtherRebar ()` |
| Method | IsUsingClearBarSpacing | 2020.1 | `public bool IsUsingClearBarSpacing ()` |
| Method | IsValid | 2014 | `public bool IsValid ()` |
| Method | ReplaceReferenceTargets | 2018 | `public void ReplaceReferenceTargets ( RebarConstrainedHandle handle , IList < Reference > targetReferences , bool isConstraintToCover , double offsetValue )` |
| Method | SetDistanceToTargetCover | 2016 | `public void SetDistanceToTargetCover ( double distanceToTargetCover )` |
| Method | SetDistanceToTargetHostFace | 2014 | `public void SetDistanceToTargetHostFace ( double offset )` |
| Method | SetDistanceToTargetRebar | 2020.1 | `public void SetDistanceToTargetRebar ( double distanceToTargetRebar )` |
| Method | SetToBindHandleWithTarget | 2020.1 | `public void SetToBindHandleWithTarget ( bool bindsHandleWithTarget )` |
| Method | SetToUseClearBarSpacing | 2020.1 | `public void SetToUseClearBarSpacing ( bool useClearBarSpacing )` |
| Method | TargetIsBarBend | 2014 | `public bool TargetIsBarBend ()` |
| Method | TargetIsHookBend | 2014 | `public bool TargetIsHookBend ()` |
| Method | TargetRebarConstraintTypeIsEdge | 2014 | `public bool TargetRebarConstraintTypeIsEdge ()` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | NumberOfTargets | 2018 | `public int NumberOfTargets { get ; }` |