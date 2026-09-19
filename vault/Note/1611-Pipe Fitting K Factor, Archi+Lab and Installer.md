---
num: 1611
date: 2017-12-13
themes: [MEP]
tags: [revit-api, tbc]
---

# Pipe Fitting K Factor, Archi+Lab and Installer

<https://jeremytammik.github.io/tbc/a/1611_pipe_k_factor.html>

```csharp
&lt;SubTable Dimensions="1" Number="3" Result="K"&gt; &lt;SubTableData1D X="Theta"&gt;&lt;XAxis&gt;0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180&lt;/XAxis&gt; &lt;Data&gt; 0.0 0.18 0.4 0.675 0.9 1.05 1.1 1.125 1.1 1.075 1.06 1.05 1.045 1.035 1.025 1.015 1.01 1.005 1.0 &lt;/Data&gt; &lt;/SubTableData1D&gt; &lt;SubTable Dimensions="0" Number="4" Result="K" DataUsage="UseLargePipeVelocity"&gt; &lt;SubTableData Coefficient="Equation 2-27"/&gt; &lt;Formula&gt;D1 &gt; D2 && Theta &gt; 45 && Theta &lt;= 180&lt;/Formula&gt; &lt;/SubTable&gt; &lt;Formula&gt;D1 &lt; D2 && Theta &lt; 180&lt;/Formula&gt; &lt;/SubTable&gt;
```

```csharp
def getServerById(serverGUID, serviceId): service = ExternalServiceRegistry.GetService(serviceId) if service != "null" and serverGUID != "null": server = service.GetServer(serverGUID) if server != "null": return server return null def getLossMethods(serviceId): service = ExternalServiceRegistry.GetService(serviceId) serverIds = service.GetRegisteredServerIds() list=List[ElementId]() for serverId in serverIds: server = getServerById(serverId, serviceId) id=serverId name=server.GetName() lc.append(id) lc.append(name) lc.append(server) return lc # Set Coefficient? TransactionManager.Instance.EnsureInTransaction(doc) param = fitting.get_Parameter(BuiltInParameter.RBS_PIPE_FITTING_LOSS_METHOD_SERVER_PARAM) lc = getLossMethods(ExternalServices.BuiltInExternalServices.PipeFittingAndAccessoryPressureDropService) schema = lc[8].GetDataSchema() field = schema.GetField("Coefficient") entity=fitting.GetEntity(schema) param.Set(lc[6].ToString()) TransactionManager.Instance.TransactionTaskDone() # Set K Factor? fitting = doc.GetElement(eleId) param = fitting.get_Parameter(BuiltInParameter.RBS_PIPE_FITTING_LOSS_METHOD_SERVER_PARAM) lc = getLossMethods(ExternalServices.BuiltInExternalServices.PipeFittingAndAccessoryPressureDropService) schema = lc[8].GetDataSchema() field = schema.GetField("KFactor") entity=fitting.GetEntity(schema) oldval = entity.Get[field.ValueType](field) # obtaining values TransactionManager.Instance.EnsureInTransaction(doc) entity.Set[field.ValueType](field, SetNew) # installation of a new coefficient value of certain fitting.SetEntity(entity) TransactionManager.Instance.TransactionTaskDone()
```
