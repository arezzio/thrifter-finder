import React, { useEffect, useState } from 'react';
import './LiveListings.css';

const DEFAULT_QUERY = 'jeans';
const API_BASE_URL = 'http://localhost:3001'; // Updated port to match Flask server

function LiveListings() {
  const [listings, setListings] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState(DEFAULT_QUERY);
  const [totalFound, setTotalFound] = useState(0);

  useEffect(() => {
    async function fetchListings() {
      setIsLoading(true);
      setError(null);
      try {
        const res = await fetch(`${API_BASE_URL}/api/ebay-search?query=${encodeURIComponent(searchQuery)}`);
        if (!res.ok) {
          const errorText = await res.text();
          throw new Error(`Failed to fetch listings: ${res.status} ${errorText}`);
        }
        const data = await res.json();
        if (data.error) {
          throw new Error(data.error);
        }
        setListings(Array.isArray(data.items) ? data.items : []);
        setTotalFound(data.total_found || 0);
      } catch (err) {
        console.error('Error fetching listings:', err);
        setError(err.message || 'Could not load live listings.');
      } finally {
        setIsLoading(false);
      }
    }
    fetchListings();
  }, [searchQuery]);

  const handleSearch = (e) => {
    e.preventDefault();
    const form = e.target;
    const query = form.search.value.trim();
    if (query) {
      setSearchQuery(query);
    }
  };

  if (isLoading) {
    return (
      <div className="live-listings-container">
        <div className="loading-state">
          <div className="spinner" />
          <p>Loading live listings...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="live-listings-container">
        <div className="error-state">
          <p>Error: {error}</p>
          <p className="error-details">Please make sure the backend server is running on port 3001</p>
        </div>
      </div>
    );
  }

  return (
    <div className="live-listings-container">
      <h1>Live Listings</h1>
      
      <form onSubmit={handleSearch} className="search-form">
        <input
          type="text"
          name="search"
          placeholder="Search for items..."
          defaultValue={searchQuery}
          className="search-input"
        />
        <button type="submit" className="search-button">
          Search
        </button>
      </form>

      {!listings.length ? (
        <div className="empty-state">
          <p>No listings found for "{searchQuery}"</p>
        </div>
      ) : (
        <>
          <div className="results-header">
            <p>Found {totalFound} results for "{searchQuery}"</p>
          </div>
          <div className="listings-grid">
            {listings.map((item) => (
              <div key={item.item_id || item.url} className="listing-card">
                <div className="listing-image-container">
                  <img
                    src={item.image || 'https://via.placeholder.com/300x300?text=No+Image'}
                    alt={item.title}
                    className="listing-image"
                    loading="lazy"
                  />
                  <div className="listing-price">
                    {item.price ? `$${item.price.toFixed(2)}` : 'N/A'}
                  </div>
                </div>
                <div className="listing-content">
                  <h3 className="truncate" title={item.title}>{item.title}</h3>
                  <div className="listing-details">
                    <p className="condition">{item.condition}</p>
                    <p className="seller">Seller: {item.seller}</p>
                    <p className="location">Location: {item.location}</p>
                  </div>
                  <a
                    href={item.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="view-button"
                  >
                    View on eBay
                  </a>
                </div>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default LiveListings; 