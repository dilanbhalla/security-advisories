---
Publication-State: Active
Access: Public
Reviewers:
- Name: Theofanis Katsimpas
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jwt-simple
Review-Date: '2016-10-31'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Forgeable Public/Private Tokens*<br><br>Recommendation: Change jwt.decode() to include an algorithm parameter.
### Details
Since "algorithm" isn't enforced in jwt.decode(), a malicious user could choose what algorithm is sent sent to the server. If the server is expecting RSA but is sent HMAC-SHA with RSA's public key, the server will think the public key is actually an HMAC private key. This could be used to forge any data an attacker wants.
<br><br>• Affected Versions: < 0.3.0
<br>• Patched Versions: >= 0.3.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/', 'https://github.com/hokaccha/node-jwt-simple/pull/14', 'https://github.com/hokaccha/node-jwt-simple/pull/16']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
