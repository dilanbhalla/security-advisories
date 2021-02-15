---
Publication-State: Active
Access: Public
Reviewers:
- Name: mcollina
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mqtt
Review-Date: '2018-01-02'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote PUBLISH DoS*<br><br>Update to version 2.15.0 or later.
### Details
MQTT.js 2.x.x prior to 2.15.0 issue in handling PUBLISH tickets may lead to an attacker causing a denial-of-service condition.
<br><br>• Affected Versions: >=2.0.0
<br>• Patched Versions: >=2.15.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/mqttjs/MQTT.js/commit/403ba53b838f2d319a0c0505a045fe00239e9923', 'https://github.com/mqttjs/MQTT.js/releases/tag/v2.15.0', 'https://jvn.jp/en/jp/JVN45494523/index.html']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
