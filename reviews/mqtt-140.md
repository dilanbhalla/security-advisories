---
Publication-State: Active
Access: Public
Reviewers:
- Name: Matteo Collina
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mqtt
Review-Date: '2016-08-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Denial of Service*<br><br>Upgrade to v1.0.0 or later
### Details
Specifically crafted MQTT packets can crash the application, making a DoS attack feasible with very little bandwidth.
<br><br>• Affected Versions: <=0.3.13
<br>• Patched Versions: >=1.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/mqttjs/MQTT.js/blob/388a084d7803934b18b43c1146c817deaa1396b1/lib/parse.js#L230']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
