---
Publication-State: Active
Access: Public
Reviewers:
- Name: Mitar, Will White & the team at Mapbox, Max Motovilov, and James Taylor
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/npm
Review-Date: '2016-04-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*npm Token Leak*<br><br>Upgrade npm itself with `npm install npm@latest -g` and [revoke your tokens](https://www.npmjs.com/settings/tokens)
### Details
The primary npm registry has, since late 2014, used HTTP bearer tokens to authenticate requests from the npm command-line interface. Due to a design flaw in the CLI, these bearer tokens were sent with every request made by the CLI for logged-in users, regardless of the destination of the request. They should instead only be included for requests made against the registry or registries used for the current install.  This flaw allows an attacker to set up an HTTP server that could collect authentication information they could use to impersonate the users whose tokens they collected. This impersonation would allow them to do anything the compromised users could do, including publishing new versions of packages.
<br><br>• Affected Versions: <= 2.15.0 || >= 3.0.0 <= 3.8.2
<br>• Patched Versions: >= 2.15.1 <= 3.0.0 || >= 3.8.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://nodejs.org/en/blog/vulnerability/npm-tokens-leak-march-2016/', 'http://blog.npmjs.org/post/142036323955/fixing-a-bearer-token-vulnerability']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
