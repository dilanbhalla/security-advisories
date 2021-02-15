---
Publication-State: Active
Access: Public
Reviewers:
- Name: Stefan Mirea
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/express-restify-mongoose
Review-Date: '2016-04-19'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Private Data Disclosure*<br><br>Recommendation: Update to at least version 3.1.0 or 2.5.0
### Details
express-restify-mongoose is a module to easily create a flexible REST interface for mongoose models.  If you have a user model that you want to protect, such as the following User model: ``` const User = mongoose.model('User', new mongoose.Schema({     name: String,     password: String, })); ```  You would normally do something such as: ``` restify.serve(router, User, {     private: ['password'], // Set the password part of User as private, so outside people can't read it }) ```  This would hide the password field from people that send your application a `GET /User` and `GET /User/some-user-id` request.   A malicious user can go to your application and send a request for `GET /User?distinct=password` and get all the passwords for all the users in the database, despite the field being set to private. This can be used for other private data if the malicious user knew what was set as private for specific routes.
<br><br>• Affected Versions: <= 2.4.2 || >= 3.0.0 <=3.0.1
<br>• Patched Versions: >=2.5.0 <= 3.0.0 || >=3.1.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/florianholzapfel/express-restify-mongoose/issues/252']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
