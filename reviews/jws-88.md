---
Publication-State: Active
Access: Public
Reviewers:
- Name: Brian Brennan and Tim McLean
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jws
Review-Date: '2016-07-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Forgeable Public/Private Tokens*<br><br>Recommendation: Update to version 3.0.0 or later.
### Details
Since "algorithm" isn't enforced in `jws.verify()`, a malicious user could choose what algorithm is sent to the server. If the server is expecting RSA but is sent HMAC-SHA with RSA's public key, the server will think the public key is actually an HMAC private key. This could be used to forge any data an attacker wants.  In addition, there is the `none` algorithm to be concerned about.  In versions prior to 3.0.0, verification of the token could be bypassed when the `alg` field is set to `none`.  *Edit ( 7/29/16 ): A previous version of this advisory incorrectly stated that the vulnerability was patched in version 2.0.0 instead of 3.0.0. The advisory has been updated to reflect this new information. Thanks to Fabien Catteau for reporting the error.*
<br><br>• Affected Versions: <3.0.0
<br>• Patched Versions: >=3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/', 'https://github.com/brianloveswords/node-jws/commit/585d0e1e97b6747c10cf5b7689ccc5618a89b299#diff-4ac32a78649ca5bdd8e0ba38b7006a1e']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
