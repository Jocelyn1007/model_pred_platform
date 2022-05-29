from flask import Flask, request, send_from_directory

from utility.model_utils import generate_model_id, compute_final_score
import json
import os
import pandas as pd
import pickle as pkl
import random

app = Flask(__name__)

@app.route('/model/check', methods=["GET", "POST"])
def model_check():
    return 'This api works well'

@app.route('/model/upload', methods=['POST'])
def upload():
    try:
        result = {}
        model_id = {'model_id': generate_model_id()}
        model_info = {'model_info': request.json}
        # bins_info = {'bins_info':bins_info}
        result.update(model_id)
        result.update(model_info)
        filepath = os.path.join('models', model_id.get('model_id'))
        os.makedirs(filepath, exist_ok=True)
        filename = os.path.join(filepath, 'model_info')
        with open(filename, 'w+') as f:
            f.truncate()
            f.write(json.dumps(model_info.get('model_info'), indent=4))
            f.flush()
        return json.dumps(result, indent=4)
    except Exception as e:
        return e


@app.route('/model/query/<model_id>', methods=['GET'])
def query(model_id):
    result = {}
    try:
        int(model_id)
        filename = os.path.join('models', model_id, 'model_info')
    except:
        model_path = model_id.split('_')[0:5]
        path = os.path.join(*model_path)
        filename = os.path.join('models', path, 'model_info')
    model_id = {'model_id': model_id}
    with open(filename, 'r') as f:
        model_info = f.read()
    model_info = {'model_info': json.loads(model_info)}
    result.update(model_id)
    result.update(model_info)
    return json.dumps(result)

@app.route('/model/predict/<model_id>', methods=['POST'])
def predict(model_id):
    try:
        int(model_id)
        model_path = model_id
        model_type = 'scorecard'
    except:
        model_path = os.path.join(*model_id.split('_')[0:-1])
        model_type = model_id.split('_')[-1]
    filepath = os.path.join('models', model_path)
    file = request.files['file']
    data_name = generate_model_id()
    filename = os.path.join(filepath, 'data', data_name + '.csv')
    os.makedirs(os.path.join(filepath, 'data'), exist_ok=True)
    file.save(filename)
    data = pd.read_csv(filename)
    if model_type == 'scorecard':
        modelname = os.path.join(filepath, 'model_info')
        with open(modelname, 'r') as f:
            model_info = f.read()
        model_info = json.loads(model_info)
        missing_var = [var for var in model_info.get('bins_info').keys() if var not in data.columns.values]
        if missing_var:
            return '''missing_var:::{0}'''.format(missing_var)
        score = compute_final_score(data, model_info=model_info)
    elif model_type == 'xgb':
        modelname = os.path.join(filepath, 'model.pkl')
        model = pkl.load(open(modelname, 'rb'))
        featurename = os.path.join(filepath, 'features.pkl')
        features = pkl.load(open(featurename, 'rb'))
        missing_var = [var for var in features if var not in data.columns.values]
        if missing_var:
            return '''missing_var:::{0}'''.format(missing_var)
        y_pred = model.predict_proba(data[features])[:,1]
        score = data.copy()
        score['pred'] = y_pred
    else:
        return "UKNOWN"
    score_name = str(data_name) + '_score.csv'
    score.to_csv(os.path.join(filepath, 'data', score_name), index_label=False, index=False)
    return json.dumps({'model_id': model_id, 'data_id': data_name})


@app.route('/model/download/<model_id>/<data_id>', methods=['GET'])
def download(model_id, data_id):
    try:
        int(model_id)
    except:
        model_path = model_id.split('_')[0:-1]
        model_id = os.path.join(*model_path)
    filepath = os.path.join('models', model_id, 'data')
    filename = data_id + '_score.csv'
    try:
        return send_from_directory(directory=filepath, filename=filename, as_attachment=True)
    except Exception as e:
        return e


@app.route('/posion')
def posion():
    with open('posion.pkl', 'rb') as f:
        poison = pkl.load(f)
    return poison[random.randrange(len(poison))]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)