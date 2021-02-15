---
Publication-State: Active
Access: Public
Reviewers:
- Name: Richard Gibson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jQuery
Review-Date: '2017-03-21'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS via improper selector detection*<br><br>Upgrade to v1.9.0 or greater.
### Details
jQuery is a javascript library for DOM manipulation.   jQuery's main method in affected versions contains an unreliable way of detecting whether the input to the `jQuery(strInput)` function is intended to be a selector or HTML.  For example, this code would be parsed as a selector, executing the code in the `onerror` attribute: ``` $("#log").html(     $("element[attribute='<img src=\"x\" onerror=\"alert(1)\" />']").html() ); ```  The fix in v1.9.0 updates a regular expression for detecting whether the input is HTML or a selector. HTML input must now explicitly start with `<`, rather than previously assuming that the input was HTML if the string contained `<` anywhere.
<br><br>• Affected Versions: >=1.7.1 <=1.8.3
<br>• Patched Versions: >=1.9.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://bugs.jquery.com/ticket/11290)', 'https://bugs.jquery.com/ticket/6429)', 'https://bugs.jquery.com/ticket/9521)', 'https://bugs.jquery.com/ticket/12531)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
