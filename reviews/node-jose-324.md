---
Publication-State: Active
Access: Public
Reviewers:
- Name: Antonio Sanso
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/node-jose
Review-Date: '2017-03-13'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Invalid Curve Attack*<br><br>Upgrade to version 0.9.3 or greater
### Details
node-jose is a JavaScript implementation of the JSON Object Signing and Encryption (JOSE) for current web browsers and node.js-based servers.  As outlined in [this post](http://blog.intothesymmetry.com/2017/03/critical-vulnerability-in-json-web.html) node-jose earlier than version 0.9.3 is vulnerable to an invalid curve attack. This allows an attacker to recover the private secret key when JWE with Key Agreement with Elliptic Curve Diffie-Hellman Ephemeral Static (ECDH-ES) is used.  [Proof of Concept](https://gist.github.com/asanso/fa25685348051ef6a28d49aa0f27a4ae)
<br><br>• Affected Versions: <0.9.3
<br>• Patched Versions: >=0.9.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['http://blog.intothesymmetry.com/2017/03/critical-vulnerability-in-json-web.html', 'https://github.com/cisco/node-jose']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
