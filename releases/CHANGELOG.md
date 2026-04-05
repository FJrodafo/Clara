# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- ...

### Changed

- ...

### Deprecated

- ...

### Removed

- ...

### Fixed

- ...

### Security

- ...

## [2.0.0] - 2026/04/05

### Added

- Interactive CLI chat loop with prompt input via `readline`.
- Persistent conversation history sent on every request to maintain multi-turn context.
- System instruction support, Clara identifies herself as an AI assistant created by FJrodafo.
- Automatic session logging, each conversation is saved as a Markdown file under `~/.clara/logs/` with a timestamped filename (e.g. `Clara_20260331_222244.md`)
- Log file includes session header with date and time, plus all user and assistant turns.
- Environment variable loading from `~/.clara/.env` (supports `GEMINI_API_KEY`).
- Graceful exit via `exit` command or `Ctrl+C` (KeyboardInterrupt), both displaying the logs path.
- Empty input detection with a friendly fallback message (`💠 Huh?`).
- Retry logic on failed API responses with a 10-second wait before retrying.
- Fallback message when the API is unreachable after all retry attempts.

### Security

- API key is read from a local `.env` file instead of being hardcoded.

[unreleased]: https://github.com/FJrodafo/Clara/compare/2.0.0...HEAD
[2.0.0]: https://github.com/FJrodafo/Clara/releases/tag/2.0.0
