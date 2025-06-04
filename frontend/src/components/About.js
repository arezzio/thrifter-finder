import React from 'react';
import './About.css';

const About = () => {
  return (
    <div className="about">
      <h1>About ThrifterFinder</h1>
      <div className="about-content">
        <section className="about-section">
          <h2>Our Mission</h2>
          <p>
            ThrifterFinder helps you discover the true value of thrifted items by providing
            real-time price analysis and market trends. We believe in making thrift shopping
            more transparent and rewarding.
          </p>
        </section>
        
        <section className="about-section">
          <h2>How It Works</h2>
          <p>
            Our platform aggregates data from various marketplaces to give you accurate
            price comparisons and market insights. Simply search for an item, and we'll
            show you current listings, price trends, and market analysis.
          </p>
        </section>
        
        <section className="about-section">
          <h2>Why Choose Us</h2>
          <ul>
            <li>Real-time price analysis</li>
            <li>Comprehensive market data</li>
            <li>User-friendly interface</li>
            <li>Save and track items</li>
          </ul>
        </section>
      </div>
    </div>
  );
};

export default About; 