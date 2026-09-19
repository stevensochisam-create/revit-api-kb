---
type: DesignToFabricationConverter
namespace: Autodesk.Revit.DB.Fabrication
version: 2024
members: 11
tags: [revit-api, class]
---

# DesignToFabricationConverter

`Autodesk.Revit.DB.Fabrication.DesignToFabricationConverter` · Revit 2024 · 11 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Constructor | DesignToFabricationConverter | 2017 | `public DesignToFabricationConverter ( Document document )` |
| Method | Convert | 2017 | `public DesignToFabricationConverterResult Convert ( ISet < ElementId > selection , int serviceId )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetConvertedFabricationParts | 2017 | `public ISet < ElementId > GetConvertedFabricationParts ()` |
| Method | GetConvertedFabricationPartsWithInvalidConnections | 2017 | `public IDictionary < ElementId , ElementId > GetConvertedFabricationPartsWithInvalidConnections ()` |
| Method | GetDesignElementAndFabricationPartsWithDifferentOffsets | 2017 | `public IDictionary < ElementId , ISet < ElementId >> GetDesignElementAndFabricationPartsWithDifferentOffsets ()` |
| Method | GetDesignElementAndFabricationPartsWithOpenConnectors | 2017 | `public IDictionary < ElementId , ISet < ElementId >> GetDesignElementAndFabricationPartsWithOpenConnectors ()` |
| Method | GetElementsWithOpenConnector | 2017 | `public ISet < ElementId > GetElementsWithOpenConnector ()` |
| Method | GetPartialConvertFailureResults | 2017 | `public IList < PartialFailureResults > GetPartialConvertFailureResults ()` |
| Method | SetMapForFamilySymbolToFabricationPartType | 2022 | `public DesignToFabricationMappingResult SetMapForFamilySymbolToFabricationPartType ( IDictionary < ElementId , ElementId > typeMappings )` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |