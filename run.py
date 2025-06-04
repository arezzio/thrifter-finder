from app import app

if __name__ == '__main__':
    print("\n🚀 Starting Flask server...")
    print("💻 Server URL: http://127.0.0.1:3000")
    print("📝 API endpoints:")
    print("   - GET /api/search")
    print("   - GET /api/ebay-search\n")
    app.run(debug=True, port=3000, host='127.0.0.1') 