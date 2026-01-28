# nb-runner

[![Discord](https://img.shields.io/badge/Discord-2319DC)](https://discord.com/invite/Xn26Q42DXD)[![NeoMatrix](https://img.shields.io/badge/Neomatrix-white)](https://neomatrix.ai)
---
[![English](https://img.shields.io/badge/docs-English-blue)](../README.md) [![한국어](https://img.shields.io/badge/docs-한국어-red)](./README.ko.md)
[![简体中文](https://img.shields.io/badge/docs-简体中文-yellow)](./README.zh-CN.md)
---

本仓库是由 `.ipynb` 和 `.py` 文件组成的笔记本运行工具，主要设计用于 [**Google Colab**](https://colab.research.google.com)。

要使用提供的 API 功能，您必须从 **NeoMatrix** 获取 `user key`。

您可以通过以下两种方式运行回测和实时交易：
- 使用您自定义的策略和配置文件
- 使用通过 [strategy](https://github.com/NeoMatrixAI/strategy) 仓库定期更新的策略和设置

---

### 📁 结构

```
nb-runner/
├── notebooks/
│   └── futures/                              # 期货交易笔记本（按1→4顺序执行）
│       ├── 1. download_sample.ipynb          # 从strategy仓库下载示例策略
│       ├── 2. futures_strategy_verify.ipynb  # 使用模拟数据本地验证策略
│       ├── 3. futures_backtest.ipynb         # 在NeoMatrix服务器上运行回测
│       └── 4. futures_trade.ipynb            # 执行实时自动交易
├── module/
│   ├── futures/                              # 期货交易API模块
│   │   ├── account.py                        # 账户余额操作
│   │   ├── market.py                         # 市场数据获取
│   │   ├── position.py                       # 仓位管理
│   │   └── trade.py                          # 交易执行
│   └── spot/                                 # 现货交易API模块（相同结构）
└── docs/                                     # 多语言文档
```

---

### 📦 使用方法

1. 克隆或下载此仓库
2. 在Google Colab中打开笔记本（或调整本地环境路径）
3. 挂载Google云端硬盘并设置您的个人路径
4. 按照笔记本执行顺序操作：
   - **`1. download_sample.ipynb`** → 下载示例策略文件
   - **`2. futures_strategy_verify.ipynb`** → 本地验证策略
   - **`3. futures_backtest.ipynb`** → 在服务器上运行回测
   - **`4. futures_trade.ipynb`** → 执行实时交易

请确保同时使用包含策略模块和配置文件的 [strategy](https://github.com/NeoMatrixAI/strategy) 仓库。

---

### ❓ 支持

如有问题或需要支持，请通过 [**NeoMatrix Discord**](https://discord.gg/Xn26Q42DXD) 联系我们。
