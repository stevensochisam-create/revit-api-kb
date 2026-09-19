---
num: 1450
date: 2016-06-23
themes: [MEP]
tags: [revit-api, tbc]
---

# MEP System Structure in Hierarchical JSON Graph

<https://jeremytammik.github.io/tbc/a/1450_mep_system_json_graph.html>

```csharp
//&nbsp;Check&nbsp;for&nbsp;shared&nbsp;parameter //&nbsp;to&nbsp;store&nbsp;graph&nbsp;information. Definition&nbsp;def&nbsp;=&nbsp;SharedParameterMgr.GetDefinition( &nbsp;&nbsp;desirableSystems.First&lt;MEPSystem&gt;()&nbsp;); if(&nbsp;null&nbsp;==&nbsp;def&nbsp;) { &nbsp;&nbsp;SharedParameterMgr.Create(&nbsp;doc&nbsp;); &nbsp;&nbsp;def&nbsp;=&nbsp;SharedParameterMgr.GetDefinition( &nbsp;&nbsp;&nbsp;&nbsp;desirableSystems.First&lt;MEPSystem&gt;()&nbsp;); &nbsp;&nbsp;if(&nbsp;null&nbsp;==&nbsp;def&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;message&nbsp;=&nbsp;&quot;Error&nbsp;creating&nbsp;the&nbsp;&quot; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+&nbsp;&quot;storage&nbsp;shared&nbsp;parameter.&quot;; &nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;Result.Failed; &nbsp;&nbsp;} }
```

```csharp
class&nbsp;Options { &nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;Store&nbsp;element&nbsp;id&nbsp;or&nbsp;UniqueId&nbsp;in&nbsp;JSON&nbsp;output? &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;public&nbsp;static&nbsp;bool&nbsp;StoreUniqueId&nbsp;=&nbsp;false; &nbsp;&nbsp;public&nbsp;static&nbsp;bool&nbsp;StoreElementId&nbsp;=&nbsp;!StoreUniqueId; &nbsp;&nbsp;///&nbsp;&lt;summary&gt; &nbsp;&nbsp;///&nbsp;Store&nbsp;parent&nbsp;node&nbsp;id&nbsp;in&nbsp;child,&nbsp;or&nbsp;recursive&nbsp; &nbsp;&nbsp;///&nbsp;tree&nbsp;of&nbsp;children&nbsp;in&nbsp;parent? &nbsp;&nbsp;///&nbsp;&lt;/summary&gt; &nbsp;&nbsp;public&nbsp;static&nbsp;bool&nbsp;StoreJsonGraphBottomUp&nbsp;=&nbsp;false; &nbsp;&nbsp;public&nbsp;static&nbsp;bool&nbsp;StoreJsonGraphTopDown &nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;!StoreJsonGraphBottomUp; }
```

```csharp
[ { "id" : "ajson1", "parent" : "#", "text" : "Simple root node" }, { "id" : "ajson2", "parent" : "#", "text" : "Root node 2" }, { "id" : "ajson3", "parent" : "ajson2", "text" : "Child 1" }, { "id" : "ajson4", "parent" : "ajson2", "text" : "Child 2" }, ]
```

```csharp
{ id: -1, name: 'Root', children: [ { id: 0, name: 'Mechanical System', children: [ { id: 0_1, name: 'Child 0_1', type: 'window', otherField: 'something...', children: [ { id: 0_1_1, name: 'Grandchild 0_1_1' }] }, { id: 0_2, name: 'Child 0_2', children: [ { id: 0_2_1, name: 'Grandchild 0_2_1' }] }] }, { id: 2, name: 'Electrical System', children: [ { id: 2_1, name: 'Child 2_1', children: [{ id: 2_1_1, name: 'Grandchild 2_1_1' }] }, { id: 2_2, name: 'Child 2_2', children: [{ id: 2_2_1, name: 'Grandchild 2_2_1' }] }] }, { id: 3, name: 'Piping System', children: [ { id: 3_1, name: 'Child 3_1', children: [{ id: 3_1_1, name: 'Grandchild 3_1_1' }] }, { id: 3_2, name: 'Child 3_2', children: [{ id: 3_2_1, name: 'Grandchild 3_2_1' }] }] }] }
```

```csharp
///&nbsp;&lt;summary&gt; ///&nbsp;Dump&nbsp;the&nbsp;top-down&nbsp;traversal&nbsp;graph&nbsp;into&nbsp;JSON. ///&nbsp;In&nbsp;this&nbsp;case,&nbsp;each&nbsp;parent&nbsp;node&nbsp;is&nbsp;populated ///&nbsp;with&nbsp;a&nbsp;full&nbsp;hierarchical&nbsp;graph&nbsp;of&nbsp;all&nbsp;its ///&nbsp;children,&nbsp;cf.&nbsp;https://www.jstree.com/docs/json. ///&nbsp;&lt;/summary&gt; public&nbsp;string&nbsp;DumpToJsonTopDown() { &nbsp;&nbsp;return&nbsp;m_startingElementNode &nbsp;&nbsp;&nbsp;&nbsp;.DumpToJsonTopDown(); } ///&nbsp;&lt;summary&gt; ///&nbsp;Dump&nbsp;the&nbsp;bottom-up&nbsp;traversal&nbsp;graph&nbsp;into&nbsp;JSON. ///&nbsp;In&nbsp;this&nbsp;case,&nbsp;each&nbsp;child&nbsp;node&nbsp;is&nbsp;equipped&nbsp;with&nbsp; ///&nbsp;a&nbsp;&#39;parent&#39;&nbsp;pointer,&nbsp;cf. ///&nbsp;https://www.jstree.com/docs/json/ ///&nbsp;&lt;/summary&gt; public&nbsp;string&nbsp;DumpToJsonBottomUp() { &nbsp;&nbsp;List&lt;string&gt;&nbsp;a&nbsp;=&nbsp;new&nbsp;List&lt;string&gt;(); &nbsp;&nbsp;m_startingElementNode.DumpToJsonBottomUp(&nbsp;a,&nbsp;&quot;#&quot;&nbsp;); &nbsp;&nbsp;return&nbsp;&quot;[&quot;&nbsp;+&nbsp;string.Join(&nbsp;&quot;,&quot;,&nbsp;a&nbsp;)&nbsp;+&nbsp;&quot;]&quot;; }
```
