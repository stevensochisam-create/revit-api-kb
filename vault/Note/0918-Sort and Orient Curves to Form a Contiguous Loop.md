---
num: 918
date: 2013-03-31
themes: [Geometry]
tags: [revit-api, tbc]
---

# Sort and Orient Curves to Form a Contiguous Loop

<https://jeremytammik.github.io/tbc/a/0918_contiguous_curves.htm>

```csharp
(2.74,8.38,0) --&gt; (2.74,8.46,0) (2.74,8.38,0) --&gt; (2.76,8.38,0) (2.76,8.38,0) --&gt; (2.76,8.44,0) (2.76,8.44,0) --&gt; (3.05,8.44,0) (3.05,8.44,0) --&gt; (3.05,8.38,0) (3.05,8.38,0) --&gt; (3.08,8.38,0) (3.08,8.46,0) --&gt; (3.08,8.38,0) (2.74,8.46,0) --&gt; (3.08,8.46,0)
```

```csharp
&nbsp; const double _inch = 1.0 / 12.0; &nbsp; const double _sixteenth = _inch / 16.0;
```

```csharp
/// &lt;summary&gt; /// Create a new curve with the same /// geometry in the reverse direction. /// &lt;/summary&gt; /// &lt;param name=&quot;orig&quot;&gt;The original curve.&lt;/param&gt; /// &lt;returns&gt;The reversed curve.&lt;/returns&gt; /// &lt;throws cref=&quot;NotImplementedException&quot;&gt;If the /// curve type is not supported by this utility.&lt;/throws&gt; static Curve CreateReversedCurve( &nbsp; Autodesk.Revit.Creation.Application creapp, &nbsp; Curve orig ) { &nbsp; if( !IsSupported( orig ) ) &nbsp; { &nbsp; &nbsp; throw new NotImplementedException( &nbsp; &nbsp; &nbsp; &quot;CreateReversedCurve for type &quot; &nbsp; &nbsp; &nbsp; + orig.GetType().Name ); &nbsp; } &nbsp; &nbsp; if( orig is Line ) &nbsp; { &nbsp; &nbsp; return creapp.NewLineBound( &nbsp; &nbsp; &nbsp; orig.GetEndPoint( 1 ), &nbsp; &nbsp; &nbsp; orig.GetEndPoint( 0 ) ); &nbsp; } &nbsp; else if( orig is Arc ) &nbsp; { &nbsp; &nbsp; return creapp.NewArc( orig.GetEndPoint( 1 ), &nbsp; &nbsp; &nbsp; orig.GetEndPoint( 0 ), &nbsp; &nbsp; &nbsp; orig.Evaluate( 0.5, true ) ); &nbsp; } &nbsp; else &nbsp; { &nbsp; &nbsp; throw new Exception( &nbsp; &nbsp; &nbsp; &quot;CreateReversedCurve - Unreachable&quot; ); &nbsp; } }
```

```csharp
0 endPoint (2.74,8.46,0) 7 start point, swap with 1 1 endPoint (3.08,8.46,0) 6 start point, swap with 2 2 endPoint (3.08,8.38,0) 5 end point, swap with reverse 3 3 endPoint (3.05,8.38,0) 4 end point, reverse 4 4 endPoint (3.05,8.44,0) 5 end point, reverse 5 5 endPoint (2.76,8.44,0) 6 end point, reverse 6 6 endPoint (2.76,8.38,0) 7 end point, reverse 7 7 endPoint (2.74,8.38,0)
```

```csharp
FamilyInstance Furniture Desk &lt;212646 1525 x 762mm&gt; has 10 loops: 0: (836,2555), (836,2580), (937,2580), (937,2555), (931,2555), (931,2574), (842,2574), (842,2555) 1: (1954,2580), (1954,2555), (1961,2555), (1961,2574), (2050,2574), (2050,2555), (2056,2555), (2056,2580) 2: (683,2542), (683,1780), (2208,1780), (2208,2542), (1802,2542), (1802,1831), (1090,1831), (1090,2542) 3: (664,2561), (664,1761), (2227,1761), (2227,2561) 4: (683,2440), (785,2440), (785,2542), (683,2542) 5: (785,1780), (785,1882), (683,1882), (683,1780) 6: (2107,1882), (2107,1780), (2208,1780), (2208,1882) 7: (2107,2542), (2107,2440), (2208,2440), (2208,2542) 8: (702,2542), (702,2555), (1071,2555), (1071,2542) 9: (1821,2542), (1821,2555), (2189,2555), (2189,2542)
```
