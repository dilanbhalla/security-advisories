---
Publication-State: Active
Access: Public
Reviewers:
- Name: Ajin Abraham
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/node-serialize
Review-Date: '2017-02-09'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Code Execution through IIFE*<br><br>Recommendation: There is no patch yet available for this vulnerability, and thus we recommend not using it in network applications in combination with untrusted user input until a patch is available.
### Details
node-serialize is a module for serializing an object or function into JSON.  node-serialize can be abused to execute arbitrary code via a [immediately invoked function expression](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression) (IIFE) if untrusted user input is passed into `unserialize()`
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/', 'https://github.com/luin/serialize/issues/4']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
