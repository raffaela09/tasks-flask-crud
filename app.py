from flask import Flask, render_template

#variave name -> __name__ = '__main__' forma manual 
app = Flask(__name__)

#rota para criar um comunicação
@app.route('/') #rota inicial - 
#o que vai ser executado a partir dessa função
def hello_world():
    return 'Hello world!'

@app.route('/about') #endpoints 
def about():
    return render_template('about.html') #chama uma pagina html 

if __name__ == '__main__':
    #rodar o codigo, desenvolvimento local, executa somente se for rodado de forma manual
    app.run(debug=True) #coleta as informações de log
    
#api - aplication programming interface - porta de entrada (interface)
#api rest - representational state transfer - conjunto de regras para que a comunicação seja de forma fluida - HTTP
#json ou xml - formato de devolver a url pro client 
#api rest e api restful - ao respeitar todos os padroes do rest - ela é restful - estilo de arquitetura para construção de api
#get - apenas para retornar
#post - para inserir informações em um recurso especifico, problema para alterar
#put - atualizações - ele substitui todas as informações atuais desse cliente, sendo obrigada a enviar tudo
#patch - modificações parciais
#delete - remove recurso especifico 
#request e response  - response vem aquisi
#documentação de api - swagger.io - usado para entender oq aquela api faz
#postman - para testar apis
