from flask import Flask, abort, jsonify, make_response, request, json
from eventoOnline import EventoOnline 
from evento import Evento

app = Flask(__name__)

ev_online = EventoOnline("Evento Online", "2023-10-01")
ev2_online = EventoOnline("Evento Presencial", "2023-10-02")
ev2 = Evento("Evento Presencial 2", "2023-10-03")

eventos = [ev_online, ev2_online, ev2]

@app.route('/')
def index():
    return "<h1>Bombando</h1>"


@app.route('/api/eventos/')
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)




@app.route('/api/eventos/', methods=["POST"])
def criar_evento():
    data = json.loads(request.data)
    nome = data.get("nome")
    local = data.get("local")
    data_evento = data.get("data")

    if not nome:
        abort(400, description="O campo 'nome' é obrigatório.")
        
    if local: 
        evento = Evento(nome, data_evento, local)
    else:
       
        evento = Evento(nome, data_evento, local)
    eventos.append(evento)
    return data


@app.errorhandler(404)
def not_found(error):
    return jsonify(erro=str(error)), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify(erro=str(error)), 400


def get_evento_by_id_or_404(evento_id):
    for ev in eventos:
        if ev.id == evento_id:
            return ev
    abort(404, description="Evento não encontrado")

@app.route('/api/eventos/<int:id>')
def detalhar_evento(id):
    evento = get_evento_by_id_or_404(id)
    return jsonify(evento.__dict__) 


@app.route('/api/eventos/<int:id>', methods=["DELETE"])
def deletar_evento(id):
    evento = get_evento_by_id_or_404(id)
    eventos.remove(evento)
    return jsonify({"message": "Evento deletado com sucesso"})