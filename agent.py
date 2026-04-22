"""
Agente de IA autônomo com Gemini
"""

import json
import re
from typing import Optional, Dict, List, Any
import google.generativeai as genai
from config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    SYSTEM_PROMPT,
    TEMPERATURE,
    TOP_P,
    MAX_OUTPUT_TOKENS,
    MAX_ITERATIONS,
    DEBUG,
)
from tools import ToolExecutor
from code_generator import CodeGenerator


class AutonomousAgent:
    """Agente autônomo com Gemini Flash"""

    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_PROMPT,
            generation_config=genai.types.GenerationConfig(
                temperature=TEMPERATURE,
                top_p=TOP_P,
                max_output_tokens=MAX_OUTPUT_TOKENS,
            ),
        )
        self.chat_session = self.model.start_chat()
        self.tool_executor = ToolExecutor()
        self.code_generator = CodeGenerator()
        self.conversation_history: List[Dict[str, str]] = []
        self.max_iterations = MAX_ITERATIONS

    def _log(self, message: str, level: str = "INFO"):
        """Log com debug opcional"""
        if DEBUG:
            print(f"[{level}] {message}")

    def _parse_tool_call(self, response: str) -> Optional[Dict[str, Any]]:
        """Tenta extrair chamada de ferramenta da resposta"""
        # Padrão: ferramenta(argumento1, argumento2)
        pattern = r"(\w+)\((.*?)\)"
        matches = re.findall(pattern, response)

        if matches:
            tool_name, args_str = matches[0]
            if tool_name in self.tool_executor.available_tools:
                self._log(f"Ferramenta detectada: {tool_name}")
                # Parse básico de argumentos
                try:
                    # Tenta parse como JSON
                    args_str = args_str.replace("'", '"')
                    args = json.loads(f"{{{args_str}}}")
                except:
                    # Fallback: split por vírgula
                    args = {}
                    for arg in args_str.split(","):
                        if "=" in arg:
                            k, v = arg.split("=", 1)
                            args[k.strip()] = v.strip().strip("\"'")

                return {"tool": tool_name, "args": args}

        return None

    def _enhance_response(self, text: str) -> str:
        """Realça a resposta com formatação"""
        if "```python" not in text and ("def " in text or "class " in text):
            # Envolve código detectado
            lines = text.split("\n")
            result = []
            in_code = False

            for line in lines:
                if line.strip().startswith(("def ", "class ", "import ", "@")):
                    if not in_code:
                        result.append("```python")
                        in_code = True
                    result.append(line)
                elif in_code and line and not line.startswith(" "):
                    result.append("```")
                    in_code = False
                    result.append(line)
                else:
                    result.append(line)

            if in_code:
                result.append("```")

            return "\n".join(result)

        return text

    def process_request(self, user_input: str, max_iterations: Optional[int] = None) -> Dict[str, Any]:
        """Processa uma requisição do usuário"""
        if max_iterations is None:
            max_iterations = self.max_iterations

        self._log(f"Iniciando processamento: {user_input}")
        self.conversation_history.append({"role": "user", "content": user_input})

        iteration = 0
        final_response = ""

        while iteration < max_iterations:
            iteration += 1
            self._log(f"Iteração {iteration}/{max_iterations}")

            try:
                # Envia mensagem ao Gemini
                response = self.chat_session.send_message(user_input)
                response_text = response.text

                self._log(f"Resposta do modelo: {response_text[:100]}...")

                # Tenta detectar e executar ferramentas
                tool_call = self._parse_tool_call(response_text)

                if tool_call and tool_call["tool"] == "generate_code":
                    # Aprimora o prompt para gerar código melhor
                    enhanced_prompt = self.code_generator.enhance_prompt(user_input)
                    self._log("Gerando código com prompt aprimorado...")

                    # Pede ao Gemini para gerar código
                    code_response = self.chat_session.send_message(enhanced_prompt)
                    code_text = code_response.text

                    # Extrai código
                    extracted_code = self.code_generator.extract_code(code_text)
                    if extracted_code:
                        # Valida sintaxe
                        is_valid, validation_msg = ToolExecutor.validate_python_code(
                            extracted_code
                        )
                        if is_valid:
                            final_response = code_text
                            break
                        else:
                            self._log(f"Código inválido: {validation_msg}")
                            user_input = f"Corrija o erro de sintaxe: {validation_msg}"
                else:
                    # Resposta direta
                    final_response = self._enhance_response(response_text)
                    break

            except Exception as e:
                self._log(f"Erro: {str(e)}", "ERROR")
                final_response = f"Erro ao processar requisição: {str(e)}"
                break

        self.conversation_history.append({"role": "assistant", "content": final_response})

        return {
            "success": True,
            "response": final_response,
            "iterations": iteration,
            "history": self.conversation_history,
        }

    def generate_code(self, description: str) -> Dict[str, Any]:
        """Interface simplificada para gerar código"""
        return self.process_request(f"Gere código Python para: {description}")

    def analyze_code(self, code: str) -> Dict[str, Any]:
        """Analisa e sugere melhorias no código"""
        prompt = f"""Analise este código e sugira melhorias:

```python
{code}
```

Considere:
- Performance
- Legibilidade
- Mantenibilidade
- Segurança
- Boas práticas"""
        return self.process_request(prompt)

    def clear_history(self):
        """Limpa histórico de conversa"""
        self.conversation_history = []
        self.chat_session = self.model.start_chat()
        self._log("Histórico limpo")
