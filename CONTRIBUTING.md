# CONTRIBUTING

## Como Contribuir

### Reportar Bugs

Abra issue com:
- Sistema operacional e versao
- Versao do Python
- Comando que causou erro
- Mensagem de erro completa

### Sugerir Funcionalidades

Abra issue descrevendo:
- Problema que resolve
- Como funcionaria
- Exemplo de uso

### Contribuir Codigo

1. Fork o repositorio
2. Crie branch: git checkout -b feature/nome
3. Commit: git commit -m "Add: descricao"
4. Push: git push origin feature/nome
5. Abra Pull Request

### Padroes de Codigo

- Python 3.6+
- Usar apenas bibliotecas padrao (os, sys, subprocess, shutil, socket)
- Manter esquema de cores: cyan (numeros), white (texto), gray (descricoes)
- Funcoes com nomes descritivos
- Comentarios apenas quando necessario

### Estrutura

PinguLinux.py - Aplicacao principal
- set_language() - Selecao de idioma
- submenu_X() - Submenus de cada ferramenta
- install_X() - Instaladores
- uninstall_X() - Desinstaladores
- menu() - Menu principal
- mainmenu() - Loop principal

### Adicionar Nova Ferramenta

1. Criar funcao install_NOME()
2. Criar funcao uninstall_NOME()
3. Criar submenu_NOME()
4. Adicionar no menu principal
5. Adicionar strings de idioma em LANG
6. Testar instalacao/desinstalacao/teste

### Testes

Antes de PR, testar:
- Instalacao em sistema limpo
- Desinstalacao completa (verificar .bashrc)
- Funcao de teste
- Ambos idiomas (PT/EN)
- Menu navegacao

### Commit Messages

- Add: nova funcionalidade
- Fix: correcao de bug
- Update: atualizacao de codigo existente
- Docs: documentacao
- Test: testes

### Code Review

PRs serao revisados para:
- Funcionalidade
- Compatibilidade
- Qualidade de codigo
- Documentacao

### Licenca

Ao contribuir, voce concorda que seu codigo sera licenciado sob a mesma licenca do projeto.
