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
- pkg:npm/hubl-server
Review-Date: '2017-06-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads resources over HTTP*<br><br>As there currently is not a fix available for this it is our recommendation that you do not use this module. If you must use it download the content and verify it's integrity in your production environment.
### Details
The hubl-server module is a wrapper for the HubL Development Server.  During installation hubl-server downloads a set of dependencies from api.hubapi.com. It appears in the code that these files are downloaded over HTTPS however the api.hubapi.com endpoint redirects to a HTTP url. Because of this behavior an attacker with the ability to man-in-the-middle a developer or system performing a package installation could compromise the integrity of the installation.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
