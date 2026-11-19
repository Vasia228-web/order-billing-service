# Release Notes

## v1.1.0

### Added
- Спеціальний базовий тариф доставки для Києва — 80.0.
- Явний параметр ставки податку `tax_rate` (за замовчуванням 0.20).

### Changed
- Коефіцієнт доставки за вагу збільшено з 12.0 до 15.0 за 1 кг.
- Модуль переведено на Data Coupling: функції отримують лише потрібні їм дані.

### Breaking Changes
- `calculate_delivery_cost(customer, weight_kg)` тепер `calculate_delivery_cost(city, weight_kg)`: замість об'єкта `CustomerProfile` передається назва міста.
- Функцію `process_invoice(..., mode_flag)` видалено. Замість неї — `process_standard_invoice(amount, city, weight_kg, tax_rate=0.20)` і `process_tax_exempt_invoice(amount, city, weight_kg)`.
- Глобальну змінну `GLOBAL_TAX_RATE` видалено.
- Статус `CANCELLED` більше не повертається.
