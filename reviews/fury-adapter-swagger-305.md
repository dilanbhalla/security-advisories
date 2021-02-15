---
Publication-State: Active
Access: Public
Reviewers:
- Name: Honza Javorek
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/fury-adapter-swagger
Review-Date: '2017-01-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Arbitrary File Read*<br><br>Upgrade to version 0.9.7 or later
### Details
fury-adapter-swagger is a fury.js adapter for loading swagger HTTP API description documents - either via YAML or JSON.  fury-adapter-swagger has a vulnerability that allows arbitrary file reads off the file system.  This could be used to retrieve sensitive data, or cause a denial of service by reading `/dev/zero`.  An example proof of concept is provided below:  ``` --- swagger: '2.0' info:   title: Read local files   version: '1.0'  paths:   /foo:     get:       responses:         200:           description: Some description           examples:             text/html:               example:                 $ref: '/etc/passwd' ```
<br><br>• Affected Versions: >= 0.2.0 <= 0.9.6 || ~0.8.0-pre
<br>• Patched Versions: > 0.9.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/distributedweaknessfiling/DWF-Database-Artifacts/blob/master/DWF/2016/1000249/CVE-2016-1000249.json']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
