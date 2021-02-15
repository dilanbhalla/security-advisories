---
Publication-State: Active
Access: Public
Reviewers:
- Name: Сковорода Никита Андреевич
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/concat-stream
Review-Date: '2016-08-19'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Memory Exposure*<br><br>Recommendation: update concat-stream to 1.5.2 or higher
### Details
.write(number) in the affected `concat-stream` versions passes a number to Buffer constructor, appending a chunk of uninitialized memory. Versions <1.3.0 are not affected due to not using unguarded Buffer constructor.
<br><br>• Affected Versions: >=1.3.0 <1.3.2 || >=1.4.0 <1.4.11 || >=1.5.0 <1.5.2
<br>• Patched Versions: >=1.5.2 || >=1.4.11 <1.5.0 || >=1.3.2 <1.4.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://gist.github.com/ChALkeR/c2d2fd3f1d72d51ad883df195be03a85', 'https://github.com/maxogden/concat-stream/pull/47']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
