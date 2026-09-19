---
num: 519
date: 2011-01-19
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# Setting Duct Width and Height Requires Regeneration

<https://jeremytammik.github.io/tbc/a/0519_set_duct_width_height.htm>

```csharp
Result AddinTest1::Execute( &nbsp; ExternalCommandData^ commandData, &nbsp; System::String^% message, &nbsp; ElementSet^ elements) {&nbsp; &nbsp; Document ^doc = commandData-&gt;Application &nbsp; &nbsp; -&gt;ActiveUIDocument-&gt;Document; &nbsp; &nbsp; // Duct/bend IDs in example project &nbsp; &nbsp; int west_east&nbsp;&nbsp; = 505594; &nbsp; int north_south = 505598; &nbsp; int bend_id&nbsp; &nbsp;&nbsp; = 505610; &nbsp; &nbsp; ElementId ^elemId = gcnew ElementId(west_east); &nbsp; Element ^ductElem1 = doc-&gt;Element::get(elemId); &nbsp; &nbsp; elemId = gcnew ElementId(north_south); &nbsp; Element ^ductElem2 = doc-&gt;Element::get(elemId); &nbsp; &nbsp; elemId = gcnew ElementId(bend_id); &nbsp; Element ^bendElem1 = doc-&gt;Element::get(elemId); &nbsp; &nbsp; FamilyInstance ^bend &nbsp; &nbsp; = safe_cast&lt;FamilyInstance^&gt;(bendElem1); &nbsp; &nbsp; ConnectorSet ^cSet &nbsp; &nbsp; = bend-&gt;MEPModel-&gt;ConnectorManager-&gt;Connectors; &nbsp; &nbsp; Transaction tr(doc, L&quot;sizing&quot;); &nbsp; tr.Start(); &nbsp; &nbsp; for each (Connector ^connector in cSet) &nbsp; { &nbsp; &nbsp; if (connector-&gt;ConnectorType &nbsp; &nbsp; &nbsp; != ConnectorType::EndConn) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; connector-&gt;Width::set((500 * 0.0032808399)); &nbsp; &nbsp; connector-&gt;Height::set((500 * 0.0032808399));&nbsp;&nbsp; // This is not set into the drawing &nbsp; &nbsp; break; &nbsp; } &nbsp; &nbsp; tr.Commit(); &nbsp; &nbsp; return Result::Succeeded; }
```

```csharp
&nbsp; Transaction tr(doc, L&quot;sizing&quot;); &nbsp; tr.Start(); &nbsp; &nbsp; // We do separate transactions for both dimensions &nbsp; &nbsp; for each (Connector ^connector in cSet) &nbsp; { &nbsp; &nbsp; if (connector-&gt;ConnectorType &nbsp; &nbsp; &nbsp; != ConnectorType::EndConn) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; connector-&gt;Width::set((500 * 0.0032808399)); &nbsp; &nbsp; break; &nbsp; } &nbsp; &nbsp; tr.Commit(); &nbsp; &nbsp; tr.Start(); &nbsp; &nbsp; for each (Connector ^connector in cSet) &nbsp; { &nbsp; &nbsp; if (connector-&gt;ConnectorType &nbsp; &nbsp; &nbsp; != ConnectorType::EndConn) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; connector-&gt;Height::set((500 * 0.0032808399)); &nbsp; &nbsp; break; &nbsp; } &nbsp; &nbsp; tr.Commit();
```
