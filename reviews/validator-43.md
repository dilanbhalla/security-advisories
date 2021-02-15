---
Publication-State: Active
Access: Public
Reviewers:
- Name: taku0
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/validator
Review-Date: '2014-10-27'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*XSS Filter Bypass via Encoded URL*<br><br>Recommendation: Upgrade to the latest version of this library. However, it should be noted that the fix for this vulnerability was to remove the xss filter functionality. Seek another library to provide proper output encoding.
### Details
The validator module for Node.js contains functionality meant to filter potential XSS attacks (a filter called xss). A method of bypassing the filter via an encoded URL has been publicly disclosed. In general, because the function’s filtering is blacklist-based it is likely that other bypasses will be discovered in the future. Developers are encouraged not to use the xss filter function in this package.  ### Details: The xss() function removes the word "javascript" when contained inside an attribute. However, it does not properly handle cases where characters have been hex-encoded. As a result, it is possible to build an input that bypasses the filter but which the browser will accept as valid JavaScript.  For example, browsers interpret `<a href="jav&#x61;script:...">abc</a>` as `<a href="javascript:...">abc</a>`.
<br><br>• Affected Versions: <2.0.0
<br>• Patched Versions: >=2.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/chriso/validator.js/issues/181']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
