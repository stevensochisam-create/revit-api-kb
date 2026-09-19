---
num: 1977
date: 2023-01-03
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# CultureInfoChanger and IronPython3

<https://jeremytammik.github.io/tbc/a/1977_cultureinfochanger.html>

```csharp
using (new CultureInfoChanger()) { connector.Radius = 0.5; }
```

```csharp
connector.SetRadius(0.5); connector.SetHeight(0.5); connector.SetWidth(0.5); /// /// Set the radius of the connector. /// /// /// public static void SetRadius(this Connector connector, double radius) { using (new CultureInfoChanger()) { connector.Radius = radius; } }
```
