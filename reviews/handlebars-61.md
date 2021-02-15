---
Publication-State: Active
Access: Public
Reviewers:
- Name: Matias P. Brutti
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/handlebars
Review-Date: '2015-12-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Quoteless Attributes in Templates can lead to Content Injection*<br><br>Recommendation: If you are unable to upgrade to version 4.0.0 or greater you can add quotes to your attributes in your handlebar templates.
### Details
Not using quotes around your attributes in handlebar templates, could lead to content injection.  ### Example Template: ```<a href={{foo}}/>```  Input: ```{ 'foo' : 'test.com onload=alert(1)'}```  Rendered result: ```<a href=test.com onload=alert(1)/>```
<br><br>• Affected Versions: <4.0.0
<br>• Patched Versions: >=4.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://blog.srcclr.com/handlebars_vulnerability_research_findings/', 'https://github.com/wycats/handlebars.js/pull/1083']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
