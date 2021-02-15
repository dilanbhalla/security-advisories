---
Publication-State: Active
Access: Public
Reviewers:
- Name: David Johansson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/engine.io-client
Review-Date: '2016-04-26'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Insecure Defaults Allow MITM Over TLS*<br><br>Upgrade to version 1.6.9 or greater. If you are unable to upgrade, make sure and force all calls to socket.io to have a `rejectedUnauthorized: true` flag.
### Details
engine.io-client is the client for [engine.io](https://github.com/socketio/engine.io), the implementation of a transport-based cross-browser/cross-device bi-directional communication layer for Socket.IO.  The vulnerability is related to the way that node.js handles the `rejectUnauthorized` setting. If the value is something that evaluates to false, certificate verification will be disabled.  This is problematic as engine.io-client passes in an object for settings that includes the rejectUnauthorized property, whether it has been set or not. If the value has not been explicitly changed, it will be passed in as `null`, resulting in certificate verification being turned off:  ```   // line that causes bug this.rejectUnauthorized = opts.rejectUnauthorized === undefined ? null : opts.rejectUnauthorized;  ```
<br><br>• Affected Versions: <= 1.6.8
<br>• Patched Versions: >= 1.6.9
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/socketio/engine.io-client/commit/2c55b278a491bf45313ecc0825cf800e2f7ff5c1', 'https://www.cigital.com/blog/node-js-socket-io/']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
