---
type: FabricationConfiguration
namespace: Autodesk.Revit.DB
version: 2024
members: 67
tags: [revit-api, class]
---

# FabricationConfiguration

`Autodesk.Revit.DB.FabricationConfiguration` · Revit 2024 · 67 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AncillaryExists | 2018 | `public bool AncillaryExists ( int ancillaryId )` |
| Method | AreItemFilesLoaded | 2019 | `public bool AreItemFilesLoaded ( IList < FabricationItemFile > itemFiles )` |
| Method | CanBeSwapped | 2016 | `public bool CanBeSwapped ()` |
| Method | CanUnloadItemFiles | 2019 | `public bool CanUnloadItemFiles ( IList < FabricationItemFile > itemFiles )` |
| Method | CustomDataExists | 2018 | `public bool CustomDataExists ( int customDataId )` |
| Method | DamperExists | 2018 | `public bool DamperExists ( int damperId )` |
| Method | GetAllDampers | 2017 Subscription Update | `public IList < int > GetAllDampers ()` |
| Method | GetAllFabricationConnectorDefinitions | 2016 | `public IList < int > GetAllFabricationConnectorDefinitions ( ConnectorDomainType domain , ConnectorProfileType shape )` |
| Method | GetAllInsulationSpecifications | 2016 | `public IList < int > GetAllInsulationSpecifications ( FabricationPart pFabPart )` |
| Method | GetAllLoadedItemFiles | 2019 | `public IList < FabricationItemFile > GetAllLoadedItemFiles ()` |
| Method | GetAllLoadedServices | 2016 | `public IList < FabricationService > GetAllLoadedServices ()` |
| Method | GetAllMaterials | 2016 | `public IList < int > GetAllMaterials ( FabricationPart part )` |
| Method | GetAllPartCustomData | 2017 Subscription Update | `public IList < int > GetAllPartCustomData ()` |
| Method | GetAllPartStatuses | 2017 Subscription Update | `public IList < int > GetAllPartStatuses ()` |
| Method | GetAllServices | 2016 | `public IList < FabricationService > GetAllServices ()` |
| Method | GetAllSpecifications | 2016 | `public IList < int > GetAllSpecifications ( FabricationPart part )` |
| Method | GetAllUsedItemFiles | 2019 | `public IList < FabricationItemFile > GetAllUsedItemFiles ()` |
| Method | GetAllUsedServices | 2016 | `public IList < FabricationService > GetAllUsedServices ()` |
| Method | GetAncillaries | 2017 Subscription Update | `public IList < int > GetAncillaries ( FabricationAncillaryType type , bool includeKits , bool filterKits )` |
| Method | GetAncillaryGroup | 2017 Subscription Update | `public string GetAncillaryGroup ( int ancillaryId )` |
| Method | GetAncillaryGroupName | 2017 Subscription Update | `public string GetAncillaryGroupName ( int ancillaryId )` |
| Method | GetAncillaryName | 2017 Subscription Update | `public string GetAncillaryName ( int ancillaryId )` |
| Method | GetDamperName | 2017 Subscription Update | `public string GetDamperName ( int damperId )` |
| Method | GetFabricationConfiguration | 2016 | `public static FabricationConfiguration GetFabricationConfiguration ( Document document )` |
| Method | GetFabricationConfigurationInfo | 2016 | `public FabricationConfigurationInfo GetFabricationConfigurationInfo ()` |
| Method | GetFabricationConnectorDomain | 2016 | `public ConnectorDomainType GetFabricationConnectorDomain ( int fabricationConnectorId )` |
| Method | GetFabricationConnectorGroup | 2016 | `public string GetFabricationConnectorGroup ( int fabricationConnectorId )` |
| Method | GetFabricationConnectorName | 2016 | `public string GetFabricationConnectorName ( int fabricationConnectorId )` |
| Method | GetFabricationConnectorShape | 2016 | `public ConnectorProfileType GetFabricationConnectorShape ( int fabricationConnectorId )` |
| Method | GetInsulationSpecificationAbbreviation | 2017 | `public string GetInsulationSpecificationAbbreviation ( int insulationSpecificationId )` |
| Method | GetInsulationSpecificationGroup | 2016 | `public string GetInsulationSpecificationGroup ( int specId )` |
| Method | GetInsulationSpecificationName | 2016 | `public string GetInsulationSpecificationName ( int specId )` |
| Method | GetItemFolders | 2019 | `public IList < FabricationItemFolder > GetItemFolders ()` |
| Method | GetMaterialAbbreviation | 2017 | `public string GetMaterialAbbreviation ( int materialId )` |
| Method | GetMaterialByGUID | 2024 | `public int GetMaterialByGUID ( Guid materialGUID )` |
| Method | GetMaterialGUID | 2024 | `public Guid GetMaterialGUID ( int materialId )` |
| Method | GetMaterialGaugeByGUID | 2024 | `public int GetMaterialGaugeByGUID ( Guid gaugeGUID , int materialId )` |
| Method | GetMaterialGaugeGUID | 2024 | `public Guid GetMaterialGaugeGUID ( int materialId , int gaugeId )` |
| Method | GetMaterialGroup | 2016 | `public string GetMaterialGroup ( int materialId )` |
| Method | GetMaterialName | 2016 | `public string GetMaterialName ( int materialId )` |
| Method | GetPartCustomDataName | 2017 Subscription Update | `public string GetPartCustomDataName ( int customDataId )` |
| Method | GetPartCustomDataType | 2017 Subscription Update | `public FabricationCustomDataType GetPartCustomDataType ( int customDataId )` |
| Method | GetPartStatusDescription | 2017 Subscription Update | `public string GetPartStatusDescription ( int statusId )` |
| Method | GetProfile | 2016 | `public string GetProfile ()` |
| Method | GetService | 2016 | `public FabricationService GetService ( int serviceId )` |
| Method | GetServiceByGUID | 2024 | `public int GetServiceByGUID ( Guid serviceGUID )` |
| Method | GetServiceGUID | 2024 | `public Guid GetServiceGUID ( int serviceId )` |
| Method | GetServiceTypeName | 2018 | `public string GetServiceTypeName ( int serviceTypeId )` |
| Method | GetSpecificationAbbreviation | 2017 | `public string GetSpecificationAbbreviation ( int specificationId )` |
| Method | GetSpecificationByGUID | 2024 | `public int GetSpecificationByGUID ( Guid specificationGUID )` |
| Method | GetSpecificationGUID | 2024 | `public Guid GetSpecificationGUID ( int specificationId )` |
| Method | GetSpecificationGroup | 2016 | `public string GetSpecificationGroup ( int specId )` |
| Method | GetSpecificationName | 2016 | `public string GetSpecificationName ( int specId )` |
| Method | HasValidConfiguration | 2016 | `public bool HasValidConfiguration ()` |
| Method | IsAncillaryKit | 2017 Subscription Update | `public bool IsAncillaryKit ( int ancillaryId )` |
| Method | LoadItemFiles | 2019 | `public IList < FabricationItemFile > LoadItemFiles ( IList < FabricationItemFile > itemFiles )` |
| Method | LoadServices | 2016 | `public IList < int > LoadServices ( IList < int > serviceIds )` |
| Method | LocateFabricationConnector | 2016 | `public int LocateFabricationConnector ( string group , string name , ConnectorDomainType domain , ConnectorProfileType shape )` |
| Method | LocateInsulationSpecification | 2016 | `public int LocateInsulationSpecification ( string group , string name )` |
| Method | LocateMaterial | 2016 | `public int LocateMaterial ( string group , string name )` |
| Method | LocateSpecification | 2016 | `public int LocateSpecification ( string group , string name )` |
| Method | ReloadConfiguration | 2016 | `public ConfigurationReloadInfo ReloadConfiguration ()` |
| Method | SetConfiguration | — | `` |
| Method | SetServicesToLoad | 2024 | `public bool SetServicesToLoad ( IList < int > serviceIds )` |
| Method | UnloadItemFiles | 2019 | `public void UnloadItemFiles ( IList < FabricationItemFile > itemFiles )` |
| Method | UnloadServices | 2016 | `public void UnloadServices ( IList < int > serviceIds )` |
| Property | Parameter | — | `` |