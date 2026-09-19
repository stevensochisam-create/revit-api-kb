---
num: 2011
date: 2023-10-20
themes: [Geometry]
tags: [revit-api, tbc]
---

# Xgbxml Fixes Building Geometry Gaps

<https://jeremytammik.github.io/tbc/a/2011_xgbxml_fix_gap.html>

```csharp
# import packages from xgbxml import get_parser from xgbxml import geometry_functions, gbxml_functions, render_functions from lxml import etree import matplotlib.pyplot as plt import copy import math from uuid import uuid4
```

```csharp
# uses xgbxml to generate a lxml parser to read gbXML version 0.37 parser=get_parser(version='0.37')
```

```csharp
# opens the file using the custom lxml parser fp='23-013 WH Swan Hill_Mass_23-08-30.xml' tree=etree.parse(fp,parser) gbxml=tree.getroot() # renders the Campus element ax=gbxml.Campus.render() ax.figure.set_size_inches(8, 8) ax.set_title(fp) plt.show()
```

```csharp
# identify gaps in surfaces of building gaps=gbxml.Campus.Building.get_gaps_in_surfaces() gaps
```

```csharp
[{'space_ids': ['aim2197'], 'shell': [ (72.2287629, -0.3141381, 0.0), (72.2287629, -0.4999998, 0.0), (72.0986211, -0.4999998, 0.0), (72.2287629, -0.3141381, 0.0)]}, {'space_ids': ['aim2553', 'aim7413'], 'shell': [(80.2291667, 14.5625, 10.0), (80.0208333, 14.5625, 10.0), (80.0208333, 16.020833, 10.0), (80.2291667, 16.020833, 10.0), (80.2291667, 14.5625, 10.0)]}, {'space_ids': ['aim6674'], 'shell': [(72.2287629, -0.4999998, 10.0), (72.2287629, -0.3141381, 10.0), (72.0986211, -0.4999998, 10.0), (72.2287629, -0.4999998, 10.0)]}]
```
