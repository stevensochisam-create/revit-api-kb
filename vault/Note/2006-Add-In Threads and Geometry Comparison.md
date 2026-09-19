---
num: 2006
date: 2023-09-01
themes: [Geometry]
tags: [revit-api, tbc]
---

# Add-In Threads and Geometry Comparison

<https://jeremytammik.github.io/tbc/a/2006_threads_geo_equal.html>

```csharp
Public Class RT_GeometryObjWithId(Of T As GeometryObject) Inherits RT_ApiObjectWithId(Of T) Public ReadOnly Property GeometryId As Integer Public Sub New(Obj As T) MyBase.New(Obj) GeometryId = Obj.Id End Sub End Class Public Class RT_ApiObjectWithId(Of T As APIObject) Implements IDisposable Public ReadOnly Property UID As Guid = Guid.NewGuid Private disposedValue As Boolean Private IntAPIObj As T Public Property APIObject As T Get Return IntAPIObj End Get Set(value As T) IntAPIObj = value End Set End Property Public Sub New(Obj As T) IntAPIObj = Obj End Sub Public Overrides Function GetHashCode() As Integer 'Force consideration of Equals 'Likely I could leave this alone and rely on the default implementation 'However I have more trust in comparing two guids than GetHashCode Return 0 End Function Public Overrides Function Equals(obj As Object) As Boolean Dim Other As RT_ApiObjectWithId(Of T) = _ TryCast(obj, RT_ApiObjectWithId(Of T)) If Other Is Nothing Then Return False else Return Me.UID = Other.UID End Function Public Shared Operator =(A As RT_ApiObjectWithId(Of T), _ B As RT_ApiObjectWithId(Of T)) As Boolean Return A.Equals(B) End Operator Public Shared Operator &lt;&gt;(A As RT_ApiObjectWithId(Of T), _ B As RT_ApiObjectWithId(Of T)) As Boolean Return Not A.Equals(B) End Operator Protected Overridable Sub Dispose(disposing As Boolean) If Not disposedValue Then If disposing Then ' TODO: dispose managed state (managed objects) If APIObject IsNot Nothing Then APIObject.Dispose() End If End If ' TODO: free unmanaged resources (unmanaged objects) and override finalizer ' TODO: set large fields to null disposedValue = True End If End Sub ' ' TODO: override finalizer only if 'Dispose(disposing As Boolean)' has code to free unmanaged resources ' Protected Overrides Sub Finalize() ' ' Do not change this code. Put cleanup code in 'Dispose(disposing As Boolean)' method ' Dispose(disposing:=False) ' MyBase.Finalize() ' End Sub Public Sub Dispose() Implements IDisposable.Dispose ' Do not change this code. Put cleanup code in 'Dispose(disposing As Boolean)' method Dispose(disposing:=True) GC.SuppressFinalize(Me) End Sub End Class
```
