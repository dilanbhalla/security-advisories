---
Publication-State: Active
Access: Public
Reviewers:
- Name: Garth Boyd
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/i18n-node-angular
Review-Date: '2016-01-25'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service and Content Injection*<br><br>Recommendation: Upgrade to version 1.4.0 or greater.
### Details
- i18n-node-angular is a module used to interact between i18n and angular without using additional resources - A REST API endpoint that is used for development was not disabled in production environments - A malicious user could fill up the server causing a Denial of Service or content injection
<br><br>• Affected Versions: <1.4.0
<br>• Patched Versions: >=1.4.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/oliversalzburg/i18n-node-angular/commit/877720d2d9bb90dc8233706e81ffa03f99fc9dc8']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
