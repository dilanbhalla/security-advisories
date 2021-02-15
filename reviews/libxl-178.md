---
Publication-State: Active
Access: Public
Reviewers:
- Name: Adam Baldwin
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/libxl
Review-Date: '2016-12-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads Resources over HTTP*<br><br>It's the recommendation of the module author that if you are using this in production to 'install the bindings using a pinned and verified version of SDK instead of the automated download. More information is available in the modules [README](https://www.npmjs.com/package/libxl)
### Details
libxl provides Node bindings for the libxl library for reading and writing excel (XLS and XLSX) spreadsheets.  libxl downloads zipped resources over HTTP, which leaves it vulnerable to MITM attacks.  It may be possible to cause remote code execution (RCE) by swapping out the requested zip file with an attacker controlled zip file if the attacker is on the network or positioned in between the user and the remote server.
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
