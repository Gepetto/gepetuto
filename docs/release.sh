#!/bin/bash -eux
# ./docs/release.sh [patch|minor|major|x.y.z]

[[ $(basename "$PWD") == docs ]] && cd ..


OLD=$(uv version --short)

uv version "$@"

NEW=$(uv version --short)
DATE=$(date +%Y-%m-%d)

sed -i "/^## \[Unreleased\]/a \\\n## [v$NEW] - $DATE" CHANGELOG.md
sed -i "/^\[Unreleased\]/s/$OLD/$NEW/" CHANGELOG.md
sed -i "/^\[Unreleased\]/a [v$NEW]: https://github.com/gepetto/gepetuto/compare/v$OLD...v$NEW" CHANGELOG.md
sed -i "/rev/s/$OLD/$NEW/" README.md

git add pyproject.toml CHANGELOG.md README.md
git commit -m "Release v$NEW"
git tag -s "v$NEW" -m "Release v$NEW"
git push
git push --tags
