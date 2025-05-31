import requests
import random
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Static sustainability scores (since API doesn't provide these)
sustainability_scores = {
    "bitcoin": 3/10,
    "ethereum": 6/10,
    "cardano": 8/10
}

# Energy use simplified from your original data
energy_use = {
    "bitcoin": "high",
    "ethereum": "medium",
    "cardano": "low"
}

def fetch_live_crypto_data():
    # Fetch top 100 coins from CoinGecko (to get market cap and price change)
    url = "https://api.coingecko.com/api/v3/coins/markets"
    api_key = os.getenv("COINGECKO_API_KEY")
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,cardano',
        'order': 'market_cap_desc',
        'per_page': 3,
        'page': 1,
        'price_change_percentage': '24h'
    }
    if api_key:
        params['x_cg_demo_api_key'] = api_key
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"API Error: {e}")
        return None

def parse_price_trend(change_pct):
    # Simple logic: rising if +1% or more, stable if between -1% and +1%, falling otherwise
    if change_pct is None:
        return "stable"
    if change_pct >= 1:
        return "rising"
    elif change_pct <= -1:
        return "falling"
    else:
        return "stable"

def build_crypto_db_live():
    data = fetch_live_crypto_data()
    if data is None:
        # fallback to static data (like before)
        print("Using fallback static data due to API error.")
        return {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            }
        }
    crypto_db = {}
    for coin in data:
        name = coin["name"]
        price_change = coin.get("price_change_percentage_24h")
        price_trend = parse_price_trend(price_change)
        market_cap_rank = coin.get("market_cap_rank")
        # Simplify market cap into 'high' or 'medium' or 'low' by rank (just for demo)
        if market_cap_rank is None:
            market_cap = "medium"
        elif market_cap_rank <= 10:
            market_cap = "high"
        elif market_cap_rank <= 50:
            market_cap = "medium"
        else:
            market_cap = "low"
        key = name.lower()
        crypto_db[name] = {
            "price_trend": price_trend,
            "market_cap": market_cap,
            "energy_use": energy_use.get(key, "medium"),
            "sustainability_score": sustainability_scores.get(key, 5/10)
        }
    return crypto_db

def crypto_chatbot(user_query, crypto_db):
    user_query = user_query.lower()
    wisdom = [
        "Remember: 'Don’t put all your eggs in one blockchain.'",
        "Old but gold: 'Buy low, sell high.'",
        "Patience is a virtue, especially in crypto.",
        "Crypto's a rollercoaster. Buckle up before you buy."
    ]
    wisdom_quote = random.choice(wisdom)

    if "trending" in user_query or "price trend" in user_query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_coins:
            return f"Coins trending up right now: {', '.join(trending_coins)}. {wisdom_quote}"
        else:
            return "No coins are currently trending up. Maybe it's time for some old-school patience."

    elif "sustainable" in user_query or "eco" in user_query:
        sustainable_coins = [coin for coin, data in crypto_db.items()
                             if data["energy_use"] == "low" and data["sustainability_score"] > 0.7]
        if sustainable_coins:
            return f"Top sustainable coins: {', '.join(sustainable_coins)} 🌱. Long-term thinking pays off!"
        else:
            return "No coins meet the high sustainability criteria right now. Sustainability takes time."

    elif "long-term growth" in user_query or "buy" in user_query or "investment" in user_query:
        disclaimer = ("Heads up: Crypto is risky and volatile. "
                      "Always do your own research and never invest more than you can afford to lose.\n")

        profitable = [coin for coin, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] == "high"]

        if profitable:
            best_coin = max(profitable, key=lambda c: crypto_db[c]["sustainability_score"])
            advice = (f"{best_coin} is trending up and has a decent sustainability score! 🚀 "
                      f"{wisdom_quote}")
            return disclaimer + advice
        else:
            return disclaimer + "No top coins fit the criteria for long-term growth right now."

    else:
        return ("I'm CryptoBuddy! Ask me about crypto trends, sustainability, or investment advice.\n"
                "Type 'exit' to quit.")

def run_chatbot_live():
    print("Hey there! I’m CryptoBuddy, your no-nonsense crypto advisor bot with live data. Ask me anything about crypto!")
    crypto_db = build_crypto_db_live()
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("CryptoBuddy: Thanks for chatting! Stay sharp and trade smart. 👋")
            break
        response = crypto_chatbot(user_input, crypto_db)
        print(f"CryptoBuddy: {response}")

# Run this to launch your live-data chatbot
run_chatbot_live()
