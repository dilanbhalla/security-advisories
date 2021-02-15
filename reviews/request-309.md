---
Publication-State: Active
Access: Public
Reviewers:
- Name: Feross Aboukhadijeh
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/request
Review-Date: '2017-04-14'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote Memory Exposure*<br><br>Recommendation: Upgrade request to version 2.68.0 or higher. Note that versions 2.47.0-2.51.0 are not vulnerable due to a node level error that occurs when a number is passed as the body.
### Details
Request is an http client.   If a request is made using ```multipart```, and the body type is a ```number```, then the specified number of non-zero memory is passed in the body.   Example to reproduce: ``` var request = require('request'); var http = require('http');  var serveFunction = function (req, res){ 	req.on('data', function (data) {             console.log(data)         }); 	res.end(); }; var server = http.createServer(serveFunction); server.listen(8000);  request({ 	method: "POST", 	uri: 'http://localhost:8000', 	multipart: [{body:500}] },function(err,res,body){}); ```
<br><br>• Affected Versions: >=2.2.6 <2.47.0 || >2.51.0 <=2.67.0
<br>• Patched Versions: >=2.68.0
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/request/request/pull/2018', 'https://github.com/request/request/issues/1904']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
