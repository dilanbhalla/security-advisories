---
Publication-State: Active
Access: Public
Reviewers:
- Name: Eric Schoffstall
  Associated-With-Project: false
  Compensation-Source: external
Domain: Security
Methodology:
- Code-Review
Issues-Identified: Not-Examined
Package-URLs:
- pkg:npm/sequelize
Review-Date: '2016-07-18'
Scope: Implementation/Full
Schema-Version: '1.0'
SPDX-License-Identifier: CC-BY-4.0
---
### Summary
*SQL Injection via GeoJSON*<br><br>Recommendation: Update to the most recent version of Sequelize.
### Details
SequelizeJS 3.23.4 is vulnerable to SQL injection via GeoJSON documents containing a value with a single quote.  This vulnerability affects postresql/postgis as well as MySQL. This vulnerability only exists within GeoJSON documents using the function `ST_GeomFromGeoJSON` for postgresql/postgis and the function `GeomFromText` for mysql. SequelizeJS's `geometry` datatype is vulnerable.  If you have SequelizeJS models with a field that has a datatype of 'Geometry' and run a mysql or postgresql/postgis backend, your application is vulnerable  SequelizeJS is a popular ORM (Object Relational Mapper) for node.    GeoJSON is a format for encoding a variety of geographic data structures.
<br><br>• Affected Versions: <3.23.6
<br>• Patched Versions: >=3.23.6
### Methodology
This review was taken directly from the Security Advisories section of npm's official website.
### External References
['https://github.com/sequelize/sequelize/issues/6194', 'http://geojson.org/', 'http://docs.sequelizejs.com/en/latest/api/datatypes/#geometry']
### Disclaimer
All security reviews are conducted on a "best-effort" basis against a software component at a point in time. We make no guarantee as to the quality or completeness of any review. If you believe any content is inaccurate, we encourage you to open an issue or submit a pull request with a correction or improvement.
### License
This text is released under at least the [Creative Commons Attribution 4.0 (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/legalcode.txt). Externally-referenced content may be licensed differently.
