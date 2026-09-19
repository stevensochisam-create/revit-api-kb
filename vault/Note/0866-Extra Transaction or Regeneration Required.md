---
num: 866
date: 2012-12-03
themes: [Pitfall, Transaction]
tags: [revit-api, tbc]
---

# Extra Transaction or Regeneration Required

<https://jeremytammik.github.io/tbc/a/0866_extra_transaction.htm>

```csharp
doc.LoadFamilySymbol( [my_tag_family.rfa], [type_name], out tagType); IndependentTag tag = doc.Create.NewTag( doc.ActiveView, element, true, TagMode.TM_ADDBY_CATEGORY, TagOrientation.Horizontal, XYZ.Zero); tag.ChangeTypeId(tagType.Id);
```

```csharp
[Transaction( TransactionMode.Manual )] public class Command : IExternalCommand { &nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication uiapp = commandData.Application; &nbsp; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; &nbsp; Application app = uiapp.Application; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; Selection sel = uidoc.Selection; &nbsp; &nbsp; FamilyInstance inst = null; &nbsp; &nbsp; &nbsp; if( 1 == sel.Elements.Size ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; foreach( Element e in sel.Elements ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; inst = e as FamilyInstance; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; if( null == inst ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; message = &quot;Please select one &quot; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;single structural column&quot;; &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; using( Transaction tx &nbsp; &nbsp; &nbsp; = new Transaction( doc ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; tx.Start( &quot;Duplicate Symbol&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; FamilySymbol symbol = inst.Symbol; &nbsp; &nbsp; &nbsp; &nbsp; string name = symbol.Name &nbsp; &nbsp; &nbsp; &nbsp; + DateTime.Now.Ticks.ToString(); &nbsp; &nbsp; &nbsp; &nbsp; int nMaterialsBefore &nbsp; &nbsp; &nbsp; &nbsp; = symbol.Materials.Size; &nbsp; &nbsp; &nbsp; &nbsp; symbol = inst.Symbol.Duplicate( name ) &nbsp; &nbsp; &nbsp; &nbsp; as FamilySymbol; &nbsp; &nbsp; &nbsp; &nbsp; // The model is in a temporary state that does &nbsp; &nbsp; &nbsp; // not make sense. Regenerate to clean this up. &nbsp; &nbsp; &nbsp; &nbsp; int nMaterialsAfter &nbsp; &nbsp; &nbsp; &nbsp; = symbol.Materials.Size; &nbsp; &nbsp; &nbsp; &nbsp; doc.Regenerate(); &nbsp; &nbsp; &nbsp; &nbsp; nMaterialsAfter = symbol.Materials.Size; &nbsp; &nbsp; &nbsp; &nbsp; Debug.Assert( &nbsp; &nbsp; &nbsp; &nbsp; nMaterialsAfter.Equals( nMaterialsBefore ), &nbsp; &nbsp; &nbsp; &nbsp; &quot;why does the material get lost, please?&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; tx.Commit(); &nbsp; &nbsp; } &nbsp; &nbsp; return Result.Succeeded; &nbsp; } }
```
