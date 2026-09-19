---
num: 1865
date: 2020-09-21
themes: [Parameter]
tags: [revit-api, tbc]
---

# On Spaces in Help and Renaming a Parameter

<https://jeremytammik.github.io/tbc/a/1865_ren_param_f1_help.html>

```csharp
https://accounts.autodesk.com/oAuth/OAuthRedirect?oauth_consumer_key=1c27193f-af5e-4e7c-9847-06cd5c3c30ae&oauth_nonce=cd819e65f0ac476099e9c795a22c05a7&oauth_redirect_url=https%3A%2F%2Fpostman-echo.com%2Fget%3Ftext%2520with%2520space&oauth_signature=xl7aBEcj5lI%2FX28ozkvQ%2Ba163qg%3D&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1600289858&oauth_token=bskZ8nJbcvBt%2FTyQvS%2FeImjP6pc%3D&oauth_version=1.0
```

```csharp
xoauth_problem=parameter_rejected&xoauth_parameters_absent=oauth_redirect_url&oauth_error_message=Invalid%20value%20for%20parameter%3Aoauth_redirect_url
```

```csharp
&nbsp;&nbsp;ContextualHelp&nbsp;contextualHelp&nbsp;=&nbsp;new&nbsp;ContextualHelp( &nbsp;&nbsp;&nbsp;&nbsp;ContextualHelpType.Url, &nbsp;&nbsp;&nbsp;&nbsp;&quot;https://postman-echo.com/get?text%20with%20space&quot;&nbsp;); &nbsp;&nbsp;pushButton.SetContextualHelp(contextualHelp);
```

```csharp
ContextualHelp&nbsp;contextualHelp&nbsp;=&nbsp;new&nbsp;ContextualHelp( &nbsp;&nbsp;ContextualHelpType.Url, &nbsp;&nbsp;&quot;http://postman-echo.com/get?text%20with%20space&quot;&nbsp;); pushButton.SetContextualHelp(contextualHelp);
```
