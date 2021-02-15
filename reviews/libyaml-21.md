---
Publication-State: Active
Access: Public
Reviewers:
- Name: N/A
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/libyaml
Review-Date: '2014-02-04'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Heap Based Buffer Overflow*<br><br>Recommendation: - Update to version 0.2.3 that includes a version of LibYAML that contains a fix for this issue.
### Details
LibYAML, the library that libyaml provides bindings for is vulnerable to a heap-based buffer overflow when parsing YAML tags.
<br><br>• Affected Versions: <0.2.3
<br>• Patched Versions: >=0.2.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://cve.mitre.org/cgi-bin/cvename.cgi?name=2013-6393)', 'https://bitbucket.org/xi/libyaml/pull-request/1/fix-cve-2013-6393/diff']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
