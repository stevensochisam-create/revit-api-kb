---
num: 2007
date: 2023-09-13
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# System Family Predicate and Python Section Creation

<https://jeremytammik.github.io/tbc/a/2007_sys_fam_py_section.html>

```csharp
def raamstaat_sections(window): # find window dimensions, center and host(wall) window_bb = window.get_BoundingBox(doc.ActiveView) window_center = (window_bb.Min + window_bb.Max)/2 window_width = window.LookupParameter("Width").AsDouble() window_height = window.LookupParameter("Height").AsDouble() window_sill_height = window.LookupParameter("Sill Height").AsDouble() host = window.Host # vectors for view direction wall_ext = host.Orientation wall_direction = XYZ(wall_ext.Y, -wall_ext.X, wall_ext.Z) up_direction = XYZ.BasisZ wall_int = XYZ(-wall_ext.X, -wall_ext.Y, wall_ext.Z) ### BOUNDING BOX FOR ELEVATION # Calculate the bounding box min_point_elev = XYZ((-window_width/2) - 500/304.8, (-window_height/2) - window_sill_height - 750/304.8, -1000/304.8) max_point_elev = XYZ((window_width/2) + 500/304.8, (window_height/2) + 1000/304.8, 0) # create 'rotated' bounding box rotation_transform_elev = Transform.Identity rotation_transform_elev.Origin = window_center rotation_transform_elev.BasisX = wall_direction rotation_transform_elev.BasisY = up_direction rotation_transform_elev.BasisZ = wall_int rotated_bounding_box_elev = BoundingBoxXYZ() rotated_bounding_box_elev.Transform = rotation_transform_elev rotated_bounding_box_elev.Min = min_point_elev rotated_bounding_box_elev.Max = max_point_elev ### CREATE SECTION # create sections, change name, apply view template t = Transaction(doc, "create section") t.Start() type = window.LookupParameter("S3A_Type").AsString() #elevation newViewElev = ViewSection.CreateSection(doc, SectionTypes[1].Id, rotated_bounding_box_elev) newViewElev.Name = type + " - aanzicht TEST" newViewElev.ViewTemplateId = templateS.Id t.Commit()
```
