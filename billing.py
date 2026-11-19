class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


# Data Coupling: функція отримує тільки ті дані, які їй потрібні (місто і вагу)
def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    base_rate = 50.0 if city == "Ivano-Frankivsk" else 110.0
        return base_rate + (weight_kg * 15.0)


# Звичайний рахунок: ставка податку передається явно, за замовчуванням 20%
def process_standard_invoice(amount: float, city: str, weight_kg: float, tax_rate: float = 0.20) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


# Рахунок без податку: окрема функція замість прапорця mode_flag
def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    total = amount + calculate_delivery_cost(city, weight_kg)
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
