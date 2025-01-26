from flask import Blueprint, jsonify, request
from app.services.ner_service import NerService

# Inicializa o Blueprint do controller
ner_controller = Blueprint('ner_controller', __name__)
ner_service = NerService()

@ner_controller.route('/ner', methods=['POST'])
def ner():
    # Obtém o texto do parâmetro de consulta (query parameter)
    textlist = request.get_json()

    if not textlist:
        return jsonify({"error": "Texto é necessário como parâmetro 'text'"}), 400

    # Chama a lógica de negócios no service
    entities = ner_service.process_text(textlist)

    # Retorna as entidades extraídas como resposta em JSON
    return jsonify(entities)