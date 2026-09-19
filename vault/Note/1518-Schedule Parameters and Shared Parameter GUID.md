---
num: 1518
date: 2017-01-23
themes: [Parameter, Schedule]
tags: [revit-api, tbc]
---

# Schedule Parameters and Shared Parameter GUID

<https://jeremytammik.github.io/tbc/a/1518_sched_param_guid.html>

```csharp
&nbsp;&nbsp;[Transaction(&nbsp;TransactionMode.ReadOnly&nbsp;)] &nbsp;&nbsp;public&nbsp;class&nbsp;CmdSharedParamGuids&nbsp;:&nbsp;IExternalCommand &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;Result&nbsp;Execute( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ExternalCommandData&nbsp;commandData, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ref&nbsp;string&nbsp;message, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ElementSet&nbsp;elements&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;uiapp&nbsp;=&nbsp;commandData.Application; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;uidoc&nbsp;=&nbsp;uiapp.ActiveUIDocument; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;doc&nbsp;=&nbsp;uidoc.Document; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;bindingMap&nbsp;=&nbsp;doc.ParameterBindings; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;it&nbsp;=&nbsp;bindingMap.ForwardIterator(); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;it.Reset(); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while(&nbsp;it.MoveNext()&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;definition&nbsp;=&nbsp;(InternalDefinition)&nbsp;it.Key; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;var&nbsp;sharedParameterElement&nbsp;=&nbsp;doc.GetElement( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;definition.Id&nbsp;)&nbsp;as&nbsp;SharedParameterElement; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;sharedParameterElement&nbsp;==&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TaskDialog.Show(&nbsp;&quot;non-shared&nbsp;parameter&quot;, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;definition.Name&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TaskDialog.Show(&nbsp;&quot;shared&nbsp;parameter&quot;, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$&quot;{sharedParameterElement.GuidValue}&quot; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+&nbsp;&quot;-&nbsp;{definition.Name}&quot;&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nb
```

```csharp
SharedParameterElement shElem = doc.GetElement( Field.ParameterId) as SharedParameterElement;
```

```csharp
Parameter par = Elem.get_Parameter( (BuiltInParameter) Field.ParameterId.IntegerValue );
```
