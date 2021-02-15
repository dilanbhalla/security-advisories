---
Publication-State: Active
Access: Public
Reviewers:
- Name: maxnikulin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sync-exec
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Tmp files readable by other users*<br><br>upgrade to Node >=0.12.0. The functionality is provided natively.
### Details
The sync-exec module is used to simulate child_process.execSync in node versions <0.11.9.   Sync-exec uses tmp directories as a buffer before returning values. Other users on the server have read access to the tmp directory, possibly allowing an attacker on the server to obtain confidential information from the buffer/tmp file, while it exists.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/gvarsanyi/sync-exec/issues/17', 'https://cwe.mitre.org/data/definitions/377.html', 'https://www.owasp.org/index.php/Insecure_Temporary_File']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
