from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Route API que la racine va appeler pour avoir les noms
@app.route('/person_api', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify([{"id": p.id, "name": p.name} for p in persons])

if __name__ == '__main__':
    app.run(port=5001, debug=True)