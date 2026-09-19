---
num: 1602
date: 2017-11-16
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# Migrating PlaceInstances to Revit 2018

<https://jeremytammik.github.io/tbc/a/1602_place_famil_instance.html>

```csharp
------ Rebuild All started: Project: PlaceInstances, Configuration: Debug Any CPU ------ error CS0246: The type or namespace name 'FamilySymbolSet' could not be found (are you missing a using directive or an assembly reference?) error CS1061: 'Family' does not contain a definition for 'Symbols' and no extension method 'Symbols' accepting a first argument of type 'Family' could be found (are you missing a using directive or an assembly reference?) warning CS0162: Unreachable code detected ========== Rebuild All: 0 succeeded, 1 failed, 0 skipped ==========
```

```csharp
&nbsp;&nbsp;FamilySymbolSet&nbsp;symbols&nbsp;=&nbsp;f.Symbols; &nbsp;&nbsp;//&nbsp;I&nbsp;have&nbsp;to&nbsp;convert&nbsp;the&nbsp;FamilySymbolSet&nbsp;to&nbsp;a &nbsp;&nbsp;//&nbsp;List,&nbsp;or&nbsp;the&nbsp;DataSource&nbsp;assignment&nbsp;will&nbsp;throw&nbsp; &nbsp;&nbsp;//&nbsp;an&nbsp;exception&nbsp;saying&nbsp;&quot;Complex&nbsp;DataBinding&nbsp; &nbsp;&nbsp;//&nbsp;accepts&nbsp;as&nbsp;a&nbsp;data&nbsp;source&nbsp;either&nbsp;an&nbsp;IList&nbsp;or &nbsp;&nbsp;//&nbsp;an&nbsp;IListSource. &nbsp;&nbsp;List&lt;FamilySymbol&gt;&nbsp;symbols2 &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;List&lt;FamilySymbol&gt;( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;symbols.Cast&lt;FamilySymbol&gt;()&nbsp;);
```

```csharp
&nbsp;&nbsp;ISet&lt;ElementId&gt;&nbsp;ids&nbsp;=&nbsp;f.GetFamilySymbolIds(); &nbsp;&nbsp;Document&nbsp;doc&nbsp;=&nbsp;f.Document; &nbsp;&nbsp;List&lt;FamilySymbol&gt;&nbsp;symbols2 &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;new&nbsp;List&lt;FamilySymbol&gt;(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ids.Select&lt;ElementId,&nbsp;FamilySymbol&gt;(&nbsp;id&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&gt;&nbsp;doc.GetElement(&nbsp;id&nbsp;)&nbsp;as&nbsp;FamilySymbol&nbsp;)&nbsp;);
```
