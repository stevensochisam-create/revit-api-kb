---
num: 1616
date: 2018-01-10
themes: [Geometry]
tags: [revit-api, tbc]
---

# Transform Utils, DirectShape Builder and DevDays Online Webinars

<https://jeremytammik.github.io/tbc/a/1616_devdays_webinars.html>

```csharp
# place family instance, get default placement points, # subtract from my desired coordinates (list) and move element inst = AdaptiveComponentInstanceUtils.CreateAdaptiveComponentInstance( doc, inst) placePointIds = [] placePointIds = AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds( inst) for ind, item in enumerate(placePointIds): # assign a point object to refpt # refpt is the orginal point of the family # newpt the new point derived from pt information refpt = doc.GetElement(item) newpt = pt[ind] trans = newpt.Subtract(refpt.Position) ElementTransformUtils.MoveElement(doc, item, trans)
```

```csharp
(refpt as ReferencePoint).SetCoordinateSystem()
```

```csharp
Element refpt = doc.GetElement(item); XYZ newpt = pt[ind]; Transform tf = Transform.Identity; tf.Origin = newpt; (refpt as ReferencePoint).SetCoordinateSystem(tf);
```

```csharp
placePointIds = AdaptiveComponentInstanceUtils.GetInstancePlacementPointElementRefIds( inst): for ind, item in enumerate(placePointIds): refpt = doc.GetElement(item) newpt = pt[ind] tf = Transform.Identity tf.Origin = newpt refpt.SetCoordinateSystem(tf);
```
