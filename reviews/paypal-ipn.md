---
Publication-State: Active
Access: Public
Reviewers:
- Name: Martin Angelov
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/paypal-ipn
Review-Date: '2014-12-03'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Validation Bypass*<br><br>- Upgrade to version 3.0.0 or greater.
### Details
paypal-ipn uses the `test_ipn` parameter (which is set by the PayPal IPN simulator) to determine if it should use the production PayPal site or the sandbox.  "With a bit of time, an attacker could craft a request using the simulator that would fool any application which does not explicitly check for test_ipn in production." [1]
<br><br>• Affected Versions: <3.0.0
<br>• Patched Versions: >=3.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/andzdroid/paypal-ipn/issues/11']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
