---
Publication-State: Active
Access: Public
Reviewers:
- Name: Tim McLean
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jsonwebtoken
Review-Date: '2015-04-01'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Verification Bypass*<br><br>Update to a version 4.2.2 or greater
### Details
It is possible for an attacker to bypass verification when "a token digitally signed with an asymetric key (RS/ES family) of algorithms but instead the attacker send a token digitally signed with a symmetric algorithm (HS* family)" [1]
<br><br>• Affected Versions: <4.2.2
<br>• Patched Versions: >=4.2.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/auth0/node-jsonwebtoken/commit/1bb584bc382295eeb7ee8c4452a673a77a68b687', 'https://www.timmclean.net/2015/02/25/jwt-alg-none.html', 'https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
