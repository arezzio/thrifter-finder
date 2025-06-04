import React, { useState, useEffect } from 'react';
import './SavedItems.css';

const SavedItems = () => {
  const [savedItems, setSavedItems] = useState([]);

  useEffect(() => {
    const items = JSON.parse(localStorage.getItem('savedItems') || '[]');
    setSavedItems(items);
  }, []);

  const removeFromSaved = (itemId) => {
    const updatedItems = savedItems.filter(item => item.id !== itemId);
    localStorage.setItem('savedItems', JSON.stringify(updatedItems));
    setSavedItems(updatedItems);
  };

  if (savedItems.length === 0) {
    return (
      <div className="saved-items-empty">
        <svg className="empty-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 21L12 16L5 21V5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V21Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
        <h2>No Saved Items</h2>
        <p>Items you save will appear here</p>
      </div>
    );
  }

  return (
    <div className="saved-items">
      <h1>Saved Items</h1>
      <div className="saved-items-grid">
        {savedItems.map((item) => (
          <div key={item.id} className="saved-item-card">
            <div className="saved-item-image-container">
              <div className="saved-item-image-wrapper">
                <img 
                  src={item.image || `https://via.placeholder.com/300x200/f3f4f6/666666?text=${encodeURIComponent(item.title)}`}
                  alt={item.title}
                  className="saved-item-image"
                />
              </div>
              <div className="saved-item-price-tag">
                <span>${item.price}</span>
              </div>
            </div>
            <div className="saved-item-content">
              <h4>{item.title}</h4>
              <div className="saved-item-actions">
                <a 
                  href={item.link} 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="view-button"
                >
                  View Listing
                </a>
                <button 
                  className="remove-button"
                  onClick={() => removeFromSaved(item.id)}
                  aria-label="Remove from saved items"
                >
                  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M19 21L12 16L5 21V5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V21Z" fill="currentColor"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SavedItems; 