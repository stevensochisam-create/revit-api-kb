---
type: TessellatedShapeBuilder
namespace: Autodesk.Revit.DB
version: 2024
members: 19
tags: [revit-api, class]
---

# TessellatedShapeBuilder

`Autodesk.Revit.DB.TessellatedShapeBuilder` · Revit 2024 · 19 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | TessellatedShapeBuilder | 2015 | `public TessellatedShapeBuilder ()` |
| Method | AddFace | 2015 | `public void AddFace ( TessellatedFace face )` |
| Method | AreTargetAndFallbackCompatible | 2015 | `public bool AreTargetAndFallbackCompatible ( TessellatedShapeBuilderTarget target , TessellatedShapeBuilderFallback fallback )` |
| Method | Build | 2017 | `public void Build ()` |
| Method | CancelConnectedFaceSet | 2015 | `public void CancelConnectedFaceSet ()` |
| Method | Clear | 2015 | `public void Clear ()` |
| Method | CloseConnectedFaceSet | 2015 | `public void CloseConnectedFaceSet ()` |
| Method | CreateMeshByExtrusion | 2015 | `public static MeshFromGeometryOperationResult CreateMeshByExtrusion ( IList < CurveLoop > profileLoops , XYZ extrusionDirection , double extrusionDistance , ElementId materialId )` |
| Method | DoesFaceHaveEnoughLoopsAndVertices | 2015 | `public bool DoesFaceHaveEnoughLoopsAndVertices ( TessellatedFace face )` |
| Method | GetBuildResult | 2015 | `public TessellatedShapeBuilderResult GetBuildResult ()` |
| Method | OpenConnectedFaceSet | 2015 | `public void OpenConnectedFaceSet ( bool isSolid )` |
| Property | Fallback | 2017 | `public TessellatedShapeBuilderFallback Fallback { get ; set ; }` |
| Property | GraphicsStyleId | 2017 | `public ElementId GraphicsStyleId { get ; set ; }` |
| Property | IsFaceSetOpen | 2015 | `public bool IsFaceSetOpen { get ; }` |
| Property | LogInteger | 2015 | `public int LogInteger { get ; set ; }` |
| Property | LogString | 2015 | `public string LogString { get ; set ; }` |
| Property | NumberOfCompletedFaceSets | 2015 | `public int NumberOfCompletedFaceSets { get ; }` |
| Property | OwnerInfo | 2015 | `public string OwnerInfo { get ; set ; }` |
| Property | Target | 2017 | `public TessellatedShapeBuilderTarget Target { get ; set ; }` |