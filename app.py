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

# Load environment variables from .env file
load_dotenv('api.env')

app = Flask(__name__)
CORS(app)

# Force port 3000
PORT = 3000

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
EBAY_USER_TOKEN = 'v^1.1#i^1#I^3#p^3#f^0#r^0#t^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'
EBAY_API_URL = 'https://api.ebay.com/buy/browse/v1/item_summary/search'  # Using production environment

if not EBAY_USER_TOKEN:
    logger.error("EBAY_USER_TOKEN not found in environment variables")
    raise ValueError("EBAY_USER_TOKEN environment variable is required")

# Mock data structure
BRANDS = {
    'luxury': ['Gucci', 'Prada', 'Louis Vuitton', 'Balenciaga', 'Saint Laurent'],
    'premium': ['Nike', 'Adidas', 'Levi\'s', 'Calvin Klein', 'Tommy Hilfiger'],
    'casual': ['H&M', 'Zara', 'Uniqlo', 'Gap', 'Old Navy']
}

CATEGORIES = {
    'jeans': {
        'styles': ['Skinny', 'Straight', 'Bootcut', 'Mom', 'Boyfriend', 'Wide Leg'],
        'colors': ['Blue', 'Black', 'Light Wash', 'Dark Wash', 'Distressed'],
        'price_range': (30, 200)
    },
    'jackets': {
        'styles': ['Bomber', 'Denim', 'Leather', 'Puffer', 'Blazer'],
        'colors': ['Black', 'Brown', 'Navy', 'Olive', 'Beige'],
        'price_range': (50, 300)
    },
    't-shirts': {
        'styles': ['Crew Neck', 'V-Neck', 'Graphic', 'Plain', 'Oversized'],
        'colors': ['White', 'Black', 'Grey', 'Navy', 'Striped'],
        'price_range': (15, 100)
    },
    'dresses': {
        'styles': ['Mini', 'Midi', 'Maxi', 'Wrap', 'Slip'],
        'colors': ['Black', 'Floral', 'Red', 'Navy', 'White'],
        'price_range': (40, 250)
    },
    'shoes': {
        'styles': ['Sneakers', 'Boots', 'Sandals', 'Loafers', 'Heels'],
        'colors': ['Black', 'White', 'Brown', 'Multi', 'Grey'],
        'price_range': (45, 350)
    }
}

CONDITIONS = {
    'New with Tags': 1.0,
    'Like New': 0.9,
    'Very Good': 0.8,
    'Good': 0.7,
    'Fair': 0.6
}

# High-quality mock product images from Unsplash
MOCK_IMAGES = {
    'jeans': [
        'https://images.unsplash.com/photo-1542272604-787c3835535d',
        'https://images.unsplash.com/photo-1541099649105-f69ad21f3246',
        'https://images.unsplash.com/photo-1602293589930-45aad59ba3ab'
    ],
    'jackets': [
        'https://images.unsplash.com/photo-1551028719-00167b16eac5',
        'https://images.unsplash.com/photo-1591047139829-d91aecb6caea',
        'https://images.unsplash.com/photo-1495105787522-5334e3ffa0ef'
    ],
    't-shirts': [
        'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab',
        'https://images.unsplash.com/photo-1503341504253-dff4815485f1',
        'https://images.unsplash.com/photo-1583743814966-8936f5b7be1a'
    ],
    'dresses': [
        'https://images.unsplash.com/photo-1595777457583-95e059d581b8',
        'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1',
        'https://images.unsplash.com/photo-1612336307429-8a898d10e223'
    ],
    'shoes': [
        'https://images.unsplash.com/photo-1549298916-b41d501d3772',
        'https://images.unsplash.com/photo-1560769629-975ec94e6a86',
        'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a'
    ]
}

def determine_category(query):
    """Determine the most likely category based on the search query."""
    query = query.lower()
    for category in CATEGORIES.keys():
        if category in query or any(style.lower() in query for style in CATEGORIES[category]['styles']):
            return category
    return random.choice(list(CATEGORIES.keys()))

def generate_mock_listings(query, count=4):
    """Generate realistic mock listings based on the search query."""
    category = determine_category(query)
    cat_data = CATEGORIES[category]
    listings = []
    
    for i in range(count):
        # Select brand tier and brand
        brand_tier = random.choice(['luxury', 'premium', 'casual'])
        brand = random.choice(BRANDS[brand_tier])
        
        # Generate price based on brand tier and condition
        condition = random.choice(list(CONDITIONS.keys()))
        base_price = random.uniform(cat_data['price_range'][0], cat_data['price_range'][1])
        adjusted_price = base_price * CONDITIONS[condition]
        
        if brand_tier == 'luxury':
            adjusted_price *= 2.5
        elif brand_tier == 'premium':
            adjusted_price *= 1.5
        
        listings.append({
            'id': f'{category}_{i}_{datetime.now().timestamp()}',
            'title': f'{brand} {random.choice(cat_data["styles"])} {random.choice(cat_data["colors"])} {category.title()}',
            'brand': brand,
            'category': category,
            'price': round(adjusted_price, 2),
            'original_price': round(base_price * 1.5, 2),
            'condition': condition,
            'color': random.choice(cat_data['colors']),
            'style': random.choice(cat_data['styles']),
            'image': random.choice(MOCK_IMAGES.get(category, MOCK_IMAGES['t-shirts'])),
            'link': f'https://example.com/listing/{category}_{i}',
        })
    
    return listings

def generate_price_history(avg_price, days=150):
    """Generate realistic price history data with trend and seasonality."""
    price_history = []
    base_date = datetime.now() - timedelta(days=days)
    
    # Add some trend and seasonality
    for i in range(days):
        current_date = base_date + timedelta(days=i)
        # Add weekly pattern and slight upward trend
        trend = i * 0.05  # Slight upward trend
        weekly = math.sin(i * 2 * math.pi / 7) * 5  # Weekly pattern
        seasonal = math.sin(i * 2 * math.pi / 365) * 10  # Seasonal pattern
        
        variation = random.uniform(-5, 5)  # Random noise
        price = avg_price + trend + weekly + seasonal + variation
        price = max(avg_price * 0.7, min(avg_price * 1.3, price))  # Keep within reasonable bounds
        
        price_history.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'price': round(price, 2)
        })
    
    return price_history

def get_ebay_headers():
    """Get properly formatted headers for eBay API requests."""
    headers = {
        'Authorization': f'Bearer {EBAY_USER_TOKEN}',
        'Content-Type': 'application/json',
        'X-EBAY-C-MARKETPLACE-ID': 'EBAY_US',
        'X-EBAY-C-ENDUSERCTX': 'contextualLocation=country=US,zip=90210'
    }
    
    # Log headers for debugging (safely)
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
            filters.append(f"conditionIds:{{{condition_map[condition]}}}")
        elif condition == 'ALL':
            filters.append("conditionIds:{1000|3000|4000|5000|6000}")
    
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

@app.route('/api/search')
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
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

@app.route('/api/test')
def test_api():
    """Test endpoint to verify API functionality."""
    try:
        # Get headers with properly formatted token
        headers = get_ebay_headers()
        
        # Make a simple test request
        test_url = f"{EBAY_API_URL}?q=test&limit=1"
        logger.info(f"Making test request to: {test_url}")
        
        response = requests.get(
            test_url,
            headers=headers,
            timeout=30
        )
        
        logger.info(f"Test response status: {response.status_code}")
        logger.info(f"Test response headers: {response.headers}")
        
        if response.status_code == 401:
            logger.error("Authentication failed in test")
            return jsonify({
                'error': 'Authentication failed',
                'details': response.text
            }), 401
            
        return jsonify({
            'status': 'success',
            'message': 'API is working',
            'response_status': response.status_code
        })
        
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
        return jsonify({
            'error': 'Test failed',
            'details': str(e)
        }), 500

@app.route('/api/ebay-search')
def ebay_search():
    """Handle eBay API search requests with pagination."""
    try:
        # Get query parameters
        query = request.args.get('query', '').strip()
        
        # Pagination parameters
        try:
            limit = min(int(request.args.get('limit', 24)), 50)
            offset = max(0, int(request.args.get('offset', 0)))
        except ValueError as e:
            logger.warning(f"Invalid pagination parameters: {str(e)}. Using defaults.")
            limit = 24
            offset = 0
        
        if not query:
            logger.warning("Search request received with empty query")
            return jsonify({
                'error': 'Please provide a search query'
            }), 400

        # Get headers with properly formatted token
        headers = get_ebay_headers()

        # Determine if this is a clothing search
        clothing_keywords = ['jeans', 'shirt', 'dress', 'jacket', 'sweater', 'hoodie', 't-shirt', 'tshirt', 'pants', 'shorts', 'skirt', 'shoes', 'nike', 'adidas']
        is_clothing_search = any(keyword in query.lower() for keyword in clothing_keywords)

        # Basic query parameters
        params = {
            'q': query,
            'limit': limit,
            'offset': offset,
            'sort': 'bestMatch',
            'filter': 'buyingOptions:{AUCTION|FIXED_PRICE}'  # Add buying options filter
        }

        # Add category filters for clothing
        if is_clothing_search:
            print(f"\n=== Category Detection ===")
            print(f"Query: {query}")
            print(f"Detected keywords: {[k for k in clothing_keywords if k in query.lower()]}")
            
            # Simplified category filters
            if 'shoes' in query.lower() or 'nike' in query.lower():
                params['category_ids'] = '15709'  # Shoes category
                print("Using Shoes category (15709)")
            else:
                params['category_ids'] = '11450'  # Clothing category
                print("Using Clothing category (11450)")
            print("========================\n")

        # URL encode parameters
        encoded_params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        request_url = f"{EBAY_API_URL}?{encoded_params}"

        # Log the full request details for debugging
        print("\n=== eBay API Request ===")
        print(f"Query: {query}")
        print(f"Is clothing search: {is_clothing_search}")
        print(f"Request URL: {request_url}")
        print(f"Parameters: {params}")
        print("=======================\n")

        try:
            response = requests.get(
                request_url,
                headers=headers,
                timeout=30
            )
            
            # Debug logging
            print("\n=== eBay API Response ===")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Response Text: {response.text[:1000]}")  # Print first 1000 chars of response
            
            if response.status_code == 401:
                print(f"Authentication Error: {response.text}")
                logger.error("Authentication failed")
                logger.error(f"Response body: {response.text}")
                return jsonify({
                    'error': 'Authentication failed. Please check the OAuth token.',
                    'debug': {
                        'status_code': response.status_code,
                        'response_headers': dict(response.headers),
                        'response_body': response.text
                    }
                }), 401
            
            response.raise_for_status()
            
            # Parse response as JSON
            try:
                data = response.json()
                if not isinstance(data, dict):
                    raise ValueError(f"Expected dict response, got {type(data)}")
                
                total_found = data.get('total', 0)
                print(f"Total items found: {total_found}")
                
                # Log item summaries if available
                item_summaries = data.get('itemSummaries', [])
                if not isinstance(item_summaries, list):
                    raise ValueError(f"Expected list for itemSummaries, got {type(item_summaries)}")
                
                if item_summaries:
                    print("\nFirst few items:")
                    for i, item in enumerate(item_summaries[:3]):
                        if not isinstance(item, dict):
                            print(f"Warning: Item {i} is not a dictionary")
                            continue
                        print(f"\nItem {i + 1}:")
                        print(f"Title: {item.get('title', 'No Title')}")
                        print(f"Price: {item.get('price', {}).get('value', 'N/A')} {item.get('price', {}).get('currency', 'USD')}")
                        print(f"Condition: {item.get('condition', {}).get('conditionDisplayName', 'Not Specified')}")
                        print(f"Category: {item.get('primaryCategory', {}).get('categoryName', 'Not Specified')}")
                else:
                    print("\nNo items found in response")
                
                print("\nFull response data:")
                print(data)
                print("========================\n")
                
            except ValueError as e:
                print(f"JSON Parse Error: {str(e)}")
                logger.error(f"Failed to parse JSON response: {str(e)}")
                return jsonify({
                    'error': f'Invalid response from eBay API: {str(e)}'
                }), 500
            
            # Transform eBay response into standardized format
            items = []
            for item in item_summaries:
                try:
                    if not isinstance(item, dict):
                        print(f"Warning: Skipping non-dict item: {item}")
                        continue
                        
                    price_info = item.get('price', {})
                    if not isinstance(price_info, dict):
                        print(f"Warning: Invalid price info for item: {item.get('title', 'No Title')}")
                        continue
                        
                    price = float(price_info.get('value', 0))
                    currency = price_info.get('currency', 'USD')
                    
                    condition_info = item.get('condition', {})
                    if not isinstance(condition_info, dict):
                        print(f"Warning: Invalid condition info for item: {item.get('title', 'No Title')}")
                        continue
                        
                    condition = condition_info.get('conditionDisplayName', 'Not Specified')
                    
                    image_info = item.get('image', {})
                    if not isinstance(image_info, dict):
                        print(f"Warning: Invalid image info for item: {item.get('title', 'No Title')}")
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
                    print(f"Warning: Error processing item: {str(e)}")
                    logger.warning(f"Error processing item: {str(e)}")
                    continue

            # Add debug info to response
            debug_info = {
                'request_url': request_url,
                'response_status': response.status_code,
                'total_found': total_found,
                'items_returned': len(items),
                'is_clothing_search': is_clothing_search,
                'query_params': params,
                'response_data': data  # Include full response data for debugging
            }

            return jsonify({
                'items': items,
                'total_items': len(items),
                'total_found': total_found,
                'query': query,
                'debug': debug_info  # Include debug info in response
            })

        except requests.RequestException as e:
            error_msg = f"eBay API request failed: {str(e)}"
            print(f"\n=== Error ===\n{error_msg}\n=============\n")
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
        print(f"\n=== Error ===\n{error_msg}\n=============\n")
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

def find_available_port(start_port):
    """Find the next available port starting from start_port."""
    import socket
    port = start_port
    while port < 65535:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('127.0.0.1', port))
            s.close()
            return port
        except OSError:
            port += 1
    raise RuntimeError('No available ports found')

if __name__ == '__main__':
    try:
        print(f"\n🚀 Starting Flask server...")
        print(f"💻 Server URL: http://127.0.0.1:{PORT}")
        print(f"📝 API endpoints:")
        print(f"   - GET /api/search")
        print(f"   - GET /api/ebay-search\n")
        app.run(debug=True, port=PORT, host='127.0.0.1')
    except Exception as e:
        print(f"❌ Error starting server: {str(e)}") 