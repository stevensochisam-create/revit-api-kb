---
num: 870
date: 2012-12-11
themes: [DynamoPython]
tags: [revit-api, tbc]
---

# BIM 360 Glue REST API Authentication Using Python

<https://jeremytammik.github.io/tbc/a/0870_py_rest_glue.htm>

```csharp
$ python Python 2.7.2 (default, Jun 20 2012, 16:23:33) [GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information. &gt;&gt;&gt; import requests &gt;&gt;&gt; r = requests.get('http://google.com') &gt;&gt;&gt; print r &lt;Response [200=&quot;&quot;]&gt; &gt;&gt;&gt; r.headers['content-type'] 'text/html; charset=ISO-8859-1' &gt;&gt;&gt; r.content '&lt;!doctype html&gt; &lt;html itemscope=&quot;itemscope&quot; itemtype=&quot;http://schema.org/WebPage&quot;&gt; &lt;head&gt; &lt;meta content=&quot;Search the world\'s information, including webpages, images, videos and more. Google has many special features...&quot;
```

```csharp
&gt;&gt;&gt; u1='https://bim360.autodesk.com/api/model/v1/info.json' &gt;&gt;&gt; r = requests.get(u1) &gt;&gt;&gt; print r &lt;Response [400=&quot;&quot;]&gt;
```

```csharp
import time def expires(): '''return a UNIX style timestamp representing 5 minutes from now''' return int(time.time()+300)
```

```csharp
&gt;&gt;&gt; key='ddbf3f51b3824ecbb824ae4e65d31be4' &gt;&gt;&gt; secret='12345678901234567890123456789012' &gt;&gt;&gt; timestamp='1305568169' &gt;&gt;&gt; s=key+secret+timestamp &gt;&gt;&gt; s 'ddbf3f51b3824ecbb824ae4e65d31be4123456789012345678901234567890121305568169' &gt;&gt;&gt; import md5 &gt;&gt;&gt; signature=md5.new(s) &gt;&gt;&gt; print signature &lt;md5 HASH=&quot;&quot; object=&quot;&quot; @=&quot;&quot; 0x10c0b5d30=&quot;&quot;&gt; &gt;&gt;&gt; print signature.hexdigest() b3298cf0b4dc88450d00773b4449ba51
```

```csharp
url = 'https://bim360.autodesk.com:443/api/security/v1/login.json' def bim_360_glue_authenticate( login_name, password, company_id, api_key, api_secret ): timestamp = str(int(time.time())) sig=md5.new(api_key + api_secret + timestamp).hexdigest() data={ 'login_name' : login_name, 'password' : password, 'company_id' : company_id, 'api_key' : api_key, 'api_secret' : api_secret, 'timestamp' : timestamp, 'sig' : sig } r = requests.post(url, data=data) print r.status_code print r.headers['content-type'] print r.content
```
