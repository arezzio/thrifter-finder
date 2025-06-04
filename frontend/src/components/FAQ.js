import React from 'react';
import './FAQ.css';

const FAQ = () => {
  return (
    <div className="faq">
      <h1>Frequently Asked Questions</h1>
      <div className="faq-content">
        <section className="faq-section">
          <h2>How does ThrifterFinder work?</h2>
          <p>
            ThrifterFinder aggregates data from various marketplaces to provide real-time
            price analysis and market trends for thrifted items. Simply search for an item,
            and we'll show you current listings and market insights.
          </p>
        </section>

        <section className="faq-section">
          <h2>Is ThrifterFinder free to use?</h2>
          <p>
            Yes, ThrifterFinder is completely free to use. We believe in making thrift
            shopping more accessible and transparent for everyone.
          </p>
        </section>

        <section className="faq-section">
          <h2>How accurate are the price estimates?</h2>
          <p>
            Our price estimates are based on real-time data from various marketplaces.
            We continuously update our algorithms to provide the most accurate market
            insights possible.
          </p>
        </section>

        <section className="faq-section">
          <h2>Can I save items for later?</h2>
          <p>
            Yes! You can save interesting items to your account and track their price
            changes over time. This feature helps you make informed decisions about
            when to buy.
          </p>
        </section>
      </div>
    </div>
  );
};

export default FAQ; 