import re
import json
import azure.functions as func

def validar_cpf(cpf):
    """
    Função para validar se um CPF é válido.
    """
    # Remover caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais (exemplo: 111.111.111-11)
    if cpf == cpf[0] * len(cpf):
        return False

    # Validação do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10 or primeiro_digito == 11:
        primeiro_digito = 0
    if int(cpf[9]) != primeiro_digito:
        return False

    # Validação do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10 or segundo_digito == 11:
        segundo_digito = 0
    if int(cpf[10]) != segundo_digito:
        return False

    return True

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Função principal que recebe a requisição HTTP e valida o CPF.
    """
    # Recebe o CPF da query string ou do corpo da requisição
    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    # Se CPF não for fornecido
    if not cpf:
        return func.HttpResponse(
            "Por favor, forneça um CPF na query string ou no corpo da requisição.",
            status_code=400
        )

    # Validar o CPF
    if validar_cpf(cpf):
        return func.HttpResponse(
            json.dumps({"cpf": cpf, "valid": True}),
            mimetype="application/json",
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps(
