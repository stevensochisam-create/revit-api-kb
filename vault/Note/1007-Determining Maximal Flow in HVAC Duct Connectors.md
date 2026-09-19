---
num: 1007
date: 2013-08-27
themes: [MEP]
tags: [revit-api, tbc]
---

# Determining Maximal Flow in HVAC Duct Connectors

<https://jeremytammik.github.io/tbc/a/1007_determine_max_flow.htm>

```csharp
*GROUP ID NAME GROUP 1 Mechanical - Airflow *PARAM GUID NAME DATATYPE DATACATEGORY GROUP VISIBLE PARAM XXXX Duct Max Airflow HVAC_AIR_FLOW 1 1
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Return the given element's connector manager, &nbsp; /// using either the family instance MEPModel or &nbsp; /// directly from the duct connector manager. &nbsp; /// &lt;/summary&gt; &nbsp; static ConnectorManager GetConnectorManager( &nbsp; &nbsp; Element e ) &nbsp; { &nbsp; &nbsp; Duct duct = e as Duct; &nbsp; &nbsp; &nbsp; return null == duct &nbsp; &nbsp; &nbsp; ? ( e as FamilyInstance ).MEPModel.ConnectorManager &nbsp; &nbsp; &nbsp; : duct.ConnectorManager; &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Retrieve max flow from all the given connectors. &nbsp; /// &lt;/summary&gt; &nbsp; static double GetMaxFlow( &nbsp; &nbsp; ConnectorSet connectors ) &nbsp; { &nbsp; &nbsp; double flow = 0.0; &nbsp; &nbsp; &nbsp; foreach( Connector c in connectors ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // Accessing flow property requires these &nbsp; &nbsp; &nbsp; // domains or throws an exception saying &nbsp; &nbsp; &nbsp; // &quot;Flow is available only for connectors &nbsp; &nbsp; &nbsp; // of DomainHavc and DomainPiping.&quot; &nbsp; &nbsp; &nbsp; &nbsp; Domain d = c.Domain; &nbsp; &nbsp; &nbsp; &nbsp; if( Domain.DomainHvac != d &nbsp; &nbsp; &nbsp; &nbsp; &amp;&amp; Domain.DomainPiping != d ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; continue; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; if( flow &lt; c.Flow ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; flow = c.Flow; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; } &nbsp; &nbsp; return flow; &nbsp; }
```

```csharp
&nbsp; /// &lt;summary&gt; &nbsp; /// Identify the 'Duct Max Airflow' shared parameter. &nbsp; /// &lt;/summary&gt; &nbsp; static Guid _shared_param_duct_max_airflow &nbsp; &nbsp; = new Guid( &quot;87b12ca4-8a4c-4731-bf88-f50bccd9c5d4&quot; ); &nbsp; &nbsp; /// &lt;summary&gt; &nbsp; /// Set the max flow parameter on the given &nbsp; /// element and return true on success. &nbsp; /// This is generic, so it can handle both &nbsp; /// ducts and fittings. Later, this proved &nbsp; /// unnecessary, and we use ot for ducts only. &nbsp; /// &lt;/summary&gt; &nbsp; static bool SetMaxFlowOnElement( Element e ) &nbsp; { &nbsp; &nbsp; ConnectorSet connectors &nbsp; &nbsp; &nbsp; = GetConnectorManager( e ).Connectors; &nbsp; &nbsp; &nbsp; int n = connectors.Size; &nbsp; &nbsp; &nbsp; double flow = GetMaxFlow( connectors ); &nbsp; &nbsp; &nbsp; Debug.Print( &nbsp; &nbsp; &nbsp; &quot;{0} has {1} connector{2} and max flow {3}.&quot;, &nbsp; &nbsp; &nbsp; Util.ElementDescription( e ), n, &nbsp; &nbsp; &nbsp; Util.PluralSuffix( n ), flow ); &nbsp; &nbsp; &nbsp; Parameter p = e.get_Parameter( &nbsp; &nbsp; &nbsp; _shared_param_duct_max_airflow ); &nbsp; &nbsp; &nbsp; bool rc = false; &nbsp; &nbsp; &nbsp; if( null == p ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; //Util.InfoMsg( &quot;Please ensure that all &quot; &nbsp; &nbsp; &nbsp; //&nbsp; + &quot;duct and their fittings have a &quot; &nbsp; &nbsp; &nbsp; //&nbsp; + &quot;'Duct Max Airflow' shared parameter.&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; Debug.Print( &quot;{0} has no 'Duct Max Airflow' &quot; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;shared parameter.&quot;, &nbsp; &nbsp; &nbsp; &nbsp; Util.ElementDescription( e ) ); &nbsp; &nbsp; } &nbsp; &nbsp; else &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; // Store the max flow value in the specified &nbsp; &nbsp; &nbsp; // parameter on the given element. &nbsp; &nbsp; &nbsp; &nbsp; rc = p.Set( flow ); &nbsp; &nbsp; } &nbsp; &nbsp; return rc; &nbsp; }
```

```csharp
&nbsp; public Result Execute( &nbsp; &nbsp; ExternalCommandData commandData, &nbsp; &nbsp; ref string message, &nbsp; &nbsp; ElementSet elements ) &nbsp; { &nbsp; &nbsp; UIApplication uiapp = commandData.Application; &nbsp; &nbsp; UIDocument uidoc = uiapp.ActiveUIDocument; &nbsp; &nbsp; &nbsp; if( null == uidoc ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; Util.InfoMsg( &quot;Please run this command &quot; &nbsp; &nbsp; &nbsp; &nbsp; + &quot;in a valid document context.&quot; ); &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; Application app = uiapp.Application; &nbsp; &nbsp; Document doc = uidoc.Document; &nbsp; &nbsp; &nbsp; int nDucts = 0; &nbsp; &nbsp; &nbsp; using( Transaction tx = new Transaction( doc ) ) &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; tx.Start( Util.Caption ); &nbsp; &nbsp; &nbsp; &nbsp; FilteredElementCollector ducts &nbsp; &nbsp; &nbsp; &nbsp; = new FilteredElementCollector( doc ) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; .OfClass( typeof( Duct ) ); &nbsp; &nbsp; &nbsp; &nbsp; foreach( Duct duct in ducts ) &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; if( SetMaxFlowOnElement( duct ) ) &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ++nDucts; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; &nbsp; else &nbsp; &nbsp; &nbsp; &nbsp; { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return Result.Failed; &nbsp; &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; tx.Commit(); &nbsp; &nbsp; } &nbsp; &nbsp; &nbsp; Util.InfoMsg( string.Format( &nbsp; &nbsp; &nbsp; &quot;Set max flow parameter on {0} duct{1}.&quot;, &nbsp; &nbsp; &nbsp; nDucts, Util.PluralSuffix( nDucts ) ) ); &nbsp; &nbsp; &nbsp; return Result.Succeeded; &nbsp; }
```
