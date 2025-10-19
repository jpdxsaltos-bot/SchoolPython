from flask import Flask, jsonify
import csv

app = Flask(__name__)

def load_airports():
    airports = {}
    with open('airports.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            airports[row['ident'].upper()] = {
                "Name": row['name'],
                "Location": row['municipality']
            }
    return airports

airports_data = load_airports()

@app.route('/airport/<icao_code>')
def airport_info(icao_code):
    icao_code = icao_code.upper()
    if icao_code in airports_data:
        data = airports_data[icao_code]
        return jsonify({
            "ICAO": icao_code,
            "Name": data["Name"],
            "Location": data["Location"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
