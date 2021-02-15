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
- pkg:npm/floody
Review-Date: '2016-01-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote Memory Exposure*<br><br>Recommendation: update floody to 1.1.1 or higher
### Details
`.write(number)` in the affected `floody` versions passes a number to Buffer constructor, appending a chunk of uninitialized memory. PoC: `var f = require('floody')(process.stdout); f.write(1000); f.stop();`
<br><br>• Affected Versions: <0.1.1
<br>• Patched Versions: >=0.1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/soldair/node-floody/commit/6c44722312131f4ac8a1af40f0f861c85efe01b0']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
