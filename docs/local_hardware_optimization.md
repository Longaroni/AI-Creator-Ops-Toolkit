Guia Rápido: Otimização de Hardware para Modelos de IA Locais

O Desafio
Correr modelos de IA em computadores normais (ex: 8GB de VRAM) causa frequentemente erros de falta de memória (OOM).

Estratégias de Mitigação

Quantização (A Regra de Ouro)
Nunca corras modelos inteiros sem compressão.
Recomendado: Utilizar formato GGUF com quantização Q4_K_M.
Ferramentas: Usar LM Studio ou Ollama para gerir isto automaticamente.
Gestão da Janela de Contexto
A memória gráfica é consumida pelo tamanho do texto que envias.
Erro Comum: Enviar janelas de 32k de texto para tarefas simples.
Solução: Limitar o contexto ao mínimo necessário (ex: 2048 tokens). Isto reduz a carga na placa gráfica em mais de 40%.
Offloading (Transferir trabalho)
Se o modelo não couber na placa gráfica:
Ajustar as definições para a placa gráfica tratar do que consegue e o processador (CPU) tratar do resto. É mais lento, mas não crasha.
