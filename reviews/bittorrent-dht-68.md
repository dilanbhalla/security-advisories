---
Publication-State: Active
Access: Public
Reviewers:
- Name: Feross Aboukhadijeh / Mathias Buss Madsen
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/bittorrent-dht
Review-Date: '2016-01-04'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*Remote Memory Disclosure*<br><br>Update to version 5.1.3 or greater
### Details
A security issue was found in bittorrent-dht that allows someone to send a specific series of messages to a listening peer and get it to reveal internal memory.  There are two mitigating factors here, that slightly reduce the impact of this vulnerability:  1. Any modern kernel will zero out new memory pages before handing them off to a process. This means that only memory previously used and deallocated by the node process can be leaked. 1. Node.js manages Buffers by creating a few large internal SlowBuffers, and slicing them up into smaller Buffers which are made accessible in JS. They are not stored on V8's heap, because garbage collection would interfere. The result is that only memory that has been previously allocated as a Buffer can be leaked.
<br><br>• Affected Versions: <5.1.3
<br>• Patched Versions: >=5.1.3
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/feross/bittorrent-dht/issues/87']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
