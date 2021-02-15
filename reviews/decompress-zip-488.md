---
Publication-State: Active
Access: Public
Reviewers:
- Name: Anonymous
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/decompress-zip
Review-Date: '2019-01-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary File Write Through Archive Extraction*<br><br>Recommendation: Update decompress-zip to either 0.2.2 or 0.3.2
### Details
attackers can write arbitrary files when a malicious archive is extracted.
<br><br>• Affected Versions: <0.2.2 || >=0.3.0 <0.3.2
<br>• Patched Versions: ~0.2.2 || >=0.3.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://snyk.io/research/zip-slip-vulnerability']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
