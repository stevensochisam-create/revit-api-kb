---
num: 358
date: 2010-05-05
themes: [Geometry]
tags: [revit-api, tbc]
---

# Detail Curve Must Indeed lie in Plane

<https://jeremytammik.github.io/tbc/a/0358_detail_curve_plane.htm>

```csharp
Normal = {(0.000000000, -0.707106781, 0.707106781)}
```

```csharp
XYZ end0 = new XYZ( 0, 0, 0 ); XYZ end1 = new XYZ( 10, 0, 0 ); XYZ pointOnCurve = new XYZ( 5, 5, 0 );
```

```csharp
Point3d Plane::closestPointTo( const Point3d &amp; p ) const { &nbsp; double d = signedDistanceTo( p ); &nbsp; return p - d * m_n; }
```

```csharp
inline double Plane::signedDistanceTo( const Point3d &amp; p ) const { &nbsp; return m_n.dotProduct( p.asVector() ) - m_d; }
```
