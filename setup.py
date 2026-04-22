#!/usr/bin/env python3
"""
Setup do Agente Autônomo
Instala dependências e configura o ambiente
"""

import os
import sys
import subprocess


def install_dependencies():
    """Instala dependências"""
    print("📦 Instalando dependências...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
    return result.returncode == 0


def create_env_file():
    """Cria arquivo .env se não existir"""
    if os.path.exists(".env"):
        print("⚠️  .env já existe")
        return True

    print("🔐 Criando arquivo .env...")
    with open(".env", "w") as f:
        api_key = input("Digite sua chave API do Gemini: ").strip()
        f.write(f"GEMINI_API_KEY={api_key}\n")
        f.write("AGENT_MODEL=gemini-2.5-flash\n")
        f.write("MAX_ITERATIONS=10\n")
        f.write("DEBUG=false\n")

    print("✅ .env criado com sucesso")
    return True


def test_api_connection():
    """Testa conexão com API"""
    print("\n🧪 Testando conexão com API...")

    try:
        from agent import AutonomousAgent
        agent = AutonomousAgent()
        print("✅ Conexão com Gemini OK")
        return True
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        return False


def show_menu():
    """Mostra menu de configuração"""
    print("\n" + "=" * 60)
    print("🤖 SETUP - AGENTE AUTÔNOMO COM GEMINI")
    print("=" * 60)
    print("\n1. Instalar dependências")
    print("2. Configurar arquivo .env")
    print("3. Testar conexão com API")
    print("4. Executar exemplo")
    print("5. Iniciar interface interativa")
    print("0. Sair")

    return input("\nEscolha (0-5): ").strip()


def run_example():
    """Executa exemplo"""
    print("\n📝 Executando exemplo...")
    result = subprocess.run([sys.executable, "test.py"])
    return result.returncode == 0


def run_interactive():
    """Inicia interface interativa"""
    print("\n💬 Iniciando interface interativa...")
    result = subprocess.run([sys.executable, "main.py"])
    return result.returncode == 0


def main():
    """Menu principal"""
    print("\n" + "=" * 60)
    print("🤖 AGENTE AUTÔNOMO COM GEMINI 2.5 FLASH")
    print("=" * 60)

    while True:
        choice = show_menu()

        if choice == "1":
            if install_dependencies():
                print("✅ Dependências instaladas com sucesso")
            else:
                print("❌ Erro ao instalar dependências")

        elif choice == "2":
            if create_env_file():
                print("✅ Arquivo .env configurado")
            else:
                print("❌ Erro ao criar .env")

        elif choice == "3":
            if test_api_connection():
                print("✅ API funcionando corretamente")
            else:
                print("❌ Problema na conexão com API")

        elif choice == "4":
            run_example()

        elif choice == "5":
            run_interactive()

        elif choice == "0":
            print("\n👋 Até logo!")
            break

        else:
            print("❌ Opção inválida")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Modo automático
        command = sys.argv[1]

        if command == "--install":
            install_dependencies()
            create_env_file()
            test_api_connection()
        elif command == "--test":
            run_example()
        elif command == "--interactive":
            run_interactive()
        else:
            print(f"Comando desconhecido: {command}")
    else:
        # Menu interativo
        main()
