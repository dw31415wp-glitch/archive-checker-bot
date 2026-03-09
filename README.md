## Overview

Takes a [./data/quarry-102912-untitled-run1079559.csv] of external links and checks the wayback machine for archived versions. Print the archived URL to a new csv file (./data/results\_<timestamp>.csv) like [./data/results_20260308204929.csv].

Obtains archive today links from https://quarry.wmcloud.org/query/102891 as suggested by Andrew Gray in [https://en.wikipedia.org/wiki/Wikipedia_talk:Archive.today_guidance#c-Andrew_Gray-20260221222900-WhatamIdoing-20260221214600]

Less than half the links have archives at the wayback machine, but this is a good start. The next step is to check archive.today for the remaining links.

## Project set up

Create a virtual environment and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Run the CLI

Run directly as a module:

```bash
python -m archive_checker_bot site-info
python -m archive_checker_bot page-info "Python (programming language)"
```

Or install the local package in editable mode and use the command name:

```bash
pip install -e .
archive-checker-bot site-info
archive-checker-bot page-info "Python (programming language)"
```

## Available commands

- `site-info` prints basic information about a wiki site.
- `page-info <title>` prints whether a page exists and basic metadata.

Both commands support:

- `--code` (default: `en`)
- `--family` (default: `wikipedia`)

Example:

```bash
archive-checker-bot site-info --code fr --family wikipedia
```
