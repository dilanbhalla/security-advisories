---
Publication-State: Active
Access: Public
Reviewers:
- Name: Phil Schleihauf
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/airbrake
Review-Date: '2016-03-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insecure Default Configuration*<br><br>Change to use https or update to at least version 0.4.0
### Details
The airbrake module defaults to sending environment variables over HTTP. Environment variables can often times contain secret keys and other sensitive values. A malicious user could be on the same network as a regular user and intercept all the secret keys the user is sending. This goes against common best practice, which is to use HTTPS.
<br><br>• Affected Versions: <=0.3.8
<br>• Patched Versions: >=0.4.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/airbrake/node-airbrake/issues/70']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
