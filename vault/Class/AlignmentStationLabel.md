---
type: AlignmentStationLabel
namespace: Autodesk.Revit.DB.Infrastructure
version: 2024
members: 12
tags: [revit-api, class]
---

# AlignmentStationLabel

`Autodesk.Revit.DB.Infrastructure.AlignmentStationLabel` · Revit 2024 · 12 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | Create | 2021.1 | `public static AlignmentStationLabel Create ( Alignment alignment , View view , AlignmentStationLabelOptions options )` |
| Method | CreateRecommendedTypeForSet | 2021.1 | `public static ElementId CreateRecommendedTypeForSet ( Document document )` |
| Method | CreateSet | 2021.1 | `public static ICollection < AlignmentStationLabel > CreateSet ( Alignment alignment , View view , AlignmentStationLabelSetOptions options )` |
| Method | Get | 2021.1 | `public static AlignmentStationLabel Get ( Element element )` |
| Method | GetAlignmentStationLabels | — | `` |
| Method | IsRecommendedTypeForSet | 2021.1 | `public static bool IsRecommendedTypeForSet ( Element type )` |
| Method | IsValid | — | `` |
| Method | IsValid | 2021.1 | `public bool IsValid ()` |
| Method | IsValidType | 2021.1 | `public static bool IsValidType ( Element type )` |
| Property | AlignmentId | 2021.1 | `public ElementId AlignmentId { get ; }` |
| Property | Element | 2021.1 | `public Element Element { get ; }` |
| Property | Station | 2021.1 | `public double Station { get ; set ; }` |