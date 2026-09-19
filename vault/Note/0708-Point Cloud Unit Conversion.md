---
num: 708
date: 2012-01-23
themes: [Units]
tags: [revit-api, tbc]
---

# Point Cloud Unit Conversion

<https://jeremytammik.github.io/tbc/a/0708_point_cloud_unit_conv.htm>

```csharp
&nbsp; class PointCloudAccess : IPointCloudAccess &nbsp; { &nbsp; &nbsp; const double _mm_per_inch = 25.4; &nbsp; &nbsp; const double _mm_per_foot = 12 * _mm_per_inch; &nbsp; &nbsp; const double _mm_to_feet = 1.0 / _mm_per_foot; &nbsp; &nbsp; &nbsp; public double GetUnitsToFeetConversionFactor() &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; return _mm_to_feet; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; // . . . &nbsp; &nbsp; }
```
