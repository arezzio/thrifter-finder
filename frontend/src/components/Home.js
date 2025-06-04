import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    setIsLoading(true);
    try {
      // Here you would typically make an API call to search for items
      // For now, we'll just navigate to the live listings page
      navigate('/live-listings');
    } catch (error) {
      console.error('Error searching:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-content">
          <h1>Discover the Value of Thrifted Fashion</h1>
          <p>Get real-time price analysis and market trends for thrifted items</p>
          <form className="search-form" onSubmit={handleSearch}>
            <div className="search-input-wrapper">
              <input
                type="text"
                placeholder="Search for items..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className={isLoading ? 'loading' : ''}
              />
              {isLoading && (
                <div className="search-spinner">
                  <div className="spinner"></div>
                </div>
              )}
            </div>
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Searching...' : 'Search'}
            </button>
          </form>
        </div>
      </section>

      <section className="features">
        <h2>Why Choose ThrifterFinder?</h2>
        <div className="features-grid">
          <div className="feature-card">
            <h3>Real-Time Analysis</h3>
            <p>Get instant price comparisons and market trends for thrifted items.</p>
          </div>
          <div className="feature-card">
            <h3>Live Listings</h3>
            <p>Browse current listings from major marketplaces in one place.</p>
          </div>
          <div className="feature-card">
            <h3>Save & Track</h3>
            <p>Save interesting items and track their price changes over time.</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home; 