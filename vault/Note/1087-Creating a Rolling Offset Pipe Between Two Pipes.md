---
num: 1087
date: 2014-01-10
themes: [MEP, Pitfall]
tags: [revit-api, tbc]
---

# Creating a Rolling Offset Pipe Between Two Pipes

<https://jeremytammik.github.io/tbc/a/1087_rolling_offset_new.htm>

```csharp
&nbsp; ElementId idSystem = pipe.MEPSystem.Id; &nbsp; ElementId idType = pipe.PipeType.Id; &nbsp; ElementId idLevel = pipe.LevelId; &nbsp; &nbsp; pipe = Pipe.Create( doc, idSystem, &nbsp; &nbsp; idType, idLevel, q0, q1 );
```

```csharp
&nbsp; BuiltInParameter bip &nbsp; &nbsp; = BuiltInParameter.RBS_PIPE_DIAMETER_PARAM; &nbsp; &nbsp; double diameter = pipe &nbsp; &nbsp; .get_Parameter( bip ) // &quot;Diameter&quot; &nbsp; &nbsp; .AsDouble(); &nbsp; &nbsp; PipeType pipe_type_standard &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; .OfClass( typeof( PipeType ) ) &nbsp; &nbsp; &nbsp; .Cast&lt;PipeType&gt;() &nbsp; &nbsp; &nbsp; .Where&lt;PipeType&gt;( e &nbsp; &nbsp; &nbsp; &nbsp; =&gt; e.Name.Equals( &quot;Standard&quot; ) ) &nbsp; &nbsp; &nbsp; .FirstOrDefault&lt;PipeType&gt;(); &nbsp; &nbsp; Debug.Assert( &nbsp; &nbsp; pipe_type_standard.Id.IntegerValue.Equals( &nbsp; &nbsp; &nbsp; pipe.PipeType.Id.IntegerValue ), &nbsp; &nbsp; &quot;expected all pipes in this simple &quot; &nbsp; &nbsp; + &quot;model to use the same pipe type&quot; ); &nbsp; &nbsp; pipe = doc.Create.NewPipe( q0, q1, &nbsp; &nbsp; pipe_type_standard ); &nbsp; &nbsp; pipe.get_Parameter( bip ) &nbsp; &nbsp; .Set( diameter );
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// This command can place either a model line &nbsp; /// to represent the rolling offset calculation &nbsp; /// result, or insert a real pipe segment and the &nbsp; /// associated fittings. &nbsp; /// &lt;/summary&gt; &nbsp; static bool _place_model_line = false; &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Switch between the new static Pipe.Create &nbsp; /// method and the obsolete &nbsp; /// Document.Create.NewPipe. &nbsp; /// &lt;/summary&gt; &nbsp; static bool _use_static_pipe_create = false;
```
