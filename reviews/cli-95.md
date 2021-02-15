---
Publication-State: Active
Access: Public
Reviewers:
- Name: Steve Kemp
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/cli
Review-Date: '2016-06-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary File Write*<br><br>Recommendation: Update to version 1.0.0 or later
### Details
``` lock_file = '/tmp/' + cli.app + '.pid', log_file = '/tmp/' + cli.app + '.log'; ``` The package `node-cli` insecurely uses the lock_file and log_file. Both of these are temporary, but it allows the starting user to overwrite any file they have access to.
<br><br>• Affected Versions: <1.0.0
<br>• Patched Versions: >=1.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=809252', 'https://github.com/node-js-libs/cli/issues/81']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
