---
num: 1050
date: 2013-11-04
themes: [Pitfall, Units]
tags: [revit-api, tbc]
---

# Unit Abbreviations

<https://jeremytammik.github.io/tbc/a/1050_unit_abbreviation.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Hard coded abbreviations for the first 26 &nbsp; /// DisplayUnitType enumeration values. &nbsp; /// &lt;/summary&gt; &nbsp; public static string[] DisplayUnitTypeAbbreviation &nbsp; &nbsp; = new string[] { &nbsp; &nbsp; &nbsp; &quot;m&quot;, // DUT_METERS = 0, &nbsp; &nbsp; &nbsp; &quot;cm&quot;, // DUT_CENTIMETERS = 1, &nbsp; &nbsp; &nbsp; &quot;mm&quot;, // DUT_MILLIMETERS = 2, &nbsp; &nbsp; &nbsp; &quot;ft&quot;, // DUT_DECIMAL_FEET = 3, &nbsp; &nbsp; &nbsp; &quot;N/A&quot;, // DUT_FEET_FRACTIONAL_INCHES = 4, &nbsp; &nbsp; &nbsp; &quot;N/A&quot;, // DUT_FRACTIONAL_INCHES = 5, &nbsp; &nbsp; &nbsp; &quot;in&quot;, // DUT_DECIMAL_INCHES = 6, &nbsp; &nbsp; &nbsp; &quot;ac&quot;, // DUT_ACRES = 7, &nbsp; &nbsp; &nbsp; &quot;ha&quot;, // DUT_HECTARES = 8, &nbsp; &nbsp; &nbsp; &quot;N/A&quot;, // DUT_METERS_CENTIMETERS = 9, &nbsp; &nbsp; &nbsp; &quot;y^3&quot;, // DUT_CUBIC_YARDS = 10, &nbsp; &nbsp; &nbsp; &quot;ft^2&quot;, // DUT_SQUARE_FEET = 11, &nbsp; &nbsp; &nbsp; &quot;m^2&quot;, // DUT_SQUARE_METERS = 12, &nbsp; &nbsp; &nbsp; &quot;ft^3&quot;, // DUT_CUBIC_FEET = 13, &nbsp; &nbsp; &nbsp; &quot;m^3&quot;, // DUT_CUBIC_METERS = 14, &nbsp; &nbsp; &nbsp; &quot;deg&quot;, // DUT_DECIMAL_DEGREES = 15, &nbsp; &nbsp; &nbsp; &quot;N/A&quot;, // DUT_DEGREES_AND_MINUTES = 16, &nbsp; &nbsp; &nbsp; &quot;N/A&quot;, // DUT_GENERAL = 17, &nbsp; &nbsp; &nbsp; &quot;N/A&quot;, // DUT_FIXED = 18, &nbsp; &nbsp; &nbsp; &quot;%&quot;, // DUT_PERCENTAGE = 19, &nbsp; &nbsp; &nbsp; &quot;in^2&quot;, // DUT_SQUARE_INCHES = 20, &nbsp; &nbsp; &nbsp; &quot;cm^2&quot;, // DUT_SQUARE_CENTIMETERS = 21, &nbsp; &nbsp; &nbsp; &quot;mm^2&quot;, // DUT_SQUARE_MILLIMETERS = 22, &nbsp; &nbsp; &nbsp; &quot;in^3&quot;, // DUT_CUBIC_INCHES = 23, &nbsp; &nbsp; &nbsp; &quot;cm^3&quot;, // DUT_CUBIC_CENTIMETERS = 24, &nbsp; &nbsp; &nbsp; &quot;mm^3&quot;, // DUT_CUBIC_MILLIMETERS = 25, &nbsp; &nbsp; &nbsp; &quot;l&quot; // DUT_LITERS = 26, &nbsp; &nbsp; };
```

```csharp
&nbsp; const string _s = &quot;unexpected display unit type &quot; &nbsp; &nbsp; + &quot;enumeration sequence&quot;; &nbsp; &nbsp; Debug.Assert( 0 == (int) DisplayUnitType.DUT_METERS, _s ); &nbsp; Debug.Assert( 1 == (int) DisplayUnitType.DUT_CENTIMETERS, _s ); &nbsp; Debug.Assert( 2 == (int) DisplayUnitType.DUT_MILLIMETERS, _s ); &nbsp; . . . &nbsp; Debug.Assert( 26 == (int) DisplayUnitType.DUT_LITERS, _s );
```

```csharp
UST_NONE = 0, UST_M = 1, UST_CM = 101, UST_MM = 201, UST_LF = 301, UST_FOOT_SINGLE_QUOTE = 302, UST_INCH_DOUBLE_QUOTE = 601, UST_ACRES = 701, UST_HECTARES = 801, UST_CY = 1001, UST_SF = 1101, UST_FT_SUP_2 = 1102, UST_FT_CARET_2 = 1103, UST_M_SUP_2 = 1201, UST_M_CARET_2 = 1202, UST_CF = 1301, UST_FT_SUP_3 = 1302, UST_FT_CARET_3 = 1303, UST_M_SUP_3 = 1401, UST_M_CARET_3 = 1402, UST_DEGREE_SYMBOL = 1501, UST_PERCENT_SIGN = 1901, ...
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Convert a UnitSymbolType enumeration value &nbsp; /// to a brief human readable abbreviation string. &nbsp; /// &lt;/summary&gt; &nbsp; public static string UnitSymbolTypeString( &nbsp; &nbsp; UnitSymbolType u ) &nbsp; { &nbsp; &nbsp; string s = u.ToString(); &nbsp; &nbsp; &nbsp; Debug.Assert( s.StartsWith( &quot;UST_&quot; ), &nbsp; &nbsp; &nbsp; &quot;expected UnitSymbolType enumeration value &quot; &nbsp; &nbsp; &nbsp; + &quot;to begin with 'UST_'&quot; ); &nbsp; &nbsp; &nbsp; s = s.Substring( 4 ) &nbsp; &nbsp; &nbsp; .Replace( &quot;_SUP_&quot;, &quot;^&quot; ) &nbsp; &nbsp; &nbsp; .ToLower(); &nbsp; &nbsp; &nbsp; return s; &nbsp; } &nbsp;
```

```csharp
&nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; DisplayUnitType n &nbsp; &nbsp; &nbsp; = DisplayUnitType.DUT_GALLONS_US; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;Here is a list of the first {0} &quot; &nbsp; &nbsp; &nbsp; + &quot;display unit types with The Building Coder &quot; &nbsp; &nbsp; &nbsp; + &quot;abbreviation and the valid unit symbols:\n&quot;, &nbsp; &nbsp; &nbsp; (int) n - 1 ); &nbsp; &nbsp; &nbsp; string valid_unit_symbols; &nbsp; &nbsp; &nbsp; for( DisplayUnitType i = DisplayUnitType &nbsp; &nbsp; &nbsp; .DUT_METERS; i &lt; n; ++i ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; valid_unit_symbols = string.Join( &quot;, &quot;, &nbsp; &nbsp; &nbsp; &nbsp; FormatOptions.GetValidUnitSymbols( i ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .Select&lt;UnitSymbolType, string&gt;( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; u =&gt; Util.UnitSymbolTypeString( u ) ) ); &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;{0,6} - {1}: {2}&quot;, &nbsp; &nbsp; &nbsp; &nbsp; Util.DisplayUnitTypeAbbreviation[(int)i], &nbsp; &nbsp; &nbsp; &nbsp; LabelUtils.GetLabelFor( i ), &nbsp; &nbsp; &nbsp; &nbsp; valid_unit_symbols, &nbsp; &nbsp; &nbsp; &nbsp; i ); &nbsp; &nbsp; } &nbsp; &nbsp; return Result.Succeeded; &nbsp; }
```
