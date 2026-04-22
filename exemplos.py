#!/usr/bin/env python3
"""
Exemplos de uso do Agente Autônomo
"""

from agent import AutonomousAgent


def exemplo_1_gerar_codigo():
    """Exemplo 1: Gerar código a partir de uma descrição"""
    print("\n" + "=" * 70)
    print("EXEMPLO 1: Gerar Código")
    print("=" * 70)

    agent = AutonomousAgent()

    descricao = "Crie uma classe que implementa um cache LRU (Least Recently Used) com limite de 100 itens"
    print(f"\n📝 Solicitação: {descricao}\n")

    response = agent.generate_code(descricao)
    print(response["response"])
    print(f"\n✅ Concluído em {response['iterations']} iteração(ões)")


def exemplo_2_analise_codigo():
    """Exemplo 2: Analisar código e sugerir melhorias"""
    print("\n" + "=" * 70)
    print("EXEMPLO 2: Análise de Código")
    print("=" * 70)

    agent = AutonomousAgent()

    codigo_ruim = """
def buscar_usuario(usuarios, id):
    for u in usuarios:
        if u['id'] == id:
            return u
    return None

def processar_dados(dados):
    resultado = []
    for d in dados:
        valor = d * 2
        resultado.append(valor)
    return resultado
"""

    print("\n📝 Código para análise:\n")
    print(codigo_ruim)
    print("\n🔍 Analisando...\n")

    response = agent.analyze_code(codigo_ruim)
    print(response["response"])


def exemplo_3_conversa_contextual():
    """Exemplo 3: Conversa com contexto (histórico)"""
    print("\n" + "=" * 70)
    print("EXEMPLO 3: Conversa com Contexto")
    print("=" * 70)

    agent = AutonomousAgent()

    # Pergunta 1
    print("\n💬 Pergunta 1: Explique o padrão Observer em Python")
    r1 = agent.process_request("Explique o padrão Observer em Python")
    print(r1["response"][:300] + "...\n")

    # Pergunta 2 (mantém contexto)
    print("💬 Pergunta 2: Agora mostre um exemplo prático e completo")
    r2 = agent.process_request("Agora mostre um exemplo prático e completo")
    print(r2["response"][:300] + "...\n")


def exemplo_4_gerador_funcoes():
    """Exemplo 4: Gerar múltiplas funções"""
    print("\n" + "=" * 70)
    print("EXEMPLO 4: Gerar Múltiplas Funções")
    print("=" * 70)

    agent = AutonomousAgent()

    funcoes = [
        "Função que valida email",
        "Função que gera um UUID aleatório",
        "Função que formata um número como moeda",
    ]

    for func in funcoes:
        print(f"\n📝 Gerando: {func}")
        response = agent.generate_code(func)
        # Mostra só o código
        if "```python" in response["response"]:
            codigo = response["response"].split("```python")[1].split("```")[0]
            print(codigo[:200] + "...")


def exemplo_5_debug_codigo():
    """Exemplo 5: Debugar código com erro"""
    print("\n" + "=" * 70)
    print("EXEMPLO 5: Debugar Código com Erro")
    print("=" * 70)

    agent = AutonomousAgent()

    codigo_com_erro = """
def calcular_media(notas):
    return sum(notas) / len(notas)

# Erro: lista vazia causará divisão por zero
resultado = calcular_media([])
print(resultado)
"""

    prompt = f"""Este código tem um bug. Identifique e corrija:

```python
{codigo_com_erro}
```

Mostre a versão corrigida e explique o problema."""

    print(f"\n🐛 Código com erro:\n{codigo_com_erro}\n")
    response = agent.process_request(prompt)
    print(response["response"][:500] + "...")


if __name__ == "__main__":
    print("\n🤖 EXEMPLOS DE USO DO AGENTE AUTÔNOMO\n")
    print("Escolha um exemplo para executar:")
    print("1. Gerar código")
    print("2. Análise de código")
    print("3. Conversa com contexto")
    print("4. Gerar múltiplas funções")
    print("5. Debugar código")
    print("0. Executar todos")

    escolha = input("\nSua escolha (0-5): ").strip()

    if escolha == "1":
        exemplo_1_gerar_codigo()
    elif escolha == "2":
        exemplo_2_analise_codigo()
    elif escolha == "3":
        exemplo_3_conversa_contextual()
    elif escolha == "4":
        exemplo_4_gerador_funcoes()
    elif escolha == "5":
        exemplo_5_debug_codigo()
    elif escolha == "0":
        exemplo_1_gerar_codigo()
        exemplo_2_analise_codigo()
        exemplo_3_conversa_contextual()
        exemplo_4_gerador_funcoes()
        exemplo_5_debug_codigo()
    else:
        print("Escolha inválida!")
