---<br>Publication-State: Active<br>Access: Public<br>Reviewers:<br>- Name: Danny Grander<br>&nbsp;&nbsp;&nbsp;Associated-With-Project: false<br>&nbsp;&nbsp;&nbsp;Compensation-Source: External<br>Domain: Security<br>Methodology:<br>- Code-Review<br>Issues-Identified: Not-Examined<br>Package-URLs:<br>- pkg:npm/adm-zip<br>Date-Reviewed: 2018-08-12<br>Scope: Implementation/Full<br>Schema-Version: 1.0<br>SPDX-License-Identifier: CC-BY-4.0<br>---<br>
### Summary
Arbitrary File Write Through Archive Extraction<br><br>Update adm-zip module to version >= 0.4.9
### Details
attackers can write arbitrary files when a malicious archive is extracted.
### Methodology
This review was taken directly from the security advisories section of npm's official website.
### External References
['https://hackerone.com/reports/362118']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
