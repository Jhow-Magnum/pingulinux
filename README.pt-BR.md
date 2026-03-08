# PinguLinux

Terminal Toolkit para DevOps, SysAdmin e Cybersecurity - Setup automatizado com assistente IA

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

Automatiza instalação e configuração de ferramentas essenciais de terminal em 5 minutos.

## Ferramentas

- **Ollama** - IA local para DevOps/Security (modelo customizado)
- **Atuin** - Histórico inteligente de comandos
- **Zoxide** - Navegação rápida entre diretórios
- **Navi** - Cheatsheets de comandos
- **Btop** - Monitor de sistema

## Instalação

```bash
git clone https://github.com/Jhow-Magnum/pingulinux.git
cd pingulinux
python3 PinguLinux.py
```

## Requisitos

- Python 3.6+
- Linux/macOS
- Conexão com internet

## Uso

Execute e selecione idioma (English/Português):

```bash
python3 PinguLinux.py
```

Opções do menu:
- Instalar ferramentas individualmente ou todas de uma vez
- Ver guias de uso
- Testar instalações
- Desinstalar completamente

## Funcionalidades

- Modelo IA customizado (2.3GB, especializado apenas em DevOps/Security)
- Configuração automática do .bashrc
- Desinstalação limpa (remove todos os rastros)
- Interface bilíngue (EN/PT)
- Testes automatizados incluídos

## Exemplos

```bash
# Assistente IA
ollama run devops-assistant "por que meu container docker está reiniciando"

# Histórico Inteligente
atuin search docker

# Navegação Rápida
z Documents

# Cheatsheets
navi

# Monitor
btop
```

## Testes

```bash
python3 test_pingulinux.py
```

## Contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md)

## Licença

MIT License - veja [LICENSE](LICENSE)

## Agradecimentos

- [Ollama](https://ollama.ai/)
- [Atuin](https://github.com/atuinsh/atuin)
- [Zoxide](https://github.com/ajeetdsouza/zoxide)
- [Navi](https://github.com/denisidoro/navi)
- [Btop](https://github.com/aristocratos/btop)
