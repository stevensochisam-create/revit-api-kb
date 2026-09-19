---
type: DividedSurface
namespace: Autodesk.Revit.DB
version: 2024
members: 30
tags: [revit-api, class]
---

# DividedSurface

`Autodesk.Revit.DB.DividedSurface` · Revit 2024 · 30 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddIntersectionElement | 2011 | `public void AddIntersectionElement ( ElementId newIntersectionElemId )` |
| Method | CanBeDivided | 2014 | `public static bool CanBeDivided ( Document document , Reference reference )` |
| Method | CanBeIntersectionElement | 2011 | `public bool CanBeIntersectionElement ( ElementId id )` |
| Method | Create | 2014 | `public static DividedSurface Create ( Document document , Reference faceReference )` |
| Method | GetAllIntersectionElements | 2011 | `public ICollection < ElementId > GetAllIntersectionElements ()` |
| Method | GetDividedSurfaceForReference | 2014 | `public static DividedSurface GetDividedSurfaceForReference ( Document document , Reference faceReference )` |
| Method | GetGridNodeLocation | — | `public GridNodeLocation GetGridNodeLocation ( GridNode gridNode )` |
| Method | GetGridNodeReference | — | `public Reference GetGridNodeReference ( GridNode gridNode )` |
| Method | GetGridNodeUV | — | `public UV GetGridNodeUV ( GridNode gridNode )` |
| Method | GetGridSegmentReference | — | `public Reference GetGridSegmentReference ( GridNode gridNode , GridSegmentDirection gridSegmentDirection )` |
| Method | GetReferencesWithDividedSurfaces | 2014 | `public static IList < Reference > GetReferencesWithDividedSurfaces ( Element host )` |
| Method | GetTileFamilyInstance | — | `public FamilyInstance GetTileFamilyInstance ( GridNode gridNode , int tileIndex )` |
| Method | GetTileReference | — | `public Reference GetTileReference ( GridNode gridNode , int tileIndex )` |
| Method | IsSeedNode | — | `public bool IsSeedNode ( GridNode gridNode )` |
| Method | RemoveAllIntersectionElements | 2011 | `public void RemoveAllIntersectionElements ()` |
| Method | RemoveIntersectionElement | 2011 | `public void RemoveIntersectionElement ( ElementId referenceElemIdToRemove )` |
| Property | AllGridRotation | — | `public double AllGridRotation { get ; set ; }` |
| Property | BorderTile | — | `public BorderTile BorderTile { get ; set ; }` |
| Property | ComponentRotation | — | `public ComponentRotation ComponentRotation { get ; set ; }` |
| Property | Host | — | `public Element Host { get ; }` |
| Property | HostReference | — | `public Reference HostReference { get ; }` |
| Property | IsComponentFlipped | — | `public bool IsComponentFlipped { get ; set ; }` |
| Property | IsComponentMirrored | — | `public bool IsComponentMirrored { get ; set ; }` |
| Property | NumberOfUGridlines | — | `public int NumberOfUGridlines { get ; }` |
| Property | NumberOfVGridlines | — | `public int NumberOfVGridlines { get ; }` |
| Property | Parameter | — | `` |
| Property | UPatternIndent | — | `public int UPatternIndent { get ; set ; }` |
| Property | USpacingRule | — | `public SpacingRule USpacingRule { get ; }` |
| Property | VPatternIndent | — | `public int VPatternIndent { get ; set ; }` |
| Property | VSpacingRule | — | `public SpacingRule VSpacingRule { get ; }` |