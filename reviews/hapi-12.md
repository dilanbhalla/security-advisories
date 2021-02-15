---
Publication-State: Active
Access: Public
Reviewers:
- Name: Michele Spagnuolo
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/hapi
Review-Date: '2014-07-08'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Rosetta-Flash JSONP Vulnerability*<br><br>Recommendation: - Update to the latest version of hapi.js
### Details
This description taken from the pull request provided by Patrick Kettner.  [Background from the vulnerabilty finder](http://miki.it/blog/2014/7/8/abusing-jsonp-with-rosetta-flash/)  tl:dr - someone created a alphanum only swf converter, which means that they can in theory use it as a callback at a JSONP endpoint, and as a result, send data across domains.  Prepending callbacks with an empty inline comment breaks the flash parser, and prevents the issue. This is a fairly common solution currently being implemented by Google, Facebook, and Github.
<br><br>• Affected Versions: < 6.1.0
<br>• Patched Versions: >= 6.1.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/spumko/hapi/pull/1766)', 'https://github.com/patrickkettner)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
