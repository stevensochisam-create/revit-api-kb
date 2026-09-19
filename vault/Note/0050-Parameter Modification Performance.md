---
num: 50
date: 2008-12-04
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameter Modification Performance

<https://jeremytammik.github.io/tbc/a/0050_modify_param.htm>

```csharp
// Start measurement int millis = Environment.TickCount; &nbsp; // Set some values Parameter p = instance.get_Parameter("Breite"); p.Set(500); &nbsp; // Set some Booleans p = instance.get_Parameter("F&#252;sse"); p.Set(1); &nbsp; p = instance.get_Parameter("Sockel"); p.Set(1); &nbsp; p = instance.get_Parameter("Rille"); p.Set(1); &nbsp; // Set some strings p = instance.get_Parameter("Bezeichnung Deutsch"); p.Set("Deutsche Bezeichnung"); &nbsp; p = instance.get_Parameter("Bezeichnung Englisch"); p.Set("English description"); &nbsp; p = instance.get_Parameter("Comments"); p.Set("A comment"); &nbsp; millis = Environment.TickCount - millis; MessageBox.Show( &nbsp; millis + "Millis to set 9 parameters. " + &nbsp; " (about " + millis / 9.0 + " millis per param)" );
```
