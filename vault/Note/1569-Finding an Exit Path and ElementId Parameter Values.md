---
num: 1569
date: 2017-06-21
themes: [ElementId, Parameter]
tags: [revit-api, tbc]
---

# Finding an Exit Path and ElementId Parameter Values

<https://jeremytammik.github.io/tbc/a/1569_path_elemid_param.html>

```csharp
if(&nbsp;request&nbsp;==&nbsp;EditPropertyOptRequest.GetAvailableValues&nbsp;) { &nbsp;&nbsp;cond.SelElemValue&nbsp;=&nbsp;null; &nbsp;&nbsp;cond.PropertyOpt.ElementValues&nbsp;=&nbsp;new&nbsp;ObservableCollection&lt;Element&gt;(); &nbsp;&nbsp;if(&nbsp;cond.SelProperty.StorageType&nbsp;==&nbsp;StorageType.ElementId&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;ElementId&nbsp;ElemId&nbsp;=&nbsp;cond.SelProperty.AsElementId; &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;ElemId&nbsp;==&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return; &nbsp;&nbsp;&nbsp;&nbsp;Element&nbsp;Elem&nbsp;=&nbsp;doc.GetElement(&nbsp;ElemId&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;ElementType&nbsp;ElemType&nbsp;=&nbsp;Elem&nbsp;as&nbsp;ElementType; &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;ElemType&nbsp;!=&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;ElemId&nbsp;in&nbsp;ElemType.GetSimilarTypes&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cond.PropertyOpt.ElementValues.Add(&nbsp;doc.GetElement(&nbsp;ElemId&nbsp;)&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;else&nbsp;if(&nbsp;Elem.Category&nbsp;!=&nbsp;null&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FilteredElementCollector&nbsp;collector&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp;doc&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector.OfCategory(&nbsp;Elem.Category.Id.IntegerValue&nbsp;).WhereElementIsNotElementType(); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;foreach(&nbsp;Elem&nbsp;in&nbsp;collector&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cond.PropertyOpt.ElementValues.Add(&nbsp;Elem&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;else &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Handle&nbsp;non-category&nbsp;elements.&nbsp;Namely&nbsp;Line&nbsp;Styles(aka&nbsp;GraphicStlyes) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;cond.SelElemValue&nbsp;=&nbsp;cond.PropertyOpt.ElementValues(&nbsp;0&nbsp;); &nbsp;&nbsp;} }
```

```csharp
ParameterValueProvider&nbsp;pvp_Demolished&nbsp; &nbsp;&nbsp;=&nbsp;new&nbsp;ParameterValueProvider(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;ElementId(&nbsp;(int)&nbsp;BuiltInParameter &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.PHASE_DEMOLISHED&nbsp;)&nbsp;); FilterNumericGreater&nbsp;fgreater&nbsp; &nbsp;&nbsp;=&nbsp;new&nbsp;FilterNumericGreater(); FilterElementIdRule&nbsp;IdFilter&nbsp; &nbsp;&nbsp;=&nbsp;new&nbsp;FilterElementIdRule(&nbsp;pvp_Demolished,&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;fgreater,&nbsp;ElementId.InvalidElementId&nbsp;); ElementParameterFilter&nbsp;efilter&nbsp; &nbsp;&nbsp;=&nbsp;new&nbsp;ElementParameterFilter(&nbsp;IdFilter&nbsp;); FilteredElementCollector&nbsp;elems&nbsp; &nbsp;&nbsp;=&nbsp;new&nbsp;FilteredElementCollector(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;doc,&nbsp;doc.ActiveView.Id&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.WherePasses(&nbsp;efilter&nbsp;);
```
