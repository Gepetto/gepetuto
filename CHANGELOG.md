# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v2.0.3] - 2025-07-02

- Release: fix permissions

## [v2.0.2] - 2025-07-02

- Release: build dist

## [v2.0.1] - 2025-07-02

- Release: commit uv.lock

## [v2.0.0] - 2025-07-02

- :warning: require python >= 3.10
- `generate` also clear cells execution count
- switch from `poetry` to `uv`
- verbosity: add `-q`/`--quiet`, follow `QUIET`/`VERBOSITY`, and no longer `GEPETUTO_LOG_LEVEL`
- update dependencies

## [v1.3.0] - 2023-08-23

- add version argument
- fix end of generated files
- fix generate for multiple ipynb with same prefix
- add type hints checks in CI
- update some type hints

## [v1.2.0] - 2023-08-17

- add directory argument

## [v1.1.1] - 2023-08-16

- updated pre-commit hooks

## [v1.1.0] - 2023-08-16

- add the -F/--filter argument
- add the -c/--check argument
- update notebook naming convention with a dash (`-`)
- allow notebooks starting with something else than a digit
- test ipynb after generation
- fix magic.py behavior when outside of ipynb
- dependency bumps

## [v1.0.0] - 2023-08-08

- project initialisation

[Unreleased]: https://github.com/gepetto/gepetuto/compare/v2.0.3...main
[v2.0.3]: https://github.com/gepetto/gepetuto/compare/v2.0.2...v2.0.3
[v2.0.2]: https://github.com/gepetto/gepetuto/compare/v2.0.1...v2.0.2
[v2.0.1]: https://github.com/gepetto/gepetuto/compare/v2.0.0...v2.0.1
[v2.0.0]: https://github.com/gepetto/gepetuto/compare/v1.3.0...v2.0.0
[v1.3.0]: https://github.com/gepetto/gepetuto/compare/v1.2.0...v1.3.0
[v1.2.0]: https://github.com/gepetto/gepetuto/compare/v1.1.1...v1.2.0
[v1.1.1]: https://github.com/gepetto/gepetuto/compare/v1.1.0...v1.1.1
[v1.1.0]: https://github.com/gepetto/gepetuto/compare/v1.0.0...v1.1.0
[v1.0.0]: https://github.com/gepetto/gepetuto/releases/tag/v1.0.0
