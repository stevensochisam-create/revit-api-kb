---
num: 2032
date: 2024-04-05
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Revit 2025 and RevitLookup 2025

<https://jeremytammik.github.io/tbc/a/2032_rvt_2025.html>

```csharp
&lt;PackageReference Include="Microsoft.Extensions.Hosting" Version="8.*" Condition="$(RevitVersion) == '2025'"/&gt; &lt;PackageReference Include="Microsoft.Extensions.Hosting" Version="7.*" Condition="$(RevitVersion) != '' And $(RevitVersion) &lt; '2025'"/&gt;
```
