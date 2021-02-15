---
Publication-State: Active
Access: Public
Reviewers:
- Name: alexmchardy
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/i18next
Review-Date: '2017-03-15'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Cross-Site Scripting*<br><br>Upgrade to v3.4.4 or greater.
### Details
i18next is a language translation framework.  When using the `.init` method, passing interpolation options without passing an `escapeValue` will default to `undefined` rather than the assumed `true`. This can result in a cross-site scripting vulnerability because user input is assumed to be escaped, but is not.  Example: ``` var init = i18n.init({   interpolation: {     prefix: "__",     suffix: "__",     escapeValue: true   } }, function(){   var test = i18n.t('__firstName__ __lastName__', {         firstName: 'Bob',         lastName: '["foo","bar"]',   });   console.log(test); }); ``` When `escapeValue` is explicitly passed, the result of `test` is: `&lt;script&gt;alert(1)&lt;&#x2F;script&gt; Johnson`   This is supposed to be the default, however if `escapeValue` is not included, the result is the unescaped string: `<script>alert(1)</script> Johnson`
<br><br>• Affected Versions: >=2.0.0 <=3.4.3
<br>• Patched Versions: >=3.4.4
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/i18next/i18next/pull/826)']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
