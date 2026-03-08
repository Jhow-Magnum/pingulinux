# PinguLinux

Terminal Toolkit for DevOps, SysAdmin & Cybersecurity - Automated setup with AI assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

Automates installation and configuration of essential terminal tools in 5 minutes.

## Tools

- **Ollama** - Local AI for DevOps/Security (custom model)
- **Atuin** - Smart command history
- **Zoxide** - Fast directory navigation
- **Navi** - Command cheatsheets
- **Btop** - System monitor

## Installation

```bash
git clone https://github.com/Jhow-Magnum/pingulinux.git
cd pingulinux
python3 PinguLinux.py
```

## Requirements

- Python 3.6+
- Linux/macOS
- Internet connection

## Usage

Run and select language (English/Português):

```bash
python3 PinguLinux.py
```

Menu options:
- Install tools individually or all at once
- View usage guides
- Test installations
- Uninstall cleanly

## Features

- Custom AI model (2.3GB, specialized in DevOps/Security only)
- Automatic .bashrc configuration
- Clean uninstallation (removes all traces)
- Bilingual interface (EN/PT)
- Automated tests included

## Examples

```bash
# AI Assistant
ollama run devops-assistant "why is my docker container restarting"

# Smart History
atuin search docker

# Fast Navigation
z Documents

# Cheatsheets
navi

# Monitor
btop
```

## Testing

```bash
python3 test_pingulinux.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT License - see [LICENSE](LICENSE)

## Acknowledgments

- [Ollama](https://ollama.ai/)
- [Atuin](https://github.com/atuinsh/atuin)
- [Zoxide](https://github.com/ajeetdsouza/zoxide)
- [Navi](https://github.com/denisidoro/navi)
- [Btop](https://github.com/aristocratos/btop)
