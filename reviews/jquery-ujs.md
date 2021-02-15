---
Publication-State: Active
Access: Public
Reviewers:
- Name: Ben Toews of GitHub
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/jquery-ujs
Review-Date: '2015-06-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*CSRF Vulnerability*<br><br>Upgrade to the latest version
### Details
This description pulled from the rubyonrails-security post.  Reported to NodeSecurity Project by Reed Loden.  CSRF Vulnerability in jquery-ujs and jquery-rails  There is an vulnerability in jquery-ujs and jquery-rails that can be used to bypass CSP protections and allows attackers to send CSRF tokens to attacker domains.  In the scenario where an attacker might be able to control the href attribute of an anchor tag or the action attribute of a form tag that will trigger a POST action, the attacker can set the href or action to " https://attacker.com" (note the leading space) that will be passed to JQuery, who will see this as a same origin request, and send the user's CSRF token to the attacker domain.
<br><br>• Affected Versions: <= 1.0.3
<br>• Patched Versions: >= 1.0.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/49935', 'https://www.npmjs.com/package/jquery-ujs', 'https://groups.google.com/forum/#!msg/rubyonrails-security/XIZPbobuwaY/fqnzzpuOlA4J', 'https://github.com/rails/jquery-ujs']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
