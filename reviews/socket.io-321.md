---
Publication-State: Active
Access: Public
Reviewers:
- Name: Martin Thomson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/socket.io
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insecure randomness*<br><br>Recommendation: Upgrade to v0.9.7 or later.
### Details
Socket.io is a realtime application framework that provides communication via websockets.  Because socket.io depends on `Math.random()` to create socket IDs, the IDs are predictable. An attacker is able to guess the socket ID and gain access to socket.io servers, potentially obtaining sensitive information.
<br><br>• Affected Versions: <=0.9.6
<br>• Patched Versions: >=0.9.7
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/socketio/socket.io/issues/856)', 'https://github.com/socketio/socket.io/pull/857', 'https://github.com/socketio/socket.io/commit/67b4eb9abdf111dfa9be4176d1709374a2b4ded8']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
