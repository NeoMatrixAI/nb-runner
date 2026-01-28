# nb-runner

[![Discord](https://img.shields.io/badge/Discord-2319DC)](https://discord.com/invite/Xn26Q42DXD)[![NeoMatrix](https://img.shields.io/badge/Neomatrix-white)](https://neomatrix.ai)
---
[![English](https://img.shields.io/badge/docs-English-blue)](./README.md) [![한국어](https://img.shields.io/badge/docs-한국어-red)](./docs/README.ko.md)
[![简体中文](https://img.shields.io/badge/docs-简体中文-yellow)](./docs/README.zh-CN.md)
---

This repository is a notebook runner composed of `.ipynb` and `.py` files, designed primarily for [**Google Colab**](https://colab.research.google.com).

To use the provided API functions, you must obtain a `user key` from **NeoMatrix**.

You can run backtests and live trading using either:
- your own custom strategies and configuration files, or
- the regularly updated strategies and settings shared via the [strategy](https://github.com/NeoMatrixAI/strategy) repository.

---

### 📁 Structure

```
nb-runner/
├── notebooks/
│   └── futures/                              # Futures trading notebooks (execute in order 1→4)
│       ├── 1. download_sample.ipynb          # Download sample strategies from strategy repo
│       ├── 2. futures_strategy_verify.ipynb  # Validate strategy locally with mock data
│       ├── 3. futures_backtest.ipynb         # Run backtest on NeoMatrix server
│       └── 4. futures_trade.ipynb            # Execute live auto-trading
├── module/
│   ├── futures/                              # Futures trading API modules
│   │   ├── account.py                        # Account balance operations
│   │   ├── market.py                         # Market data fetching
│   │   ├── position.py                       # Position management
│   │   └── trade.py                          # Trade execution
│   └── spot/                                 # Spot trading API modules (same structure)
└── docs/                                     # Multi-language documentation
```

---

### 📦 How to Use

1. Clone or download this repository
2. Open notebooks in Google Colab (or adjust paths for local environment)
3. Mount Google Drive and set your personal path
4. Follow the notebook execution order:
   - **`1. download_sample.ipynb`** → Download sample strategy files
   - **`2. futures_strategy_verify.ipynb`** → Validate strategy locally
   - **`3. futures_backtest.ipynb`** → Run backtest on server
   - **`4. futures_trade.ipynb`** → Execute live trading

Make sure you are also using the [strategy](https://github.com/NeoMatrixAI/strategy) repository, which contains the strategy modules and configuration files.

---

### ❓ Support

For questions or support, please reach out via the [**NeoMatrix Discord**](https://discord.gg/Xn26Q42DXD)
