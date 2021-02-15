---
Publication-State: Active
Access: Public
Reviewers:
- Name: Unknown
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/passport-azure-ad
Review-Date: '2016-12-06'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Authentication bypass*<br><br>Recommendation: If using passport-azure-ad 1.x update to at least version 1.4.6, if using 2.x update to at least version 2.0.1
### Details
The Microsoft Azure Active Directory Passport (aka Passport-Azure-AD) library 1.x before 1.4.6 and 2.x before 2.0.1 for Node.js does not recognize the validateIssuer setting, which allows remote attackers to bypass authentication via a crafted token.
<br><br>• Affected Versions: >= 1.0.0 < 1.4.6 || 2.0.0
<br>• Patched Versions: >= 1.4.6 < 2.0.0 || >= 2.0.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/AzureAD/passport-azure-ad/blob/master/SECURITY-NOTICE.MD', 'https://support.microsoft.com/en-us/kb/3187742']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
