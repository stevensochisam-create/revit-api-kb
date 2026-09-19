---
num: 2031
date: 2024-03-29
themes: [MEP]
tags: [revit-api, tbc]
---

# Change Pipe Level and PreviewControl Border

<https://jeremytammik.github.io/tbc/a/2031_previewcontrol.html>

```csharp
// get preview window host var previewWndHost = previewControl.Content; if (previewWndHost is null) return; // get preview view handle var previewHwnd = (IntPtr)previewWndHost.GetType().GetProperty("Handle").GetValue(previewWndHost, null); if (previewHwnd == IntPtr.Zero) return; // remove WS_EX_CLIENTEDGE on all child windows foreach (var hwnd in HwndHelpers.GetAllChildHandles(previewHwnd).Append(previewHwnd)) { var style = User32.GetWindowLong(hwnd, Constants.GWL_EXSTYLE).ToInt32() & ~(int)Constants.WS_EX_CLIENTEDGE; User32.SetWindowLong(hwnd, Constants.GWL_EXSTYLE, style); } // trigger redraw by adding or removing a slight padding at the bottom // the original padding is stored in the tag, so try to avoid using the // tag property for anything else if you want this to work. var p = previewControl.Padding; if (previewControl.Tag is null) previewControl.Tag = p; if (previewControl.Tag is System.Windows.Thickness t) { p.Bottom = p.Bottom == t.Bottom ? p.Bottom + 1 : t.Bottom; previewControl.Padding = p; }
```

```csharp
public static IList&lt;IntPtr&gt; GetAllChildHandles(IntPtr hwnd) { var childHandles = new List&lt;IntPtr&gt;(); var gcChildHandles = GCHandle.Alloc(childHandles); try { bool EnumWindow(IntPtr hWnd, IntPtr lParam) { (GCHandle.FromIntPtr(lParam).Target as List&lt;IntPtr&gt;)?.Add(hWnd); return true; } var childProc = new User32.EnumWindowsProc(EnumWindow); User32.EnumChildWindows(hwnd, childProc, GCHandle.ToIntPtr(gcChildHandles)); } finally { gcChildHandles.Free(); } return childHandles; }
```

```csharp
public void Initialize() { var previewControl = new PreviewControl(_context, view.Id); previewControl.Loaded += RemovePreviewControlStyles; } private void RemovePreviewControlStyles(object sender, EventArgs args) { var control = (PreviewControl)sender; var previewHost = (FrameworkElement)control.Content; var previewType = previewHost.GetType(); var hostField = previewType.GetField("m_hwndHost", BindingFlags.NonPublic | BindingFlags.DeclaredOnly | BindingFlags.Instance)!; var handle = (IntPtr)hostField.GetValue(previewHost); var childHandles = UnsafeNativeMethods.GetChildHandles(handle); UnsafeNativeMethods.RemoveWindowStyles(handle); UnsafeNativeMethods.RemoveWindowCaption(handle); foreach (var childHandle in childHandles) { UnsafeNativeMethods.RemoveWindowStyles(childHandle); } }
```

```csharp
/// &lt;summary&gt; /// Tries to remove styles from selected window handle. /// &lt;/summary&gt; /// &lt;param name="handle"&gt;Window handle.&lt;/param&gt; /// &lt;returns&gt;&lt;see langword="true"/&gt; if invocation of native Windows function succeeds.&lt;/returns&gt; public static bool RemoveWindowStyles(IntPtr handle) { if (handle == IntPtr.Zero) { return false; } if (!User32.IsWindow(handle)) { return false; } var cornerResult = ApplyWindowCornerPreference(handle, WindowCornerPreference.DoNotRound); if (!cornerResult) return false; var windowStyleLong = User32.GetWindowLong(handle, User32.GWL.GWL_EXSTYLE); windowStyleLong &= ~(int)User32.WS_EX.CLIENTEDGE; var styleResult = SetWindowLong(handle, User32.GWL.GWL_EXSTYLE, windowStyleLong); return styleResult.ToInt64() &gt; 0x0; } /// &lt;summary&gt; /// Get the child windows that belong to the specified parent window by passing the handle to each child window. /// &lt;/summary&gt; /// &lt;param name="hwnd"&gt;Window handle.&lt;/param&gt; public static IList&lt;IntPtr&gt; GetChildHandles(IntPtr hwnd) { var handles = new List&lt;IntPtr&gt;(); var gcHandles = GCHandle.Alloc(handles); try { var callbackPointer = new User32.EnumWindowsProc(EnumWindowCallback); User32.EnumChildWindows(hwnd, callbackPointer, GCHandle.ToIntPtr(gcHandles)); } finally { gcHandles.Free(); } return handles; } private static bool EnumWindowCallback(IntPtr hwnd, IntPtr lParam) { var target = GCHandle.FromIntPtr(lParam).Target as List&lt;IntPtr&gt;; if (target is null) return false; target.Add(hwnd); return true; }
```

```csharp
/// &lt;summary&gt; /// An application-defined callback function used with the EnumChildWindows function. /// It receives the child window handles. The WNDENUMPROC type defines a pointer to /// this callback function. EnumChildProc is a placeholder for the application-defined /// function name. /// &lt;/summary&gt; public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam); /// &lt;summary&gt; /// Enumerates the child windows that belong to the specified parent window by /// passing the handle to each child window, in turn, to an application-defined /// callback function. EnumChildWindows continues until the last child window /// is enumerated or the callback function returns FALSE. /// &lt;/summary&gt; /// &lt;param name="hwnd"&gt;The window that you want to get information about.&lt;/param&gt; /// &lt;param name="func"&gt;A pointer to an application-defined callback function&lt;/param&gt; /// &lt;param name="lParam"&gt;An application-defined value to be passed to the callback function.&lt;/param&gt; /// &lt;returns&gt;&lt;/returns&gt; [DllImport(Libraries.User32)] public static extern bool EnumChildWindows(IntPtr hwnd, EnumWindowsProc func, IntPtr lParam);
```
