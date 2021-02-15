### Summary
XSS in Hover Over Label Names<br><br>Escape the label names. They can be escaped using only a few lines of code. A pull request with a fix has been merged on GitHub, but not published to npm. This can be found on [Github.](https://github.com/morrisjs/morris.js/commit/1c66cfc4ac7b23d324f131bec7739265887e30fc)
### Details
Morris.js creates an svg graph, with labels that appear when hovering over a point. The hovering label names are not escaped. If control over the labels is obtained, script can be injected. The script will run on the client side whenever that specific graph is loaded.
### Methodology
This review was taken directly from the security advisories section of npm's official website.
### External References
['https://github.com/morrisjs/morris.js/pull/464']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
