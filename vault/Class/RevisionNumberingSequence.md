---
type: RevisionNumberingSequence
namespace: Autodesk.Revit.DB
version: 2024
members: 13
tags: [revit-api, class]
---

# RevisionNumberingSequence

`Autodesk.Revit.DB.RevisionNumberingSequence` · Revit 2024 · 13 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | CreateAlphanumericSequence | 2022 | `public static RevisionNumberingSequence CreateAlphanumericSequence ( Document document , string name , AlphanumericRevisionSettings settings )` |
| Method | CreateNumericSequence | 2022 | `public static RevisionNumberingSequence CreateNumericSequence ( Document document , string name , NumericRevisionSettings settings )` |
| Method | GetAllRevisionNumberingSequences | 2022 | `public static ISet < ElementId > GetAllRevisionNumberingSequences ( Document document )` |
| Method | GetAlphanumericRevisionSettings | 2022 | `public AlphanumericRevisionSettings GetAlphanumericRevisionSettings ()` |
| Method | GetNumericRevisionSettings | 2022 | `public NumericRevisionSettings GetNumericRevisionSettings ()` |
| Method | HasValidAlphanumericRevisionSettings | 2022 | `public bool HasValidAlphanumericRevisionSettings ()` |
| Method | HasValidNumericRevisionSettings | 2022 | `public bool HasValidNumericRevisionSettings ()` |
| Method | HasValidRevisionSettingsForNumberType | 2022 | `public bool HasValidRevisionSettingsForNumberType ()` |
| Method | SetAlphanumericRevisionSettings | 2022 | `public void SetAlphanumericRevisionSettings ( AlphanumericRevisionSettings settings )` |
| Method | SetNumericRevisionSettings | 2022 | `public void SetNumericRevisionSettings ( NumericRevisionSettings settings )` |
| Property | NumberType | 2022 | `public RevisionNumberType NumberType { get ; }` |
| Property | Parameter | — | `` |
| Property | SequenceName | 2022 | `public string SequenceName { get ; set ; }` |