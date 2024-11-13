from flask import Flask, jsonify, request

app = Flask(__name__)

import random
@app.route('/quote', methods=['GET'])
def primary():
  #print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  if (request.method == 'GET'):
    data = {"data": quotes[rnd]}
    return jsonify(data)
  #print(quotes[rnd])

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=9001)
  primary()

