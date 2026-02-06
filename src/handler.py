from src.lex_response import close, elicit_slot


def _get_slot_value(slots: dict, name: str):
    """
    Lex V2 typically provides slots like:
    { "slot_name": { "value": { "interpretedValue": "123" } } }
    """
    if not slots or name not in slots or slots[name] is None:
        return None
    return slots[name].get("value", {}).get("interpretedValue")


def lambda_handler(event, context):
    intent = event["sessionState"]["intent"]["name"]
    slots = event["sessionState"]["intent"].get("slots", {})

    # 1) FAQ - business hours
    if intent == "FAQ_Horario":
        return close("Nosso atendimento é de segunda a sexta, 09h às 18h.")

    # 2) Order status (simulated)
    if intent == "StatusPedido":
        pedido_id = _get_slot_value(slots, "pedido_id")

        if not pedido_id:
            return elicit_slot(
                slot_to_elicit="pedido_id",
                message="Qual é o número do seu pedido?",
                slots=slots,
                intent_name=intent,
            )

        # Simple simulation: status depends on last digit
        last_digit = int(str(pedido_id)[-1])
        status_map = {0: "APROVADO", 1: "EM SEPARAÇÃO", 2: "ENVIADO", 3: "ENTREGUE"}
        status = status_map.get(last_digit % 4, "EM ANÁLISE")

        return close(f"Seu pedido {pedido_id} está com status: {status}.")

    # 3) Ticket creation
    if intent == "AbrirChamado":
        nome = _get_slot_value(slots, "nome")
        email = _get_slot_value(slots, "email")
        descricao = _get_slot_value(slots, "descricao")

        if not nome:
            return elicit_slot("nome", "Qual seu nome?", slots, intent)
        if not email:
            return elicit_slot("email", "Qual seu e-mail?", slots, intent)
        if not descricao:
            return elicit_slot("descricao", "Descreva o problema em uma frase:", slots, intent)

        ticket_id = f"TCK-{abs(hash(email)) % 100000}"
        return close(
            f"Chamado aberto! ID: {ticket_id}. Obrigado, {nome}. Entraremos em contato em {email}."
        )

    # Fallback
    return close("Desculpe, não entendi. Você quer consultar status do pedido ou abrir um chamado?")
