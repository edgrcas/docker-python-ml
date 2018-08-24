# Logos Engine Core
[![Standard Version](https://img.shields.io/badge/release-standard%20version-brightgreen.svg)](https://github.com/conventional-changelog/standard-version)

## Developer Stage
### Pre-Install

 - Docker 1.*

### Run Dev

    cd /[project_path]
    docker build -t python-ml .
    docker run -v $(pwd):/app:rw -it python-ml sh
