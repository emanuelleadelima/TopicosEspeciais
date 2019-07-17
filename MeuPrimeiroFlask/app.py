from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nome>")
def hello_world(nome):
    return ("Olá %s! Estou aprendendo Flask" %(nome), 200)

@app.route("/usuario/<int:id>", methods=['GET'])
def getUsuario(id):
    usuarios = [{1: "Harry"}, {2: "Rony"}, {3: "Hermione"}, {4: "Hagrid"}]
    for usuario in usuarios:
        if(id in usuario.keys()):
            print(usuario[id])
            return(usuario[id], 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
