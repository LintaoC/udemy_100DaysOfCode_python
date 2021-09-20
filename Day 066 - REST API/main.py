import sqlalchemy.exc
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            # print(column)
            # print(f"ColumnName: {column.name}  /// getattr: {getattr(self, column.name)}")
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        # # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # My solution before to look at Angela solution
    # random_number = random.randint(1, db.session.query(Cafe).count())
    # rand_cafe = Cafe.query.get(random_number)
    return jsonify(cafe=random_cafe.to_dict()), 200


@app.route("/all", methods=["GET"])
def get_all_cafe():
    cafes = db.session.query(Cafe).all()
    cafes_list = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafes_list), 200


@app.route("/search", methods=["GET"])
def search_cafe():
    cafes = Cafe.query.filter_by(location=request.args.get("loc")).all()
    cafes_list = [cafe.to_dict() for cafe in cafes]
    if cafes_list:
        return jsonify(cafes=cafes_list), 200
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    if request.args.get("api_key") == "TopSecretAPIKey":
        # Converting string from Postman into boolean value
        has_toilet = request.form.get("has_toilet").lower() in ['true', '1', 't', 'y']
        has_wifi = request.form.get("has_wifi").lower() in ['true', '1', 't', 'y']
        has_sockets = request.form.get("has_sockets").lower() in ['true', '1', 't', 'y']
        can_take_calls = request.form.get("can_take_calls").lower() in ['true', '1', 't', 'y']

        # Create the new_cafe object
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=has_toilet,
            has_wifi=has_wifi,
            has_sockets=has_sockets,
            can_take_calls=can_take_calls,
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify(
                response={"Error": "Sorry, data were not added to the database. Coffee already in the database?"}),  404
        else:
            return jsonify(response={"success": "Successfully added the new cafe."}), 200
    else:
        return jsonify(error="Sorry, that's not allowed. Make sur you have the correct api_key"), 403


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    if request.args.get("api_key") == "TopSecretAPIKey":
        cafe_to_update = Cafe.query.get(cafe_id)
        if cafe_to_update:
            cafe_to_update.coffee_price = request.args.get("new_price")
            db.session.commit()
            return jsonify(success="Successfully updated the coffee price."), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sur you have the correct api_key"), 403


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api_key") == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(success="Successfully removed the Cafe."), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sur you have the correct api_key"), 403


if __name__ == '__main__':
    app.run(debug=True)
