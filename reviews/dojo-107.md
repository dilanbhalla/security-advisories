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
- pkg:npm/dojo
Review-Date: '2016-05-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross Site Scripting*<br><br>Recommendation: Upgrade to at least version 1.1
### Details
dojo is the core module for the Dojo Toolkit. The dojo package covers a wide range of functionality like AJAX, DOM manipulation, class-type programming, events, promises, data stores, drag-and-drop and internationalization libraries.  There is a bug in the `dijit.Editor` and `textarea` where input, even sanitized, executes javascript. This is because the `<textarea>` tag only sees the final, unsanitized, user input.
<br><br>• Affected Versions: <= 1.0
<br>• Patched Versions: >= 1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://bugs.dojotoolkit.org/ticket/2140']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
