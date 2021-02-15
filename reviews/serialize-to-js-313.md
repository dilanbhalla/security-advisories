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
- pkg:npm/serialize-to-js
Review-Date: '2017-02-10'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Code Execution Through IIFE*<br><br>Recommendation: Upgrade to version 1.0.0, be aware of [this disclaimer](https://www.npmjs.com/package/serialize-to-js#deserialize) from the author.
### Details
Serialize-to-js can "serialize objects into a require-able module while checking circular structures and respecting references."  Passing untrusted data to the `.deserialize` function can cause arbitrary code execution through an Immediately Invoked Function Expression (IIFE).   Example: ``` var payload = "{e: (function(){ eval('console.log(`exploited`)') })() }" var serialize = require('serialize-to-js'); serialize.deserialize(payload); ```
<br><br>• Affected Versions: <=0.5.0
<br>• Patched Versions: >=1.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://www.npmjs.com/package/serialize-to-js#deserialize']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
