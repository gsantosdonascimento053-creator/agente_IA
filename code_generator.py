"""
Gerador de código inteligente
"""

import json
from typing import Optional
import re


class CodeGenerator:
    """Gera código de alta qualidade"""

    @staticmethod
    def enhance_prompt(description: str) -> str:
        """Melhora o prompt para gerar código melhor"""
        enhanced = f"""
Gere código Python de qualidade profissional com base nisso:

{description}

Requisitos:
1. Código limpo e legível
2. Variáveis com nomes descritivos
3. Funções com docstrings
4. Tratamento de exceções apropriado
5. Comentários para lógica complexa
6. Type hints quando possível
7. Boas práticas Python (PEP 8)
8. Sem dependências desnecessárias
9. Eficiente em performance
10. Testável e modular

Formato: Use blocos ```python para o código.
"""
        return enhanced

    @staticmethod
    def extract_code(response: str) -> Optional[str]:
        """Extrai código Python de uma resposta"""
        # Tenta encontrar blocos de código Python
        pattern = r"```(?:python)?\n(.*?)```"
        matches = re.findall(pattern, response, re.DOTALL)

        if matches:
            return matches[0].strip()

        # Se não encontrar, tenta extrair linhas que parecem código
        lines = response.split("\n")
        code_lines = []
        in_code = False

        for line in lines:
            if line.strip().startswith("def ") or line.strip().startswith("class "):
                in_code = True
            if in_code:
                code_lines.append(line)

        return "\n".join(code_lines) if code_lines else None

    @staticmethod
    def add_error_handling(code: str) -> str:
        """Adiciona tratamento de erro básico se não tiver"""
        if "try:" not in code and "except" not in code:
            # Se for uma função simples, envolva com try/except
            if code.strip().startswith("def "):
                lines = code.split("\n")
                # Identifica o corpo da função
                body_start = 1
                for i, line in enumerate(lines[1:], 1):
                    if line and not line.startswith(" "):
                        body_start = i
                        break

                if body_start > 1:
                    indent = "    "
                    wrapper = lines[:body_start]
                    body = lines[body_start:]

                    wrapped = wrapper + [f"{indent}try:"]
                    for line in body:
                        if line:
                            wrapped.append(f"{indent}{line}")
                        else:
                            wrapped.append(line)
                    wrapped.append(f"{indent}except Exception as e:")
                    wrapped.append(f"{indent}{indent}print(f'Erro: {{e}}')")
                    wrapped.append(f"{indent}{indent}raise")

                    return "\n".join(wrapped)

        return code

    @staticmethod
    def add_docstring(code: str) -> str:
        """Adiciona docstrings se não tiver"""
        if 'def ' in code and '"""' not in code and "'''" not in code:
            lines = code.split("\n")
            result = []

            for i, line in enumerate(lines):
                result.append(line)
                if line.strip().startswith("def ") and i + 1 < len(lines):
                    # Verifica se já tem docstring
                    next_line = lines[i + 1].strip()
                    if not next_line.startswith('"""') and not next_line.startswith("'''"):
                        indent = len(line) - len(line.lstrip()) + 4
                        result.append(" " * indent + '"""TODO: Adicionar documentação"""')

            return "\n".join(result)

        return code

    @staticmethod
    def format_code(code: str) -> str:
        """Formata código básicamente (remove espaços extras)"""
        lines = code.split("\n")
        # Remove linhas vazias múltiplas
        cleaned = []
        prev_empty = False

        for line in lines:
            is_empty = not line.strip()
            if is_empty and prev_empty:
                continue
            cleaned.append(line)
            prev_empty = is_empty

        return "\n".join(cleaned).strip()

    @classmethod
    def generate(cls, description: str, enhance: bool = True) -> str:
        """Interface principal para gerar código"""
        if enhance:
            prompt = cls.enhance_prompt(description)
        else:
            prompt = description

        return prompt
