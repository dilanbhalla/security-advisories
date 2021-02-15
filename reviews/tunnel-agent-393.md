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
- pkg:npm/tunnel-agent
Review-Date: '2018-03-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Memory Exposure*<br><br>Recommendation: update tunnel-agent to 0.6.0 or higher
### Details
PoC: ```js require('request')({   method: 'GET',   uri: 'http://www.example.com',   tunnel: true,   proxy:{       protocol: 'http:',       host:'127.0.0.1',       port:8080,       auth:80 // number   } }); ```  Reported at 2016-11-20.
<br><br>• Affected Versions: <0.6.0
<br>• Patched Versions: >=0.6.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://gist.github.com/ChALkeR/fd6b2c445834244e7d440a043f9d2ff4', 'https://github.com/request/tunnel-agent/commit/9ca95ec7219daface8a6fc2674000653de0922c0']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
