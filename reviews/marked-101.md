---
Publication-State: Active
Access: Public
Reviewers:
- Name: Matt Austin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/marked
Review-Date: '2016-04-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Sanitization bypass using HTML Entities*<br><br>Upgrade to version 0.3.6 or greater.
### Details
marked is an application that is meant to parse and compile markdown.  Due to the way that marked parses input, specifically HTML entities, it's possible to bypass marked's content injection protection (`sanitize: true`) to inject a `javascript:` URL.  This flaw exists because `&#xNNanything;` gets parsed to what it could and leaves the rest behind, resulting in just `anything;` being left.   For example:  If a malicious user could provide this input to the application `javascript&#x58document;alert&#40;1&#41;` resulting in a valid link, that when a user clicked it would execute `alert(1)`.
<br><br>• Affected Versions: <=0.3.5
<br>• Patched Versions: >=0.3.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/chjj/marked/pull/592', 'https://github.com/chjj/marked/pull/592/commits/2cff85979be8e7a026a9aca35542c470cf5da523']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
