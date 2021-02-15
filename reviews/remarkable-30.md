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
- pkg:npm/remarkable
Review-Date: '2014-11-13'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Content Injection*<br><br>Upgrade to version 1.4.1 or greater
### Details
Certain input when passed into remarkable will bypass the bad prototcol check that disallows the javascript: scheme allowing for javascript: url's to be injected into the rendered content.  ### Example  ``` [link](<javascript:alert(1)>) ``` This will be turned into `<a href="javascript:alert(1)">link</a>`  where as  ``` [link](javascript:alert(1)) ```  Would be rendered as `[link](javascript:alert(1))` because it's an invalid scheme.
<br><br>• Affected Versions: <1.4.1
<br>• Patched Versions: >=1.4.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/jonschlinkert/remarkable/issues/97']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
