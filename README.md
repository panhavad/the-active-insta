# The Active Insta

![Language](https://img.shields.io/github/languages/top/panhavad/the-active-insta) ![Last commit](https://img.shields.io/github/last-commit/panhavad/the-active-insta) [![Release](https://img.shields.io/github/v/release/panhavad/the-active-insta?include_prereleases)](https://github.com/panhavad/the-active-insta/releases/latest)

An **Instagram automation script** that performs routine account activity to keep an account active, built on a bundled copy of `instagram_private_api` / `instagram_web_api`.

![System snapshot](docs/snapshot.svg)

## Features

- Login and session handling
- Automated feed / user activity
- Core logic in `modules/insta_core.py`
- Bundled API client libraries in `libs/`

## How it works

```mermaid
flowchart LR
    M["main.py"] --> C["insta_core"]
    C --> A["instagram_private_api client"]
    A -->|"HTTPS"| I["Instagram"]
    I --> A
    C --> L["Activity loop"]
```

## Getting started

```bash
python main.py
```

## Download

Grab the packaged source from the [latest release](https://github.com/panhavad/the-active-insta/releases/latest).

## Tech stack

- Python
- instagram_private_api

## Project structure

```text
the-active-insta/
├── docs/
├── libs/
├── modules/
├── .gitignore
├── main.py
├── README.md
└── requirements
```
