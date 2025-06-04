import React, { useState, useEffect } from 'react';
import './SavedItems.css';

const SavedItems = () => {
  const [savedItems, setSavedItems] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadSavedItems = () => {
      try {
        const items = JSON.parse(localStorage.getItem('savedItems') || '[]');
        setSavedItems(items);
      } catch (error) {
        console.error('Error loading saved items:', error);
      } finally {
        setIsLoading(false);
      }
    };

    loadSavedItems();
  }, []);

  const removeItem = (itemId) => {
    try {
      const updatedItems = savedItems.filter(item => item.id !== itemId);
      localStorage.setItem('savedItems', JSON.stringify(updatedItems));
      setSavedItems(updatedItems);
    } catch (error) {
      console.error('Error removing item:', error);
    }
  };

  if (isLoading) {
    return (
      <div className="saved-items-container">
        <div className="loading-state">
          <div className="spinner"></div>
          <p>Loading saved items...</p>
        </div>
      </div>
    );
  }

  if (savedItems.length === 0) {
    return (
      <div className="saved-items-container">
        <div className="empty-state">
          <h2>No Saved Items</h2>
          <p>Items you save will appear here.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="saved-items-container">
      <h1>Saved Items</h1>
      <div className="saved-items-grid">
        {savedItems.map((item) => (
          <div key={item.id} className="saved-item-card">
            <div className="saved-item-image-container">
              <img 
                src={item.image || `https://via.placeholder.com/300x200/f3f4f6/666666?text=${encodeURIComponent(item.title || 'No Image')}`}
                alt={item.title}
                className="saved-item-image"
                loading="lazy"
              />
              <div className="saved-item-price">
                ${item.price?.toFixed(2)}
              </div>
              <button 
                className="remove-button"
                onClick={() => removeItem(item.id)}
                aria-label="Remove item"
              >
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M6 18L18 6M6 6L18 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
            </div>
            <div className="saved-item-content">
              <h3>{item.title}</h3>
              <a 
                href={item.url} 
                target="_blank" 
                rel="noopener noreferrer"
                className="view-button"
              >
                View Listing
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SavedItems; 