from data import user_id_counter, users, budget, income_data, expenses_data, predefined_categories, custom_categories
from flask import Flask, render_template
from routes.budget_routes import budget_routes
from routes.categories_routes import categories_routes
from routes.expense_routes import expense_routes
from routes.reports_routes import reports_routes
from routes.user_routes import user_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(budget_routes)
app.register_blueprint(categories_routes)
app.register_blueprint(expense_routes)
app.register_blueprint(reports_routes)
app.register_blueprint(user_routes)
@app.route('/')
def index():
    return render_template(
        'index.html',
        user_id_counter=user_id_counter,
        users=users,
        budget=budget,
        income_data=income_data,
        expenses_data=expenses_data,
        predefined_categories=predefined_categories,
        custom_categories=custom_categories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
