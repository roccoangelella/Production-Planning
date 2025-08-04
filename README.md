# Production Planning
 Python code to solve production planning exercises as described in "Inventory Management - Mathematical models and their application" by L.Tiacci

Forecasting & Inventory Tools

This project includes simple Python functions for:

    📈 Time series forecasting

    📦 Inventory optimization with safety stock

Forecasting Methods

    Linear Regression

    Moving Averages

    Brown’s Method

    Holt’s Method

    Winters’ Method (seasonal)

Example Usage

Brown_method(data, a=0.3, N=3, init=5)
Holt_method(data, n=5, alpha=0.5, beta=0.3)
static_method(data, p=4)

Inventory Optimization

Calculate safety stock using different service-level criteria.
Example Usage

items = [{'Dt': 1200, 'v': 10, 'sigma': 35}]
criteria = [0, 0.03, 0, 0, 0, 0]  # Using B2
R = 0.083
r = 0.12
L = 0.04

other_constraint_solver(items, criteria, R, r, L, constraint=1200)

Requirements

    Python 3

    No external libraries

Notes

    All methods use standard Python only

    Criteria format: [B1, B2, B3, P1, P2, TBS]
