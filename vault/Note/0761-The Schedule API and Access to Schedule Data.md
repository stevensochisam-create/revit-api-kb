---
num: 761
date: 2012-05-07
themes: [Schedule]
tags: [revit-api, tbc]
---

# The Schedule API and Access to Schedule Data

<https://jeremytammik.github.io/tbc/a/0761_access_schedule_data.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Wrapper class for converting &nbsp; /// IntPtr to IWin32Window. &nbsp; /// &lt;/summary&gt; &nbsp; public class JtWindowHandle : IWin32Window &nbsp; { &nbsp; &nbsp; IntPtr _hwnd; &nbsp; &nbsp; &nbsp; public JtWindowHandle( IntPtr h ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Debug.Assert( IntPtr.Zero != h, &nbsp; &nbsp; &nbsp; &nbsp; &quot;expected non-null window handle&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; _hwnd = h; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; public IntPtr Handle &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; get &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; return _hwnd; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; }
```

```csharp
&nbsp; FilteredElementCollector col &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( ViewSchedule ) ); &nbsp; &nbsp; ViewScheduleExportOptions opt &nbsp; &nbsp; = new ViewScheduleExportOptions(); &nbsp; &nbsp; foreach( ViewSchedule vs in col ) &nbsp; { &nbsp; &nbsp; Directory.CreateDirectory( &nbsp; &nbsp; &nbsp; _export_folder_name ); &nbsp; &nbsp; &nbsp; vs.Export( _export_folder_name, &nbsp; &nbsp; &nbsp; vs.Name + _ext, opt ); &nbsp; }
```

```csharp
&nbsp; string filename; &nbsp; &nbsp; while( FileSelect( _export_folder_name, &nbsp; &nbsp; out filename ) ) &nbsp; { &nbsp; &nbsp; DisplayScheduleData( filename, &nbsp; &nbsp; &nbsp; revit_window ); &nbsp; }
```

```csharp
&nbsp; void DisplayScheduleData( &nbsp; &nbsp; string filename, &nbsp; &nbsp; IWin32Window owner ) &nbsp; { &nbsp; &nbsp; ScheduleDataParser parser &nbsp; &nbsp; &nbsp; = new ScheduleDataParser( filename ); &nbsp; &nbsp; &nbsp; System.Windows.Forms.Form form &nbsp; &nbsp; &nbsp; = new System.Windows.Forms.Form(); &nbsp; &nbsp; form.Size = new Size( 400, 400 ); &nbsp; &nbsp; form.Text = _caption_prefix + parser.Name; &nbsp; &nbsp; &nbsp; DataGridView dg = new DataGridView(); &nbsp; &nbsp; dg.AllowUserToAddRows = false; &nbsp; &nbsp; dg.AllowUserToDeleteRows = false; &nbsp; &nbsp; dg.AllowUserToOrderColumns = true; &nbsp; &nbsp; dg.Dock = System.Windows.Forms.DockStyle.Fill; &nbsp; &nbsp; dg.Location = new System.Drawing.Point( 0, 0 ); &nbsp; &nbsp; dg.ReadOnly = true; &nbsp; &nbsp; dg.TabIndex = 0; &nbsp; &nbsp; dg.DataSource = parser.Table; &nbsp; &nbsp; dg.Parent = form; &nbsp; &nbsp; &nbsp; form.ShowDialog( owner ); &nbsp; }
```

```csharp
class ScheduleDataParser { &nbsp; /// &lt;summary&gt; &nbsp; /// Default schedule data file field delimiter. &nbsp; /// &lt;/summary&gt; &nbsp; static char[] _tabs = new char[] { '\t' }; &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Strip the quotes around text strings &nbsp; /// in the schedule data file. &nbsp; /// &lt;/summary&gt; &nbsp; static char[] _quotes = new char[] { '&quot;' }; &nbsp; &nbsp; string _name = null; &nbsp; DataTable _table = null; &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Schedule name &nbsp; /// &lt;/summary&gt; &nbsp; public string Name &nbsp; { &nbsp; &nbsp; get { return _name; } &nbsp; } &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Schedule columns and row data &nbsp; /// &lt;/summary&gt; &nbsp; public DataTable Table &nbsp; { &nbsp; &nbsp; get { return _table; } &nbsp; } &nbsp; &nbsp; public ScheduleDataParser( string filename ) &nbsp; { &nbsp; &nbsp; StreamReader stream = File.OpenText( filename ); &nbsp; &nbsp; &nbsp; string line; &nbsp; &nbsp; string[] a; &nbsp; &nbsp; &nbsp; while( null != ( line = stream.ReadLine() ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; a = line &nbsp; &nbsp; &nbsp; &nbsp; .Split( _tabs ) &nbsp; &nbsp; &nbsp; &nbsp; .Select&lt;string, string&gt;( s =&gt; s.Trim( _quotes ) ) &nbsp; &nbsp; &nbsp; &nbsp; .ToArray(); &nbsp; &nbsp; &nbsp; &nbsp; // First line of text file contains &nbsp; &nbsp; &nbsp; // schedule name &nbsp; &nbsp; &nbsp; &nbsp; if( null == _name ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; _name = a[0]; &nbsp; &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; // Second line of text file contains &nbsp; &nbsp; &nbsp; // schedule column names &nbsp; &nbsp; &nbsp; &nbsp; if( null == _table ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; _table = new DataTable(); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; foreach( string column_name in a ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DataColumn column = new DataColumn(); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; column.DataType = typeof( string ); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; column.ColumnName = column_name; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; _table.Columns.Add( column ); &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; _table.BeginLoadData(); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; // Remaining lines define schedula da
```
