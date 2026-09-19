---
num: 1527
date: 2017-02-13
themes: [MEP]
tags: [revit-api, tbc]
---

# Revit MEP Connector Number

<https://jeremytammik.github.io/tbc/a/1527_mep_connector_number.html>

```csharp
int&nbsp;ConnectorElem::defaultIndex() { &nbsp;&nbsp;//&nbsp;... &nbsp;&nbsp; for(&nbsp;elemIter.initIter();&nbsp;!elemIter.isDone();&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;elemIter.increment()&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;pElem&nbsp;=&nbsp;getDocument()-&gt;getElement(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elemIter.getElementId()&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;!pElem&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue; &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;IS_A(&nbsp;ConnectorElem,&nbsp;pElem&nbsp;)&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pConnectorElem&nbsp;=&nbsp;downcast&nbsp;&lt;const&nbsp;ConnectorElem*&gt;&nbsp;(&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pElem&nbsp;); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nIndex&nbsp;=&nbsp;pConnectorElem-&gt;getIndex(); &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(&nbsp;nIndex&nbsp;&gt;&nbsp;nMaxIndex&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nMaxIndex&nbsp;=&nbsp;nIndex; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;&nbsp;&nbsp;} &nbsp;&nbsp;} &nbsp;&nbsp;//&nbsp;We&nbsp;want&nbsp;to&nbsp;start&nbsp;the&nbsp;indices&nbsp;at&nbsp;1&nbsp;if&nbsp;there&nbsp;are&nbsp;none. &nbsp;&nbsp;if(&nbsp;nMaxIndex&nbsp;&lt;=&nbsp;0&nbsp;) &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;nMaxIndex&nbsp;=&nbsp;1; &nbsp;&nbsp;} &nbsp;&nbsp;else &nbsp;&nbsp;{ &nbsp;&nbsp;&nbsp;&nbsp;nMaxIndex++; &nbsp;&nbsp;} &nbsp;&nbsp;return&nbsp;nMaxIndex; }
```
