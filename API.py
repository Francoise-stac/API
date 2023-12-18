from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)
df = pd.DataFrame({'item_id':["12","13","14"], 'name':['douze', 'treize', 'quatorze']})
@app.route('/')
def home():
    return "hello toi"
@app.route('/api/<int:item_id>', methods=['GET'])
def get_data(item_id):
    item_id = str(item_id)
    return jsonify({'name': df[df.item_id == item_id].name.item()})
if __name__ == '__main__':
    app.run(debug=True)

