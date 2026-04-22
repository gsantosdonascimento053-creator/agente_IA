# 🚀 Quick Start - Agente de IA Autônomo

## ⚡ 30 segundos para começar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. A chave API já está em .env (AIzaSyDuEOqN0CtFJkrhruL91Uc216ZASHFAtUM)

# 3. Rodar interface interativa
python main.py
```

## 📝 Primeiros Comandos

```bash
# Dentro do programa, digite:

# Gerar função de fibonacci
/gerar Função que calcula fibonacci com memoização

# Analisar código
/analisar 
def sum(a, b):
    return a + b

# Pergunta livre
Como funciona decoradores em Python?

# Sair
/sair
```

## 💻 Em 3 Linhas de Código

```python
from agent import AutonomousAgent

agent = AutonomousAgent()
response = agent.generate_code("Função de busca binária")
print(response["response"])
```

## 🎯 Exemplos Rápidos

### Exemplo 1: Gerar Código
```python
from agent import AutonomousAgent

agent = AutonomousAgent()
response = agent.generate_code("Uma classe que implementa um cache LRU")
print(response["response"])
```

### Exemplo 2: Analisar Código
```python
code = """
def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

response = agent.analyze_code(code)
print(response["response"])
```

### Exemplo 3: Conversa
```python
agent = AutonomousAgent()
r1 = agent.process_request("Explique o padrão Factory")
r2 = agent.process_request("Me dê um exemplo em Python")
```

## 📊 Estrutura do Projeto

```
agente_IA/
├── main.py              ← Interface interativa
├── agent.py             ← Coração do agente
├── config.py            ← Configurações
├── tools.py             ← Ferramentas
├── code_generator.py    ← Gerador de código
├── .env                 ← Chave API
├── requirements.txt     ← Dependências
└── exemplos.py          ← Exemplos de uso
```

## 🔧 Configuração

### Mudar Criatividade
```python
# Em config.py
TEMPERATURE = 0.3  # Mais conservador
TEMPERATURE = 1.0  # Mais criativo
```

### Usar Outro Modelo
```python
# Em .env
AGENT_MODEL=gemini-2.5-pro  # Mais poderoso mas mais lento
```

### Ativar Debug
```python
# Em .env
DEBUG=true
```

## 📚 Modos de Uso

### 1. **Modo Interativo**
```bash
python main.py
```
Ideal para: exploração, experiência

### 2. **Programático**
```python
from agent import AutonomousAgent
agent = AutonomousAgent()
```
Ideal para: integração em aplicações

### 3. **Exemplos**
```bash
python exemplos.py
```
Ideal para: aprender as capacidades

### 4. **Integração**
```bash
python integracao.py api      # API endpoint
python integracao.py cli      # CLI avançado
python integracao.py pipeline # Pipeline de tarefas
python integracao.py batch    # Processamento em lote
```

## ⚡ 5 Casos de Uso Principais

### ✅ 1. Gerar código a partir de descrição
```python
agent.generate_code("Uma função que valida CPF")
```

### ✅ 2. Analisar e melhorar código existente
```python
agent.analyze_code(seu_codigo)
```

### ✅ 3. Aprender conceitos de programação
```python
agent.process_request("Explique async/await em Python")
```

### ✅ 4. Debugar código com erro
```python
agent.process_request(f"Corrija este erro: {seu_codigo}")
```

### ✅ 5. Gerar testes automaticamente
```python
agent.process_request(f"Crie testes unitários para: {seu_codigo}")
```

## 🎓 Aprenda

## 📖 Documentação Completa

- **README.md** - Visão geral e features
- **TECNICO.md** - Documentação técnica detalhada
- **exemplos.py** - Exemplos de código
- **integracao.py** - Diferentes modos de integração

## 🚨 Troubleshooting

### Erro: "API key inválida"
Verifique se está em .env:
```bash
GEMINI_API_KEY=AIzaSyDuEOqN0CtFJkrhruL91Uc216ZASHFAtUM
```

### Erro: "Modelo não encontrado"
Atualize .env com um modelo válido:
```bash
AGENT_MODEL=gemini-2.5-flash
```

### Código gerado com erro
Aumente iterações em .env:
```bash
MAX_ITERATIONS=15
```

## 💡 Dicas Rápidas

1. **Prompts claros = melhor código**
   - ❌ "Faz uma função"
   - ✅ "Crie uma função com type hints que valida emails"

2. **Mantenha contexto na conversa**
   - Próximas perguntas herdam contexto anterior
   - Use `/limpar` para começar novo contexto

3. **Combine ferramentas**
   ```python
   # Gerar → Analisar → Melhorar
   r1 = agent.generate_code(desc)
   r2 = agent.analyze_code(extrair_codigo(r1))
   ```

4. **Debug mode ativa logs**
   ```bash
   DEBUG=true python main.py
   ```

## 🔐 Segurança

Sua chave API está segura em .env (não versionada):
```bash
# Se precisar resetar a chave:
# 1. Regenere em Google Cloud Console
# 2. Atualize .env
# 3. Não commit .env
```

## 📈 Próximas Etapas

1. Explore os exemplos
2. Adapte para seu caso de uso
3. Integre em sua aplicação
4. Crie suas próprias ferramentas

## 🎯 API Rápida

```python
agent = AutonomousAgent()

# Gerar código
agent.generate_code(description)

# Analisar código
agent.analyze_code(code)

# Chat livre
agent.process_request(message)

# Limpar histórico
agent.clear_history()

# Histórico
agent.conversation_history
```

## 📞 Suporte

- Leia o TECNICO.md para tópicos avançados
- Verifique exemplos.py para mais casos
- Ative DEBUG=true para entender o fluxo

---

**Aproveite seu agente de IA autônomo! 🚀**
