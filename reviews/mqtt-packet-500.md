---
Publication-State: Active
Access: Public
Reviewers:
- Name: Alexander Kaiser
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mqtt-packet
Review-Date: '2019-04-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Buffer Over-read*<br><br>Update mqtt-packet module to version >=3.5.1 <4.0.0 || >=4.1.3 <5.0.0 || >=5.6.1 <6.0.0 || >=6.1.2
### Details
A specifically malformed MQTT Subscribe packet crashes MQTT Brokers using the mqtt-packet module for decoding  
<br><br>• Affected Versions: <3.5.1 || >=4.0.0 <4.1.3 || >=5.0.0 <5.6.1 || >=6.0.0 <6.1.2
<br>• Patched Versions: >=3.5.1 <4.0.0 || >=4.1.3 <5.0.0 || >=5.6.1 <6.0.0 || >=6.1.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/541354']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
