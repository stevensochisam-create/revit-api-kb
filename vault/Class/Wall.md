---
type: Wall
namespace: Autodesk.Revit.DB
version: 2024
members: 19
tags: [revit-api, class]
---

# Wall

`Autodesk.Revit.DB.Wall` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CanHaveProfileSketch | — | `public bool CanHaveProfileSketch ()` |
| Method | Create | — | `` |
| Method | CreateProfileSketch | 2022 | `public Sketch CreateProfileSketch ()` |
| Method | Flip | — | `public void Flip ()` |
| Method | GetStackedWallMemberIds | 2015 | `public IList < ElementId > GetStackedWallMemberIds ()` |
| Method | IsWallCrossSectionValid | 2022 | `public bool IsWallCrossSectionValid ( WallCrossSection wallCrossSection )` |
| Method | RemoveProfileSketch | 2022 | `public void RemoveProfileSketch ()` |
| Property | CrossSection | 2022 | `public WallCrossSection CrossSection { get ; set ; }` |
| Property | CurtainGrid | — | `public CurtainGrid CurtainGrid { get ; }` |
| Property | Flipped | — | `public bool Flipped { get ; }` |
| Property | IsStackedWall | 2015 | `public bool IsStackedWall { get ; }` |
| Property | IsStackedWallMember | 2015 | `public bool IsStackedWallMember { get ; }` |
| Property | Orientation | — | `public XYZ Orientation { get ; }` |
| Property | Parameter | — | `` |
| Property | SketchId | 2022 | `public ElementId SketchId { get ; }` |
| Property | StackedWallOwnerId | 2015 | `public ElementId StackedWallOwnerId { get ; }` |
| Property | StructuralUsage | — | `public StructuralWallUsage StructuralUsage { get ; set ; }` |
| Property | WallType | — | `public WallType WallType { get ; set ; }` |
| Property | Width | — | `public double Width { get ; }` |