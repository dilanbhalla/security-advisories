---<br>Publication-State: "Active"<br>Access: Public<br>Reviewers:<br>- Name: Adam Baldwin<br>&nbsp;&nbsp;&nbsp;Associated-With-Project: false<br>&nbsp;&nbsp;&nbsp;Compensation-Source: "External"<br>Domain: Security<br>Methodology:<br>- Code-Review<br>Issues-Identified: "Not-Examined"<br>Package-URLs:<br>- pkg:npm/adamvr-geoip-lite<br>Date-Reviewed: '2017-01-01'<br>Scope: "Implementation/Full"<br>Schema-Version: '1.0'<br>SPDX-License-Identifier: CC-BY-4.0<br>---<br>
### Summary
Downloads Resources over HTTP<br><br>No fix is currently available for this vulnerability.  It is our recommendation to not install or use this module at this time.
### Details
adamvr-geoip-lite is a light weight native JavaScript implementation of GeoIP API from MaxMind  adamvr-geoip-lite downloads geoip resources over HTTP, which leaves it vulnerable to MITM attacks.  This impacts the integrity and availability of this geoip data that may alter the decisions made by an application using this data.
### Methodology
This review was taken directly from the security advisories section of npm's official website.
### External References
None
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
