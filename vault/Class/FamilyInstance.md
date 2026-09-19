---
type: FamilyInstance
namespace: Autodesk.Revit.DB
version: 2024
members: 57
tags: [revit-api, class]
---

# FamilyInstance

`Autodesk.Revit.DB.FamilyInstance` · Revit 2024 · 57 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddCoping | — | `public bool AddCoping ( FamilyInstance cutter )` |
| Method | FlipFromToRoom | — | `public void FlipFromToRoom ()` |
| Method | GetCopingIds | — | `public ICollection < ElementId > GetCopingIds ()` |
| Method | GetFamilyPointPlacementReferences | 2011 | `public IList < FamilyPointPlacementReference > GetFamilyPointPlacementReferences ()` |
| Method | GetOriginalGeometry | — | `public GeometryElement GetOriginalGeometry ( Options options )` |
| Method | GetReferenceByName | 2018 | `public Reference GetReferenceByName ( string name )` |
| Method | GetReferenceName | 2018 | `public string GetReferenceName ( Reference reference )` |
| Method | GetReferenceType | 2018 | `public FamilyInstanceReferenceType GetReferenceType ( Reference reference )` |
| Method | GetReferences | 2018 | `public IList < Reference > GetReferences ( FamilyInstanceReferenceType referenceType )` |
| Method | GetSpatialElementCalculationPoint | 2016 | `public XYZ GetSpatialElementCalculationPoint ()` |
| Method | GetSpatialElementFromToCalculationPoints | 2016 | `public IList < XYZ > GetSpatialElementFromToCalculationPoints ()` |
| Method | GetSubComponentIds | — | `public ICollection < ElementId > GetSubComponentIds ()` |
| Method | GetSweptProfile | 2016 | `public SweptProfile GetSweptProfile ()` |
| Method | HasModifiedGeometry | 2016 | `public bool HasModifiedGeometry ()` |
| Method | HasSweptProfile | 2016 | `public bool HasSweptProfile ()` |
| Method | RemoveCoping | — | `public bool RemoveCoping ( FamilyInstance cutter )` |
| Method | SetCopingIds | — | `public bool SetCopingIds ( ICollection < ElementId > cutters )` |
| Method | Split | — | `public ElementId Split ( double param )` |
| Method | flipFacing | — | `public bool flipFacing ()` |
| Method | flipHand | — | `public bool flipHand ()` |
| Method | rotate | — | `public bool rotate ()` |
| Property | CanFlipFacing | — | `public bool CanFlipFacing { get ; }` |
| Property | CanFlipHand | — | `public bool CanFlipHand { get ; }` |
| Property | CanFlipWorkPlane | — | `public bool CanFlipWorkPlane { get ; }` |
| Property | CanRotate | — | `public bool CanRotate { get ; }` |
| Property | CanSplit | — | `public bool CanSplit { get ; }` |
| Property | ExtensionUtility | — | `public IExtension ExtensionUtility { get ; }` |
| Property | FacingFlipped | — | `public bool FacingFlipped { get ; }` |
| Property | FacingOrientation | — | `public XYZ FacingOrientation { get ; }` |
| Property | FromRoom | — | `` |
| Property | FromRoom | — | `public Room FromRoom { get ; }` |
| Property | HandFlipped | — | `public bool HandFlipped { get ; }` |
| Property | HandOrientation | — | `public XYZ HandOrientation { get ; }` |
| Property | HasSpatialElementCalculationPoint | 2016 | `public bool HasSpatialElementCalculationPoint { get ; }` |
| Property | HasSpatialElementFromToCalculationPoints | 2016 | `public bool HasSpatialElementFromToCalculationPoints { get ; }` |
| Property | Host | — | `public Element Host { get ; }` |
| Property | HostFace | — | `public Reference HostFace { get ; }` |
| Property | HostParameter | — | `public double HostParameter { get ; }` |
| Property | Invisible | — | `public bool Invisible { get ; }` |
| Property | IsSlantedColumn | — | `public bool IsSlantedColumn { get ; }` |
| Property | IsWorkPlaneFlipped | — | `public bool IsWorkPlaneFlipped { get ; set ; }` |
| Property | Location | — | `public override Location Location { get ; }` |
| Property | MEPModel | — | `public MEPModel MEPModel { get ; }` |
| Property | Mirrored | — | `public bool Mirrored { get ; }` |
| Property | Parameter | — | `` |
| Property | Room | — | `` |
| Property | Room | — | `public Room Room { get ; }` |
| Property | Space | — | `` |
| Property | Space | — | `public Space Space { get ; }` |
| Property | StructuralMaterialId | — | `public ElementId StructuralMaterialId { get ; set ; }` |
| Property | StructuralMaterialType | — | `public StructuralMaterialType StructuralMaterialType { get ; }` |
| Property | StructuralType | — | `public StructuralType StructuralType { get ; }` |
| Property | StructuralUsage | — | `public StructuralInstanceUsage StructuralUsage { get ; set ; }` |
| Property | SuperComponent | — | `public Element SuperComponent { get ; }` |
| Property | Symbol | — | `public FamilySymbol Symbol { get ; set ; }` |
| Property | ToRoom | — | `` |
| Property | ToRoom | — | `public Room ToRoom { get ; }` |