#!/usr/bin/env python3
"""
Testes automatizados para PinguLinux
Executa: python3 test_pingulinux.py
"""

import os
import sys
import subprocess
import shutil

# Cores
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def test_imports():
    """Testa se todos os modulos necessarios estao disponiveis"""
    try:
        import os
        import sys
        import subprocess
        import shutil
        import socket
        print(f"{GREEN}✓{RESET} Imports: OK")
        return True
    except ImportError as e:
        print(f"{RED}✗{RESET} Imports: FALHOU - {e}")
        return False

def test_python_version():
    """Testa se Python e 3.6+"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"{GREEN}✓{RESET} Python version: {version.major}.{version.minor}")
        return True
    else:
        print(f"{RED}✗{RESET} Python version: {version.major}.{version.minor} (requer 3.6+)")
        return False

def test_file_exists():
    """Testa se PinguLinux.py existe"""
    if os.path.exists("PinguLinux.py"):
        print(f"{GREEN}✓{RESET} PinguLinux.py: Existe")
        return True
    else:
        print(f"{RED}✗{RESET} PinguLinux.py: Nao encontrado")
        return False

def test_modelfile_exists():
    """Testa se Modelfile.devops existe"""
    if os.path.exists("Modelfile.devops"):
        print(f"{GREEN}✓{RESET} Modelfile.devops: Existe")
        return True
    else:
        print(f"{RED}✗{RESET} Modelfile.devops: Nao encontrado")
        return False

def test_syntax():
    """Testa sintaxe do Python"""
    try:
        result = subprocess.run(
            ["python3", "-m", "py_compile", "PinguLinux.py"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"{GREEN}✓{RESET} Sintaxe: OK")
            return True
        else:
            print(f"{RED}✗{RESET} Sintaxe: ERRO")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"{RED}✗{RESET} Sintaxe: FALHOU - {e}")
        return False

def test_import_module():
    """Testa se PinguLinux pode ser importado"""
    try:
        sys.path.insert(0, os.getcwd())
        import PinguLinux
        print(f"{GREEN}✓{RESET} Import PinguLinux: OK")
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Import PinguLinux: FALHOU - {e}")
        return False

def test_functions_exist():
    """Testa se funcoes principais existem"""
    try:
        import PinguLinux
        functions = [
            'set_language',
            'menu',
            'mainmenu',
            'install_ollama',
            'install_atuin',
            'install_zoxide',
            'install_navi',
            'install_btop',
            'uninstall_ollama',
            'uninstall_atuin',
            'uninstall_zoxide',
            'uninstall_navi',
            'uninstall_btop',
            'submenu_ollama',
            'submenu_atuin',
            'submenu_zoxide',
            'submenu_navi',
            'submenu_btop'
        ]
        
        missing = []
        for func in functions:
            if not hasattr(PinguLinux, func):
                missing.append(func)
        
        if not missing:
            print(f"{GREEN}✓{RESET} Funcoes: Todas presentes ({len(functions)})")
            return True
        else:
            print(f"{RED}✗{RESET} Funcoes: Faltando {missing}")
            return False
    except Exception as e:
        print(f"{RED}✗{RESET} Funcoes: FALHOU - {e}")
        return False

def test_check_functions():
    """Testa funcoes de verificacao"""
    try:
        import PinguLinux
        
        # Testa check_internet
        internet = PinguLinux.check_internet()
        print(f"{GREEN}✓{RESET} check_internet: {internet}")
        
        # Testa check_dns
        dns = PinguLinux.check_dns()
        print(f"{GREEN}✓{RESET} check_dns: {dns}")
        
        # Testa already_installed com comando que existe
        python_installed = PinguLinux.already_installed("python3")
        if python_installed:
            print(f"{GREEN}✓{RESET} already_installed: OK")
        else:
            print(f"{RED}✗{RESET} already_installed: FALHOU")
            return False
        
        return True
    except Exception as e:
        print(f"{RED}✗{RESET} Check functions: FALHOU - {e}")
        return False

def test_colors_defined():
    """Testa se cores estao definidas"""
    try:
        import PinguLinux
        colors = ['cyan', 'white', 'gray', 'reset']
        
        missing = []
        for color in colors:
            if not hasattr(PinguLinux, color):
                missing.append(color)
        
        if not missing:
            print(f"{GREEN}✓{RESET} Cores: Todas definidas")
            return True
        else:
            print(f"{RED}✗{RESET} Cores: Faltando {missing}")
            return False
    except Exception as e:
        print(f"{RED}✗{RESET} Cores: FALHOU - {e}")
        return False

def run_all_tests():
    """Executa todos os testes"""
    print("\n=== TESTES PINGULINUX ===\n")
    
    tests = [
        test_python_version,
        test_imports,
        test_file_exists,
        test_modelfile_exists,
        test_syntax,
        test_import_module,
        test_functions_exist,
        test_check_functions,
        test_colors_defined
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"{RED}✗{RESET} {test.__name__}: EXCEPTION - {e}")
            failed += 1
    
    print(f"\n=== RESULTADO ===")
    print(f"{GREEN}Passou: {passed}{RESET}")
    print(f"{RED}Falhou: {failed}{RESET}")
    print(f"Total: {passed + failed}\n")
    
    if failed == 0:
        print(f"{GREEN}✓ TODOS OS TESTES PASSARAM{RESET}\n")
        return 0
    else:
        print(f"{RED}✗ ALGUNS TESTES FALHARAM{RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
