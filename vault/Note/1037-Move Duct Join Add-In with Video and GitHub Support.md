---
num: 1037
date: 2013-10-16
themes: [MEP]
tags: [revit-api, tbc]
---

# Move Duct Join Add-In with Video and GitHub Support

<https://jeremytammik.github.io/tbc/a/1037_move_duct_join.htm>

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return the connector &nbsp; /// connected to the one given. &nbsp; /// &lt;/summary&gt; &nbsp; static Connector GetConnectedConnector( &nbsp; &nbsp; Connector con ) &nbsp; { &nbsp; &nbsp; Connector neighbour = null; &nbsp; &nbsp; &nbsp; int ownerId = con.Owner.Id.IntegerValue; &nbsp; &nbsp; &nbsp; ConnectorSet refs = con.AllRefs; &nbsp; &nbsp; &nbsp; foreach( Connector c in refs ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // Ignore non-End connectors and&nbsp; &nbsp; &nbsp; &nbsp; // connectors on the same element &nbsp; &nbsp; &nbsp; &nbsp; if( c.ConnectorType == ConnectorType.End &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; !ownerId.Equals( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; c.Owner.Id.IntegerValue ) ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; neighbour = c; &nbsp; &nbsp; &nbsp; &nbsp; break; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return neighbour; &nbsp; }
```

```csharp
/v/C/a/vs/MoveDuctJoin/ $ git push Username for 'https://github.com': jeremytammik Password for 'https://jeremytammik@github.com': Counting objects: 13, done. Delta compression using up to 8 threads. Compressing objects: 100% (10/10), done. Writing objects: 100% (11/11), 5.26 KiB, done. Total 11 (delta 0), reused 0 (delta 0) To https://github.com/jeremytammik/MoveDuctJoin 944fbf8..7eb010f master -> master
```
