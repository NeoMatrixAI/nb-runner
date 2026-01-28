# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/claude-code) when working with code in this repository.

## Project Overview

**nb-runner** is a notebook runner for cryptocurrency trading strategies, designed primarily for Google Colab. It provides tools for backtesting and live trading on Binance futures markets using the NeoMatrix API.

## Repository Structure

```
nb-runner/
├── notebooks/
│   └── futures/           # Futures trading notebooks (execute in order 1→4)
│       ├── 1. download_sample.ipynb    # Download sample strategies
│       ├── 2. futures_strategy_verify.ipynb  # Validate strategy locally
│       ├── 3. futures_backtest.ipynb   # Run backtest on server
│       └── 4. futures_trade.ipynb      # Execute live auto-trading
├── module/
│   ├── futures/           # Futures trading modules
│   │   ├── account.py     # Account balance operations
│   │   ├── market.py      # Market data fetching
│   │   ├── position.py    # Position management
│   │   └── trade.py       # Trade execution
│   └── spot/              # Spot trading modules (same structure)
└── docs/                  # Multi-language documentation
```

## Key Concepts

### Strategy Format
Strategies must return a dictionary in this format:
```python
{
    "SYMBOL": {
        "weight": float,              # Position weight (-1 to 1)
        "presetStopLossPrice": float, # Stop loss price
        "presetStopSurplusPrice": float  # Take profit price
    }
}
```
- Sum of absolute weights must not exceed 1

### API Keys Required
- `USER_KEY`: User authentication key from NeoMatrix
- `DATA_KEY`: Data API key (fixed value provided in notebooks)

### Trading Flow
1. **Verify** strategy locally with mock data
2. **Upload** strategy and config to NeoMatrix server
3. **Backtest** to validate performance
4. **Trade** live with session management

## Development Notes

- Notebooks are designed for Google Colab but can work locally with path adjustments
- All API interactions go through `https://aifapbt.fin.cloud.ainode.ai/` (trade) or `https://zipline.fin.cloud.ainode.ai/` (backtest)
- Strategy files are loaded from Google Drive path: `/content/drive/MyDrive/NeoMatrixAI/`

## Important Rules

### Documentation Sync
**When modifying `README.md`, you MUST also update the translated versions in `docs/`:**
- `docs/README.ko.md` (Korean)
- `docs/README.zh-CN.md` (Simplified Chinese)

All documentation files must stay synchronized.

## Common Commands

```bash
# Check module structure
ls module/futures/

# View notebook content
cat "notebooks/futures/1. download_sample.ipynb" | python -m json.tool
```
