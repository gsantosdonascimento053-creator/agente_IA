#!/usr/bin/env python3
"""
Script de teste do agente autônomo
"""

from agent import AutonomousAgent
import json


def test_agent():
    """Testa o agente com exemplos"""
    print("🤖 TESTANDO AGENTE AUTÔNOMO\n")
    print("=" * 60)

    agent = AutonomousAgent()

    # Teste 1: Gerar código simples
    print("\n📝 TESTE 1: Gerar função simples")
    print("-" * 60)
    response1 = agent.generate_code("Crie uma função que calcula o fatorial de um número com tratamento de erro")
    print(response1["response"][:500] + "..." if len(response1["response"]) > 500 else response1["response"])
    print(f"✅ Iterações: {response1['iterations']}")

    # Teste 2: Limpar e fazer nova pergunta
    print("\n📝 TESTE 2: Conversa livre")
    print("-" * 60)
    agent.clear_history()
    response2 = agent.process_request("O que é um decorator em Python? Explique brevemente.")
    print(response2["response"][:400] + "..." if len(response2["response"]) > 400 else response2["response"])

    # Teste 3: Análise de código
    print("\n📝 TESTE 3: Análise de código")
    print("-" * 60)
    agent.clear_history()
    bad_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(100)
print(result)
"""
    response3 = agent.analyze_code(bad_code)
    print(response3["response"][:400] + "..." if len(response3["response"]) > 400 else response3["response"])

    print("\n" + "=" * 60)
    print("✅ TESTES CONCLUÍDOS!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        test_agent()
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
