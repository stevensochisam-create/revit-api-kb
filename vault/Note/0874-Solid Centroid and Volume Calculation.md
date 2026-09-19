---
num: 874
date: 2012-12-19
themes: [Geometry]
tags: [revit-api, tbc]
---

# Solid Centroid and Volume Calculation

<https://jeremytammik.github.io/tbc/a/0874_centroid.htm>

```csharp
for each point dx += point.x dy += point.y dz += point.z count ++ dx/=count dy/=count dz/=count for each point point.x-=dx point.y-=dy point.z-=dz
```

```csharp
for each point mindx = min( point.x, mindx ) maxdx = max( point.x, maxdx ) same for y and z dx = (mindx + maxdx) / 2 same for dy, dz; for each point point.x -= dx same for y and z
```

```csharp
x1*(y2*z3 - y3*z2) + y1*(z2*x3 - z3*x2) + z1*(x2*y3 - x3*y2)
```

```csharp
var cx, cy, cz, volume, v, i, x1, y1, z1, x2, y2, z2, x3, y3, z3; volume = 0; cx = 0; cy = 0; cz = 0; // Assuming vertices are in vertX[i], vertY[i], and vertZ[i] // and faces are faces[i, j] where the first index indicates the // face and the second index indicates the vertex of that face // The value in the faces array is an index into the vertex array i = 0; repeat (numFaces) { x1 = vertX[faces[i, 0]]; y1 = vertY[faces[i, 0]]; z1 = vertZ[faces[i, 0]]; x2 = vertX[faces[i, 1]]; y2 = vertY[faces[i, 1]]; z2 = vertZ[faces[i, 1]]; x3 = vertX[faces[i, 2]]; y3 = vertY[faces[i, 2]]; z3 = vertZ[faces[i, 2]]; v = x1*(y2*z3 - y3*z2) + y1*(z2*x3 - z3*x2) + z1*(x2*y3 - x3*y2); volume += v; cx += (x1 + x2 + x3)*v; cy += (y1 + y2 + y3)*v; cz += (z1 + z2 + z3)*v; i += 1; } // Set centroid coordinates to their final value cx /= 4 * volume; cy /= 4 * volume; cz /= 4 * volume; // And, just in case you want to know the total volume of the model: volume /= 6;
```

```csharp
A = sqrt( s * (s - a) * (s - b) * (s - c) )
```
