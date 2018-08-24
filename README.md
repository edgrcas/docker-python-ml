# Logos Engine Core
[![Standard Version](https://img.shields.io/badge/release-standard%20version-brightgreen.svg)](https://github.com/conventional-changelog/standard-version)

## Developer Stage
### Pre-Install

 - Docker 1.*

### Build Alphanum

    cd /alphanum
    docker build -t py-alphanum-ml .
    docker run -v $(pwd):/app:rw -it py-alphanum-ml sh

### Build Bot

    cd /bot
    docker build -t py-bot-ml .
    docker run -v $(pwd):/app:rw -it py-bot-ml sh
