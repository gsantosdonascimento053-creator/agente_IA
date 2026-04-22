"""
Ponto de entrada - Agente de IA Autônomo
"""

import sys
from agent import AutonomousAgent


def print_banner():
    """Mostra banner inicial"""
    print("=" * 60)
    print("🤖 AGENTE DE IA AUTÔNOMO - GEMINI FLASH")
    print("=" * 60)
    print("Comandos disponíveis:")
    print("  /gerar <descrição>     - Gera código Python")
    print("  /analisar <código>     - Analisa código")
    print("  /sair                  - Sai do programa")
    print("  /limpar                - Limpa histórico")
    print("=" * 60 + "\n")


def format_response(response: dict) -> str:
    """Formata resposta para exibição"""
    result = response.get("response", "")
    iterations = response.get("iterations", 0)

    output = f"\n{result}\n"
    if iterations > 1:
        output += f"\n[Iterações: {iterations}]\n"

    return output


def interactive_mode():
    """Modo interativo"""
    agent = AutonomousAgent()
    print_banner()

    while True:
        try:
            user_input = input("👤 Você: ").strip()

            if not user_input:
                continue

            # Comandos especiais
            if user_input == "/sair":
                print("👋 Até logo!")
                break

            if user_input == "/limpar":
                agent.clear_history()
                print("✅ Histórico limpo")
                continue

            if user_input.startswith("/gerar "):
                description = user_input[7:]
                print("⏳ Gerando código...")
                response = agent.generate_code(description)
                print(format_response(response))
                continue

            if user_input.startswith("/analisar "):
                code = user_input[10:]
                print("⏳ Analisando código...")
                response = agent.analyze_code(code)
                print(format_response(response))
                continue

            # Requisição normal
            print("⏳ Processando...")
            response = agent.process_request(user_input)
            print(format_response(response))

        except KeyboardInterrupt:
            print("\n\n👋 Interrompido pelo usuário")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")


def script_mode(script):
    """Modo script"""
    agent = AutonomousAgent()

    if script == "--gerar-exemplo":
        print("📝 Gerando exemplo de código...")
        desc = "Crie uma função que calcula fibonacci com memoização"
        response = agent.generate_code(desc)
        print(response["response"])

    elif script == "--analisar-exemplo":
        print("📝 Analisando código de exemplo...")
        code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
        response = agent.analyze_code(code)
        print(response["response"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_mode(sys.argv[1])
    else:
        interactive_mode()
