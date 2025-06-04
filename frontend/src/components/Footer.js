import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>ThrifterFinder</h3>
            <p>Discover the value of thrifted fashion with real-time market analysis.</p>
          </div>
          <div className="footer-section">
            <h4>Quick Links</h4>
            <Link to="/">Search</Link>
            <Link to="/live-listings">Live Listings</Link>
            <Link to="/about">About</Link>
            <Link to="/faq">FAQ</Link>
          </div>
          <div className="footer-section">
            <h4>Legal</h4>
            <Link to="/terms">Terms & Conditions</Link>
            <Link to="/privacy">Privacy Policy</Link>
          </div>
          <div className="footer-section">
            <h4>Contact</h4>
            <Link to="/contact">Contact Us</Link>
            <a href="mailto:support@thrifterfinder.com">support@thrifterfinder.com</a>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} ThrifterFinder. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 