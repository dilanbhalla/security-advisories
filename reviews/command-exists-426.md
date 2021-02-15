---
Publication-State: Active
Access: Public
Reviewers:
- Name: Сковорода Никита Андреевич
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/command-exists
Review-Date: '2018-05-11'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Command Injection - Generic*<br><br>Recommendation: update command-exists to 1.2.4 or higher
### Details
`command-exists` concatenates unsanitized input into exec()/execSync() commands
<br><br>• Affected Versions: <=1.2.3
<br>• Patched Versions: >=1.2.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/324453', 'https://github.com/mathisonian/command-exists/blob/v1.2.2/lib/command-exists.js#L49-L94']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
