---
num: 1652
date: 2018-05-14
themes: [Parameter]
tags: [revit-api, tbc]
---

# Parameters, Walls and Driving Revit via WCF Service

<https://jeremytammik.github.io/tbc/a/1652_revit_wcf_service.html>

```csharp
lock (Locker) { // Enque GetDocumentPath task: TaskContainer.Instance.EnqueueTask(GetDocumentPath); // Waiting for invoking Monitor.Pulse(Locker) // somewhere in desired time interval Monitor.Wait(Locker, WaitTimeout); } return currentDocumentPath;
```

```csharp
private void GetDocumentPath(UIApplication uiapp) { try { currentDocumentPath = uiapp.ActiveUIDocument.Document.PathName; } finally { lock (Locker) { Monitor.Pulse(Locker); // <- HERE! } } }
```

```csharp
private const string ServiceUrlHttp = "http://localhost:9001/RevitExternalService"; private const string ServiceUrlTcp = "net.tcp://localhost:9002/RevitExternalService"; // ... public Result OnStartup(UIControlledApplication application) { application.Idling += OnIdling; try { Task.Factory.StartNew(() => { var serviceHost = new ServiceHost( typeof(RevitExternalService), new Uri(ServiceUrlHttp), new Uri(ServiceUrlTcp)); serviceHost.Description.Behaviors.Add( new ServiceMetadataBehavior()); serviceHost.AddServiceEndpoint( typeof(IRevitExternalService), new BasicHttpBinding(), ServiceUrlHttp); serviceHost.AddServiceEndpoint( typeof(IRevitExternalService), new NetTcpBinding(), ServiceUrlTcp); serviceHost.AddServiceEndpoint( typeof(IMetadataExchange), MetadataExchangeBindings.CreateMexHttpBinding(), "mex"); serviceHost.Open(); }, TaskCreationOptions.LongRunning); } catch (Exception ex) { //.... } return Result.Succeeded; }
```

```csharp
public partial class Form1 : Form { private const string ServiceUrlHttp = "http://localhost:9001/ExternalService"; private const string ServiceUrlTcp = "net.tcp://localhost:9002/ExternalService"; public Form1() { InitializeComponent(); } private void Form1_Load(object sender, EventArgs e) { Task.Factory.StartNew(() => { while (true) { OnIdling(); Thread.Sleep(TimeSpan.FromSeconds(1)); } }, TaskCreationOptions.LongRunning); var serviceHost = new ServiceHost( typeof(ExternalService), new Uri(ServiceUrlHttp), new Uri(ServiceUrlTcp)); serviceHost.Description.Behaviors.Add( new ServiceMetadataBehavior()); serviceHost.AddServiceEndpoint( typeof(IExternalService), new BasicHttpBinding(), ServiceUrlHttp); serviceHost.AddServiceEndpoint( typeof(IExternalService), new NetTcpBinding(), ServiceUrlTcp); serviceHost.AddServiceEndpoint( typeof(IMetadataExchange), MetadataExchangeBindings.CreateMexHttpBinding(), "mex"); serviceHost.Open(); } private static void OnIdling() { if (!TaskContainer.Instance.HasTaskToPerform) return; var task = TaskContainer.Instance.DequeueTask(); task(); } }
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Wall&nbsp;type&nbsp;predicate&nbsp;for&nbsp;exterior&nbsp;wall&nbsp;function ///&nbsp;&lt;/summary&gt; bool&nbsp;IsExterior(&nbsp;WallType&nbsp;wallType&nbsp;) { &nbsp;&nbsp;Parameter&nbsp;p&nbsp;=&nbsp;wallType.get_Parameter( &nbsp;&nbsp;&nbsp;&nbsp;BuiltInParameter.FUNCTION_PARAM&nbsp;); &nbsp;&nbsp;Debug.Assert(&nbsp;null&nbsp;!=&nbsp;p,&nbsp;&quot;expected&nbsp;wall&nbsp;type&nbsp;&quot; &nbsp;&nbsp;&nbsp;&nbsp;+&nbsp;&quot;to&nbsp;have&nbsp;wall&nbsp;function&nbsp;parameter&quot;&nbsp;); &nbsp;&nbsp;WallFunction&nbsp;f&nbsp;=&nbsp;(WallFunction)&nbsp;p.AsInteger(); &nbsp;&nbsp;return&nbsp;WallFunction.Exterior&nbsp;==&nbsp;f; }
```
