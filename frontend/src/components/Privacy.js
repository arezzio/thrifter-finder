import React from 'react';
import './Privacy.css';

const Privacy = () => {
  return (
    <div className="privacy-container">
      <h1>Privacy Policy</h1>
      <div className="privacy-content">
        <section className="privacy-section">
          <h2>1. Information We Collect</h2>
          <p>
            We collect information that you provide directly to us, including:
          </p>
          <ul>
            <li>Name and contact information</li>
            <li>Account credentials</li>
            <li>Search history and preferences</li>
            <li>Communication with our support team</li>
          </ul>
        </section>

        <section className="privacy-section">
          <h2>2. How We Use Your Information</h2>
          <p>
            We use the collected information to:
          </p>
          <ul>
            <li>Provide and improve our services</li>
            <li>Personalize your experience</li>
            <li>Communicate with you about our services</li>
            <li>Analyze and enhance our platform</li>
          </ul>
        </section>

        <section className="privacy-section">
          <h2>3. Information Sharing</h2>
          <p>
            We do not sell your personal information. We may share your information with:
          </p>
          <ul>
            <li>Service providers who assist in our operations</li>
            <li>Legal authorities when required by law</li>
            <li>Third parties with your consent</li>
          </ul>
        </section>

        <section className="privacy-section">
          <h2>4. Data Security</h2>
          <p>
            We implement appropriate security measures to protect your personal information.
            However, no method of transmission over the internet is 100% secure.
          </p>
        </section>

        <section className="privacy-section">
          <h2>5. Your Rights</h2>
          <p>
            You have the right to:
          </p>
          <ul>
            <li>Access your personal information</li>
            <li>Correct inaccurate data</li>
            <li>Request deletion of your data</li>
            <li>Opt-out of marketing communications</li>
          </ul>
        </section>

        <section className="privacy-section">
          <h2>6. Cookies and Tracking</h2>
          <p>
            We use cookies and similar tracking technologies to improve your experience.
            You can control cookie preferences through your browser settings.
          </p>
        </section>

        <section className="privacy-section">
          <h2>7. Changes to Privacy Policy</h2>
          <p>
            We may update this privacy policy from time to time. We will notify you of any changes
            by posting the new policy on this page.
          </p>
        </section>

        <section className="privacy-section">
          <h2>8. Contact Us</h2>
          <p>
            If you have any questions about this Privacy Policy, please contact us at:
            <br />
            Email: privacy@thrifterfinder.com
            <br />
            Phone: +1 (555) 123-4567
          </p>
        </section>
      </div>
    </div>
  );
};

export default Privacy; 