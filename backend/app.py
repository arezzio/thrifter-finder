print("Running app.py...")

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()

    if "jean" in query:
        data = {
            "average_price": 30.5,
            "last_sold_price": 32.0,
            "net_profit": 24.0,
            "chart_data": [
                {"date": "Jan", "price": 25.5},
                {"date": "Feb", "price": 28.0},
                {"date": "Mar", "price": 31.0},
                {"date": "Apr", "price": 33.0},
                {"date": "May", "price": 32.5},
            ],
            "example_listings": [
                {"title": "Levi's 501 Jeans", "price": 29.99, "link": "https://example.com/item1"},
                {"title": "Wrangler Vintage Jeans", "price": 27.5, "link": "https://example.com/item2"},
            ]
        }

    elif "hoodie" in query:
        data = {
            "average_price": 45.0,
            "last_sold_price": 47.5,
            "net_profit": 35.0,
            "chart_data": [
                {"date": "Jan", "price": 38.0},
                {"date": "Feb", "price": 41.5},
                {"date": "Mar", "price": 43.0},
                {"date": "Apr", "price": 46.0},
                {"date": "May", "price": 47.5},
            ],
            "example_listings": [
                {"title": "Nike Club Fleece Hoodie", "price": 44.0, "link": "https://example.com/item3"},
                {"title": "Adidas Originals Hoodie", "price": 46.5, "link": "https://example.com/item4"},
            ]
        }

    elif "t-shirt" in query or "shirt" in query:
        data = {
            "average_price": 21.0,
            "last_sold_price": 23.5,
            "net_profit": 15.5,
            "chart_data": [
                {"date": "Jan", "price": 15.5},
                {"date": "Feb", "price": 18.25},
                {"date": "Mar", "price": 21.0},
                {"date": "Apr", "price": 23.5},
                {"date": "May", "price": 20.75},
            ],
            "example_listings": [
                {"title": "Supreme Graphic Tee", "price": 23.0, "link": "https://example.com/item5"},
                {"title": "Gildan Plain T-shirt", "price": 18.0, "link": "https://example.com/item6"},
            ]
        }

    else:
        data = {}

    return jsonify(data)

# This is important: it actually starts the server when you run python app.py
if __name__ == "__main__":
    app.run(debug=True)
