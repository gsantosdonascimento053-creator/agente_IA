import os
from dotenv import load_dotenv

load_dotenv()

# Configurações
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("AGENT_MODEL", "gemini-1.5-flash")
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Validação
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não configurada. Crie um arquivo .env com sua API key.")

# Configurações de temperatura e tokens
TEMPERATURE = 0.7
TOP_P = 0.95
MAX_OUTPUT_TOKENS = 4096

# Prompts do sistema
SYSTEM_PROMPT = """Você é um agente de IA autônomo especializado em gerar e executar código.

Suas responsabilidades:
1. Analisar requisições do usuário
2. Gerar código Python limpo e eficiente
3. Explicar seu raciocínio
4. Sugerir melhorias
5. Fornecer soluções robustas

Formato de resposta:
- Use markdown para formatação
- Separe código em blocos ```python
- Explique cada seção importante
- Quando gerar código, sempre inclua tratamento de erros
"""

TOOL_DESCRIPTIONS = {
    "generate_code": "Gera código Python baseado na descrição",
    "analyze_code": "Analisa código e sugere melhorias",
    "explain_code": "Explica o que um código faz",
    "debug_code": "Ajuda a debugar código com erros"
}
