# Production Planning
 Python code to solve production planning exercises as described in "Inventory Management - Mathematical models and their application" by L.Tiacci

# Forecasting & Inventory Tools

This project includes simple Python functions for:

- 📈 **Time series forecasting**
- 📦 **Inventory optimization with safety stock**

---

## Forecasting Methods

- **Linear Regression**
- **Moving Averages**
- **Brown’s Method**
- **Holt’s Method**
- **Winters’ Method** (seasonal)

### Example Usage

```python
Brown_method(data, a=0.3, N=3, init=5)
Holt_method(data, n=5, alpha=0.5, beta=0.3)
static_method(data, p=4)

