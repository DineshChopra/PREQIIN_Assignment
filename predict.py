from flask import Flask, request, jsonify

# Load Model on Startup
# with open('model.bin', 'rb') as f_in:
#     (dv, model) = pickle.load(f_in)

# Init app
app = Flask('text-prediction')

def predict(features):
  # prediiction = model.predict(features)
  prediction = [1.32, 0.393, 0.9312] # Dummy Return values
  return prediction

# Converter
@app.route('/predict', methods=['POST'])
def predict_endpoint():
  print('convrter post request ---- -', request)
  features = request.json['text']
  print('features --- ', features)
  prediction = predict(features)
  response = {
    'prediction': prediction
  }
  return jsonify(response)


# Run Server
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=9696)

