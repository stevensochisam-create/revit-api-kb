---
num: 578
date: 2011-05-06
themes: [MEP]
tags: [revit-api, tbc]
---

# Improved MEP Element Shape and Mount Ararat

<https://jeremytammik.github.io/tbc/a/0578_mep_element_shape_2.htm>

```csharp
&nbsp; Element e = &lt;selected element&gt;; &nbsp; &nbsp; Util.InfoMsg( string.Format( &nbsp; &nbsp; &quot;{0} is {1} ({2})&quot;, &nbsp; &nbsp; Util.ElementDescription( e ), &nbsp; &nbsp; MepElementShape.GetElementShape( e ), &nbsp; &nbsp; MepElementShapeV1.GetElementShape( e ) ) ); &nbsp;
```

```csharp
Mechanical Equipment Parallel Fan Powered VAV is unknown (unknown) Duct Fittings Rectangular Duct Radius Elbow is RectProfile 2 RectProfile (rectangular2rectangular) Ducts is RectProfile 2 RectProfile (rectangular) Duct Fittings Rectangular Duct Tee is RectProfile 2 RectProfile-RectProfile (unknown) Air Terminals Supply Diffuser is unknown (unknown)
```
