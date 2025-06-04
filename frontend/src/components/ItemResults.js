import React, { useState, useEffect } from 'react';
import './ItemResults.css';

const CATEGORIES = [
  { id: 'all', label: 'All' },
  { id: 'jeans', label: 'Jeans' },
  { id: 'jackets', label: 'Jackets' },
  { id: 'shoes', label: 'Shoes' },
  { id: 'tshirts', label: 'T-Shirts' },
  { id: 'dresses', label: 'Dresses' },
  { id: 'accessories', label: 'Accessories' }
];

const ItemResults = ({ average_price, last_sold_price, net_profit, example_listings, chartData }) => {
  const [failedImages, setFailedImages] = useState(new Set());
  const [savedItems, setSavedItems] = useState(new Set());
  const [activeCategory, setActiveCategory] = useState('all');
  const [filteredListings, setFilteredListings] = useState(example_listings || []);
  const [imageLoadingStates, setImageLoadingStates] = useState({});

  useEffect(() => {
    const items = JSON.parse(localStorage.getItem('savedItems') || '[]');
    setSavedItems(new Set(items.map(item => item.id)));
  }, []);

  useEffect(() => {
    if (!example_listings) return;
    
    if (activeCategory === 'all') {
      setFilteredListings(example_listings);
    } else {
      setFilteredListings(example_listings.filter(item => 
        item.category?.toLowerCase() === activeCategory
      ));
    }
  }, [activeCategory, example_listings]);

  const handleImageError = (index) => {
    setFailedImages(prev => new Set([...prev, index]));
  };

  const handleImageLoad = (index) => {
    setImageLoadingStates(prev => ({
      ...prev,
      [index]: false
    }));
  };

  const getPlaceholderImage = (title) => {
    return `https://via.placeholder.com/300x200/f3f4f6/666666?text=${encodeURIComponent(title || 'No Image')}`;
  };

  const toggleSave = (item) => {
    const items = JSON.parse(localStorage.getItem('savedItems') || '[]');
    const itemWithId = { ...item, id: `${item.title}-${Date.now()}` };
    
    if (savedItems.has(itemWithId.id)) {
      const updatedItems = items.filter(savedItem => savedItem.id !== itemWithId.id);
      localStorage.setItem('savedItems', JSON.stringify(updatedItems));
      setSavedItems(prev => {
        const next = new Set(prev);
        next.delete(itemWithId.id);
        return next;
      });
    } else {
      const updatedItems = [...items, itemWithId];
      localStorage.setItem('savedItems', JSON.stringify(updatedItems));
      setSavedItems(prev => new Set([...prev, itemWithId.id]));
    }
  };

  return (
    <div className="item-results fade-in">
      <div className="price-summary">
        <div className="price-card slide-up">
          <h3>Average Price</h3>
          <p>${average_price?.toFixed(2)}</p>
        </div>
        <div className="price-card slide-up" style={{ animationDelay: '0.1s' }}>
          <h3>Last Sold</h3>
          <p>${last_sold_price?.toFixed(2)}</p>
        </div>
        <div className="price-card slide-up" style={{ animationDelay: '0.2s' }}>
          <h3>Net Profit</h3>
          <p>${net_profit?.toFixed(2)}</p>
        </div>
      </div>

      {filteredListings && filteredListings.length > 0 && (
        <div className="listings-container fade-in" style={{ animationDelay: '0.3s' }}>
          <div className="listings-header">
            <h3>Current Listings</h3>
            <div className="category-filters" role="tablist">
              {CATEGORIES.map((category, index) => (
                <button
                  key={category.id}
                  role="tab"
                  aria-selected={activeCategory === category.id}
                  className={`category-tag ${activeCategory === category.id ? 'active' : ''}`}
                  onClick={() => setActiveCategory(category.id)}
                  style={{ animationDelay: `${0.1 * index}s` }}
                >
                  {category.label}
                </button>
              ))}
            </div>
          </div>

          <div className="listings-grid">
            {filteredListings.map((item, index) => {
              const itemWithId = { ...item, id: `${item.title}-${Date.now()}-${index}` };
              const isSaved = savedItems.has(itemWithId.id);
              const isLoading = imageLoadingStates[index] !== false;

              return (
                <div 
                  key={itemWithId.id} 
                  className="listing-card slide-up"
                  style={{ animationDelay: `${0.4 + index * 0.1}s` }}
                >
                  <div className="listing-image-container">
                    <div className="listing-image-wrapper">
                      {isLoading && (
                        <div className="image-skeleton">
                          <div className="skeleton-shimmer"></div>
                        </div>
                      )}
                      <img 
                        src={failedImages.has(index) ? getPlaceholderImage(item.title) : (item.image || getPlaceholderImage(item.title))}
                        alt={item.title}
                        className={`listing-image ${isLoading ? 'loading' : ''}`}
                        onError={() => handleImageError(index)}
                        onLoad={() => handleImageLoad(index)}
                        loading="lazy"
                      />
                    </div>
                    <div className="listing-price-tag">
                      <span>${item.price?.toFixed(2)}</span>
                    </div>
                    <button 
                      className={`bookmark-button ${isSaved ? 'saved' : ''}`}
                      onClick={() => toggleSave(itemWithId)}
                      aria-label={isSaved ? 'Remove from saved items' : 'Save item'}
                    >
                      <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 21L12 16L5 21V5C5 4.46957 5.21071 3.96086 5.58579 3.58579C5.96086 3.21071 6.46957 3 7 3H17C17.5304 3 18.0391 3.21071 18.4142 3.58579C18.7893 3.96086 19 4.46957 19 5V21Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                      </svg>
                    </button>
                  </div>
                  <div className="listing-content">
                    <h4>{item.title}</h4>
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
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};

export default ItemResults; 