---
Publication-State: Active
Access: Public
Reviewers:
- Name: Sergio Arcos
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/connect
Review-Date: '2013-07-01'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*methodOverride Middleware Reflected Cross-Site Scripting*<br><br>Update to the newest version of Connect or disable methodOverride. It is not possible to avoid the vulnerability if you have enabled this middleware in the top of your stack.
### Details
Connect is a stack of middleware that is executed in order in each request.  The "methodOverride" middleware allows the http post to override the method of the request with the value of the "_method" post key or with the header "x-http-method-override".  Because the user post input was not checked, req.method could contain any kind of value. Because the req.method did not match any common method VERB, connect answered with a 404 page containing the "Cannot [method] [url]" content. The method was not properly encoded for output in the browser.   ###Example: ``` ~ curl "localhost:3000" -d "_method=<script src=http://nodesecurity.io/xss.js></script>" Cannot <SCRIPT SRC=HTTP://NODESECURITY.IO/XSS.JS></SCRIPT> / ```  ###Credit: [Sergio Arcos](https://twitter.com/martes_trece)  ###History (2013-06-27) Bug reported: https://github.com/senchalabs/connect/issues/831  (2013-06-27) First fix: escape req.method output https://github.com/senchalabs/connect/commit/277e5aad6a95d00f55571a9a0e11f2fa190d8135  (2013-06-27) Second fix: whitelist https://github.com/senchalabs/connect/commit/126187c4e12162e231b87350740045e5bb06e93a
<br><br>• Affected Versions: <=2.8.0
<br>• Patched Versions: >=2.8.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
