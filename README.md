# CryptoBuddy: Your First AI-Powered Financial Sidekick! 🌟

## Overview

**CryptoBuddy** is a beginner-friendly, rule-based chatbot that delivers cryptocurrency investment insights using real-time data from the CoinGecko API. It helps users understand both the **profitability** (via price trends and market cap) and **sustainability** (via energy usage and custom scores) of popular cryptocurrencies. CryptoBuddy is designed for newcomers to both AI and crypto, making complex data simple and actionable.

---

## Features

- 📈 **Live Crypto Analysis:** Fetches and analyzes real-time price trends and market data using the CoinGecko API.
- 🌱 **Sustainability Insights:** Evaluates coins based on energy usage and custom sustainability scores.
- 🤖 **Rule-Based Engine:** No machine learning required—decisions are made using clear, transparent rules.
- 💡 **Crypto Wisdom:** Offers motivational tips and classic investment advice.
- 🛡️ **Reliable Fallback:** Automatically uses static data if the API is unavailable.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/cryptobuddy.git
   cd cryptobuddy
   ```

2. **(Optional) Create a virtual environment:**
   ```sh
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install requests
   ```

4. **Run the chatbot:**
   ```sh
   python crypto_buddy.py
   ```

---

## Usage

1. **Start the chatbot** by running the script as shown above.
2. **Ask CryptoBuddy questions like:**
   - "Which cryptos are trending?"
   - "Tell me about sustainable coins."
   - "What’s a good long-term investment?"
3. **Type `exit` to quit the session.**

CryptoBuddy will respond with up-to-date insights, sustainability tips, and motivational wisdom!

---

## How It Works

- **Live Data:** CryptoBuddy fetches real-time data for selected cryptocurrencies (Bitcoin, Ethereum, Cardano) from CoinGecko.
- **Rule-Based Logic:** It applies simple rules to determine which coins are trending, sustainable, or suitable for long-term investment.
- **Fallback Mode:** If the API is unreachable, CryptoBuddy uses static sample data to ensure uninterrupted advice.

---

## Contributing

We welcome contributions!

1. **Fork the repository** on GitHub.
2. **Create a new feature branch:**
   ```sh
   git checkout -b feature-name
   ```
3. **Commit your changes:**
   ```sh
   git commit -m "Describe your changes"
   ```
4. **Push and open a Pull Request:**
   ```sh
   git push origin feature-name
   ```

Please include clear descriptions and, if possible, tests for new features.

---

## Disclaimer

CryptoBuddy is for educational and informational purposes only. Cryptocurrency investments are risky and volatile. Always do your own research and never invest more than you can afford to lose.

---

**Enjoy your journey into crypto with CryptoBuddy! 🚀**
