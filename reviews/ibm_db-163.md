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
- pkg:npm/ibm_db
Review-Date: '2016-12-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Downloads Resources over HTTP*<br><br>Update to version 1.0.2 or later
### Details
ibm_db is an asynchronous/synchronous interface for node.js to IBM DB2 and IBM Informix.  ibm_db downloads binary resources over HTTP, which leaves it vulnerable to MITM attacks.  It may be possible to cause remote code execution (RCE) by swapping out the requested binary with an attacker controlled binary if the attacker is on the network or positioned in between the user and the remote server.
<br><br>• Affected Versions: <1.0.2
<br>• Patched Versions: >=1.0.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/ibmdb/node-ibm_db/commit/d7e2d4b4cbeb6f067df8bba7d0b2ac5d40fcfc19#diff-315091eb1586966006e05ebc21cd2a94']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
