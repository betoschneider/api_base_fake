from flask import Flask, request, jsonify
from faker import Faker
import pandas as pd

app = Flask(__name__)

#end points
#base padrao
@app.route('/base', methods=['GET'])
def get_padrao():
    try:
        qtd_linhas = min(int(request.args.get('rows')), 999)
    except:
        qtd_linhas = 50

    fake = Faker('pt_BR')

    base = []
    for i in range(qtd_linhas):
        base.append([fake.name(),
                     fake.date_of_birth().strftime('%d/%m/%Y'),
                     fake.street_prefix() + ' ' + fake.street_name() + ', ' + fake.building_number(),
                     fake.bairro(),
                     fake.city(),
                     fake.estado_sigla(),
                     int(fake.building_number()) // 25 * 1000
                     ])
    
    base = pd.DataFrame(base, columns=['nome', 'nascimento', 'endereco', 'bairro', 'cidade', 'estado', 'renda'])
        
        
    return base.to_csv(index=False, sep=';', lineterminator='\n'), 200

@app.route('/base/custom', methods=['GET'])
def get_custom():
    try:
        colunas = request.args.get('colunas')
        colunas = colunas.split('-')
        return jsonify(colunas), 200
    except:
        return jsonify({"message": "Nenhum parametro enviado"}), 400


if __name__ == '__main__':
    app.run(debug=False)