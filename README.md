# Production Planning
 Python code to solve production planning exercises as described in "Inventory Management - Mathematical models and their application" by L.Tiacci

    📈 Forecasting Methods

        Linear Regression

        Moving Averages (single & double)

        Brown’s Exponential Smoothing

        Holt’s Linear Method

        Winters’ Multiplicative Method

    📦 Inventory Optimization

        Multi-item safety stock k calculation using service-level constraints

        Constraint checking and iterative tuning (e.g., using B1 for budget)

Requirements

This project uses only the Python standard library — no external dependencies are required.
How to Use
Forecasting Examples

# Example datasets
Dt_brown = [130,104,122,143,107,133,125,139,183,172,168,182]
Dt_holt = [97,118,107,145,141,128,135,216,245,360,400,460]
Dt_static = [4000,6500,11500,17000,5000,9000,11500,19000,6000,6500,16000,20500]

# Brown method
Brown_method(Dt_brown, a=0.3, N=3, init=5)

# Holt method
Holt_method(Dt_holt, n=5, alpha=0.5, beta=0.3)

# Static method (seasonal decomposition)
static_method(Dt_static, p=4)

Inventory Safety Stock Calculation

items = [
    {'Dt': 1200, 'v': 10, 'sigma': 35},
    {'Dt': 350,  'v': 35, 'sigma': 50},
    {'Dt': 700,  'v': 17, 'sigma': 40}
]

# Set constraints and service level criteria
R = 0.083
r = 0.12
L = 0.04
criteria = [0, 0.03, 0, 0, 0, 0]  # Using B2

# Solve with other constraints (manual k input needed)
other_constraint_solver(items, criteria, R, r, L, constraint=1200)

Functions Overview

    linear_regression(x, y)
    Computes slope and intercept for linear trends.

    moving_average(values, p)
    Simple moving average over period p.

    static_method(Dt, p)
    Decomposes time series into trend and seasonality.

    Brown_method(Dt, a, N, init)
    Applies Brown's single exponential smoothing.

    Holt_method(data, n, alpha, beta)
    Applies Holt’s linear trend method.

    Winters_method(data_init, data_forecast, p, alpha, beta, gamma)
    Forecasts seasonal time series using Winters’ method.

    multi_item_k_finder(...)
    Calculates safety stock factor k for multiple items based on criteria.

    multi_item_constraint(...)
    Verifies if total safety stock cost meets constraints.

    B1_constraint_solver(...)
    Iteratively tunes B1 to meet budget constraint.

    other_constraint_solver(...)
    Helper for non-B1 service-level scenarios.

License

This project is provided as-is without warranty. You may use and modify it freely for academic or professional use.
