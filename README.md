# 🤖 Lex + Lambda Chatbot (AWS Serverless)

Simple customer-support chatbot built with **Amazon Lex (V2)** and **AWS Lambda (Python)**.
The bot handles FAQ, order status lookup (simulated), and ticket creation.

## ✅ Features
- FAQ: business hours
- Order status: extracts `pedido_id` and returns a simulated status
- Ticket creation: collects `nome`, `email`, and `descricao`
- Fallback handling for unknown messages
- Ready for logs/monitoring with CloudWatch

## 🧩 Architecture (Serverless)
User → Amazon Lex → AWS Lambda (Python) → Response  
(Optional) CloudWatch Logs for analysis

## 🧠 Refinement (Conversation Design)

### Intent 1 — `FAQ_Horario`
**Goal:** answer business hours.

**Sample utterances**
- "qual o horário de atendimento?"
- "vocês atendem até que horas?"
- "funciona no fim de semana?"

**Expected response**
- "Nosso atendimento é de segunda a sexta, 09h às 18h."

---

### Intent 2 — `StatusPedido`
**Goal:** get an order id and return status (simulated).

**Slots**
- `pedido_id` (required)

**Sample utterances**
- "status do pedido {pedido_id}"
- "meu pedido é {pedido_id}"
- "acompanhar pedido {pedido_id}"

**Expected response**
- "Seu pedido {pedido_id} está com status: ..."

---

### Intent 3 — `AbrirChamado`
**Goal:** collect user details and confirm ticket opening.

**Slots**
- `nome` (required)
- `email` (required)
- `descricao` (required)

**Sample utterances**
- "quero abrir um chamado"
- "preciso de ajuda"
- "suporte, por favor"

**Expected response**
- "Chamado aberto! ID: TCK-XXXXX ..."

---

### Fallback
If the bot can't understand:
- "Desculpe, não entendi. Você quer consultar status do pedido ou abrir um chamado?"
