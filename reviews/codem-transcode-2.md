---
Publication-State: Active
Access: Public
Reviewers:
- Name: Neal Poole
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/codem-transcode
Review-Date: '2013-07-07'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Potential Command Injection*<br><br>Recommendation: An updated and patched version of the module (version 0.5.0) is available via npm. Users who have enabled the ffprobe functionality are especially encouraged to upgrade.
### Details
When the ffprobe functionality is enabled on the server, HTTP POST requests can be made to /probe. These requests are passed to the ffprobe binary on the server. Through this HTTP endpoint it is possible to send a malformed source file name to ffprobe that results in arbitrary command execution.  ### Mitigating Factors: The ffprobe functionality is not enabled by default. In addition, exploitation opportunities are limited in a standard configuration because the server binds to the local interface by default.
<br><br>• Affected Versions: <0.5.0
<br>• Patched Versions: >=0.5.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
