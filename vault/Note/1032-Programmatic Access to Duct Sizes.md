---
num: 1032
date: 2013-10-04
themes: [MEP]
tags: [revit-api, tbc]
---

# Programmatic Access to Duct Sizes

<https://jeremytammik.github.io/tbc/a/1032_duct_sizes.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// List all duct sizes, thus proving that the duct &nbsp; /// size settings available in the Revit UI through &nbsp; /// Manage &gt; MEP Settings &gt; Mechanical Settings &gt; &nbsp; /// Duct Settings &gt; Round/Oval/Rectangular are &nbsp; /// indeed available via the API. &nbsp; /// &lt;/summary&gt; &nbsp; void ListDuctSizes( Document doc ) &nbsp; { &nbsp; &nbsp; DuctSizeSettings settings &nbsp; &nbsp; &nbsp; = DuctSizeSettings.GetDuctSizeSettings( doc ); &nbsp; &nbsp; &nbsp; foreach( KeyValuePair&lt;DuctShape, DuctSizes&gt; pair &nbsp; &nbsp; &nbsp; in settings ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Debug.Print( pair.Key.ToString() ); &nbsp; &nbsp; &nbsp; &nbsp; foreach( MEPSize size in pair.Value ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; string value = FormatUtils.Format( doc, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; UnitType.UT_HVAC_DuctSize, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; size.NominalDiameter ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &quot;&nbsp; {0}: used in size lists/sizing: {1}/{2}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; size.UsedInSizeLists.ToString(), &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; size.UsedInSizing.ToString() ); &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```

```csharp
Round 3": used in size lists/sizing: True/True 4": used in size lists/sizing: True/True 4": used in size lists/sizing: True/True ... 88": used in size lists/sizing: True/True 90": used in size lists/sizing: True/True Rectangular 3": used in size lists/sizing: True/True 4": used in size lists/sizing: True/True 4": used in size lists/sizing: True/True ... 94": used in size lists/sizing: True/True 96": used in size lists/sizing: True/True Oval 3": used in size lists/sizing: True/True 4": used in size lists/sizing: True/True 5": used in size lists/sizing: True/True ... 143": used in size lists/sizing: True/True 144": used in size lists/sizing: True/True
```
