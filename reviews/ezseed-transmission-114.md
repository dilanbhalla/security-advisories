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
- pkg:npm/ezseed-transmission
Review-Date: '2016-07-29'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insecure Defaults Leads to Potential MITM*<br><br>Recommendation: Upgrade to at least version 0.0.15
### Details
ezseed-transmission is a module that provides shell bindings for Ezseed transmission.  Between versions 0.0.10 and 0.0.14 (inclusive), ezseed-transmission would download a script from `http://stedolan.github.io/jq/download/linux64/jq` without checking the certificate.  An attacker on the same network or on an ISP level could intercept the traffic and push their own version of the file, causing the attackers code to be executed.
<br><br>• Affected Versions: >= 0.0.10 <= 0.0.14
<br>• Patched Versions: >= 0.0.15
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
