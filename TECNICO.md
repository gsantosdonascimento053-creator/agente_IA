# 📚 Documentação Técnica - Agente Autônomo

## Arquitetura Detalhada

### 1. **AutonomousAgent (agent.py)**

Classe principal que gerencia interação com Gemini.

```python
agent = AutonomousAgent()

# Métodos principais
response = agent.process_request(user_input)      # Processa requisição
response = agent.generate_code(description)       # Gera código
response = agent.analyze_code(code)              # Analisa código
agent.clear_history()                             # Limpa contexto
```

**Estrutura de Resposta:**
```python
{
    "success": True,
    "response": "...",           # Texto da resposta
    "iterations": 1,             # Número de iterações
    "history": [                 # Histórico mantido
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
}
```

### 2. **CodeGenerator (code_generator.py)**

Gerador inteligente de código com aprimoramento de prompts.

```python
from code_generator import CodeGenerator

# Extrai código de resposta
code = CodeGenerator.extract_code(response_text)

# Valida sintaxe
is_valid, msg = CodeGenerator.validate_python_code(code)

# Formata código
formatted = CodeGenerator.format_code(code)

# Aprimora prompt para melhor qualidade
enhanced_prompt = CodeGenerator.enhance_prompt(description)
```

### 3. **ToolExecutor (tools.py)**

Sistema de ferramentas extensível.

```python
from tools import ToolExecutor

executor = ToolExecutor()

# Ferramentas disponíveis
code_blocks = ToolExecutor.extract_code_blocks(text)
is_valid, error = ToolExecutor.validate_python_code(code)
tools_list = executor.list_tools()
```

## Configuração Avançada

### Parâmetros de Geração

```python
# Em config.py
TEMPERATURE = 0.7      # 0.0 = determinístico, 1.0 = criativo
TOP_P = 0.95          # Nucleus sampling
MAX_OUTPUT_TOKENS = 4096
MAX_ITERATIONS = 10    # Máximo de iterações do agente
```

### Debug Mode

```bash
# Em .env
DEBUG=true

# Mostrará logs de cada iteração
```

## Uso Programático Avançado

### Exemplo 1: Gerar Código com Callbacks

```python
from agent import AutonomousAgent

agent = AutonomousAgent()

def processar_resposta(response):
    print(f"Iterações: {response['iterations']}")
    print(f"Sucesso: {response['success']}")
    
    # Extrai código
    from code_generator import CodeGenerator
    code = CodeGenerator.extract_code(response['response'])
    
    return code

response = agent.generate_code("Função de busca binária")
codigo = processar_resposta(response)
print(codigo)
```

### Exemplo 2: Conversa Multi-Turno

```python
agent = AutonomousAgent()

# Turno 1
r1 = agent.process_request("O que é closure em Python?")
print(r1['response'])

# Turno 2 (mantém contexto)
r2 = agent.process_request("Me dê 3 exemplos práticos")
print(r2['response'])

# Turno 3
r3 = agent.process_request("Qual é melhor prática ao usar closures?")
print(r3['response'])

# Ver histórico completo
print(agent.conversation_history)
```

### Exemplo 3: Análise Profunda de Performance

```python
agent = AutonomousAgent()

prompt = """
Analise este código em termos de Big O:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

1. Qual é a complexidade de tempo?
2. Qual é a complexidade de espaço?
3. Existem algoritmos melhores?
4. Mostre uma versão otimizada.
"""

response = agent.process_request(prompt)
print(response['response'])
```

### Exemplo 4: Gerar e Testar Código

```python
import subprocess
import tempfile

agent = AutonomousAgent()

# Gerar código
response = agent.generate_code("Função que verifica se um número é primo")

# Extrair código
from code_generator import CodeGenerator
code = CodeGenerator.extract_code(response['response'])

# Salvar em arquivo temporário
with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
    f.write(code)
    temp_file = f.name

# Testar
try:
    result = subprocess.run(['python', temp_file], capture_output=True)
    print("Saída:", result.stdout.decode())
except Exception as e:
    print("Erro:", e)
```

## Extensão e Customização

### Adicionar Nova Ferramenta

```python
# Em tools.py, na classe ToolExecutor

def nova_ferramenta(self, param1: str, param2: int) -> str:
    """Descrição da ferramenta"""
    # Implementação
    return resultado

# Registrar
self.available_tools["nova_ferramenta"] = self.nova_ferramenta
```

### Customizar Prompt do Sistema

```python
# Em config.py

SYSTEM_PROMPT = """
Você é um especialista em [DOMÍNIO].

Suas responsabilidades:
1. ...
2. ...

Formato esperado:
- ...
"""
```

### Integração com Banco de Dados

```python
import sqlite3

class AgentComDatabase:
    def __init__(self, db_path="agent.db"):
        self.agent = AutonomousAgent()
        self.db = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY,
                user_input TEXT,
                response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db.commit()
    
    def process(self, user_input):
        response = self.agent.process_request(user_input)
        
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO requests (user_input, response) VALUES (?, ?)",
            (user_input, response['response'])
        )
        self.db.commit()
        
        return response
```

## Performance e Otimização

### 1. Cachear Respostas Similares

```python
from functools import lru_cache

class AgentOptimizado:
    @lru_cache(maxsize=128)
    def process_request(self, text):
        # Respostas similares serão cacheadas
        return self.agent.process_request(text)
```

### 2. Executar em Thread

```python
import threading

def processar_async(prompt, callback):
    def run():
        response = agent.process_request(prompt)
        callback(response)
    
    thread = threading.Thread(target=run)
    thread.start()

# Uso
processar_async("Gere um algoritmo", lambda r: print(r['response']))
```

## Troubleshooting

### Erro: "API key inválida"
- Verifique se GEMINI_API_KEY está correta em .env
- Regenere a chave no console do Google Cloud

### Erro: "Modelo não encontrado"
- Execute: `python3 -c "import google.generativeai as genai; genai.configure(api_key='CHAVE'); print([m.name for m in genai.list_models()])"`
- Atualize o MODEL_NAME em .env

### Código gerado com erro
- Aumentar MAX_ITERATIONS em .env
- Ativar DEBUG=true para ver logs
- Refinar a descrição do código desejado

## Rate Limiting

Gemini Free tem limites de requisições. Se receber erro 429:

```python
import time

def process_with_retry(agent, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            return agent.process_request(prompt)
        except Exception as e:
            if "429" in str(e):
                wait_time = 2 ** attempt  # Backoff exponencial
                print(f"Rate limited. Esperando {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Máximo de tentativas atingido")
```

## Segurança

⚠️ **Cuidados:**
- Nunca commitar `.env` com API keys
- Usar variáveis de ambiente em produção
- Validar entrada do usuário antes de passar ao agente
- Não expor erros detalhados ao usuário
- Rate limit requisições

```python
import re

def validar_entrada(text, max_length=5000):
    """Valida entrada do usuário"""
    if not text or len(text) > max_length:
        raise ValueError("Entrada inválida")
    
    # Prevenir injection
    if any(pattern in text for pattern in ["__import__", "eval", "exec"]):
        raise ValueError("Padrão suspeito detectado")
    
    return text
```
