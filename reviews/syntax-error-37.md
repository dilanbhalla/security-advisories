---
Publication-State: Active
Access: Public
Reviewers:
- Name: Cal Leeming
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/syntax-error
Review-Date: '2014-07-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Potential for Script Injection*<br><br>Recommendation: Update to version 1.1.1 or greater. If this is being used in conjunction with browserify, update browserify to 4.2.1 or greater.
### Details
The below overview of the issue is quoted from https://github.com/substack/node-browserify/blob/master/changelog.markdown#421  Make sure your installation of browserify is using syntax-error@1.1.1 or later. there was a security vulnerability where a malicious file could execute code when browserified.  The vulnerability involves breaking out of Function(), which was used to check syntax for more informative errors. In node 0.10, Function() seems to be implemented in terms of eval(), so malicious code can execute even if the function returned by Function() was never called. node 0.11 does not appear to be vulnerable.  Thanks to Cal Leeming [cal@iops.io] for discovering and disclosing this bug!
<br><br>• Affected Versions: < 1.1.1
<br>• Patched Versions: >= 1.1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/substack/node-browserify/blob/master/changelog.markdown#421)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
