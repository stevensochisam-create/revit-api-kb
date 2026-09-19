---
num: 204
date: 2009-08-18
themes: [MEP]
tags: [revit-api, tbc]
---

# Fixing RvtMgdDbg for MEP Connectors

<https://jeremytammik.github.io/tbc/a/0204_rvtmgddbg_mep_connectors.htm>

```csharp
Angle is available only for connectors of DomainHavc and DomainPiping.
```

```csharp
data.Add( new Snoop.Data.Double( &quot;Angle&quot;, connector.Angle ) );
```

```csharp
if( Domain.DomainHvac == connector.Domain &nbsp; || Domain.DomainPiping == connector.Domain ) { &nbsp; data.Add( new Snoop.Data.Double( &quot;Angle&quot;, &nbsp; &nbsp; connector.Angle ) ); }
```

```csharp
{data\.Add.*, connector\.}{[^\.\)]*}{[\)\.].*}\n
```

```csharp
try\n{\n\1\2\3\n}\ncatch\n{\nDebug.Print( "\2: "+ex.Message );\n}\n
```
