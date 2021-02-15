---
Publication-State: Active
Access: Public
Reviewers:
- Name: Sven Slootweg
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/react-native-meteor-oauth
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Random Token based off Math.random()*<br><br>### Details
react-native-meteor-oauth is a library for Oauth2 login to a Meteor server in React Native. The oauth Random Token is generated using a non-cryptographically strong RNG (Math.random()).
<br><br>• Affected Versions: <=99.999.99999
<br>• Patched Versions: <0.0.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/tableflip/react-native-meteor-oauth/blob/a7eb738b74c469f5db20296b44b7cae4e2337435/src/meteor-oauth.js#L66']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
