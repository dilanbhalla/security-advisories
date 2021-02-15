---
Publication-State: Active
Access: Public
Reviewers:
- Name: Mark Lee
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/electron-packager
Review-Date: '2016-04-22'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*SSL Validation Defaults to False*<br><br>Recommendation: Upgrade to at least version 7.0.0  It's also recommended to delete the electron-download cache folder, by default named .electron, and located in your home folder. For example:  ``` rm -rf ~/.electron ```
### Details
- electron-packager is a command line tool that packages Electron source code into `.app` and `.exe` packages. along with Electron. - The `--strict-ssl` command line option defaults to false if not explicitly set to true  This could allow an attacker to Man In The Middle (MITM) the step where electron-packager does the following step: "Download all supported target platforms and arches of Electron using the installed electron-prebuilt version (and cache the downloads in ~/.electron)" effecting the integrity of the package and the cached downloads in ~/.electron.  This only affects users using the electron-packager CLI. The strict-ssl option defaults to true for the node.js API.
<br><br>• Affected Versions: >= 5.2.1 <= 6.0.0 || >=6.0.0 <= 6.0.2
<br>• Patched Versions: >= 7.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/electron-userland/electron-packager/issues/333']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
