---
type: ColorFillScheme
namespace: Autodesk.Revit.DB
version: 2024
members: 25
tags: [revit-api, class]
---

# ColorFillScheme

`Autodesk.Revit.DB.ColorFillScheme` · Revit 2024 · 25 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddEntry | 2022 | `public void AddEntry ( ColorFillSchemeEntry entry )` |
| Method | AreEntriesConsistentWithScheme | 2022 | `public EntryAndSchemeConsistency AreEntriesConsistentWithScheme ( IList < ColorFillSchemeEntry > entries )` |
| Method | CanDefineByRange | 2022 | `public bool CanDefineByRange ()` |
| Method | CanRemoveEntry | 2022 | `public bool CanRemoveEntry ( ColorFillSchemeEntry entry )` |
| Method | CanUpdateEntry | 2022 | `public bool CanUpdateEntry ( ColorFillSchemeEntry entry )` |
| Method | Duplicate | 2022 | `public ElementId Duplicate ( string name )` |
| Method | GetEntries | 2022 | `public IList < ColorFillSchemeEntry > GetEntries ()` |
| Method | GetFormatOptions | 2022 | `public FormatOptions GetFormatOptions ()` |
| Method | GetSupportedParameterIds | 2022 | `public IList < ElementId > GetSupportedParameterIds ()` |
| Method | IsEntryConsistentWithScheme | 2022 | `public EntryAndSchemeConsistency IsEntryConsistentWithScheme ( ColorFillSchemeEntry entry )` |
| Method | IsValidParameterDefinitionId | 2022 | `public bool IsValidParameterDefinitionId ( ElementId parameterId )` |
| Method | IsValidSchemeName | 2022 | `public bool IsValidSchemeName ( string name )` |
| Method | RemoveEntry | 2022 | `public void RemoveEntry ( ColorFillSchemeEntry entry )` |
| Method | SetEntries | 2022 | `public void SetEntries ( IList < ColorFillSchemeEntry > entries )` |
| Method | SetFormatOptions | 2022 | `public void SetFormatOptions ( FormatOptions formatOptions )` |
| Method | SortEntries | 2022 | `public void SortEntries ()` |
| Method | UpdateEntry | 2022 | `public void UpdateEntry ( ColorFillSchemeEntry entry )` |
| Property | AreaSchemeId | 2022 | `public ElementId AreaSchemeId { get ; }` |
| Property | CategoryId | 2022 | `public ElementId CategoryId { get ; }` |
| Property | IsByRange | 2022 | `public bool IsByRange { get ; set ; }` |
| Property | IsLinkedFilesIncluded | 2022 | `public bool IsLinkedFilesIncluded { get ; set ; }` |
| Property | Parameter | — | `` |
| Property | ParameterDefinition | 2022 | `public ElementId ParameterDefinition { get ; set ; }` |
| Property | StorageType | 2022 | `public StorageType StorageType { get ; }` |
| Property | Title | 2022 | `public string Title { get ; set ; }` |