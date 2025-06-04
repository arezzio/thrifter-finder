print("Running app.py...")

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import random
import math
import requests
import os
import base64
import logging
from dotenv import load_dotenv
import urllib.parse
import socket

# Load environment variables from .env file
load_dotenv('api.env')

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('ebay_api.log')
    ]
)
logger = logging.getLogger(__name__)

# eBay API configuration
EBAY_APP_ID = 'ArezzioR-Thrifter-PRD-bf041d21c-42dd030c'
EBAY_CERT_ID = 'PRD-f041d21c8614-bf79-488a-b12e-ba10'
EBAY_DEV_ID = '1c8921c8-6ba7-42c7-b32d-4b982b20439d'
EBAY_USER_TOKEN = 'v^1.1#i^1#f^0#r^0#I^3#p^3#t^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'
EBAY_API_URL = 'https://api.ebay.com/buy/browse/v1/item_summary/search'

def find_available_port(start_port=5000, max_port=5010):
    """Find an available port in the given range."""
    for port in range(start_port, max_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', port))
                return port
        except OSError:
            continue
    raise RuntimeError(f"No available ports found between {start_port} and {max_port}")

def get_ebay_headers():
    """Get properly formatted headers for eBay API requests."""
    token = EBAY_USER_TOKEN.strip()
    
    # Log token type for debugging
    if token.startswith('v^1.1'):
        logger.info("Using IAF token format")
        auth_header = f'Bearer {token}'  # Using Bearer format for all tokens
    else:
        logger.info("Using Bearer token format")
        auth_header = f'Bearer {token}'
    
    headers = {
        'Authorization': auth_header,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-EBAY-C-MARKETPLACE-ID': 'EBAY-US',
        'X-EBAY-C-ENDUSERCTX': 'contextualLocation=country=US,zip=90210'
    }
    
    # Log headers safely
    safe_headers = headers.copy()
    safe_headers['Authorization'] = f"{safe_headers['Authorization'][:20]}..."
    logger.info(f"Request headers: {safe_headers}")
    
    return headers

def build_ebay_filter(condition=None, min_price=None, max_price=None):
    """Build eBay API filter string based on parameters."""
    filters = []
    
    # Convert condition to eBay condition IDs
    condition_map = {
        'NEW': '1000',
        'USED': '3000',
        'VERY_GOOD': '4000',
        'GOOD': '5000',
        'ACCEPTABLE': '6000'
    }
    
    if condition:
        condition = condition.upper()
        if condition in condition_map:
            filters.append(f"conditions:{{{condition_map[condition]}}}")
        elif condition == 'ALL':
            filters.append("conditions:{1000|3000|4000|5000|6000}")
    
    # Add price filter if min or max price specified
    if min_price is not None or max_price is not None:
        price_filter = 'price:'
        if min_price is not None and max_price is not None:
            price_filter += f"[{min_price}..{max_price}]"
        elif min_price is not None:
            price_filter += f"[{min_price}..]"
        elif max_price is not None:
            price_filter += f"[..{max_price}]"
        filters.append(price_filter)
    
    return ','.join(filters)

def generate_mock_listings(query):
    """Generate mock listings for testing."""
    brands = ['Levi\'s', 'Wrangler', 'Lee', 'Carhartt', 'Dickies']
    conditions = ['New', 'Used', 'Very Good', 'Good', 'Acceptable']
    styles = ['501', '505', '550', 'Classic', 'Vintage']
    
    listings = []
    for _ in range(random.randint(5, 10)):
        brand = random.choice(brands)
        style = random.choice(styles)
        condition = random.choice(conditions)
        price = round(random.uniform(20, 100), 2)
        
        listings.append({
            'title': f"{brand} {style} {query} - {condition}",
            'price': price,
            'condition': condition,
            'url': f"https://example.com/item/{random.randint(1000, 9999)}",
            'image': f"https://via.placeholder.com/150?text={brand}+{style}",
            'timestamp': datetime.now().isoformat()
        })
    
    return listings

def generate_price_history(base_price):
    """Generate mock price history data."""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    history = []
    
    for month in months:
        # Add some random variation to the base price
        price = round(base_price * random.uniform(0.8, 1.2), 2)
        history.append({
            'date': month,
            'price': price
        })
    
    return history

@app.route('/search')
def search():
    """Handle search requests and return mock data."""
    try:
        query = request.args.get('query', '').strip()
        
        if not query:
            return jsonify({
                'error': 'Please provide a search query'
            }), 400

        # Generate mock listings
        listings = generate_mock_listings(query)
        
        # Calculate statistics
        prices = [item['price'] for item in listings]
        avg_price = round(sum(prices) / len(prices), 2)
        last_sold_price = round(random.uniform(avg_price * 0.9, avg_price * 1.1), 2)
        
        # Calculate potential profit
        estimated_cost = round(avg_price * 0.4, 2)  # Assume 60% markup
        net_profit = round(avg_price - estimated_cost, 2)

        response_data = {
            'query': query,
            'average_price': avg_price,
            'last_sold_price': last_sold_price,
            'net_profit': net_profit,
            'listings': listings,
            'price_history': generate_price_history(avg_price),
            'estimated_cost': estimated_cost,
            'total_listings_found': len(listings)
        }

        return jsonify(response_data)

    except Exception as e:
        logger.error(f"Error in search endpoint: {str(e)}", exc_info=True)
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/ebay-search')
def ebay_search():
    """Handle eBay API search requests with pagination."""
    try:
        # Get query parameters
        query = request.args.get('query', '').strip()
        condition = request.args.get('condition')
        min_price = request.args.get('min_price')
        max_price = request.args.get('max_price')
        
        # Convert price strings to float if present
        if min_price:
            min_price = float(min_price)
        if max_price:
            max_price = float(max_price)
        
        # Pagination parameters
        try:
            limit = min(int(request.args.get('limit', 10)), 50)  # Cap at 50 items per page
            offset = max(0, int(request.args.get('offset', 0)))  # Ensure non-negative
        except ValueError as e:
            logger.warning(f"Invalid pagination parameters: {str(e)}. Using defaults.")
            limit = 10
            offset = 0
        
        if not query:
            logger.warning("Search request received with empty query")
            return jsonify({
                'error': 'Please provide a search query'
            }), 400

        # Get headers with properly formatted token
        headers = get_ebay_headers()

        # Build query parameters
        params = {
            'q': query,
            'limit': limit,
            'offset': offset,
            'sort': 'price'  # Sort by price ascending
        }
        
        # Add filter if present
        filter_str = build_ebay_filter(condition, min_price, max_price)
        if filter_str:
            params['filter'] = filter_str

        # URL encode parameters
        encoded_params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        request_url = f"{EBAY_API_URL}?{encoded_params}"

        # Log the full request details for debugging
        logger.info(f"Making request to eBay API - URL: {request_url}")
        logger.info(f"Request Headers: {headers}")

        try:
            response = requests.get(
                request_url,
                headers=headers,
                timeout=30
            )
            
            # Debug logging
            logger.info(f"eBay API Response Status: {response.status_code}")
            logger.debug(f"eBay API Response Headers: {response.headers}")
            
            if response.status_code == 401:
                error_data = response.json()
                logger.error(f"Authentication failed: {error_data}")
                return jsonify({
                    'error': 'Authentication failed. Please check the OAuth token.',
                    'details': error_data
                }), 401
            
            if response.status_code == 400:
                error_data = response.json()
                logger.error(f"Bad request: {error_data}")
                return jsonify({
                    'error': 'Invalid request parameters',
                    'details': error_data
                }), 400
            
            response.raise_for_status()
            
            try:
                data = response.json()
            except ValueError as e:
                logger.error(f"Failed to parse JSON response: {str(e)}")
                logger.error(f"Response content: {response.text}")
                return jsonify({
                    'error': 'Invalid response from eBay API',
                    'details': str(e)
                }), 502
            
            # Transform eBay response into standardized format
            items = []
            if isinstance(data, dict):
                item_summaries = data.get('itemSummaries', [])
                if not isinstance(item_summaries, list):
                    logger.error(f"Unexpected itemSummaries format: {item_summaries}")
                    return jsonify({
                        'error': 'Invalid response format from eBay API',
                        'details': 'itemSummaries is not a list'
                    }), 502
                
                for item in item_summaries:
                    try:
                        if not isinstance(item, dict):
                            logger.warning(f"Skipping invalid item format: {item}")
                            continue
                            
                        price_info = item.get('price', {})
                        if not isinstance(price_info, dict):
                            logger.warning(f"Invalid price info format: {price_info}")
                            continue
                            
                        price = float(price_info.get('value', 0))
                        currency = price_info.get('currency', 'USD')
                        
                        condition_info = item.get('condition', {})
                        if not isinstance(condition_info, dict):
                            logger.warning(f"Invalid condition info format: {condition_info}")
                            continue
                            
                        condition = condition_info.get('conditionDisplayName', 'Not Specified')
                        
                        image_info = item.get('image', {})
                        if not isinstance(image_info, dict):
                            logger.warning(f"Invalid image info format: {image_info}")
                            continue
                            
                        image_url = image_info.get('imageUrl', 'https://via.placeholder.com/150?text=No+Image')
                        
                        items.append({
                            'title': item.get('title', 'No Title'),
                            'price': price,
                            'currency': currency,
                            'condition': condition,
                            'url': item.get('itemWebUrl', '#'),
                            'image': image_url,
                            'item_id': item.get('itemId', ''),
                            'timestamp': datetime.now().isoformat()
                        })
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Error processing item: {str(e)}")
                        continue

            return jsonify({
                'items': items,
                'total_items': len(items),
                'query': query,
                'filters': {
                    'condition': condition,
                    'min_price': min_price,
                    'max_price': max_price
                }
            })

        except requests.RequestException as e:
            error_msg = f"eBay API request failed: {str(e)}"
            logger.error(error_msg)
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_data = e.response.json()
                    logger.error(f"eBay API Error Response: {error_data}")
                except ValueError:
                    logger.error(f"eBay API Error Response: {e.response.text}")
                logger.error(f"eBay API Error Status Code: {e.response.status_code}")
            return jsonify({'error': error_msg}), 503

    except Exception as e:
        error_msg = f"Unexpected error in ebay_search: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return jsonify({'error': error_msg}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'error': 'Resource not found'
    }), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    try:
        port = find_available_port()
        print(f"\n🚀 Starting Flask server...")
        print(f"💻 Server URL: http://127.0.0.1:{port}")
        print(f"📝 API endpoints:")
        print(f"   - GET /search")
        print(f"   - GET /api/ebay-search\n")
        app.run(debug=True, port=port)
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        exit(1)
