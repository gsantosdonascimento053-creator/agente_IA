# 🤖 Agente de IA Autônomo com Gemini 1.5 Flash

Um agente de IA autônomo estilo **Claude Code** que gera e analisa código Python usando Google Gemini 1.5 Flash.

## 🚀 Features

- ✅ Geração de código Python de qualidade
- ✅ Análise e sugestão de melhorias
- ✅ Explicação de código
- ✅ Debug automático
- ✅ Tratamento de erros robusto
- ✅ Histórico de conversa
- ✅ Modo interativo e script

## 📦 Instalação

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. A chave API já está configurada em .env
```

## 🎯 Quick Start

### Modo Interativo

```bash
python main.py
```

**Comandos:**
- `/gerar <descrição>` - Gera código Python
- `/analisar <código>` - Analisa código
- `/limpar` - Limpa histórico
- `/sair` - Sai

### Exemplos

```bash
/gerar Crie uma função que calcula fibonacci com memoização
/analisar def sum(a, b): return a + b
```

## 🏗️ Arquitetura

```
agent.py          → Lógica principal do agente (AutonomousAgent)
config.py         → Configurações (API key, modelo, temperatura)
tools.py          → Ferramentas disponíveis (ToolExecutor)
code_generator.py → Gerador inteligente de código (CodeGenerator)
main.py           → Interface interativa/scripts
```

### AutonomousAgent (agent.py)
- Gerencia sessão com Gemini
- Processa requisições iterativamente
- Valida código gerado
- Mantém histórico de conversa

### CodeGenerator (code_generator.py)
- Aprimora prompts para melhor qualidade
- Extrai blocos de código
- Valida sintaxe Python
- Formata código automaticamente

### ToolExecutor (tools.py)
- Ferramentas disponíveis: generate_code, analyze_code, explain_code, debug_code
- Valida código Python
- Extrai blocos de código

### Config (config.py)
- `GEMINI_API_KEY` ✅ Já configurada
- `MODEL_NAME` = gemini-1.5-flash
- `MAX_ITERATIONS` = 10
- `TEMPERATURE` = 0.7 (criatividade)

## 💻 Uso Programático

```python
from agent import AutonomousAgent

agent = AutonomousAgent()

# Gerar código
response = agent.generate_code("Função fibonacci com memoização")
print(response["response"])

# Analisar código
code = "def sum(a, b): return a + b"
response = agent.analyze_code(code)
print(response["response"])

# Conversa com contexto
r1 = agent.process_request("Explique Factory Pattern")
r2 = agent.process_request("Exemplo em Python?")  # mantém contexto
```

## 🔒 Segurança

⚠️ **IMPORTANTE:**
- Chave API em `.env` (não versionar em produção)
- Em produção: `export GEMINI_API_KEY=sua_chave`
- Adicione `.env` a `.gitignore`

```bash
echo ".env" >> .gitignore
```

## 📈 Fluxo

```
Input → Agent → Parse Tool → Validate → Gemini → Format → Output
                                  ↓
                           Continua iterando?
```

## 🚀 Recursos Principais

1. **Geração Inteligente** - Prompts aprimorados para melhor código
2. **Validação** - Valida sintaxe Python automaticamente
3. **Iterações** - Corrige código com erro automaticamente
4. **Contexto** - Mantém histórico de conversa
5. **Ferramentas** - Sistema extensível de tools
6. **Debug** - Mode DEBUG para troubleshooting

## 🛠️ Configuração

Editar `.env`:
```env
GEMINI_API_KEY=AIzaSyDuEOqN0CtFJkrhruL91Uc216ZASHFAtUM
AGENT_MODEL=gemini-1.5-flash
MAX_ITERATIONS=10
TEMPERATURE=0.7
DEBUG=false
```