# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [0.3] - 2019-10-03

### Added
* --where option added to geopoints command for conditionals.


## [0.2] - 2019-10-01
### Added
* Entry point py3odb with commands: dump, geopoints, and query.
* Row objects (immutable dictionary-like, iterable sequences).
* Connection objects now have filename attribute.
* Cursor execution operations now support \<odb> tag in place of filename:

        cur.execute("SELECT DISTINCT varno FROM <odb>")

* Constants submodule with ColumnType enum and Varno static class.
* Context-manager Reader class for iterating single cursor executions:

        with Reader(filename, "SELECT lat,lon,obsvalue FROM <odb>") as odb_reader:
            for row in odb_reader:
                print(row)

### Changed
* Cursor fetches now return Row objects.
* Cursor metadata now stores column type as ColumnType.
* Split code coverage reports into unit/integration.

### Fixed
* Suppressed (by default) STDOUT messages coming from odbql.


## [0.1.1] - 2019-09-26

### Fixed
* Fixed PyPI link typo in README.md.


## [0.1] - 2019-09-26
* Initial Release.
