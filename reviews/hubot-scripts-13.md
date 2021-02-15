---
Publication-State: Active
Access: Public
Reviewers:
- Name: Neal Poole
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hubot-scripts
Review-Date: '2013-05-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Potential Command Injection*<br><br>Recommendation: A new version containing a fix has yet to be pushed to NPM. Use the version located at https://github.com/github/hubot-scripts/ until version 2.4.4 comes out.
### Details
Untrusted input passed in to the hubot-scripts/package/src/scripts/email.coffee module can allow for command injection. This may be unexpected behavior for the caller.  ### Mitigating Factors The email script is not enabled by default, it has to be manually added to hubot's list of loaded scripts.
<br><br>• Affected Versions: <= 2.4.3
<br>• Patched Versions: > 2.4.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
