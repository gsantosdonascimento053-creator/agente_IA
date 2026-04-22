"""
Ferramentas disponíveis para o agente de IA
"""

import json
import re
from typing import Any, Dict, List


class ToolExecutor:
    """Executor de ferramentas para o agente"""

    def __init__(self):
        self.available_tools = {
            "generate_code": self.generate_code,
            "analyze_code": self.analyze_code,
            "explain_code": self.explain_code,
            "debug_code": self.debug_code,
            "list_tools": self.list_tools,
        }

    def execute(self, tool_name: str, **kwargs) -> str:
        """Executa uma ferramenta"""
        if tool_name not in self.available_tools:
            return f"Erro: Ferramenta '{tool_name}' não encontrada"

        try:
            return self.available_tools[tool_name](**kwargs)
        except Exception as e:
            return f"Erro ao executar {tool_name}: {str(e)}"

    def generate_code(self, description: str, language: str = "python") -> str:
        """Gera código baseado em descrição"""
        return {
            "status": "waiting_for_gemini",
            "task": "generate_code",
            "description": description,
            "language": language,
        }

    def analyze_code(self, code: str) -> str:
        """Analisa código e sugere melhorias"""
        return {
            "status": "waiting_for_gemini",
            "task": "analyze_code",
            "code_length": len(code.split("\n")),
            "needs_analysis": True,
        }

    def explain_code(self, code: str) -> str:
        """Explica o que um código faz"""
        return {
            "status": "waiting_for_gemini",
            "task": "explain_code",
            "code_length": len(code.split("\n")),
        }

    def debug_code(self, code: str, error: str) -> str:
        """Ajuda a debugar código"""
        return {
            "status": "waiting_for_gemini",
            "task": "debug_code",
            "error": error,
            "code_length": len(code.split("\n")),
        }

    def list_tools(self) -> str:
        """Lista todas as ferramentas disponíveis"""
        tools_info = {
            "generate_code": "gera_codigo(descricao, linguagem='python')",
            "analyze_code": "analisa_codigo(codigo)",
            "explain_code": "explica_codigo(codigo)",
            "debug_code": "debuga_codigo(codigo, erro)",
            "list_tools": "lista_ferramentas()",
        }
        return json.dumps(tools_info, indent=2, ensure_ascii=False)

    @staticmethod
    def extract_code_blocks(text: str) -> List[str]:
        """Extrai blocos de código de um texto"""
        pattern = r"```(?:python)?\n(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        return matches

    @staticmethod
    def validate_python_code(code: str) -> tuple[bool, str]:
        """Valida se o código Python tem sintaxe correta"""
        try:
            compile(code, "<string>", "exec")
            return True, "Código válido"
        except SyntaxError as e:
            return False, f"Erro de sintaxe: {e.msg} na linha {e.lineno}"
        except Exception as e:
            return False, f"Erro: {str(e)}"
