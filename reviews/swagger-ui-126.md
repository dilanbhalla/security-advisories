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
Review-Date: '2016-07-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS in key names*<br><br>Update to the latest version of swagger-ui.  Our primary recommendation is to host swagger documentation on a separate domain distinct from the application domain.  Also, we recommend implementing a content security policy (CSP) that restricts the domains from which JSON files can be requested in order to avoid loading malicious JSON docs via the `URL` query string parameter.
### Details
Swagger is a standardized library for documenting API endpoints and their parameters.  Swagger uses a JSON document to organize API endpoint parameter data.  Swagger-ui contains a cross site scripting (XSS) vulnerability in the key names for the following object path in the JSON document: ```  .definitions.<USER_DEFINED>.properties.<INJECTABLE_KEY_NAME> ``` Supplying a key name with script tags causes arbitrary code execution.  In addition it is possible to load the arbitrary JSON files remotely via the `URL` query-string parameter.  This advisory is being disclosed before a public patched release is available because of a public Github issue documenting the vulnerability.
<br><br>• Affected Versions: <=2.2.0
<br>• Patched Versions: >=2.2.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/swagger-api/swagger-ui/issues/1865', 'https://en.wikipedia.org/wiki/Content_Security_Policy']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
