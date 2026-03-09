"""
data/faqs.py — FAQ Database
=============================
Add, remove, or edit FAQ entries here.
Each entry requires: id, topic, question, answer.
"""

FAQ_DB = [
    {
        "id": 1,
        "topic": "Account",
        "question": "How do I reset my password?",
        "answer": "To reset your password, click 'Forgot Password' on the login page. You'll receive an email with a secure reset link valid for 30 minutes. Enter your new password (min. 8 characters with at least one number and symbol), and you're good to go!"
    },
    {
        "id": 2,
        "topic": "Account",
        "question": "How can I change my email address?",
        "answer": "Go to Settings → Profile → Contact Info → Edit Email. Enter your new email and confirm via a verification link sent to the new address. Note: you can only change your email once every 30 days."
    },
    {
        "id": 3,
        "topic": "Account",
        "question": "How do I delete my account?",
        "answer": "Account deletion is permanent. Go to Settings → Privacy → Delete Account. You'll be asked to confirm via email. All your data will be permanently erased within 30 days per our GDPR compliance policy."
    },
    {
        "id": 4,
        "topic": "Billing",
        "question": "What payment methods do you accept?",
        "answer": "We accept all major credit/debit cards (Visa, Mastercard, Amex), PayPal, Apple Pay, Google Pay, and bank transfers for annual plans. All payments are processed securely via Stripe and are PCI-DSS compliant."
    },
    {
        "id": 5,
        "topic": "Billing",
        "question": "How do I cancel my subscription?",
        "answer": "You can cancel anytime from Settings → Billing → Manage Subscription → Cancel Plan. You retain access until the end of your billing period. No partial refunds, but you won't be charged again after cancellation."
    },
    {
        "id": 6,
        "topic": "Billing",
        "question": "Can I get a refund?",
        "answer": "We offer a 14-day money-back guarantee for new subscriptions. Contact support@smarthelp.io with your order ID within this window. Refunds are processed within 5–7 business days to your original payment method."
    },
    {
        "id": 7,
        "topic": "Billing",
        "question": "How do I upgrade or downgrade my plan?",
        "answer": "Navigate to Settings → Billing → Change Plan. Upgrades are prorated — you only pay the difference for remaining days. Downgrades take effect at the next billing date. Enterprise plans require contacting sales."
    },
    {
        "id": 8,
        "topic": "Security",
        "question": "Is my data secure and private?",
        "answer": "Absolutely. We use AES-256 encryption at rest and TLS 1.3 in transit. We are SOC 2 Type II certified and GDPR compliant. We never sell your data. Export or delete all your data anytime from Settings → Privacy."
    },
    {
        "id": 9,
        "topic": "Security",
        "question": "Do you offer two-factor authentication?",
        "answer": "Yes! Enable 2FA from Settings → Security → Two-Factor Authentication. We support authenticator apps (Google Authenticator, Authy) and SMS codes. We recommend authenticator apps for better security."
    },
    {
        "id": 10,
        "topic": "Support",
        "question": "How do I contact support?",
        "answer": "Reach our support team via: Live Chat (bottom-right, 9am–6pm EST Mon–Fri), Email at support@smarthelp.io (response within 24h), or Community Forum at community.smarthelp.io. Pro users get <2h priority response."
    },
    {
        "id": 11,
        "topic": "Support",
        "question": "What are your support hours?",
        "answer": "Live support is available Monday–Friday, 9:00 AM – 6:00 PM Eastern Time. Email support is monitored 7 days a week. Our AI assistant is available 24/7 to answer common questions instantly."
    },
    {
        "id": 12,
        "topic": "Getting Started",
        "question": "How do I install the app?",
        "answer": "SmartHelp is available on iOS (App Store), Android (Google Play), macOS, and Windows. Visit smarthelp.io/download. You can also use the web app at app.smarthelp.io — no installation needed!"
    },
    {
        "id": 13,
        "topic": "Getting Started",
        "question": "What are the system requirements?",
        "answer": "Web App: Chrome 90+, Firefox 88+, Safari 14+, or Edge 90+. Desktop: Windows 10+ or macOS 11+, 4GB RAM, 2GB storage. Mobile: iOS 14+ or Android 8+. A stable internet connection is recommended."
    },
    {
        "id": 14,
        "topic": "Teams",
        "question": "How many users can I add to my team?",
        "answer": "Starter: up to 5 users. Professional: up to 25 users. Enterprise: unlimited users. Invite members from Settings → Team → Invite Members. Admins can set role-based permissions for each member."
    },
    {
        "id": 15,
        "topic": "Integrations",
        "question": "Can I integrate with third-party tools?",
        "answer": "Yes! We integrate with 50+ tools including Slack, Notion, Jira, Google Workspace, Microsoft 365, Zapier, GitHub, and Salesforce. Browse our marketplace at smarthelp.io/integrations."
    },
    {
        "id": 16,
        "topic": "Security",
        "question": "How do I export my data?",
        "answer": "Go to Settings → Privacy → Export Data. Export everything as a ZIP archive with JSON and CSV files. Large exports may take up to 24 hours — we'll email you when ready. Includes all content, settings, and activity."
    },
    {
        "id": 17,
        "topic": "Getting Started",
        "question": "How do I get started with SmartHelp?",
        "answer": "Sign up at smarthelp.io/signup for a free 14-day trial — no credit card required. After registration, follow our interactive onboarding wizard. Check our Quick Start Guide at docs.smarthelp.io for step-by-step tutorials."
    },
    {
        "id": 18,
        "topic": "Billing",
        "question": "How much does SmartHelp cost?",
        "answer": "Plans start at $9/month (Starter), $29/month (Professional), and custom pricing for Enterprise. Annual billing saves 20%. All plans include a 14-day free trial. Visit smarthelp.io/pricing for full details."
    },
]