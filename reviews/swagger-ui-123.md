---
Publication-State: Active
Access: Public
Reviewers:
- Name: Joe Vennix
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/swagger-ui
Review-Date: '2016-07-20'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in Consumes/Produces Parameter*<br><br>Recommendation: Update to version 2.1.5 or greater.
### Details
Swagger is a standardized library for documenting API endpoints and their parameters.  Swagger uses a JSON document to organize API endpoint parameter data.  Swagger-UI version 2.1.4 contains a cross site scripting (XSS) vulnerability in the `consumes` and `produces` parameters of the swagger json document for a given API.  A maliciously crafted swagger JSON doc can be loaded via the URL query-string parameter `url`.   To exploit the vulnerability, an attacker would convince a user to visit a malicious url crafted in the following format:  ``` http://<USER_HOSTNAME>/swagger-ui/index.html?url=http://<MALICIOUS_HOSTNAME>/malicious-swagger-file.json ````  This issue is being disclosed before a public patched release is available due to the issue being made public in a Github issue.
<br><br>• Affected Versions: 2.1.4
<br>• Patched Versions: >=2.1.5
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/swagger-api/swagger-ui/issues/1866', 'https://github.com/swagger-api/swagger-ui/pull/1867']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
