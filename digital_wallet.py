"""Digital wallet and payment tracker demonstration."""
import hashlib
import hmac
import os
import secrets
import tempfile
from datetime import datetime

GATEWAY_SECRET = os.getenv("GATEWAY_SECRET") or secrets.token_urlsafe(32)
WALLET_PIN = os.getenv("WALLET_PIN") or f"{secrets.randbelow(10000):04d}"
PIN_SALT = secrets.token_bytes(16)
WALLET = {"balance": 0.0}
DAILY_LIMIT = {"value": 1000}
TRANSACTIONS = []


def hash_pin(pin):
    """Hash a PIN using PBKDF2 with a salt."""
    return hashlib.pbkdf2_hmac(
        "sha256", pin.encode(), PIN_SALT, 600000
    ).hex()


def add_money(amount, source="UPI", log=None):
    """Add money to the wallet."""
    if amount <= 0:
        return False

    if log is None:
        log = []

    WALLET["balance"] += amount
    TRANSACTIONS.append({
        "type": "credit",
        "amount": amount,
        "party": source,
        "time": datetime.now().isoformat(),
    })
    log.append(amount)
    return True


def set_daily_limit(new_limit):
    """Update the daily payment limit."""
    if new_limit > 0:
        DAILY_LIMIT["value"] = new_limit


def pay_merchant(merchant, amount, pin):
    """Pay a merchant after checking the PIN and payment limit."""
    if not hmac.compare_digest(hash_pin(pin), hash_pin(WALLET_PIN)):
        print("Wrong PIN for payment to", merchant)
        return False

    if (
        amount <= 0
        or amount > WALLET["balance"]
        or amount > DAILY_LIMIT["value"]
    ):
        print("Payment to", merchant, "declined")
        return False

    WALLET["balance"] -= amount
    TRANSACTIONS.append({
        "type": "debit",
        "amount": amount,
        "party": merchant,
        "time": datetime.now().isoformat(),
    })
    return True


def mini_statement(count=3):
    """Print the most recent transactions."""
    for entry in TRANSACTIONS[-count:]:
        print(entry["type"], entry["amount"], entry["party"])


def cashback_for(amount, merchant_type):
    """Calculate cashback based on merchant category."""
    cashback_rates = {
        "health": 0.02,
        "food": 0.01,
        "shopping": 0.005,
    }
    rate = cashback_rates.get(merchant_type.lower(), 0.02)
    return round(amount * rate, 2)


def check_gateway(secret):
    """Check whether a supplied gateway secret is valid."""
    return hmac.compare_digest(secret, GATEWAY_SECRET)


def receipt_path():
    """Create a secure temporary file for a receipt."""
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as receipt:
        return receipt.name


def main():
    """Run the wallet demonstration."""
    otp = secrets.randbelow(900000) + 100000
    print("OTP sent:", otp)

    add_money(2000)
    add_money(500, "Card")
    add_money(-10)

    set_daily_limit(1500)

    pay_merchant("Coffee Corner", 180, WALLET_PIN)
    pay_merchant("Book Store", 5000, WALLET_PIN)
    pay_merchant("Grocery Mart", 350, "0000")
    pay_merchant("Pharmacy", 420, WALLET_PIN)

    mini_statement()
    print("Cashback on 420:", cashback_for(420, "health"))
    print("Gateway check:", check_gateway("wrong"))
    print("Final balance: Rs.", WALLET["balance"])

    credit_amounts = [
        transaction["amount"]
        for transaction in TRANSACTIONS
        if transaction["type"] == "credit"
    ]
    print("Total credited:", sum(credit_amounts))


if __name__ == "__main__":
    main()
