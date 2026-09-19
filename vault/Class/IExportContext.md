---
type: IExportContext
namespace: Autodesk.Revit.DB
version: 2024
members: 17
tags: [revit-api, class]
---

# IExportContext

`Autodesk.Revit.DB.IExportContext` · Revit 2024 · 17 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Finish | 2014 | `void Finish ()` |
| Method | IsCanceled | 2014 | `bool IsCanceled ()` |
| Method | OnElementBegin | 2014 | `RenderNodeAction OnElementBegin ( ElementId elementId )` |
| Method | OnElementEnd | 2014 | `void OnElementEnd ( ElementId elementId )` |
| Method | OnFaceBegin | 2014 | `RenderNodeAction OnFaceBegin ( FaceNode node )` |
| Method | OnFaceEnd | 2014 | `void OnFaceEnd ( FaceNode node )` |
| Method | OnInstanceBegin | 2014 | `RenderNodeAction OnInstanceBegin ( InstanceNode node )` |
| Method | OnInstanceEnd | 2014 | `void OnInstanceEnd ( InstanceNode node )` |
| Method | OnLight | 2014 | `void OnLight ( LightNode node )` |
| Method | OnLinkBegin | 2014 | `RenderNodeAction OnLinkBegin ( LinkNode node )` |
| Method | OnLinkEnd | 2014 | `void OnLinkEnd ( LinkNode node )` |
| Method | OnMaterial | 2014 | `void OnMaterial ( MaterialNode node )` |
| Method | OnPolymesh | 2014 | `void OnPolymesh ( PolymeshTopology node )` |
| Method | OnRPC | 2014 | `void OnRPC ( RPCNode node )` |
| Method | OnViewBegin | 2014 | `RenderNodeAction OnViewBegin ( ViewNode node )` |
| Method | OnViewEnd | 2014 | `void OnViewEnd ( ElementId elementId )` |
| Method | Start | 2014 | `bool Start ()` |