---
Publication-State: Active
Access: Public
Reviewers:
- Name: Evan Johnson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sails
Review-Date: '2016-10-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Broken CORS*<br><br>Recommendation: When using Sails make sure to double check your CORS configuration.  using `allRoutes: true` with `origin:'*'` will enable the vulnerable behavior, as will failing to uncomment out `origin` and setting it to a reasonable value.  Ensure that if `origin` is set to `*` that you truly mean for all other websites to be able to make cross-domain requests to your API.  Likewise, ensure `credentials` is uncommented out and set to the appropriate value. Make sure to explicitly set which origins may request resources via CORS.  A misconfiguration in a production environment will result in a error message being written to the node process console upon application start in versions 0.12.7 and higher of sails.
### Details
Sails is an MVC style framework for building realtime web applications.  Version 0.12.6 and lower have an issue with the CORS configuration where the value of the origin header is reflected as the value for the Access-Control-Allow-Origin header.  This would allow an attacker to make AJAX requests to vulnerable hosts through cross site scripting or a malicious HTML Document, effectively bypassing the Same Origin Policy. Note that this is only an issue when `allRoutes` is set to `true` and `origin` is set to `*` or left commented out in the sails CORS config file.  The problem can be compounded when the cors `credentials` setting is not provided.  At that point authenticated cross domain requests are possible.
<br><br>• Affected Versions: <=0.12.7
<br>• Patched Versions: >0.12.7
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://sailsjs.org/documentation/reference/configuration/sails-config-cors', 'http://sailsjs.org/documentation/concepts/security/cors']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
