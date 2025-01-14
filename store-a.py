from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

@get("/admin")
def admin_portal():
	return template("pages/admin.html")



@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

@get('/categories')
def get_categories():
    sql = "select * from categories"
    cursor.execute(sql)
    result = cursor.fetchall()
    return json.dumps(result)




# run(host='0.0.0.0', port=argv[1])
run(host='127.0.0.1', port=3000)
