---
num: 554
date: 2011-03-15
themes: [MEP]
tags: [revit-api, tbc]
---

# Distinguishing MEP Element Shape

<https://jeremytammik.github.io/tbc/a/0554_mep_element_shape.htm>

```csharp
&nbsp; if( size.Split( 'x' ).Length == 3 ) // could use a regex &quot;[0-9]x[0-9]+-[0-9]+/[0-9]+&quot; but splitting is less costly &nbsp; &nbsp; return &quot;rectangular2rectangular&quot;; &nbsp; else if( size.Split( '/' ).Length == 3 ) &nbsp; &nbsp; return &quot;oval2oval&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+x[0-9]+-[0-9]+/[0-9]+&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;rectangular2oval&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+/[0-9]+-[0-9]+x[0-9]+&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;oval2rectangular&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+[^0-9]-[0-9]+x[0-9]+&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;round2rectangular&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+x[0-9]+-[0-9]+[^0-9]&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;rectangular2round&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+[^0-9]-[0-9]+/[0-9]+&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;round2oval&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+/[0-9]+-[0-9]+[^0-9]&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;oval2round&quot;; &nbsp; else if( &nbsp; &nbsp; new Regex( @&quot;[0-9]+[^0-9]-[0-9]+[^0-9]&quot; ) &nbsp; &nbsp; &nbsp; .IsMatch( size ) ) &nbsp; &nbsp; &nbsp; &nbsp; return &quot;round2round&quot;; &nbsp; else { return &quot;other case&quot;; }
```

```csharp
return ( e.Category.Id.Equals( e.Document.Settings.Categories.get_Item( c ).Id ) ) ? true : false;
```

```csharp
&nbsp; return e.Category.Id.Equals( &nbsp; &nbsp; e.Document.Settings.Categories.get_Item( &nbsp; &nbsp; &nbsp; c ).Id );
```

```csharp
&nbsp; return e.Category.Id.IntegerValue.Equals( &nbsp; &nbsp; (int) c );
```

```csharp
class RegexCache : Dictionary&lt;string, Regex&gt; { &nbsp; /// &lt;summary&gt; &nbsp; /// Apply regular expression pattern matching &nbsp; /// to a given input string. The compiled &nbsp; /// regular expression is cached for efficient &nbsp; /// future reuse. &nbsp; /// &lt;/summary&gt; &nbsp; /// &lt;param name=&quot;pattern&quot;&gt;Regular expression pattern&lt;/param&gt; &nbsp; /// &lt;param name=&quot;input&quot;&gt;Input string&lt;/param&gt; &nbsp; /// &lt;returns&gt;True if input matches pattern, else false&lt;/returns&gt; &nbsp; public bool Match( string pattern, string input ) &nbsp; { &nbsp; &nbsp; if( !ContainsKey( pattern ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Add( pattern, new Regex( pattern ) ); &nbsp; &nbsp; } &nbsp; &nbsp; return this[pattern].IsMatch( input ); &nbsp; } }
```
