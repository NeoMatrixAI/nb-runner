# nb-runner 🚀

[![NeoMatrix](https://img.shields.io/badge/Neomatrix-white)]([https://discord.com/invite/Xn26Q42DXD](https://neomatrix.ai))[![Website](https://img.shields.io/badge/Website-2319DC)](https://neomatrix.ai)
[![Invite-link](https://img.shields.io/badge/Discord-white)](https://discord.com/invite/Xn26Q42DXD)[![Discord](https://img.shields.io/badge/Invitation-2319DC)](https://discord.com/invite/Xn26Q42DXD)
---
[![English](https://img.shields.io/badge/docs-English-blue)](./README.md) [![한국어](https://img.shields.io/badge/docs-한국어-red)](./docs/README.ko.md)
[![简体中文](https://img.shields.io/badge/docs-简体中文-yellow)](./docs/README.zh-CN.md)
---
This repository is a notebook runner composed of `.ipynb` and `.py` files.

It is primarily designed to run in a local environment such as [**Google Colab**](https://colab.research.google.com).  
If you adjust the "Mount Google Drive" cell and specify your **personal path**, it can be easily adapted to other local environments as well.

To use the provided API functions, you must obtain a `data apikey` and `user key` from **NeoMatrix**.

You can run backtests and live trading using either:  
- your own custom strategies and configuration files, or  
- the regularly updated strategies and settings shared via the [strategy](https://github.com/NeoMatrixAI/strategy) repository.

### 📘 Notebook Usage Flow

#### 📂 Futures Trading (`notebooks/futures/`)

For **futures trading**, follow these steps in order:

1. **`1. download_sample.ipynb`**
   → Downloads sample strategy files and configurations from the [strategy repository](https://github.com/NeoMatrixAI/strategy) to your Google Drive.

2. **`2. futures_strategy_verify.ipynb`**
   → Validates your custom strategy locally using mock data before uploading to the server. Checks that the strategy returns proper weight dictionaries and ensures the sum of absolute weights does not exceed 1.

3. **`3. futures_backtest.ipynb`**
   → Uploads your strategy and config files to the NeoMatrix server, then runs a backtest. Generates performance metrics and an optional HTML report.

4. **`4. futures_trade.ipynb`**
   → Executes live auto-trading with your verified strategy. Includes session management, log monitoring, and forced liquidation utilities for safe termination.

---
### ❓ Support

For questions or support, please reach out via the [**NeoMatrix Discord**](https://discord.gg/Xn26Q42DXD)
