from flask import Flask, render_template, request, redirect, url_for
from ShirtService import ShirtService
import configparser


app = Flask(__name__)
service = ShirtService()
app.config['DEBUG'] = True

config = configparser.ConfigParser()
config.read('config.ini')


@app.route(config['Routes']['index'])
def index():
    shirts = []
    try:
        shirts = service.GetAllShirts()
    except Exception as e:
            print("Error getting shirts: {}".format(e))
    return render_template('index.html', shirts=shirts)


@app.route(config['Routes']['add_shirt'], methods=['POST'])
def add_shirt():
    if request.method == 'POST':
        color = request.form['color']
        design = request.form['text']
        try:
            shirt = service.AddShirt(color, design)
            if shirt:
                return redirect(url_for('index'))
            else:
                return "Error adding shirt"
        except Exception as e:
            print("Error adding shirt: {}".format(e))
            return "Error adding shirt"


@app.route(config['Routes']['update_shirt']+'/<int:shirt_id>', methods=['POST'])
def update_shirt(shirt_id):
    if request.method == 'POST':
        new_color = request.form['new_color']
        new_design = request.form['new_text']
        try:
            updated_shirt = service.UpdateShirt(shirt_id, new_color, new_design)
            if updated_shirt:
                return redirect(url_for('index'))
            else:
                return "Error updating shirt"
        except Exception as e:
            print("Error updating shirt: {}".format(e))
            return "Error updating shirt"


@app.route(config['Routes']['delete_shirt']+'/<int:shirt_id>', methods=['POST'])
def delete_shirt(shirt_id):
    try:
        deleted = service.DeleteShirt(shirt_id)
        return redirect(url_for('index'))
    except Exception as e:
        print("Error deleting shirt: {}".format(e))
        return "Error deleting shirt" 

if __name__ == '__main__':
    app.run()
