from flask import Flask, request
from flask_restful import Resource, Api
import os
from quickstart import getData

# from restapi import TodoSimple

app = Flask(__name__)
api = Api(app)

port = int(os.getenv("PORT", 9009))

@app.route('/', )
def hello_world():
	return 'Hello World! Welcome to SAP Cloud Platform'

todos = {
    '1':  'My first task.',
    '2':  'Remeber the milk.'
}
	
class TodoSimple(Resource):
	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	def put(self, todo_id):
		print(request.form['data'])
		todos[todo_id] = request.form['data']
		return {todo_id: todos[todo_id]}
		
class HanaDbMockUp(Resource):
	def get(self):
		return getData()

api.add_resource(TodoSimple, '/TODO/<string:todo_id>')
api.add_resource(HanaDbMockUp, '/myhana')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
