---
Publication-State: Active
Access: Public
Reviewers:
- Name: Alexandra Ulsh, Abdullah Ahmet Erdem
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/mapbox.js
Review-Date: '2016-01-12'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Content Injection via TileJSON Name*<br><br>Upgrade to Mapbox.js version 2.2.4. If you are still using a 1.x version and unable to upgrade to 2.2.4, upgrade to 1.6.6.  If you are unable to upgrade to either 2.2.4 or 1.6.6, you can also remove instances of L.mapbox.shareControl from your maps.
### Details
Mapbox.js versions 1.x prior to 1.6.6 and 2.x prior to 2.2.4 are vulnerable to a cross-site-scripting attack in certain uncommon usage scenarios.  If you use L.mapbox.map and L.mapbox.shareControl it is possible for a malicious user with control over the TileJSON content to inject script content into the name value of the TileJSON. After clicking on the share control, the malicious code will execute in the context of the page using Mapbox.js.  Such usage is uncommon. L.mapbox.shareControl is not automatically added to mapbox.js maps and must be explicitly added. The following usage scenarios are not vulnerable:  - the map does not use a share control (L.mapbox.sharecontrol) - only trusted TileJSON content is loaded  Timeline: January 12, 2016 - CVE Requested
<br><br>• Affected Versions: <1.6.6 || < 2.2.4 > 2.0.0
<br>• Patched Versions: >=1.6.6 <2.0.0 || >= 2.2.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://hackerone.com/reports/99245']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
