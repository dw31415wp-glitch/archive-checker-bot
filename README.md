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
