# math49e

Solutions to [Project Euler](https://projecteuler.net/archives) problems

## Installation

If you haven't already, start by [installing uv](https://docs.astral.sh/uv/getting-started/installation/).

Install all dependencies:

```bash
uv sync
```

Install [pre-commit](https://pre-commit.com) git hook scripts:

```bash
uv run pre-commit install
```

## Usage

Run Python file:

```bash
uv run ./problem_zero.py
```

Run [pre-commit](https://pre-commit.com) hooks:

```bash
uv run pre-commit run --all-files
```
