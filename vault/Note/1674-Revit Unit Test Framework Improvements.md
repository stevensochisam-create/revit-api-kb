---
num: 1674
date: 2018-08-20
themes: [Units]
tags: [revit-api, tbc]
---

# Revit Unit Test Framework Improvements

<https://jeremytammik.github.io/tbc/a/1674_revittestframework.html>

```csharp
[TestFixture] public class TestAllModels { [Test, TestModel(@"C:\Models\test_models_2019\*.rvt")] public void SomeTest() { ... } }
```
