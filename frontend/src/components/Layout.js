import React from 'react';
import './Layout.css';
import DarkModeToggle from './DarkModeToggle';

const Layout = ({ children, onNavigate, currentPage }) => {
  return (
    <div className="layout">
      <nav className="top-nav">
        <div className="nav-content">
          <div 
            className="nav-brand" 
            onClick={() => onNavigate('home')} 
            role="button" 
            tabIndex={0}
            aria-label="Go to home page"
          >
            <span className="brand-text">ThrifterFinder</span>
          </div>
          <div className="nav-right">
            <div className="nav-links">
              <button 
                className={`nav-link ${currentPage === 'home' ? 'active' : ''}`}
                onClick={() => onNavigate('home')}
                aria-current={currentPage === 'home' ? 'page' : undefined}
              >
                Search
              </button>
              <button 
                className={`nav-link ${currentPage === 'live' ? 'active' : ''}`}
                onClick={() => onNavigate('live')}
                aria-current={currentPage === 'live' ? 'page' : undefined}
              >
                Live Listings
              </button>
              <button 
                className={`nav-link ${currentPage === 'saved' ? 'active' : ''}`}
                onClick={() => onNavigate('saved')}
                aria-current={currentPage === 'saved' ? 'page' : undefined}
              >
                Saved
              </button>
              <button 
                className={`nav-link ${currentPage === 'about' ? 'active' : ''}`}
                onClick={() => onNavigate('about')}
                aria-current={currentPage === 'about' ? 'page' : undefined}
              >
                About
              </button>
              <button 
                className={`nav-link ${currentPage === 'faq' ? 'active' : ''}`}
                onClick={() => onNavigate('faq')}
                aria-current={currentPage === 'faq' ? 'page' : undefined}
              >
                FAQ
              </button>
            </div>
            <DarkModeToggle />
          </div>
        </div>
      </nav>
      <main className="main-content">
        {children}
      </main>
      <footer className="footer">
        <p>© 2024 ThrifterFinder. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Layout; 