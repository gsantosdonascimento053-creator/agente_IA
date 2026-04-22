#!/usr/bin/env python3
from agent import AutonomousAgent

print("\n🎬 DEMO FINAL - Agente Autônomo com Gemini\n")

agent = AutonomousAgent()

# Demo 1: Gerar código
print("=" * 70)
print("DEMO 1: Gerando função para validar email")
print("=" * 70)

response = agent.generate_code(
    "Função Python com type hints que valida email e retorna bool"
)

# Mostrar resposta truncada
response_text = response["response"]
print(response_text[:400] + "\n[...]\n")

# Demo 2: Análise
print("=" * 70)
print("DEMO 2: Analisando código")
print("=" * 70)

agent.clear_history()
codigo_teste = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

response = agent.analyze_code(codigo_teste)
print(response["response"][:400] + "\n[...]\n")

# Demo 3: Chat
print("=" * 70)
print("DEMO 3: Chat inteligente")
print("=" * 70)

agent.clear_history()
response = agent.process_request("O que é um decorator em Python?")
print(response["response"][:400] + "\n[...]\n")

print("=" * 70)
print("✅ AGENTE FUNCIONANDO PERFEITAMENTE!")
print("=" * 70)
print("\n🚀 Para começar: python main.py")
print("📚 Documentação: Leia GUIDE.md ou RESUMO.md\n")
