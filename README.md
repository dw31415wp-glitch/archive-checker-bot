## Overview

Takes a [quarry csv](./data/quarry-102912-untitled-run1079559.csv) of external links and checks the wayback machine for archived versions. Print the archived URL to a new csv file (./data/results\_<timestamp>.csv) like [results](./data/results_20260308204929.csv).

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

## Interstitial page demo

The repository root now includes a static `index.html` interstitial page intended
for GitHub Pages hosting. It accepts a destination URL through the `url` query
parameter and displays a warning page before navigation.

Example:

```text
https://your-pages-url.example/?url=https://archive.today/2025.01.01-120000/https://example.org/article
```

For local preview, serve the repository root with a simple static server such as:

```bash
python -m http.server
```

## GitHub Pages deployment

The repository now includes `.github/workflows/pages.yml`, which publishes the
static interstitial page with GitHub Actions.

Expected public URL:

```text
https://dw31415wp-glitch.github.io/archive-checker-bot/
```

To publish it:

1. Commit and push the changes to `main`.
2. In GitHub, open `Settings` -> `Pages`.
3. Under **Build and deployment**, set **Source** to **GitHub Actions** if it is
   not already enabled.
4. Wait for the `Deploy GitHub Pages` workflow to finish.
5. Open the public URL with a test destination, for example:

```text
https://dw31415wp-glitch.github.io/archive-checker-bot/?url=https://archive.today/2025.01.01-120000/https://example.org/article
```
