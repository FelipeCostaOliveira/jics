from flask import Flask, render_template, request, redirect, url_for
from Classes import *
from cadastro import cadastro, cadastro_professor

app = Flask(__name__, template_folder='template', static_url_path='/static')
# Use 'template' como o diretório de templates

# Lista de alunos para fins de demonstração (substitua por sua própria lógica de armazenamento)
alunos = []
professores = [
    {"matricula": "12345", "senha": "senha123"},
    {"matricula": "67890", "senha": "outraSenha"}
]

def professor_valido(matricula, senha):
    for professor in professores:
        if professor["matricula"] == matricula and professor["senha"] == senha:
            return True
    return False
# Define routes for student and professor registration
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        curso = request.form['curso']
        turma = request.form['turma']
        aluno = Aluno(nome, matricula, curso, turma)
        aluno.cadastrar_aluno(turma, curso)
        alunos.append(aluno)  # Adicione o aluno à lista (substitua por sua própria lógica de armazenamento)
    return render_template('cadastro_aluno.html')

@app.route('/cadastro_professor', methods=['GET', 'POST'])
def cadastrar_professor():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula_prof = request.form['matricula_prof']
        senha = request.form['senha']
        servidor = professor(nome, matricula_prof, senha)
        servidor.cad_professor(senha)
    return render_template('cadastro_professor.html')

@app.route('/editar_aluno', methods=['GET', 'POST'])
def editar_aluno():
    if request.method == 'POST':
        matricula = request.form['matricula']  # Matrícula do aluno a ser editado
        for aluno in alunos:
            if aluno.get_matricula() == matricula:
                # Atualize as informações do aluno com base nos dados do formulário
                aluno.set_nome(request.form['novo_nome'])
                aluno.set_curso(request.form['novo_curso'])
                aluno.set_turma(request.form['nova_turma'])
                return redirect(url_for('exibir_alunos'))
        # Se a matrícula não for encontrada, você pode adicionar uma lógica de tratamento de erro aqui
    return render_template('editar_aluno.html')

@app.route('/excluir_aluno', methods=['GET', 'POST'])
def excluir_aluno():
    if request.method == 'POST':
        matricula = request.form['matricula']  # Matrícula do aluno a ser excluído
        for aluno in alunos:
            if aluno.get_matricula() == matricula:
                alunos.remove(aluno)  # Remove o aluno da lista (substitua por sua própria lógica de armazenamento)
                return redirect(url_for('exibir_alunos'))
        # Se a matrícula não for encontrada, você pode adicionar uma lógica de tratamento de erro aqui
    return render_template('excluir_aluno.html')

@app.route('/exibir_alunos')
def exibir_alunos():
    return render_template('exibir_alunos.html', alunos=alunos)
@app.route('/login_professor', methods=['GET', 'POST'])
def login_professor():
    if request.method == 'POST':
        matricula = request.form['matricula']
        senha = request.form['senha']

        # Verifique as credenciais do professor (por exemplo, comparando com o banco de dados)
        if professor_valido(matricula, senha):
            # Redirecione para a página de ações do professor
            return redirect(url_for('acoes_professor'))
       

    return render_template('login_professor.html')

if __name__ == '__main__':
    app.run(debug=True)
