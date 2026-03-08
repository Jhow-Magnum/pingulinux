# PinguLinux

DevOps, SysAdmin & Cybersecurity Terminal Toolkit - Professional setup in 5 minutes

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

Automated installation and configuration of essential tools for DevOps, SysAdmin and Cybersecurity professionals.

## Problem

Setting up a professional terminal environment takes 1-2 hours:
- Manual installation of Ollama, Atuin, Zoxide, Navi, Btop
- Individual configuration of each tool
- Testing functionality
- Cleanup when no longer needed

## Solution

PinguLinux automates everything in 5 minutes with an interactive interface.

## Tools

- **Ollama** - Local AI specialized in DevOps/Security
- **Atuin** - Smart command history
- **Zoxide** - Fast directory navigation
- **Navi** - Interactive command cheatsheets
- **Btop** - Visual system monitor

## Installation

```bash
git clone https://github.com/your-username/pingulinux.git
cd pingulinux
python3 PinguLinux.py
```

## Requirements

- Python 3.6+
- Linux/macOS
- Internet connection

## Usage

```bash
python3 PinguLinux.py
```

Select language (Portuguese/English) and navigate menus:

```
01 - Ollama      Local AI
02 - Atuin       Smart history
03 - Zoxide      Fast navigation
04 - Navi        Command cheatsheets
05 - Btop        System monitor

90 - Install All
91 - Uninstall All
99 - Update
00 - Exit
```

Each tool has submenu:
- Install
- Usage guide
- Uninstall
- Test

## Features

**Custom AI**
- phi3:mini model (2.3GB) - 50% smaller than llama3
- Specialized context: only answers DevOps/Security
- Rejects irrelevant topics

**Smart Installation**
- Checks if already installed
- Tests connectivity
- Automatic configuration (.bashrc)

**Clean Uninstallation**
- Removes binaries and configurations
- Cleans .bashrc automatically
- No residues

**Professional Interface**
- Bilingual (PT/EN)
- Intuitive menus
- Integrated usage guides
- Automated tests

## Use Cases

**SysAdmin**
- Server management
- Critical command history
- Visual resource monitoring

**DevOps/SRE**
- Instant troubleshooting with AI
- Fast navigation between projects
- Ready Docker/K8s commands

**Cybersecurity**
- AI specialized in hardening
- Vulnerability analysis
- Ready pentest commands

**Students**
- Learn Linux commands 10x faster
- AI explains any command
- Professional environment

## Time Savings

**Setup:**
- Manual: 60-120 min
- PinguLinux: 5 min

**Daily usage:**
- Search commands: -80% time
- Navigate directories: -90% time
- Troubleshooting: -70% time
- Learn commands: -85% time

## Examples

**AI DevOps**
```bash
ollama run devops-assistant "why is my docker container restarting"
ollama run devops-assistant "how to secure ssh server"
```

**Smart History**
```bash
atuin search docker
atuin stats
Ctrl+R
```

**Fast Navigation**
```bash
z Documents
z proj
zi
```

**Cheatsheets**
```bash
navi
Ctrl+G
```

**Monitor**
```bash
btop
```

## Tests

```bash
python3 test_pingulinux.py
```

9 automated tests verify:
- Imports and syntax
- Main functions
- System checks
- Colors and interface

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Bug reports
- Feature suggestions
- Code contributions
- Project standards

## Structure

```
pingulinux/
├── PinguLinux.py          Main application
├── Modelfile.devops       Custom AI model
├── test_pingulinux.py     Automated tests
├── README.md              This file
├── LICENSE                MIT License
├── CONTRIBUTING.md        Contribution guide
├── HISTORICO.md           Development history
├── OLLAMA_MODELS.md       AI models documentation
├── RESUMO.md              Project summary
└── USO_REAL.md            Detailed use cases
```

## Technologies

- Python 3.6+ (standard libraries only)
- Ollama (phi3:mini)
- Atuin
- Zoxide
- Navi
- Btop

## License

MIT License - see [LICENSE](LICENSE) for details.

## Support

- Issues: [GitHub Issues](https://github.com/your-username/pingulinux/issues)
- Discussions: [GitHub Discussions](https://github.com/your-username/pingulinux/discussions)

## Acknowledgments

Included tools:
- [Ollama](https://ollama.ai/)
- [Atuin](https://github.com/atuinsh/atuin)
- [Zoxide](https://github.com/ajeetdsouza/zoxide)
- [Navi](https://github.com/denisidoro/navi)
- [Btop](https://github.com/aristocratos/btop)
