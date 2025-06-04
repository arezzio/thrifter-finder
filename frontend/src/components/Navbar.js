import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-brand">
          ThrifterFinder
        </Link>
        <div className="navbar-links">
          <Link 
            to="/" 
            className={`navbar-link ${isActive('/') ? 'active' : ''}`}
          >
            Search
          </Link>
          <Link 
            to="/live-listings" 
            className={`navbar-link ${isActive('/live-listings') ? 'active' : ''}`}
          >
            Live Listings
          </Link>
          <Link 
            to="/about" 
            className={`navbar-link ${isActive('/about') ? 'active' : ''}`}
          >
            About
          </Link>
          <Link 
            to="/faq" 
            className={`navbar-link ${isActive('/faq') ? 'active' : ''}`}
          >
            FAQ
          </Link>
          <Link 
            to="/contact" 
            className={`navbar-link ${isActive('/contact') ? 'active' : ''}`}
          >
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 