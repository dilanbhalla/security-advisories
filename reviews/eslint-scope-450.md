---
Publication-State: Active
Access: Public
Reviewers:
- Name: pronebird
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/eslint-scope
Review-Date: '2018-07-12'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Malicious Package*<br><br>Use 3.7.1 for the latest 3.x major or upgrade to version 4.0.0 and above. It is advised that you revoke all of your existing npm tokens, recreate new tokens, enable 2FA for publishes (`auth-and-writes`).
### Details
[eslint-scope] version 3.7.2 has been published as a malicious package, where-as eslint-scope is part of the larger and more popular eslint package
<br><br>• Affected Versions: 3.7.2
<br>• Patched Versions: <=3.7.1 || >= 3.7.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/eslint/eslint-scope/issues/39', 'https://snyk.io/vuln/npm:eslint-scope', 'https://blog.sqreen.io/eslint-backdoor', 'https://docs.npmjs.com/getting-started/using-two-factor-authentication']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
