from flask import Flask, render_template, request, json, jsonify
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)

app.config.from_pyfile('database.cfg')
#------- MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'sqluser'
#app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
#app.config['MYSQL_DATABASE_DB'] = 'greetingsdb'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/version")
def get_version():
    return "v1.0.1 \n"

@app.route("/all")
def all_greetings():
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM greetings_tbl')
    results = cursor.fetchall()
    rows = [] 
    for row in results:
        rows.append(row)
    #db.close()
    return jsonify(rows)
    #return render_template("index.html", rows=results)

@app.route("/")
def main():
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute('SELECT greeting FROM greetings_tbl WHERE gr_lang = "En"')
    result = cursor.fetchall()
    #return jsonify(result)
    return render_template("index.html", result = result)

@app.route("/<int:gr_id>")
def greeting_by_id(gr_id):
    db = mysql.connect()
    cursor = db.cursor()
    cursor.execute("SELECT greeting FROM greetings_tbl WHERE gr_id = '%s'", gr_id)
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
