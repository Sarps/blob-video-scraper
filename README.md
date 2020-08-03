# Blob Video Scraper

Scrape complex blob videos 

## Prerequisites

* [ffmpeg](https://www.ffmpeg.org/) (concatenate)
* [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* pip install -r requirements.txt

## Setup

`cp .env.example .env` For linux and MacOS
`copy .env.example .env` For windows

## Configure

In `config.json`

#### require

* `uri`
* `output_dir`
* `output_file`(if `concat` is `true`)

#### optional with default

* `concat`: true
* `timeout`: 20
* `headers`: {}
* `ffmpeg_path`: ffmpeg
* `ffmpeg_loglevel`: warning
* `ignore_small_file_size`: 10240
* `continue`: false
* `ssl`: true
* `base_uri`: None
