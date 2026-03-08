#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil
import socket

# LANGUAGE STRINGS
LANG = {}

def set_language():
    global LANG
    
    os.system("clear")
    print(f"""{cyan}

 _____   _                        _       _
|  __ \\ (_)                      | |     (_)
| |__) | _  _ __    __ _  _   _  | |      _  _ __   _   _ __  __
|  ___/ | || '_ \\  / _` || | | | | |     | || '_ \\ | | | |\\ \\/ /
| |     | || | | || (_| || |_| | | |____ | || | | || |_| | >  <
|_|     |_||_| |_| \\__, | \\__,_| |______||_||_| |_| \\__,_|/_/\\_\\
                    __/ |
                   |___/

{reset}""")
    
    print(f"         {white}Select Language / Selecione o Idioma:\n")
    print(f"         {cyan}1{white} - English")
    print(f"         {cyan}2{white} - Português\n")
    
    choice = input(f"         {white}> ")
    
    if choice == "2":
        LANG = {
            'menu_desc1': 'Kit de ferramentas para terminal profissional',
            'menu_desc2': 'Instale utilidades essenciais para DevOps/SysAdmin',
            'menu_choose': 'Escolha o número ou digite sair',
            'ollama_desc': 'IA Local (modelos leves)',
            'atuin_desc': 'Histórico inteligente',
            'zoxide_desc': 'Navegação rápida',
            'navi_desc': 'Comandos prontos',
            'btop_desc': 'Monitor de sistema',
            'install_all': 'Instalar Tudo',
            'update': 'Atualizar',
            'exit': 'Sair',
            'choose': 'escolha',
            'press_enter': 'Pressione ENTER para voltar',
            'exiting': 'Fechando',
            'already_installed': 'já instalado',
            'server_running': 'Servidor rodando',
            'start_server': 'Iniciar servidor?',
            'choose_model': 'Escolha o modelo:',
            'install_q': 'Instalar',
            'cancelled': 'Cancelado',
            'installing': 'Instalando',
            'installed': 'Instalado!',
            'failed': 'Falhou',
            'not_configured': 'Não configurado',
            'recent_dirs': 'Diretórios recentes:',
            'no_dirs': 'Nenhum rastreado',
            'usage': 'Uso:',
            'launch_with': 'Iniciar:',
            'shortcuts': 'Atalhos:',
            'installing_all': 'Instalando tudo...',
            'updating': 'Atualizando...',
            'updated': 'Atualizado'
        }
    else:
        LANG = {
            'menu_desc1': 'Terminal bootstrap toolkit',
            'menu_desc2': 'Essential utilities for DevOps/SysAdmin',
            'menu_choose': 'Choose number or type exit',
            'ollama_desc': 'Local AI (lightweight)',
            'atuin_desc': 'Smart history',
            'zoxide_desc': 'Fast navigation',
            'navi_desc': 'Command cheatsheets',
            'btop_desc': 'System monitor',
            'install_all': 'Install All',
            'update': 'Update',
            'exit': 'Exit',
            'choose': 'choose',
            'press_enter': 'Press ENTER to return',
            'exiting': 'Exiting',
            'already_installed': 'already installed',
            'server_running': 'Server running',
            'start_server': 'Start server?',
            'choose_model': 'Choose model:',
            'install_q': 'Install',
            'cancelled': 'Cancelled',
            'installing': 'Installing',
            'installed': 'Installed!',
            'failed': 'Failed',
            'not_configured': 'Not configured',
            'recent_dirs': 'Recent directories:',
            'no_dirs': 'No tracked dirs',
            'usage': 'Usage:',
            'launch_with': 'Launch:',
            'shortcuts': 'Shortcuts:',
            'installing_all': 'Installing all...',
            'updating': 'Updating...',
            'updated': 'Updated'
        }

# COLORS
cyan = "\033[36m"
white = "\033[97m"
gray = "\033[2;37m"
reset = "\033[0m"

space = "         "

logo = f"""{cyan}

 _____   _                        _       _
|  __ \\ (_)                      | |     (_)
| |__) | _  _ __    __ _  _   _  | |      _  _ __   _   _ __  __
|  ___/ | || '_ \\  / _` || | | | | |     | || '_ \\ | | | |\\ \\/ /
| |     | || | | || (_| || |_| | | |____ | || | | || |_| | >  <
|_|     |_||_| |_| \\__, | \\__,_| |______||_||_| |_| \\__,_|/_/\\_\\
                    __/ |
                   |___/

{reset}
"""

box = f"""{white}
{space}┏───────────────────────────────────────────────┓
{space}│          DEVOPS TERMINAL TOOLKIT              │
{space}│     Linux • DevOps • SysAdmin Environment     │
{space}│        github.com/yourprojectname             │
{space}└───────────────────────────────────────────────┘
{reset}
"""


# -------------------------
# SUBMENUS
# -------------------------

def submenu_ollama():
    while True:
        os.system("clear")
        print(logo)
        print(f"\n{space}{cyan}=== OLLAMA ==={reset}\n")
        print(f"{space}{white}1{reset} - {LANG['install_q']}")
        print(f"{space}{white}2{reset} - {LANG['usage']}")
        print(f"{space}{white}3{reset} - Desinstalar / Uninstall")
        print(f"{space}{white}4{reset} - Testar / Test")
        print(f"{space}{white}0{reset} - {LANG['exit']}\n")
        
        choice = input(f"{space}{white}> ")
        
        if choice == "1":
            install_ollama()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "2":
            print(f"\n{space}{cyan}# 1. Iniciar servidor:{reset}")
            print(f"{space}{white}ollama serve{reset}\n")
            print(f"{space}{cyan}# 2. Usar IA:{reset}")
            print(f"{space}{white}ollama run devops-assistant{reset}")
            print(f"{space}{white}ollama run devops-assistant 'explain docker ps'{reset}")
            print(f"{space}{white}ollama run devops-assistant 'how to secure ssh'{reset}\n")
            print(f"{space}{cyan}# 3. Listar modelos:{reset}")
            print(f"{space}{white}ollama list{reset}")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "3":
            uninstall_ollama()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "4":
            if already_installed("ollama"):
                print(f"\n{space}{cyan}Testando Ollama...{reset}\n")
                subprocess.run("ollama list", shell=True)
            else:
                print(f"\n{space}{white}Ollama não instalado / Not installed{reset}")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "0":
            break

def submenu_atuin():
    while True:
        os.system("clear")
        print(logo)
        print(f"\n{space}{cyan}=== ATUIN ==={reset}\n")
        print(f"{space}{white}1{reset} - {LANG['install_q']}")
        print(f"{space}{white}2{reset} - {LANG['usage']}")
        print(f"{space}{white}3{reset} - Desinstalar / Uninstall")
        print(f"{space}{white}4{reset} - Testar / Test")
        print(f"{space}{white}0{reset} - {LANG['exit']}\n")
        
        choice = input(f"{space}{white}> ")
        
        if choice == "1":
            install_atuin()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "2":
            print(f"\n{space}{cyan}# 1. Ativar no terminal:{reset}")
            print(f"{space}{white}atuin init bash >> ~/.bashrc{reset}")
            print(f"{space}{white}source ~/.bashrc{reset}\n")
            print(f"{space}{cyan}# 2. Usar:{reset}")
            print(f"{space}{white}Ctrl+R{reset} - Buscar no histórico")
            print(f"{space}{white}atuin stats{reset} - Ver estatísticas")
            print(f"{space}{white}atuin search docker{reset} - Buscar 'docker'")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "3":
            uninstall_atuin()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "4":
            if already_installed("atuin"):
                print(f"\n{space}{cyan}Testando Atuin...{reset}\n")
                subprocess.run("atuin stats", shell=True)
            else:
                print(f"\n{space}{white}Atuin não instalado / Not installed{reset}")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "0":
            break

def submenu_zoxide():
    while True:
        os.system("clear")
        print(logo)
        print(f"\n{space}{cyan}=== ZOXIDE ==={reset}\n")
        print(f"{space}{white}1{reset} - {LANG['install_q']}")
        print(f"{space}{white}2{reset} - {LANG['usage']}")
        print(f"{space}{white}3{reset} - Desinstalar / Uninstall")
        print(f"{space}{white}4{reset} - Testar / Test")
        print(f"{space}{white}0{reset} - {LANG['exit']}\n")
        
        choice = input(f"{space}{white}> ")
        
        if choice == "1":
            install_zoxide()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "2":
            print(f"\n{space}{cyan}# 1. Ativar no terminal:{reset}")
            print(f"{space}{white}eval \"$(zoxide init bash)\" >> ~/.bashrc{reset}")
            print(f"{space}{white}source ~/.bashrc{reset}\n")
            print(f"{space}{cyan}# 2. Usar:{reset}")
            print(f"{space}{white}z Documents{reset} - Ir para Documents")
            print(f"{space}{white}z proj{reset} - Ir para pasta 'proj'")
            print(f"{space}{white}zi{reset} - Busca interativa")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "3":
            uninstall_zoxide()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "4":
            if already_installed("zoxide"):
                print(f"\n{space}{cyan}Testando Zoxide...{reset}\n")
                subprocess.run("zoxide query --list | head -10", shell=True)
            else:
                print(f"\n{space}{white}Zoxide não instalado / Not installed{reset}")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "0":
            break

def submenu_navi():
    while True:
        os.system("clear")
        print(logo)
        print(f"\n{space}{cyan}=== NAVI ==={reset}\n")
        print(f"{space}{white}1{reset} - {LANG['install_q']}")
        print(f"{space}{white}2{reset} - {LANG['usage']}")
        print(f"{space}{white}3{reset} - Desinstalar / Uninstall")
        print(f"{space}{white}4{reset} - Testar / Test")
        print(f"{space}{white}0{reset} - {LANG['exit']}\n")
        
        choice = input(f"{space}{white}> ")
        
        if choice == "1":
            install_navi()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "2":
            print(f"\n{space}{cyan}# 1. Abrir interface:{reset}")
            print(f"{space}{white}navi{reset}")
            print(f"{space}{white}Ctrl+G{reset} - Atalho no terminal\n")
            print(f"{space}{cyan}# 2. Buscar comandos:{reset}")
            print(f"{space}{white}docker{reset} - Comandos Docker")
            print(f"{space}{white}ssh{reset} - Comandos SSH")
            print(f"{space}{white}find{reset} - Buscar arquivos")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "3":
            uninstall_navi()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "4":
            if already_installed("navi"):
                print(f"\n{space}{cyan}Testando Navi...{reset}\n")
                subprocess.run("navi --version", shell=True)
            else:
                print(f"\n{space}{white}Navi não instalado / Not installed{reset}")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "0":
            break

def submenu_btop():
    while True:
        os.system("clear")
        print(logo)
        print(f"\n{space}{cyan}=== BTOP ==={reset}\n")
        print(f"{space}{white}1{reset} - {LANG['install_q']}")
        print(f"{space}{white}2{reset} - {LANG['usage']}")
        print(f"{space}{white}3{reset} - Desinstalar / Uninstall")
        print(f"{space}{white}4{reset} - Testar / Test")
        print(f"{space}{white}0{reset} - {LANG['exit']}\n")
        
        choice = input(f"{space}{white}> ")
        
        if choice == "1":
            install_btop()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "2":
            print(f"\n{space}{cyan}# 1. Iniciar:{reset}")
            print(f"{space}{white}btop{reset}\n")
            print(f"{space}{cyan}# 2. Atalhos:{reset}")
            print(f"{space}{white}q{reset} - Sair")
            print(f"{space}{white}m{reset} - Menu")
            print(f"{space}{white}k{reset} - Matar processo")
            print(f"{space}{white}f{reset} - Filtrar")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "3":
            uninstall_btop()
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "4":
            if already_installed("btop"):
                print(f"\n{space}{cyan}Testando Btop...{reset}\n")
                subprocess.run("btop --version", shell=True)
            else:
                print(f"\n{space}{white}Btop não instalado / Not installed{reset}")
            input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
        elif choice == "0":
            break


# -------------------------
# CHECKS
# -------------------------

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False


def check_dns():
    try:
        socket.gethostbyname("google.com")
        return True
    except:
        return False





def already_installed(cmd):

    if shutil.which(cmd):
        return True

    # special case for atuin
    if cmd == "atuin":
        atuin_path = os.path.expanduser("~/.atuin/bin/atuin")
        if os.path.exists(atuin_path):
            return True

    return False


def offer_test(cmd):
    test = input(f"{space}{white}Would you like to test it now? (y/n): ")
    if test.lower() == "y":
        try:
            subprocess.run(cmd, shell=True, timeout=10)
        except subprocess.TimeoutExpired:
            print(f"{space}{white}⏱ Test timed out")
        except Exception as e:
            print(f"{space}{white}✖ Test failed: {e}")


def verify_network():

    if not check_internet():
        print(f"\n{space}{white}✖ No internet connection\n")
        pause()
        return False

    if not check_dns():
        print(f"\n{space}{white}✖ DNS resolution failed\n")
        pause()
        return False

    return True


# -------------------------
# TOOL INSTALLERS
# -------------------------

def install_ollama():
    if not verify_network():
        return

    if already_installed("ollama"):
        print(f"\n{space}{cyan}✔ Ollama {LANG['already_installed']}\n")
        
        try:
            subprocess.run("curl -s http://localhost:11434 > /dev/null", shell=True, check=True, timeout=2)
            print(f"{space}{cyan}✔ {LANG['server_running']}\n")
        except:
            start = input(f"{space}{white}{LANG['start_server']} (y/n): ")
            if start.lower() == "y":
                subprocess.Popen("ollama serve > /dev/null 2>&1", shell=True)
                print(f"{space}{cyan}✔ OK\n")
        
        print(f"{space}{white}{LANG['choose_model']}")
        print(f"{space}{cyan} 1{white} phi3:mini      {gray}(2.3GB - DevOps)")
        print(f"{space}{cyan} 2{white} gemma2:2b      {gray}(1.6GB)")
        print(f"{space}{cyan} 3{white} qwen2.5-coder  {gray}(1.5GB)")
        print(f"{space}{cyan} 4{white} devops-custom  {gray}(2.3GB - Security)\n")
        
        choice = input(f"{space}{white}> ")
        
        if choice == "1":
            subprocess.run("ollama pull phi3:mini", shell=True)
        elif choice == "2":
            subprocess.run("ollama pull gemma2:2b", shell=True)
        elif choice == "3":
            subprocess.run("ollama pull qwen2.5-coder:1.5b", shell=True)
        elif choice == "4":
            modelfile = os.path.join(os.path.dirname(__file__), "Modelfile.devops")
            if os.path.exists(modelfile):
                subprocess.run("ollama pull phi3:mini", shell=True)
                subprocess.run(f"ollama create devops-assistant -f {modelfile}", shell=True)
                print(f"\n{space}{cyan}✔ OK\n")
        return

    confirm = input(f"{space}{white}{LANG['install_q']} Ollama? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return

    print(f"\n{space}{white}{LANG['installing']}...\n")
    try:
        subprocess.run(
            "bash -c 'set -o pipefail; curl -fsSL https://ollama.com/install.sh | sh'",
            shell=True, check=True
        )
        print(f"\n{space}{cyan}✔ {LANG['installed']}\n")
        
        start = input(f"{space}{white}{LANG['start_server']} (y/n): ")
        if start.lower() == "y":
            subprocess.Popen("ollama serve > /dev/null 2>&1", shell=True)
            subprocess.run("sleep 2 && ollama pull phi3:mini", shell=True)
            print(f"\n{space}{cyan}✔ phi3:mini OK\n")
    except Exception as e:
        print(f"{space}{white}✖ {LANG['failed']}\n")


def install_atuin():
    if not verify_network():
        return

    if already_installed("atuin"):
        print(f"\n{space}{cyan}✔ Atuin já instalado / already installed\n")
        try:
            result = subprocess.run("atuin stats", shell=True, capture_output=True, text=True, timeout=5)
            print(result.stdout)
        except:
            print(f"{space}{white}✖ Não configurado / Not configured. Run: atuin init bash >> ~/.bashrc\n")
        return

    confirm = input(f"{space}{white}Instalar Atuin? / Install? (y/n): ")

    if confirm.lower() != "y":
        print(f"{space}{gray}Cancelado / Cancelled\n")
        return

    print(f"\n{space}{white}Instalando / Installing...\n")

    try:

        subprocess.run(
            "bash -c 'set -o pipefail; curl https://raw.githubusercontent.com/atuinsh/atuin/main/install.sh | bash'",
            shell=True,
            check=True
        )

        print(f"\n{space}{cyan}✔ Instalado! / Installed!\n")

        print(f"{space}{white}Próximo passo / Next step:")
        print(f"{space}{cyan}atuin init bash >> ~/.bashrc\n")

        offer_test("atuin --help")

    except:
        print(f"{space}{white}Instalação falhou / Installation failed\n")


def install_zoxide():
    if not verify_network():
        return

    if already_installed("zoxide"):
        print(f"\n{space}{cyan}✔ Zoxide já instalado / already installed\n")
        try:
            result = subprocess.run("zoxide query --list | head -5", shell=True, capture_output=True, text=True, timeout=5)
            if result.stdout.strip():
                print(f"{space}{white}Diretórios recentes / Recent directories:\n{result.stdout}")
            else:
                print(f"{space}{gray}Nenhum diretório rastreado / No directories tracked. Use 'z <dir>'\n")
        except:
            print(f"{space}{white}✖ Não configurado / Not configured. Add: eval \"$(zoxide init bash)\"\n")
        return

    confirm = input(f"{space}{white}Instalar Zoxide? / Install? (y/n): ")

    if confirm.lower() != "y":
        print(f"{space}{gray}Cancelado / Cancelled\n")
        return

    print(f"\n{space}{white}Instalando / Installing...\n")

    try:

        subprocess.run(
            "bash -c 'set -o pipefail; curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash'",
            shell=True,
            check=True
        )

        print(f"\n{space}{cyan}✔ Instalado! / Installed!\n")

        print(f"{space}{white}Adicionar ao shell / Add to shell:")
        print(f"{space}{cyan}eval \"$(zoxide init bash)\"\n")

        offer_test("zoxide --help")

    except:
        print(f"{space}{white}Instalação falhou / Installation failed\n")


def install_navi():
    if not verify_network():
        return

    if already_installed("navi"):
        print(f"\n{space}{cyan}✔ Navi já instalado / already installed\n")
        print(f"{space}{white}Uso / Usage: Ctrl+G no terminal ou digite 'navi'\n")
        print(f"{space}{cyan}Exemplos de busca / Example searches:")
        print(f"{space}{gray}  - 'docker container'")
        print(f"{space}{gray}  - 'ssh tunnel'")
        print(f"{space}{gray}  - 'find files'\n")
        return

    confirm = input(f"{space}{white}Instalar Navi? / Install? (y/n): ")

    if confirm.lower() != "y":
        print(f"{space}{gray}Cancelado / Cancelled\n")
        return

    print(f"\n{space}{white}Instalando / Installing...\n")

    try:

        subprocess.run(
            "bash -c 'set -o pipefail; curl -sL https://raw.githubusercontent.com/denisidoro/navi/master/scripts/install | bash'",
            shell=True,
            check=True
        )

        print(f"\n{space}{cyan}✔ Instalado! / Installed!\n")

        offer_test("navi")

    except:
        print(f"{space}{white}Instalação falhou / Installation failed\n")


def install_btop():
    if already_installed("btop"):
        print(f"\n{space}{cyan}✔ btop já instalado / already installed\n")
        print(f"{space}{white}Iniciar com / Launch with: btop\n")
        print(f"{space}{cyan}Atalhos / Shortcuts:")
        print(f"{space}{gray}  q - sair/quit")
        print(f"{space}{gray}  m - menu")
        print(f"{space}{gray}  k - matar processo/kill process\n")
        return

    confirm = input(f"{space}{white}Instalar btop? / Install? (y/n): ")

    if confirm.lower() != "y":
        print(f"{space}{gray}Cancelado / Cancelled\n")
        return

    print(f"\n{space}{white}Instalando / Installing...\n")

    try:

        if shutil.which("apt"):
            subprocess.run("sudo apt install -y btop", shell=True, check=True)

        elif shutil.which("dnf"):
            subprocess.run("sudo dnf install -y btop", shell=True, check=True)

        elif shutil.which("pacman"):
            subprocess.run("sudo pacman -S --noconfirm btop", shell=True, check=True)

        print(f"\n{space}{cyan}✔ Instalado! / Installed!\n")

        offer_test("btop")

    except:
        print(f"{space}{white}Instalação falhou / Installation failed\n")


# -------------------------
# UNINSTALLERS
# -------------------------

def uninstall_ollama():
    confirm = input(f"{space}{white}Desinstalar Ollama? / Uninstall? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return
    
    print(f"\n{space}{white}Desinstalando / Uninstalling...\n")
    try:
        subprocess.run("sudo systemctl stop ollama", shell=True)
        subprocess.run("sudo systemctl disable ollama", shell=True)
        subprocess.run("sudo rm /etc/systemd/system/ollama.service", shell=True)
        subprocess.run("sudo rm $(which ollama)", shell=True)
        subprocess.run("sudo rm -rf /usr/share/ollama", shell=True)
        subprocess.run("rm -rf ~/.ollama", shell=True)
        print(f"{space}{cyan}✔ Ollama removido / Removed\n")
    except Exception as e:
        print(f"{space}{white}✖ {LANG['failed']}\n")

def uninstall_atuin():
    confirm = input(f"{space}{white}Desinstalar Atuin? / Uninstall? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return
    
    print(f"\n{space}{white}Desinstalando / Uninstalling...\n")
    try:
        subprocess.run("rm -rf ~/.atuin", shell=True)
        subprocess.run("rm -rf ~/.local/share/atuin", shell=True)
        
        # Remove do .bashrc
        bashrc = os.path.expanduser("~/.bashrc")
        if os.path.exists(bashrc):
            with open(bashrc, 'r') as f:
                lines = f.readlines()
            with open(bashrc, 'w') as f:
                for line in lines:
                    if 'atuin' not in line.lower():
                        f.write(line)
        
        print(f"{space}{cyan}✔ Atuin removido / Removed\n")
        print(f"{space}{gray}Reinicie o terminal: source ~/.bashrc\n")
    except Exception as e:
        print(f"{space}{white}✖ {LANG['failed']}\n")

def uninstall_zoxide():
    confirm = input(f"{space}{white}Desinstalar Zoxide? / Uninstall? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return
    
    print(f"\n{space}{white}Desinstalando / Uninstalling...\n")
    try:
        subprocess.run("rm -rf ~/.local/bin/zoxide", shell=True)
        subprocess.run("rm -rf ~/.local/share/zoxide", shell=True)
        
        # Remove do .bashrc
        bashrc = os.path.expanduser("~/.bashrc")
        if os.path.exists(bashrc):
            with open(bashrc, 'r') as f:
                lines = f.readlines()
            with open(bashrc, 'w') as f:
                for line in lines:
                    if 'zoxide init' not in line:
                        f.write(line)
        
        print(f"{space}{cyan}✔ Zoxide removido / Removed\n")
    except Exception as e:
        print(f"{space}{white}✖ {LANG['failed']}\n")

def uninstall_navi():
    confirm = input(f"{space}{white}Desinstalar Navi? / Uninstall? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return
    
    print(f"\n{space}{white}Desinstalando / Uninstalling...\n")
    try:
        subprocess.run("rm -rf ~/.local/bin/navi", shell=True)
        subprocess.run("rm -rf ~/.local/share/navi", shell=True)
        print(f"{space}{cyan}✔ Navi removido / Removed\n")
    except Exception as e:
        print(f"{space}{white}✖ {LANG['failed']}\n")

def uninstall_btop():
    confirm = input(f"{space}{white}Desinstalar btop? / Uninstall? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return
    
    print(f"\n{space}{white}Desinstalando / Uninstalling...\n")
    try:
        if shutil.which("apt"):
            subprocess.run("sudo apt remove -y btop", shell=True)
        elif shutil.which("dnf"):
            subprocess.run("sudo dnf remove -y btop", shell=True)
        elif shutil.which("pacman"):
            subprocess.run("sudo pacman -R --noconfirm btop", shell=True)
        print(f"{space}{cyan}✔ Btop removido / Removed\n")
    except Exception as e:
        print(f"{space}{white}✖ {LANG['failed']}\n")

def uninstall_all():
    confirm = input(f"{space}{white}Desinstalar TUDO? / Uninstall ALL? (y/n): ")
    if confirm.lower() != "y":
        print(f"{space}{gray}{LANG['cancelled']}\n")
        return
    
    print(f"\n{space}{white}Desinstalando tudo / Uninstalling all...\n")
    uninstall_ollama()
    uninstall_atuin()
    uninstall_zoxide()
    uninstall_navi()
    uninstall_btop()
    print(f"{space}{cyan}✔ Tudo removido / All removed\n")


# -------------------------
# BULK
# -------------------------

def install_all():

    print(f"\n{space}{white}Instalando tudo / Installing full toolkit...\n")

    install_ollama()
    install_atuin()
    install_zoxide()
    install_navi()
    install_btop()


def update_tools():

    print(f"\n{space}{white}Atualizando / Updating tools...\n")

    if shutil.which("apt"):
        subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)

    elif shutil.which("dnf"):
        subprocess.run("sudo dnf upgrade -y", shell=True)

    elif shutil.which("pacman"):
        subprocess.run("sudo pacman -Syu", shell=True)

    print(f"\n{space}{cyan}✔ Sistema atualizado / System updated\n")


# -------------------------
# MENU
# -------------------------

def menu():
    os.system("clear")
    print(logo)
    print(box)

    print(f"{space}{gray}{LANG['menu_desc1']}{reset}")
    print(f"{space}{gray}{LANG['menu_desc2']}{reset}\n")
    print(f"{space}{white}{LANG['menu_choose']}{reset}\n")

    print(f"{space}{cyan} 01{reset}  {white}Ollama      {gray}{LANG['ollama_desc']}{reset}")
    print(f"{space}{cyan} 02{reset}  {white}Atuin       {gray}{LANG['atuin_desc']}{reset}")
    print(f"{space}{cyan} 03{reset}  {white}Zoxide      {gray}{LANG['zoxide_desc']}{reset}")
    print(f"{space}{cyan} 04{reset}  {white}Navi        {gray}{LANG['navi_desc']}{reset}")
    print(f"{space}{cyan} 05{reset}  {white}Btop        {gray}{LANG['btop_desc']}{reset}\n")

    print(f"{space}{cyan} 90{white}  {LANG['install_all']}")
    print(f"{space}{cyan} 91{white}  Desinstalar Tudo / Uninstall All")
    print(f"{space}{cyan} 99{white}  {LANG['update']}")
    print(f"{space}{cyan} 00{white}  {LANG['exit']}\n")

    mainmenu()


# -------------------------
# MAIN LOOP
# -------------------------

def mainmenu():
    while True:
        try:
            choice = input(f"{space}{white}> {LANG['choose']}:{cyan} ")

            if choice in ("00","0","exit","sair"):
                sys.exit(f"{white}\n{space}* {LANG['exiting']}\n")

            elif choice in ("1","01"):
                submenu_ollama()
                menu()

            elif choice in ("2","02"):
                submenu_atuin()
                menu()

            elif choice in ("3","03"):
                submenu_zoxide()
                menu()

            elif choice in ("4","04"):
                submenu_navi()
                menu()

            elif choice in ("5","05"):
                submenu_btop()
                menu()

            elif choice == "90":
                install_all()
                input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
                menu()

            elif choice == "91":
                uninstall_all()
                input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
                menu()

            elif choice == "99":
                update_tools()
                input(f"\n{space}{gray}{LANG['press_enter']}{reset}")
                menu()

            else:
                continue

        except KeyboardInterrupt:
            sys.exit(f"\n{space}* {LANG['exiting']}")


# -------------------------
# START
# -------------------------

if __name__ == "__main__":
    set_language()
    menu()
