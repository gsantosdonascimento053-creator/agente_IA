"""
Integrações do Agente - Exemplos de uso em diferentes contextos
"""

import json
import re
from typing import Dict, Any
from agent import AutonomousAgent


class AgentAPI:
    """API REST-like para o agente (sem framework web)"""

    def __init__(self):
        self.agent = AutonomousAgent()
        self.requests_log = []

    def generate_code_endpoint(self, description: str) -> Dict[str, Any]:
        """POST /api/generate-code"""
        response = self.agent.generate_code(description)

        self.requests_log.append({
            "type": "generate_code",
            "input": description,
            "timestamp": str(__import__("datetime").datetime.now())
        })

        return {
            "status": "success",
            "data": response
        }

    def analyze_code_endpoint(self, code: str) -> Dict[str, Any]:
        """POST /api/analyze-code"""
        response = self.agent.analyze_code(code)

        self.requests_log.append({
            "type": "analyze_code",
            "lines": len(code.split("\n")),
            "timestamp": str(__import__("datetime").datetime.now())
        })

        return {
            "status": "success",
            "data": response
        }

    def chat_endpoint(self, message: str) -> Dict[str, Any]:
        """POST /api/chat"""
        response = self.agent.process_request(message)

        self.requests_log.append({
            "type": "chat",
            "message_length": len(message),
            "timestamp": str(__import__("datetime").datetime.now())
        })

        return {
            "status": "success",
            "data": response
        }

    def get_history_endpoint(self) -> Dict[str, Any]:
        """GET /api/history"""
        return {
            "requests": self.requests_log,
            "total": len(self.requests_log)
        }


class AgentCLI:
    """Interface CLI para usar via terminal"""

    def __init__(self):
        self.agent = AutonomousAgent()

    def run(self):
        """Loop principal do CLI"""
        print("🤖 AGENTE CLI")
        print("Comandos: /help, /gerar, /analisar, /chat\n")

        while True:
            try:
                cmd = input(">>> ").strip()

                if cmd == "/help":
                    self.show_help()
                elif cmd.startswith("/gerar "):
                    self.handle_generate(cmd[7:])
                elif cmd.startswith("/analisar "):
                    self.handle_analyze(cmd[9:])
                elif cmd.startswith("/chat "):
                    self.handle_chat(cmd[6:])
                elif cmd == "/sair":
                    print("Até logo!")
                    break
                else:
                    print("Comando desconhecido. Digite /help")

            except KeyboardInterrupt:
                print("\nInterrompido")
                break
            except Exception as e:
                print(f"Erro: {e}")

    def show_help(self):
        """Mostra ajuda"""
        help_text = """
        /gerar <descrição>  - Gerar código Python
        /analisar <código>  - Analisar código
        /chat <mensagem>    - Enviar mensagem
        /sair               - Sair
        """
        print(help_text)

    def handle_generate(self, description):
        response = self.agent.generate_code(description)
        print(f"\n{response['response']}\n")

    def handle_analyze(self, code):
        response = self.agent.analyze_code(code)
        print(f"\n{response['response']}\n")

    def handle_chat(self, message):
        response = self.agent.process_request(message)
        print(f"\n{response['response']}\n")


class AgentPipeline:
    """Pipeline para processar múltiplos prompts em sequência"""

    def __init__(self):
        self.agent = AutonomousAgent()
        self.results = []

    def add_task(self, task_type: str, **kwargs):
        """Adiciona tarefa ao pipeline"""
        self.results.append({
            "task": task_type,
            "params": kwargs,
            "status": "pending"
        })

    def execute(self) -> list:
        """Executa todas as tarefas"""
        for task in self.results:
            if task["status"] != "pending":
                continue

            task_type = task["task"]

            try:
                if task_type == "generate":
                    result = self.agent.generate_code(task["params"]["description"])
                elif task_type == "analyze":
                    result = self.agent.analyze_code(task["params"]["code"])
                elif task_type == "chat":
                    result = self.agent.process_request(task["params"]["message"])
                else:
                    raise ValueError(f"Tipo de tarefa desconhecido: {task_type}")

                task["response"] = result
                task["status"] = "completed"

            except Exception as e:
                task["status"] = "failed"
                task["error"] = str(e)

        return self.results


class AgentBatch:
    """Processamento em lote"""

    def __init__(self):
        self.agent = AutonomousAgent()

    def process_list(self, items: list, task_type: str = "generate") -> list:
        """Processa lista de itens"""
        results = []

        for i, item in enumerate(items, 1):
            print(f"[{i}/{len(items)}] Processando...")

            try:
                if task_type == "generate":
                    result = self.agent.generate_code(item)
                elif task_type == "analyze":
                    result = self.agent.analyze_code(item)
                else:
                    result = self.agent.process_request(item)

                results.append({
                    "input": item,
                    "status": "success",
                    "output": result["response"]
                })

            except Exception as e:
                results.append({
                    "input": item,
                    "status": "failed",
                    "error": str(e)
                })

        return results


# Exemplos de uso
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso: python integracao.py [api|cli|pipeline|batch]")
        sys.exit(1)

    modo = sys.argv[1]

    if modo == "api":
        print("🌐 Iniciando API...")
        api = AgentAPI()

        # Exemplo de requisição
        result = api.generate_code_endpoint("Função que criptografa strings")
        print(json.dumps(result, indent=2, ensure_ascii=False))

    elif modo == "cli":
        print("📺 Iniciando CLI...")
        cli = AgentCLI()
        cli.run()

    elif modo == "pipeline":
        print("🔄 Executando Pipeline...")
        pipeline = AgentPipeline()

        pipeline.add_task("generate", description="Função de hash")
        pipeline.add_task("generate", description="Classe de thread pool")
        pipeline.add_task("chat", message="O que é uma closure?")

        results = pipeline.execute()

        print("\nResultados:")
        for i, result in enumerate(results, 1):
            status = "✅" if result["status"] == "completed" else "❌"
            print(f"{i}. {result['task']} - {status} {result['status']}")

    elif modo == "batch":
        print("📦 Processamento em Lote...")
        batch = AgentBatch()

        descricoes = [
            "Função de busca binária",
            "Classe de fila",
            "Função de validação de email"
        ]

        results = batch.process_list(descricoes, task_type="generate")

        print("\nResultados:")
        for result in results:
            print(f"- {result['status'].upper()}: {result['input'][:30]}")
