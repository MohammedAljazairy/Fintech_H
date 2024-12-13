import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, jsonify

with open("model RandomForestClassifier.pkl", 'rb') as f:
    loaded_grid_search = pickle.load(f)

with open("scaler.pkl", 'rb') as f:
    loaded_scaler = pickle.load(f)

def fun( arr ):
  n=np.array(arr)
  random_array=loaded_scaler.transform(n.reshape(1,-1))
  pred =loaded_grid_search.predict(random_array)
  return pred[0]

app = Flask(__name__)

@app.route('/modelpoint', methods=['POST'])
def modelpoint():
    data = request.get_json()
    l=data['numbers']
    mes=fun( l )

    return jsonify({'message': str(mes)}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000, use_reloader=False)