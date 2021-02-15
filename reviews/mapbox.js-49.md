---
Publication-State: Active
Access: Public
Reviewers:
- Name: John Firebaugh, Juan Broullón Sampedro
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mapbox.js
Review-Date: '2015-10-24'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Content Injection via TileJSON attribute*<br><br>Recommendation: Upgrade to Mapbox.js version 2.1.7. If you are still using a 1.x version and unable to upgrade to 2.1.7, upgrade to 1.6.5.
### Details
Mapbox.js versions 1.x prior to 1.6.5 and 2.x prior to 2.1.7 are vulnerable to a cross-site-scripting attack in certain uncommon usage scenarios.  If you use L.mapbox.map or L.mapbox.tileLayer to load untrusted TileJSON content from a non-Mapbox URL, it is possible for a malicious user with control over the TileJSON content to inject script content into the "attribution" value of the TileJSON which will be executed in the context of the page using Mapbox.js.  Such usage is uncommon. The following usage scenarios are not vulnerable:  - only trusted TileJSON content is loaded - TileJSON content comes only from mapbox.com URLs - a Mapbox map ID is supplied, rather than a TileJSON URL
<br><br>• Affected Versions: <1.6.5 || < 2.1.7 > 2.0.0
<br>• Patched Versions: >=1.6.5 <2.0.0 || >= 2.1.7
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/54327']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
