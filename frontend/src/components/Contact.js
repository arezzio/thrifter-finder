import React from 'react';
import './Contact.css';

const Contact = () => {
  return (
    <div className="contact">
      <h1>Contact Us</h1>
      <div className="contact-content">
        <section className="contact-info">
          <h2>Get in Touch</h2>
          <p>
            Have questions or feedback? We'd love to hear from you. Fill out the form
            below and we'll get back to you as soon as possible.
          </p>
          <div className="contact-details">
            <div className="contact-item">
              <h3>Email</h3>
              <p>support@thrifterfinder.com</p>
            </div>
            <div className="contact-item">
              <h3>Follow Us</h3>
              <div className="social-links">
                <a href="#" target="_blank" rel="noopener noreferrer">Twitter</a>
                <a href="#" target="_blank" rel="noopener noreferrer">Instagram</a>
                <a href="#" target="_blank" rel="noopener noreferrer">Facebook</a>
              </div>
            </div>
          </div>
        </section>

        <form className="contact-form">
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input type="text" id="name" name="name" required />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="email" id="email" name="email" required />
          </div>
          <div className="form-group">
            <label htmlFor="message">Message</label>
            <textarea id="message" name="message" rows="5" required></textarea>
          </div>
          <button type="submit" className="submit-button">
            Send Message
          </button>
        </form>
      </div>
    </div>
  );
};

export default Contact; 