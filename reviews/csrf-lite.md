---
Publication-State: Active
Access: Public
Reviewers:
- Name: Todd Wolfson
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/csrf-lite
Review-Date: '2016-04-23'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Non-Constant Time String Comparison*<br><br>Update to at least version 0.1.2
### Details
- csrf-lite is a cross-site request forgery protection library for framework-less node sites - csrf-lite uses `===`, a fail first string comparison, instead of a time constant string comparison - This enables an attacker being able to calculate minuscule differences in CSRF tokens, essentially enabling them to guess the token one character at a time   _Example psuedo-code of how the built-in string comparison (fail first) works_: ``` function compareTokens(a, b)     tempCheck = 0;     if a.length() != b.length()         return false;     for each character in a {         tempCheck += 1;         if a[current character check] != b[current character check]             return false;     }     return true;  csrfToken = "63737266546f6b656e"; csrfTokenCompare = user_input();  compareTokens(csrfToken, csrfTokenCompare); ``` Each check increases the variable `tempCheck` by one. If a malicious user is able to see what `tempCheck` is at each run (how long it takes to do a check), then they can see when it increases. This increase indicates that the character they just put in for `csrfTokenCompare` is the correct one.
<br><br>• Affected Versions: <=0.1.1
<br>• Patched Versions: >=0.1.2
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/isaacs/csrf-lite/pull/1']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
