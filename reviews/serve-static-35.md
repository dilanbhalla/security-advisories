---
Publication-State: Active
Access: Public
Reviewers:
- Name: Pierre-Élie Fauché
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/serve-static
Review-Date: '2015-01-13'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Open Redirect*<br><br>Recommendation: * Update to version 1.7.2 or greater (or 1.6.5 if sticking to the 1.6.x line).   * Disable redirects if not using the feature with 'redirect: false' option and cannot upgrade.
### Details
When using serve-static middleware version < 1.7.2 and it's configured to mount at the root it creates an open redirect on the site.  For example: If a user visits `http://example.com//www.google.com/%2e%2e` they will be redirected to `//www.google.com/%2e%2e`, which some browsers interpret as `http://www.google.com/%2e%2e`.
<br><br>• Affected Versions: <1.6.5 || >=1.7.0 <1.7.2
<br>• Patched Versions: ~1.6.5 || >=1.7.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/expressjs/serve-static/issues/26', 'https://www.owasp.org/index.php/Open_redirect']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
