---
num: 382
date: 2010-06-06
themes: [Pitfall, Units]
tags: [revit-api, tbc]
---

# Voltage Units

<https://jeremytammik.github.io/tbc/a/0382_voltage_units.htm>

```csharp
enum BaseUnit { &nbsp; BU_Length = 0,&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; // length, feet (ft) &nbsp; BU_Angle,&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // angle, radian (rad) &nbsp; BU_Mass,&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; // mass, kilogram (kg) &nbsp; BU_Time,&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; // time, second (s) &nbsp; BU_Electric_Current,&nbsp;&nbsp; // electric current, ampere (A) &nbsp; BU_Temperature,&nbsp; &nbsp; &nbsp; &nbsp; // temperature, kelvin (K) &nbsp; BU_Luminous_Intensity, // luminous intensity, candela (cd) &nbsp; BU_Solid_Angle,&nbsp; &nbsp; &nbsp; &nbsp; // solid angle, steradian (sr) };
```
