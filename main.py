#ORM  :  permet  ajouter dans les données vers sql  comme si on ajouté dans les liste
#avec orm on a pas besoin d utiliser des commandes sql
#les tableau vont etre créé dans les classe et les methods
#source flask sqlalchemy
#
#
#
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

#APP
app = Flask(__name__)                                   #crée app flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ismail.sesen1/Documents/zperso/toDoApp/todo.db'   #app ORM
db = SQLAlchemy(app)                                    #creer le objet ORM

#APP ROUTE----index
@app.route("/")                             #dans le server si on arrive au main repertoire "/" execute ce qui suit
def index():                                #ce fonction va etre execute quand arrive au main repertoire "/"
    todos=Todo.query.all()
    return  render_template("index.html",todos=todos)   #render le fichier index.html


#APP ROUTE----post add
@app.route("/add",methods=["POST"])         #executé quant dans index.html is action /add est envoyé avec methon post
def addTodo():                                  #ce fonction va etre execute on pese bouton add dans index.html (action)
    titre=request.form.get("title")         # prend la valeur du input title  et met dans objet  titre
    newTodo=Todo(title=titre,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return  redirect(url_for("index"))      #redrige vers le fonction index


#APP ROUTE----update
@app.route("/complete/<string:id>")         #executé quant dans index.html is action /add est envoyé avec methon post
def completeTodo(id):                       #ce fonction va etre execute on pese bouton add dans index.html (action)
    todo=Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return  redirect(url_for("index"))      #redrige vers le fonction index

#APP ROUTE----update
@app.route("/delete/<string:id>")         #executé quant dans index.html is action /add est envoyé avec methon post
def deleteTodo(id):                       #ce fonction va etre execute on pese bouton add dans index.html (action)
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return  redirect(url_for("index"))      #redrige vers le fonction index


#CLASSES
class Todo(db.Model):                                   #classe utilise Model methode du ORM
    id = db.Column(db.Integer, primary_key=True)        #crée colomn id , INT
    title = db.Column(db.String(80))                    #crée colomn title , STR , max 80
    complete = db.Column(db.Boolean)                    #crée colomn complete , valeur Boolean True or False



#EXECUTION
if __name__ =="__main__":
    db.create_all()                                     #crée la table
    app.run(debug=True)                                 #execute app flask

