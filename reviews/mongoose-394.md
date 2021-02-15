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
- pkg:npm/mongoose
Review-Date: '2016-01-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote Memory Exposure*<br><br>Recommendation: update mongoose to 4.3.6 or higher
### Details
Trying to save a number to a field of type Buffer on the affected mongoose versions allocates a chunk of uninitialized memory and stores it in the database.
<br><br>• Affected Versions: >=3.5.5 <=3.8.38 || >=4.0.0 <=4.3.5
<br>• Patched Versions: >=4.3.6 || >=3.8.39 <4.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/Automattic/mongoose/issues/3764', 'https://gist.github.com/ChALkeR/d4a8055625221b6e65f0', 'https://gist.github.com/ChALkeR/440bc3dfcbd9b6da75c3']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
