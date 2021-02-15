---
Publication-State: Active
Access: Public
Reviewers:
- Name: Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/product-monitor
Review-Date: '2016-12-16'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads Resources over HTTP*<br><br>Update to versions 2.2.5 or later.
### Details
product-monitor is a HTML/JavaScript template for monitoring a product by encouraging product developers to gather all the information about the status of a product, including live monitoring, statistics, endpoints, and test results into one place.  product-monitor versions below 2.2.5 download JavaScript resources over HTTP, which leaves the module vulnerable to MITM attacks.  It may be possible to cause remote code execution (RCE) by swapping out the requested JavaScript file with an attacker controlled JavaScript file if the attacker is on the network or positioned in between the user and the remote server.
<br><br>• Affected Versions: <2.2.5
<br>• Patched Versions: >=2.2.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
