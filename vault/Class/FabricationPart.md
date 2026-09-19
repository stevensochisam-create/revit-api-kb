---
type: FabricationPart
namespace: Autodesk.Revit.DB
version: 2024
members: 116
tags: [revit-api, class]
---

# FabricationPart

`Autodesk.Revit.DB.FabricationPart` · Revit 2024 · 116 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddPartCustomData | 2018 | `public bool AddPartCustomData ( int customId )` |
| Method | AdjustEndLength | 2017 | `public double AdjustEndLength ( Connector connector , double lengthToAdjust , bool totalLengthOnly )` |
| Method | AlignPartByConnector | 2018 | `public static bool AlignPartByConnector ( Document document , Connector connector , XYZ position , double rotation , double rotationPerpendicular , double slope , FabricationPartJustification justification , Transform tr` |
| Method | AlignPartByConnectorToConnector | 2018 | `public static bool AlignPartByConnectorToConnector ( Document document , Connector connector , Connector fixedConnector , double rotation , double slope , FabricationPartJustification justification )` |
| Method | AlignPartByConnectors | 2016 | `public static bool AlignPartByConnectors ( Document document , Connector connector , Connector toConnector , double axisRotation )` |
| Method | AlignPartByInsertionPoint | 2018 | `public static bool AlignPartByInsertionPoint ( Document document , ElementId partId , XYZ position , double rotation , double rotationPerpendicular , double slope , FabricationPartJustification justification , Transform ` |
| Method | AlignPartByInsertionPointAndCutInToStraight | 2018 | `public static bool AlignPartByInsertionPointAndCutInToStraight ( Document document , ElementId straightId , ElementId partId , XYZ position , double rotation , double slope , bool flip )` |
| Method | CanASlopeBeApplied | 2018 | `public bool CanASlopeBeApplied ()` |
| Method | CanAdjustEndLength | 2017 | `public bool CanAdjustEndLength ( Connector connector )` |
| Method | CanFlipPart | 2023 | `public bool CanFlipPart ()` |
| Method | CanSplitStraight | 2018 | `public bool CanSplitStraight ( XYZ position )` |
| Method | ConnectAndCouple | 2016 | `public static bool ConnectAndCouple ( Document document , Connector connector , Connector toConnector )` |
| Method | Create | — | `` |
| Method | CreateHanger | — | `` |
| Method | Flip | 2023 | `public bool Flip ()` |
| Method | GetCalculatedDimensionValue | 2016 | `public string GetCalculatedDimensionValue ( FabricationDimensionDefinition dim )` |
| Method | GetDimensionCalculatedOptions | 2016 | `public IList < string > GetDimensionCalculatedOptions ( FabricationDimensionDefinition dim )` |
| Method | GetDimensionValue | 2016 | `public double GetDimensionValue ( FabricationDimensionDefinition dim )` |
| Method | GetDimensions | 2016 | `public IList < FabricationDimensionDefinition > GetDimensions ()` |
| Method | GetHostedInfo | 2016 | `public FabricationHostedInfo GetHostedInfo ()` |
| Method | GetInsulationLiningGeometry | 2019.1 | `public GeometryElement GetInsulationLiningGeometry ()` |
| Method | GetPartAncillaryUsage | 2017 Subscription Update | `public IList < FabricationAncillaryUsage > GetPartAncillaryUsage ()` |
| Method | GetPartCustomDataInteger | 2017 Subscription Update | `public int GetPartCustomDataInteger ( int customId )` |
| Method | GetPartCustomDataReal | 2017 Subscription Update | `public double GetPartCustomDataReal ( int customId )` |
| Method | GetPartCustomDataText | 2017 Subscription Update | `public string GetPartCustomDataText ( int customId )` |
| Method | GetProductListEntryCount | 2016 Subscription Release | `public int GetProductListEntryCount ()` |
| Method | GetProductListEntryName | 2016 Subscription Release | `public string GetProductListEntryName ( int index )` |
| Method | GetRodInfo | 2016 | `public FabricationRodInfo GetRodInfo ()` |
| Method | GetTransform | 2016 | `public Transform GetTransform ()` |
| Method | GetVersionHistory | 2019 | `public IList < FabricationVersionInfo > GetVersionHistory ()` |
| Method | HasCustomData | 2017 Subscription Update | `public bool HasCustomData ( int customId )` |
| Method | HasNoConnections | 2018 | `public bool HasNoConnections ()` |
| Method | IsAHanger | 2016 | `public bool IsAHanger ()` |
| Method | IsAStraight | 2016 | `public bool IsAStraight ()` |
| Method | IsATap | 2016 | `public bool IsATap ()` |
| Method | IsDimensionCalculated | 2016 | `public bool IsDimensionCalculated ( FabricationDimensionDefinition dim )` |
| Method | IsProductList | 2016 Subscription Release | `public bool IsProductList ()` |
| Method | IsProductListEntryCompatibleSize | 2016 Subscription Release | `public bool IsProductListEntryCompatibleSize ( int productEntry )` |
| Method | IsSameAs | 2018 | `public bool IsSameAs ( FabricationPart part , IList < FabricationPartCompareType > ignoreFields )` |
| Method | OptimizeLengths | 2016 | `public static ISet < ElementId > OptimizeLengths ( Document document , ISet < ElementId > partIds )` |
| Method | PlaceAsTap | 2016 | `public static void PlaceAsTap ( Document document , Connector tapPartConnector , Connector hostPartConnector , double distance , double axisRotation , double secondaryAxisRotation )` |
| Method | PlaceFittingAsCutIn | 2017 | `public static bool PlaceFittingAsCutIn ( Document document , ElementId straightId , ElementId fittingId , XYZ position , Connector fittingConnector , double axisRotation )` |
| Method | RemovePartCustomData | 2018 | `public bool RemovePartCustomData ( int customId )` |
| Method | Reposition | 2017 | `public static void Reposition ( Document document , ElementId partId )` |
| Method | RotateConnectedPartByConnector | 2016 Subscription Release | `public static void RotateConnectedPartByConnector ( Document document , Connector connector , double axisRotationBy )` |
| Method | RotateConnectedTap | 2016 Subscription Release | `public static void RotateConnectedTap ( Document document , FabricationPart tap , double primaryAxisRotateBy , double secondaryAxisRotateBy )` |
| Method | SaveAsFabricationJob | 2019 | `public static ISet < ElementId > SaveAsFabricationJob ( Document document , ISet < ElementId > ids , string filename , FabricationSaveJobOptions saveOptions )` |
| Method | SetCalculatedDimensionValue | 2016 | `public void SetCalculatedDimensionValue ( FabricationDimensionDefinition dim , string value )` |
| Method | SetDimensionValue | 2016 | `public void SetDimensionValue ( FabricationDimensionDefinition dim , double newValue )` |
| Method | SetPartCustomDataInteger | 2018 | `public void SetPartCustomDataInteger ( int customId , int value )` |
| Method | SetPartCustomDataReal | 2018 | `public void SetPartCustomDataReal ( int customId , double value )` |
| Method | SetPartCustomDataText | 2017 Subscription Update | `public void SetPartCustomDataText ( int customId , string value )` |
| Method | SetPositionByEnd | 2016 | `public void SetPositionByEnd ( Connector connector , XYZ position )` |
| Method | SplitStraight | — | `` |
| Method | StretchAndFit | 2017 | `public static FabricationPartFitResult StretchAndFit ( Document document , Connector stretchConnector , FabricationPartRouteEnd target , out ISet < ElementId > newPartIds )` |
| Property | Alias | 2017 | `public string Alias { get ; }` |
| Property | BottomOfPartElevation | 2017 | `public double BottomOfPartElevation { get ; }` |
| Property | CenterlineLength | 2018.1 | `public double CenterlineLength { get ; }` |
| Property | ConnectorManager | 2016 | `public ConnectorManager ConnectorManager { get ; }` |
| Property | CutType | 2017 | `public int CutType { get ; }` |
| Property | DomainType | 2016 | `public ConnectorDomainType DomainType { get ; }` |
| Property | DoubleWallMaterial | 2017 | `public int DoubleWallMaterial { get ; }` |
| Property | DoubleWallMaterialArea | 2017 | `public double DoubleWallMaterialArea { get ; }` |
| Property | DoubleWallMaterialThickness | 2017 | `public double DoubleWallMaterialThickness { get ; }` |
| Property | FreeSize | 2019 | `public string FreeSize { get ; }` |
| Property | GeometryChecksum | 2018.2 | `public AssetPropertyUInt64 GeometryChecksum { get ; }` |
| Property | HangerRodKit | 2017 Subscription Update | `public int HangerRodKit { get ; set ; }` |
| Property | HasDoubleWall | 2017 | `public bool HasDoubleWall { get ; }` |
| Property | HasInsulation | 2017 | `public bool HasInsulation { get ; }` |
| Property | HasLining | 2017 | `public bool HasLining { get ; }` |
| Property | InsulationArea | 2017 | `public double InsulationArea { get ; }` |
| Property | InsulationSpecification | 2016 | `public int InsulationSpecification { get ; set ; }` |
| Property | InsulationThickness | 2017 | `public double InsulationThickness { get ; }` |
| Property | InsulationType | 2017 | `public string InsulationType { get ; }` |
| Property | IsBoughtOut | 2017 | `public bool IsBoughtOut { get ; }` |
| Property | ItemCustomId | 2017 | `public int ItemCustomId { get ; }` |
| Property | ItemNumber | 2017 | `public string ItemNumber { get ; set ; }` |
| Property | LevelOffset | 2016 | `public double LevelOffset { get ; }` |
| Property | LiningArea | 2017 | `public double LiningArea { get ; }` |
| Property | LiningThickness | 2017 | `public double LiningThickness { get ; }` |
| Property | LiningType | 2017 | `public string LiningType { get ; }` |
| Property | Material | 2016 | `public int Material { get ; set ; }` |
| Property | MaterialGauge | 2024 | `public int MaterialGauge { get ; }` |
| Property | MaterialThickness | 2017 | `public double MaterialThickness { get ; }` |
| Property | Notes | 2017 | `public string Notes { get ; set ; }` |
| Property | Origin | 2016 | `public XYZ Origin { get ; }` |
| Property | OverallSize | 2017 | `public string OverallSize { get ; }` |
| Property | Parameter | — | `` |
| Property | PartGuid | 2017 Subscription Update | `public Guid PartGuid { get ; }` |
| Property | PartStatus | 2017 Subscription Update | `public int PartStatus { get ; set ; }` |
| Property | ProductCode | 2016 | `public string ProductCode { get ; }` |
| Property | ProductDataRange | 2017 | `public string ProductDataRange { get ; }` |
| Property | ProductFinishDescription | 2017 | `public string ProductFinishDescription { get ; }` |
| Property | ProductInstallType | 2017 | `public string ProductInstallType { get ; }` |
| Property | ProductListEntry | 2016 Subscription Release | `public int ProductListEntry { get ; set ; }` |
| Property | ProductLongDescription | 2017 | `public string ProductLongDescription { get ; }` |
| Property | ProductMaterialDescription | 2017 | `public string ProductMaterialDescription { get ; }` |
| Property | ProductName | 2017 | `public string ProductName { get ; }` |
| Property | ProductOriginalEquipmentManufacture | 2017 | `public string ProductOriginalEquipmentManufacture { get ; }` |
| Property | ProductShortDescription | 2017 | `public string ProductShortDescription { get ; }` |
| Property | ProductSizeDescription | 2017 | `public string ProductSizeDescription { get ; }` |
| Property | ProductSpecificationDescription | 2017 | `public string ProductSpecificationDescription { get ; }` |
| Property | ServiceAbbreviation | 2017 | `public string ServiceAbbreviation { get ; }` |
| Property | ServiceId | 2016 Subscription Release | `public int ServiceId { get ; set ; }` |
| Property | ServiceName | 2017 | `public string ServiceName { get ; }` |
| Property | ServiceType | 2018 | `public int ServiceType { get ; }` |
| Property | SheetMetalArea | 2017 | `public double SheetMetalArea { get ; }` |
| Property | Size | 2017 | `public string Size { get ; }` |
| Property | Slope | 2017 | `public double Slope { get ; }` |
| Property | Specification | 2016 | `public int Specification { get ; set ; }` |
| Property | SpoolName | 2018 | `public string SpoolName { get ; set ; }` |
| Property | TopOfPartElevation | 2017 | `public double TopOfPartElevation { get ; }` |
| Property | ValidationStatus | 2016 | `public ValidationStatus ValidationStatus { get ; }` |
| Property | Vendor | 2017 | `public string Vendor { get ; }` |
| Property | VendorCode | 2017 | `public string VendorCode { get ; }` |
| Property | Weight | 2017 | `public double Weight { get ; }` |