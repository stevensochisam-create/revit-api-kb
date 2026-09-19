---
num: 688
date: 2011-12-05
themes: [Pitfall, Units]
tags: [revit-api, tbc]
---

# Unit Conversion and Display String Formatting

<https://jeremytammik.github.io/tbc/a/0688_unit_display_str.htm>

```csharp
&nbsp; Dim value As String = &quot;=2' + 4'/3&quot; &nbsp; Dim t As New Transaction(doc, &quot;Format Length&quot;) &nbsp; t.Start() &nbsp; p.SetValueString(value) &nbsp; value = p.AsValueString &nbsp; t.RollBack() &nbsp; Return value
```

```csharp
&nbsp; Public Shared Function StringValueString( _ &nbsp; &nbsp; ByVal doc As Document, _ &nbsp; &nbsp; ByVal value As String) As String &nbsp; &nbsp; &nbsp; ' Locate the arbitrary Length parameter &nbsp; &nbsp; &nbsp; Dim p As Parameter _ &nbsp; &nbsp; &nbsp; = doc.ProjectInformation.Parameter( _ &nbsp; &nbsp; &nbsp; &quot;Parameter Name&quot;) &nbsp; &nbsp; &nbsp; If p Is Nothing Then &nbsp; &nbsp; &nbsp; TaskDialog.Show( _ &nbsp; &nbsp; &nbsp; &nbsp; &quot;Revit&quot;, _ &nbsp; &nbsp; &nbsp; &nbsp; &quot;Missing Project Parameter: Parameter Name&quot;) &nbsp; &nbsp; &nbsp; Return value &nbsp; &nbsp; End If &nbsp; &nbsp; &nbsp; Dim tr As New Transaction(doc) &nbsp; &nbsp; tr.Start(&quot;Format Length&quot;) &nbsp; &nbsp; &nbsp; Try &nbsp; &nbsp; &nbsp; p.SetValueString(value) &nbsp; &nbsp; &nbsp; value = p.AsValueString &nbsp; &nbsp; Catch ex As Exception &nbsp; &nbsp; &nbsp; End Try &nbsp; &nbsp; &nbsp; tr.RollBack() &nbsp; &nbsp; &nbsp; Return value &nbsp; &nbsp; End Function
```

```csharp
p.Set(value) sValueString = p.AsValueString
```

```csharp
p.SetValueString(value) dValue = p.AsDouble
```

```csharp
Parameter name: Top Extension Distance Parameter value (imperial): 0 Parameter unit value: 0 Parameter AsValueString: 0.0 Parameter name: Length Parameter value (imperial): 45.5 Parameter unit value: 13868.4 Parameter AsValueString: 13868.4 Parameter name: Base Extension Distance Parameter value (imperial): 0 Parameter unit value: 0 Parameter AsValueString: 0.0 Parameter name: Top Offset Parameter value (imperial): 0 Parameter unit value: 0 Parameter AsValueString: 0.0 Parameter name: Volume Parameter value (imperial): 455.9586023831 Parameter unit value: 12.911309795985 Parameter AsValueString: 12.911 m³ Parameter name: Unconnected Height Parameter value (imperial): 18.0446194225722 Parameter unit value: 5500 Parameter AsValueString: 5500.0 Parameter name: Base Offset Parameter value (imperial): 0 Parameter unit value: 0 Parameter AsValueString: 0.0 Parameter name: Area Parameter value (imperial): 694.880910031848 Parameter unit value: 64.5565489799251 Parameter AsValueString: 64.557 m²
```
