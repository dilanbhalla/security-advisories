---
Publication-State: Active
Access: Public
Reviewers:
- Name: Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hapi
Review-Date: '2015-12-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of service - Potential socket exhaustion*<br><br>Recommendation: Upgrade to hapi v11.1.3 or greater.
### Details
Certain input passed into the If-Modified-Since or Last-Modified headers will cause an 'illegal access' exception to be raised. Instead of sending a HTTP 500 error back to the sender, hapi will continue to hold the socket open until timed out (default node timeout is 2 minutes).   Special thanks to [James Halliday](https://github.com/substack) for bringing this exception pattern to our attention via the [ecstatic advisory](https://nodesecurity.io/advisories/64) which lead to identifying this.
<br><br>• Affected Versions: <11.1.3
<br>• Patched Versions: >=11.1.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/hapijs/hapi/commit/aab2496e930dce5ee1ab28eecec94e0e45f03580', 'https://github.com/jfhbrook/node-ecstatic/pull/179']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
