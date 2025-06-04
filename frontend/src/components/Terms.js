import React from 'react';
import './Terms.css';

const Terms = () => {
  return (
    <div className="terms-container">
      <h1>Terms and Conditions</h1>
      <div className="terms-content">
        <section className="terms-section">
          <h2>1. Acceptance of Terms</h2>
          <p>
            By accessing and using ThrifterFinder, you agree to be bound by these Terms and Conditions.
            If you do not agree to these terms, please do not use our service.
          </p>
        </section>

        <section className="terms-section">
          <h2>2. Description of Service</h2>
          <p>
            ThrifterFinder is a platform that helps users discover and analyze thrifted fashion items
            by providing real-time price data and market trends from various resale marketplaces.
          </p>
        </section>

        <section className="terms-section">
          <h2>3. User Responsibilities</h2>
          <p>
            Users are responsible for:
          </p>
          <ul>
            <li>Providing accurate information when using our services</li>
            <li>Maintaining the confidentiality of their account information</li>
            <li>Using the service in compliance with all applicable laws and regulations</li>
            <li>Not engaging in any activity that could harm or disrupt the service</li>
          </ul>
        </section>

        <section className="terms-section">
          <h2>4. Data and Privacy</h2>
          <p>
            We collect and process user data in accordance with our Privacy Policy.
            By using ThrifterFinder, you consent to such processing and warrant that all data provided by you is accurate.
          </p>
        </section>

        <section className="terms-section">
          <h2>5. Intellectual Property</h2>
          <p>
            All content, features, and functionality of ThrifterFinder are owned by us and are protected by
            international copyright, trademark, and other intellectual property laws.
          </p>
        </section>

        <section className="terms-section">
          <h2>6. Limitation of Liability</h2>
          <p>
            ThrifterFinder is provided "as is" without any warranties, expressed or implied.
            We are not liable for any damages arising from the use or inability to use our service.
          </p>
        </section>

        <section className="terms-section">
          <h2>7. Changes to Terms</h2>
          <p>
            We reserve the right to modify these terms at any time. Users will be notified of any changes,
            and continued use of the service constitutes acceptance of the modified terms.
          </p>
        </section>

        <section className="terms-section">
          <h2>8. Contact Information</h2>
          <p>
            For any questions regarding these Terms and Conditions, please contact us at:
            <br />
            Email: support@thrifterfinder.com
            <br />
            Phone: +1 (555) 123-4567
          </p>
        </section>
      </div>
    </div>
  );
};

export default Terms; 