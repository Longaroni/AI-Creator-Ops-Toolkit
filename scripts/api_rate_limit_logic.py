"""
Lógica Conceptual: Gestão de Rate Limits em APIs de IA
Este script serve como base para evitar bloqueios ao fazer
múltiplos pedidos a APIs como a Anthropic ou OpenAI.
"""

import time

class APIPipelineManager:
def init(self, api_keys, requests_per_minute=50):
self.api_keys = api_keys
self.rpm = requests_per_minute
# Calcula quantos segundos esperar entre cada pedido para não banir a conta
self.delay_between_requests = 60.0 / requests_per_minute
self.current_key_index = 0

def get_next_key(self):
"""Rotação simples de chaves para distribuir a carga."""
key = self.api_keys[self.current_key_index]
# Passa para a próxima chave na lista
self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
return key

def make_safe_request(self, prompt):
"""Simula um pedido seguro, respeitando o tempo de espera."""
print(f"[LOG] A aguardar {self.delay_between_requests:.2f} segundos...")
time.sleep(self.delay_between_requests)

api_key = self.get_next_key()
print(f"[LOG] A usar a chave: {api_key[:8]}...")
print("[LOG] Pedido feito com sucesso!")
return {"status": "success"}
Exemplo de como funcionaria
if name == "main":
# Chaves de exemplo
keys = ["sk-ant-chave1", "sk-ant-chave2"]
pipeline = APIPipelineManager(api_keys=keys, requests_per_minute=10)

# Faz 3 pedidos seguidos de forma segura
for i in range(3):
print(f"\n--- Pedido {i+1} ---")
pipeline.make_safe_request(prompt="Gera um roteiro sobre IA...")
