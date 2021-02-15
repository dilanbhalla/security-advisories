---
Publication-State: Active
Access: Public
Reviewers:
- Name: Isaac Schlueter
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/st
Review-Date: '2014-02-06'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>- Upgrade to version 0.2.5 or greater.
### Details
Versions prior to 0.2.5 did not properly prevent folder traversal. Literal dots in a path were resolved out, but url encoded dots were not. Thus, a request like ``` /%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd ``` would leak sensitive data from the server.  As of version 0.2.5, any ```'/../'``` in the request path, urlencoded or not, will be replaced with ```'/'```. If your application depends on url traversal, then you are encouraged to please refactor so that you do not depend on having ```..``` in url paths, as this tends to expose data that you may be surprised to be exposing.
<br><br>• Affected Versions: <0.2.5
<br>• Patched Versions: >=0.2.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/isaacs/st#security-status']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
