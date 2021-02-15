---
Publication-State: Active
Access: Public
Reviewers:
- Name: Сковорода Никита Андреевич
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/openwhisk
Review-Date: '2018-03-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote Memory Exposure*<br><br>Recommendation: update openwhisk to 3.3.1 or higher
### Details
When a number is passed to `api_key`, affected versions of openwhisk allocate an uninitialized buffer and send that over network in Authorization header (base64-encoded). PoC: ```js var openwhisk = require('openwhisk'); var options = {apihost: '127.0.0.1:1433', api_key: 50}; var ow = openwhisk(options); ow.actions.invoke({actionName: 'sample'}).then(result => console.log(result)) ```  Reported at 2017-03-01
<br><br>• Affected Versions: <3.3.1
<br>• Patched Versions: >=3.3.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/openwhisk/openwhisk-client-js/pull/34']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
