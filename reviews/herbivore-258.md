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
- pkg:npm/herbivore
Review-Date: '2017-01-01'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads Resources over HTTP*<br><br>Recommendation: An update is available in GitHub, but has yet to be published. Apply [this update](https://github.com/samatt/Herbivore/commit/0a041defc3463e99948e5d2064aef54b2128c5a3) manually before installing the module.
### Details
herbivore is a packet sniffing and crafting library. Built on libtins  herbivore 0.0.3 and below download binary resources over HTTP, which leaves it vulnerable to MITM attacks.  It may be possible to cause remote code execution (RCE) by swapping out the requested resources with an attacker controlled copy if the attacker is on the network or positioned in between the user and the remote server.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/samatt/Herbivore/commit/0a041defc3463e99948e5d2064aef54b2128c5a3']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
