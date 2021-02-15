---
Publication-State: Active
Access: Public
Reviewers:
- Name: Peter Sorowka
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mqtt-packet
Review-Date: '2016-01-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service*<br><br>Update to version 3.4.6 or 4.0.5 or greater to fix the problem.
### Details
Specifically crafted MQTT packets can crash the application, making a DoS attack feasible with very little bandwidth.   Timeline - January 15, 2016 - Initial Report (self disclosed from maintainer) - January 15, 2016 - CVE Requested
<br><br>• Affected Versions: <3.4.6 || > 4.0.0 <4.0.5
<br>• Patched Versions: >=3.4.6 < 4.0.0|| >=4.0.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/mqttjs/mqtt-packet/pull/8', 'https://github.com/mcollina/mosca/issues/393']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
