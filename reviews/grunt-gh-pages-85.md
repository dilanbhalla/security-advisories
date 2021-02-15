---
Publication-State: Active
Access: Public
Reviewers:
- Name: Stephan Bönnemann
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/grunt-gh-pages
Review-Date: '2016-03-16'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Authentication credentails logged in clear text*<br><br>Recommendation: - Upgrade to version 1.0.0 or greater. - Consider any credentials used with these modules compromised and rotate those credentials.
### Details
A common setup to deploy to gh-pages on every commit via a CI system is to expose a github token to ENV and to use it directly in the auth part of the url.   In module versions < 0.9.1 the auth portion of the url is outputted as part of the grunt tasks logging function. If this output is publicly available then the credentials should be considered compromised.
<br><br>• Affected Versions: <=0.9.1
<br>• Patched Versions: >=0.10.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/tschaub/grunt-gh-pages/pull/41']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
