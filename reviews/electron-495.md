---
Publication-State: Active
Access: Public
Reviewers:
- Name: Clement Lecigne
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/electron
Review-Date: '2019-03-04'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary Code Execution*<br><br>Recommendation: Update electron module to ^2.0.18 || ^3.0.16 || ^3.1.6 || ^4.0.8 || ^5.0.0-beta.5
### Details
A vulnerability in Chromium, which Electron is based on, can be exploited and used to execute arbitrary code. According to the Electron team, "this affects any Electron application that may run third-party or untrusted JavaScript." Depending on the Electron application's privileges, this can allow an attacker to create and delete files or modify a user's system in other ways. Google has received reports of this vulnerability being exploited in the wild.
<br><br>• Affected Versions: <2.0.18 || <3.0.16 || <3.1.6 || <4.0.8 || <5.0.0-beta.5
<br>• Patched Versions: ^2.0.18 || ^3.0.16 || ^3.1.6 || ^4.0.8 || ^5.0.0-beta.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://electronjs.org/blog/filereader-fix', 'https://www.cisecurity.org/advisory/a-vulnerability-in-google-chrome-could-allow-for-arbitrary-code-execution_2019-026/', 'https://security.googleblog.com/2019/03/disclosing-vulnerabilities-to-protect.html']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
