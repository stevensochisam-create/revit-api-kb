---
num: 2019
date: 2023-12-12
themes: [Geometry]
tags: [revit-api, tbc]
---

# 3D View, Curved Section and Browser Round-Trip

<https://jeremytammik.github.io/tbc/a/2019_cefsharp_roundtrip.html>

```csharp
public class BoundObject { public int Add(int a, int b) { ExtApp.handler.a = a; ExtApp.handler.b = b; ExtApp.testEvent.Raise(); return a+b; } }
```

```csharp
internal class ExtApp : IExternalApplication { public static IExternalApplication MyApp; public static ChromiumWebBrowser browser; public static ExternalEvent testEvent; public static MyEvent handler; public Result OnShutdown(UIControlledApplication application) { // Cef.Shutdown(); return Result.Succeeded; } public Result OnStartup(UIControlledApplication application) { MyApp = this; //code for making a button handler = new MyEvent(); testEvent= ExternalEvent.Create(handler); return Result.Succeeded; } }
```

```csharp
&lt;Window x:Class="RevitTestProject.TestWindow" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:d="http://schemas.microsoft.com/expression/blend/2008" xmlns:local="clr-namespace:RevitTestProject" xmlns:cef="clr-namespace:CefSharp.Wpf;assembly=CefSharp.Wpf" mc:Ignorable="d" Width="1000" Height="500"&gt; &lt;Grid Background="PapayaWhip"&gt; &lt;cef:ChromiumWebBrowser Name="ChromiumBrowser" Address="http://www.google.com" Width="900" Height="450" /&gt; &lt;/Grid&gt; &lt;/Window&gt;
```

```csharp
public TestWindow() { InitializeComponent(); ChromiumBrowser.Address = "https://www.google.com"; ChromiumBrowser.Address = "C:\\Users\\XXX\\Desktop\\index.html"; BoundObject bo = new BoundObject(); ChromiumBrowser.JavascriptObjectRepository.Register("boundAsync", bo, true, BindingOptions.DefaultBinder); } public void Dispose() { this.Dispose(); }
```

```csharp
&lt;html&gt; &lt;head&gt; &lt;title&gt;Bridge Test&lt;/title&gt; &lt;!-- &lt;script src="script.js"&gt;&lt;/script&gt; --&gt; &lt;script type="text/javascript"&gt; async function callCSharpAction() { await CefSharp.BindObjectAsync("boundAsync"); boundAsync.add(16, 2); } &lt;/script&gt; &lt;/head&gt; &lt;body&gt; &lt;button id="action1" onclick="callCSharpAction()"&gt;Action 1&lt;/button&gt; &lt;button id="action2" onclick="alert('Button is working')"&gt;Action 2&lt;/button&gt; &lt;button id="action3"&gt;Action 3&lt;/button&gt; &lt;/body&gt; &lt;/html&gt;
```
