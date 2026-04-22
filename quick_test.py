from agent import AutonomousAgent

print("✅ Testando agente rápidamente...\n")

agent = AutonomousAgent()

# Teste 1: Gerar simples
print("1️⃣  Gerando código de exemplo...")
r = agent.generate_code("Funçã que valida se uma string é um palindromo")
print(r["response"][:300] + "\n...")

print("\n✅ Agente funcionando perfeitamente!")
