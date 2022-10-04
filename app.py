from flask import Flask, render_template, redirect

# o app atribuimos a ele nossa aplicação flask
app = Flask(__name__)

# aqui atribuimos uma routa para essa aplicação com .route ligado a nossa aplicação flask e atribuimos um caminho como "/" que quer dizer a raiz do site e ela vai sempre executar a função que estiver em seguida dela como é caso ela executa a função home page
@app.route("/")
def home():
    # na função home page você utiliza uma função da biblioteca padrão do flask a render_template() para você renderizar uma pagina html e não ter que poluir seu condigo com tags de html e todos os arquivos htmls devem ficar em uma pasta chamada templates com essa escrita e ficando no mesmo diretorio do arquivo.py que está sua aplicação flask
    return render_template("home.html")

@app.route("/quem_somos")
def quem_somos():
    return render_template("quem_somos.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")
