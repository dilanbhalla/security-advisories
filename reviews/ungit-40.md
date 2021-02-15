---
Publication-State: Active
Access: Public
Reviewers:
- Name: CodingTwinky
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/ungit
Review-Date: '2015-01-22'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Command Injection*<br><br>Recommendation: Update to the version >=0.9.0
### Details
Due to the use of `child_process.exec` when executing git commands, ungit allows for commands to be injection from user input fields that end up in an executed git command.
<br><br>• Affected Versions: <=0.8.4
<br>• Patched Versions: >=0.9.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/FredrikNoren/ungit/issues/486']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
