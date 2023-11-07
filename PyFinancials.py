from flask import Flask
from routes.expense_routes import expense_routes
from routes.budget_routes import budget_routes
from routes.user_routes import user_routes
from routes.reports_routes import reports_routes
from routes.categories_routes import categories_routes

app = Flask(__name__)

app.register_blueprint(expense_routes)
app.register_blueprint(budget_routes)
app.register_blueprint(user_routes)
app.register_blueprint(reports_routes)
app.register_blueprint(categories_routes)
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
