from flask import Flask, json
from faker import Faker

app = Flask(__name__)

#end points
#base padrao
@app.route('/base/padrao', methods=['GET'])
def get_padrao():
    fake = Faker('pt_BR')
    base = {'nome': [], 
            'nascimento': [],
            'endereco': [],
            'bairro': [],
            'cidade': [],
            'estado': [],
            'renda': []
            }
    for i in range(10):
        base['nome'].append(fake.name())
        base['nascimento'].append(fake.date_of_birth().strftime('%d/%m/%Y'))
        base['endereco'].append(fake.street_address())
        base['bairro'].append(fake.bairro())
        base['cidade'].append(fake.city())
        base['estado'].append(fake.estado_sigla())
        base['renda'].append(int(fake.building_number()) // 25 * 1000)
        
    return json.dumps(base, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)