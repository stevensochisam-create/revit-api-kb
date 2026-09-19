---
type: NumberingSchema
namespace: Autodesk.Revit.DB
version: 2024
members: 18
tags: [revit-api, class]
---

# NumberingSchema

`Autodesk.Revit.DB.NumberingSchema` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AppendSequence | 2015 | `public void AppendSequence ( string fromPartition , string toPartition )` |
| Method | AssignElementsToSequence | 2015 | `public void AssignElementsToSequence ( ISet < ElementId > elementIds , string partitionName )` |
| Method | ChangeNumber | 2015 | `public IList < ElementId > ChangeNumber ( string partition , int fromNumber , int toNumber )` |
| Method | GetMinimumNumberOfDigits | 2015 | `public static int GetMinimumNumberOfDigits ( Document document )` |
| Method | GetNumberingSchema | 2015 | `public static NumberingSchema GetNumberingSchema ( Document document , NumberingSchemaType schemaType )` |
| Method | GetNumberingSequences | 2015 | `public IList < string > GetNumberingSequences ()` |
| Method | GetNumbers | 2015 | `public IList < IntegerRange > GetNumbers ( string partition )` |
| Method | GetSchemasInDocument | 2015 | `public static ISet < ElementId > GetSchemasInDocument ( Document document )` |
| Method | IsValidPartitionName | 2015 | `public static bool IsValidPartitionName ( string name , out string message )` |
| Method | MergeSequences | 2015 | `public void MergeSequences ( IList < string > sourcePartitions , string newPartition )` |
| Method | MoveSequence | 2015 | `public void MoveSequence ( string fromPartition , string newPartition )` |
| Method | RemoveGaps | 2015 | `public void RemoveGaps ( string partition )` |
| Method | SetMinimumNumberOfDigits | 2015 | `public static void SetMinimumNumberOfDigits ( Document document , int value )` |
| Method | ShiftNumbers | 2015 | `public void ShiftNumbers ( string partition , int firstNumber )` |
| Property | MaximumStartingNumber | 2015 | `public static int MaximumStartingNumber { get ; }` |
| Property | NumberingParameterId | 2015 | `public ElementId NumberingParameterId { get ; }` |
| Property | Parameter | — | `` |
| Property | SchemaType | 2015 | `public NumberingSchemaType SchemaType { get ; }` |