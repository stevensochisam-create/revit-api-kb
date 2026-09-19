---
num: 2054
date: 2024-09-22
themes: [Geometry, Pitfall]
tags: [revit-api, tbc]
---

# Solid Boolean Operation Alternatives

<https://jeremytammik.github.io/tbc/a/2054_boolean_alternative.html>

```csharp
public static bool WriteOff( this Solid solid, out List&lt;string&gt; listString) { listString = ["OFF"]; if(solid.CreateMesh(out var listVectors, out var listTri)) { listString.Add($"{listVectors.Count} {listTri.Count} 0"); listString.Add($""); foreach (var p in listVectors) { listString.Add(p.Write()); } foreach (var v in listTri) { listString.Add($"3 {v.iA} {v.iB} {v.iC}"); } return true; } return false; }
```

```csharp
public static bool CreateMesh( this Solid solid, out List&lt;XYZ&gt; listVectors, out List&lt;Tri&gt; listTri) { double k = UnitUtils.ConvertFromInternalUnits(1, UnitTypeId.Meters); listVectors = []; listTri = []; bool allPlanar = true; int indV = 0; foreach (Face face in solid.Faces) { if (face is PlanarFace pFace) { Mesh mesh = pFace.Triangulate(); for (int tN = 0; tN &lt; mesh.NumTriangles; tN++) { var tri = mesh.get_Triangle(tN); var pT = new int[3]; for (int vN = 0; vN &lt; 3; vN++) { var p = tri.get_Vertex(vN) * k; if (p.Contain(listVectors, out XYZ pF, out int index)) { pT[vN] = index; } else { pT[vN] = indV; listVectors.Add(p); indV++; } } listTri.Add(new(pT[2], pT[1], pT[0])); } } else { allPlanar = false; } } return allPlanar; }
```

```csharp
#pragma once bool load_from(const char* path, Mesh& output) { output.clear(); std::ifstream input; input.open(path); if (!input) { return false; } else if (!(input &gt;&gt; output)) { return false; } input.close(); return true; }>
```

```csharp
#pragma once bool boolean_simple(Mesh m1, Mesh m2, b_t type, Mesh& out) { out.clear(); int code = 0; if (!CGAL::is_triangle_mesh(m1)) { PMP::triangulate_faces(m1); } if (!CGAL::is_triangle_mesh(m2)) { PMP::triangulate_faces(m2); } if (type == b_t::join) { if (!PMP::corefine_and_compute_union(m1, m2, out)){ std::cout &lt;&lt; "fail_join "; return false; } } else if (type == b_t::inter) { if (!PMP::corefine_and_compute_intersection(m1, m2, out)){ std::cout &lt;&lt; "fail_inter "; return false; } } else if (type == b_t::dif) { if (!PMP::corefine_and_compute_difference(m1, m2, out)) { std::cout &lt;&lt; "fail_dif "; return false; } } else { throw; } return true; }
```

```csharp
#pragma once #include &lt;CGAL/Polygon_mesh_processing/IO/polygon_mesh_io.h&gt; bool save_to(const std::string path, Mesh input) { if (!CGAL::is_valid_polygon_mesh(input)) { return false; } try { if (CGAL::IO::write_polygon_mesh(path + ".off", input, CGAL::parameters::stream_precision(17))) { return true; } else { return false; } } catch (const std::exception& e) { std::cout &lt;&lt; "save_to: exception!" &lt;&lt; std::endl; } return false; }
```
