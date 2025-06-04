import React from 'react';
import './LoadingSkeleton.css';

const LoadingSkeleton = () => {
  return (
    <div className="loading-skeleton animate-pulse">
      <div className="skeleton-cards">
        {[1, 2, 3].map((i) => (
          <div key={i} className="skeleton-card">
            <div className="skeleton-line h-8 w-1/3 mb-4"></div>
            <div className="skeleton-line h-6 w-1/2 mb-2"></div>
          </div>
        ))}
      </div>
      
      <div className="skeleton-listings">
        <div className="skeleton-line h-8 w-1/4 mb-6"></div>
        <div className="skeleton-grid">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="skeleton-listing">
              <div className="skeleton-image"></div>
              <div className="skeleton-content">
                <div className="skeleton-line h-5 w-3/4 mb-2"></div>
                <div className="skeleton-line h-6 w-1/3 mb-3"></div>
                <div className="skeleton-line h-8 w-1/2"></div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default LoadingSkeleton; 