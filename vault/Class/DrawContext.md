---
type: DrawContext
namespace: Autodesk.Revit.DB.DirectContext3D
version: 2024
members: 11
tags: [revit-api, class]
---

# DrawContext

`Autodesk.Revit.DB.DirectContext3D.DrawContext` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | FlushBuffer | 2017 | `public static void FlushBuffer ( VertexBuffer vertexBuffer , int vertexCount , IndexBuffer indexBuffer , int indexCount , VertexFormat vertexFormat , EffectInstance effectInstance , PrimitiveType primitiveType , int star` |
| Method | GetCamera | 2017 | `public static Camera GetCamera ()` |
| Method | GetClipPlanes | 2017 | `public static IList < ClipPlane > GetClipPlanes ()` |
| Method | GetClipRectangle | 2017 | `public static Rectangle GetClipRectangle ()` |
| Method | GetOverrideColor | 2017 | `public static bool GetOverrideColor ( out Color color )` |
| Method | GetOverrideTransparency | 2017 | `public static bool GetOverrideTransparency ( out double transparency )` |
| Method | GetViewRectangle | 2017 | `public static Rectangle GetViewRectangle ()` |
| Method | IsAvailable | 2017 | `public static bool IsAvailable ()` |
| Method | IsInterrupted | 2017 | `public static bool IsInterrupted ()` |
| Method | IsTransparentPass | 2017 | `public static bool IsTransparentPass ()` |
| Method | SetWorldTransform | 2017 | `public static void SetWorldTransform ( Transform trf )` |