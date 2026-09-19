---
num: 903
date: 2013-02-28
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# What's New in the Revit 2012 API

<https://jeremytammik.github.io/tbc/a/0903_whats_new_2012.htm>

```csharp
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-16&quot; standalone=&quot;no&quot;? &lt;RevitAddIns&gt; &nbsp; &lt;AddIn Type=&quot;Command&quot;&gt; &nbsp; &nbsp; &lt;Assembly&gt;Command.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;ClientId&gt;d7e30025-97d4-4012-a581-5f8ed8d18808&lt;/ClientId&gt; &nbsp; &nbsp; &lt;FullClassName&gt;Revit.Command&lt;/FullClassName&gt; &nbsp; &nbsp; &lt;Text&gt;Command&lt;/Text&gt; &nbsp; &nbsp; &lt;VendorId&gt;ADSK&lt;/VendorId&gt; &nbsp; &nbsp; &lt;VendorDescription&gt;Autodesk, www.autodesk.com&lt;/VendorDescription&gt; &nbsp; &lt;/AddIn&gt; &lt;/RevitAddIns&gt;
```

```csharp
// Create a data structure, attach it to a wall, // populate it with data, and retrieve the data // back from the wall public void StoreDataInWall( &nbsp; Wall wall, &nbsp; XYZ dataToStore ) { &nbsp; Transaction createSchemaAndStoreData &nbsp; &nbsp; = new Transaction(wall.Document, &quot;tCreateAndStore&quot;); &nbsp; createSchemaAndStoreData.Start(); &nbsp; SchemaBuilder schemaBuilder = new SchemaBuilder( &nbsp; &nbsp; new Guid(&quot;720080CB-DA99-40DC-9415-E53F280AA1F0&quot;)); &nbsp; // allow anyone to read the object &nbsp; schemaBuilder.SetReadAccessLevel(AccessLevel.Public); &nbsp; // restrict writing to this vendor only &nbsp; schemaBuilder.SetWriteAccessLevel(AccessLevel.Vendor); &nbsp; // required because of restricted write-access &nbsp; schemaBuilder.SetVendorId(&quot;ADSK&quot;); &nbsp; // create a field to store an XYZ &nbsp; FieldBuilder fieldBuilder = schemaBuilder &nbsp; &nbsp; .AddSimpleField(&quot;WireSpliceLocation&quot;, typeof(XYZ)); &nbsp; fieldBuilder.SetUnitType(UnitType.UT_Length); &nbsp; fieldBuilder.SetDocumentation( &nbsp; &nbsp; &quot;A stored location value representing a wiring splice in a wall.&quot;); &nbsp; schemaBuilder.SetSchemaName(&quot;WireSpliceLocation&quot;); &nbsp; // register the Schema object &nbsp; Schema schema = schemaBuilder.Finish(); &nbsp; // create an entity (object) for this schema (class) &nbsp; Entity entity = new Entity(schema); &nbsp; // get the field from the schema &nbsp; Field fieldSpliceLocation &nbsp; &nbsp; = schema.GetField(&quot;WireSpliceLocation&quot;); &nbsp; // set the value for this entity &nbsp; entity.Set&lt;XYZ&gt;(fieldSpliceLocation, &nbsp; &nbsp; dataToStore, DisplayUnitType.DUT_METERS); &nbsp; // store the entity in the element &nbsp; wall.SetEntity(entity); &nbsp; // get the data back from the wall &nbsp; Entity retrievedEntity = wall.GetEntity(schema); &nbsp; XYZ retrievedData = retrievedEntity.Get&lt;XYZ&gt;( &nbsp; &nbsp; schema.GetField(&quot;WireSpliceLocation&quot;), &nbsp; &nbsp; DisplayUnitType.DUT_METERS); &nbsp; createSchemaAndStoreData.Commit(); }
```

```csharp
&nbsp; ElementId categoryId = doc.get_Element( &nbsp; &nbsp; uidoc.Selection.GetElementIds(). &nbsp; FirstOrDefault() ).Category.Id; &nbsp; &nbsp; ElementId titleblockId &nbsp; &nbsp; = doc.TitleBlocks.Cast&lt;FamilySymbol&gt;() &nbsp; &nbsp; &nbsp; .First&lt;FamilySymbol&gt;().Id; &nbsp; &nbsp; AssemblyInstance instance = null; &nbsp; &nbsp; Transaction t = new Transaction( doc ); &nbsp; &nbsp; if( AssemblyInstance.IsValidNamingCategory( doc, &nbsp; &nbsp; categoryId, uidoc.Selection.GetElementIds() ) ) &nbsp; { &nbsp; &nbsp; t.SetName( &quot;Create Assembly Instance&quot; ); &nbsp; &nbsp; t.Start(); &nbsp; &nbsp; instance = AssemblyInstance.Create( doc, &nbsp; &nbsp; &nbsp; uidoc.Selection.GetElementIds(), categoryId ); &nbsp; &nbsp; t.Commit(); &nbsp; &nbsp; &nbsp; t.SetName( &quot;Set Assembly Name&quot; ); &nbsp; &nbsp; t.Start(); &nbsp; &nbsp; string assemblyName = &quot;Assembly #1&quot;; &nbsp; &nbsp; if( AssemblyInstance.IsValidAssemblyName( doc, &nbsp; &nbsp; &nbsp; assemblyName, categoryId ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; instance.AssemblyTypeName = assemblyName; &nbsp; &nbsp; } &nbsp; &nbsp; t.Commit(); &nbsp; }
```

```csharp
&nbsp; if( instance.AllowsAssemblyViewCreation() ) &nbsp; { &nbsp; &nbsp; ViewSheet viewSheet = AssemblyViewUtils &nbsp; &nbsp; &nbsp; .CreateSheet( doc, instance.Id, titleblockId ); &nbsp; &nbsp; &nbsp; View3D view3d = AssemblyViewUtils &nbsp; &nbsp; &nbsp; .Create3DOrthographic( doc, instance.Id ); &nbsp; &nbsp; &nbsp; ViewSection detailSectionA = AssemblyViewUtils &nbsp; &nbsp; &nbsp; .CreateDetailSection( doc, instance.Id, &nbsp; &nbsp; &nbsp; AssemblyDetailViewOrientation.DetailSectionA ); &nbsp; &nbsp; &nbsp; View materialTakeoff = AssemblyViewUtils &nbsp; &nbsp; &nbsp; .CreateMaterialTakeoff( doc, instance.Id ); &nbsp; &nbsp; &nbsp; View partList = AssemblyViewUtils &nbsp; &nbsp; &nbsp; .CreatePartList( doc, instance.Id ); &nbsp; }
```

```csharp
&lt;?xml version=&quot;1.0&quot; standalone=&quot;no&quot;?&gt; &lt;RevitAddIns&gt; &nbsp; &lt;AddIn Type=&quot;DBApplication&quot;&gt; &nbsp; &nbsp; &lt;Assembly&gt;MyDBLevelApplication.dll&lt;/Assembly&gt; &nbsp; &nbsp; &lt;AddInId&gt;DA3D570A-1AB3-4a4b-B09F-8C15DFEC6BF0&lt;/AddInId&gt; &nbsp; &nbsp; &lt;FullClassName&gt;MyCompany.MyDBLevelAddIn&lt;/FullClassName&gt; &nbsp; &nbsp; &lt;Name&gt;My DB-Level AddIn&lt;/Name&gt; &nbsp; &lt;/AddIn&gt; &lt;/RevitAddIns&gt;
```
