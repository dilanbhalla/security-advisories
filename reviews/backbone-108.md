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
- pkg:npm/backbone
Review-Date: '2016-05-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross Site Scripting*<br><br>Recommendation: Upgrade to at least version 0.5.0
### Details
backbone is a module that adds in structure to a JavaScript heavy application through key-value pairs and custom events connecting to your RESTful API through JSON  There exists a potential Cross Site Scripting vulnerability in the `Model#Escape` function if a user is able to supply input.  This is due to the regex that's replacing things to miss the conversion of things such as `&#60;` to `<`.
<br><br>• Affected Versions: <= 0.3.3
<br>• Patched Versions: >= 0.5.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/jashkenas/backbone/compare/0.3.3...0.5.0#diff-0d56d0d310de7ff18b3cef9c2f8f75dcL1008']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
