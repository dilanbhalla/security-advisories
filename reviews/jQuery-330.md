---
Publication-State: Active
Access: Public
Reviewers:
- Name: Michał Gołębiowski
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jQuery
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Exceeding Stack Call Limit DoS*<br><br>Recommendation: Upgrade to v3.0.0 or greater.
### Details
jQuery is a DOM manipulation javascript library.  In v2.2.4 and previous, a lowercasing logic was used on the attribute names and was removed in v3.0.0. Because of this, boolean attributes whose names were not all lowercase cause infinite recursion, and will exceed the stack call limit.
<br><br>• Affected Versions: =3.0.0-rc.1
<br>• Patched Versions: >=3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/jquery/jquery/issues/3133)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
