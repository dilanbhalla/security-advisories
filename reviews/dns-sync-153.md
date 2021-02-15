---
Publication-State: Active
Access: Public
Reviewers:
- Name: Steve Kemp
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/dns-sync
Review-Date: '2017-04-11'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Command Injection*<br><br>Upgrade to dns-sync version 0.1.1 or greater.
### Details
The dns-sync library for node.js allows resolving hostnames in a synchronous fashion  All versions of dns-sync prior to the release 0.1.1 were vulnerable to arbitrary command execution via maliciously formed hostnames.  For example:      var dnsSync = require('dns-sync');     console.log(dnsSync.resolve('$(id > /tmp/foo)'));  This is caused by the hostname being passed through a shell as part of a command execution.
<br><br>• Affected Versions: <0.1.1
<br>• Patched Versions: >=0.1.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/skoranga/node-dns-sync/issues/1)', 'https://github.com/skoranga/node-dns-sync/commit/d9abaae384b198db1095735ad9c1c73d7b890a0d)', 'http://www.openwall.com/lists/oss-security/2014/11/11/6']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
