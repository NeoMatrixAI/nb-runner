# nb-runner

[![Discord](https://img.shields.io/badge/Discord-2319DC)](https://discord.com/invite/Xn26Q42DXD)[![NeoMatrix](https://img.shields.io/badge/Neomatrix-white)](https://neomatrix.ai)
---
[![English](https://img.shields.io/badge/docs-English-blue)](../README.md) [![한국어](https://img.shields.io/badge/docs-한국어-red)](./README.ko.md)
[![简体中文](https://img.shields.io/badge/docs-简体中文-yellow)](./README.zh-CN.md)
---

이 레포지토리는 `.ipynb` 및 `.py` 파일로 구성된 노트북 실행 도구이며, 주로 [**Google Colab**](https://colab.research.google.com)에서 사용하도록 설계되었습니다.

제공된 API 기능을 사용하려면 **NeoMatrix**에서 `user key`를 발급받아야 합니다.

다음 중 하나를 통해 백테스트 및 실시간 트레이딩을 실행할 수 있습니다:
- 직접 만든 전략 및 설정 파일 사용
- [strategy](https://github.com/NeoMatrixAI/strategy) 레포지토리에서 제공되는 정기 업데이트 전략 및 설정 사용

---

### 📁 구조

```
nb-runner/
├── notebooks/
│   └── futures/                              # 선물 거래 노트북 (1→4 순서로 실행)
│       ├── 1. download_sample.ipynb          # strategy 레포에서 샘플 전략 다운로드
│       ├── 2. futures_strategy_verify.ipynb  # 모의 데이터로 전략 로컬 검증
│       ├── 3. futures_backtest.ipynb         # NeoMatrix 서버에서 백테스트 실행
│       └── 4. futures_trade.ipynb            # 실시간 자동 거래 실행
├── module/
│   ├── futures/                              # 선물 거래 API 모듈
│   │   ├── account.py                        # 계좌 잔액 조회
│   │   ├── market.py                         # 시장 데이터 조회
│   │   ├── position.py                       # 포지션 관리
│   │   └── trade.py                          # 거래 실행
│   └── spot/                                 # 현물 거래 API 모듈 (동일 구조)
└── docs/                                     # 다국어 문서
```

---

### 📦 사용 방법

1. 이 레포지토리를 클론하거나 다운로드합니다
2. Google Colab에서 노트북을 열거나 (로컬 환경의 경우 경로 조정)
3. Google Drive를 마운트하고 개인 경로를 설정합니다
4. 노트북 실행 순서를 따릅니다:
   - **`1. download_sample.ipynb`** → 샘플 전략 파일 다운로드
   - **`2. futures_strategy_verify.ipynb`** → 로컬에서 전략 검증
   - **`3. futures_backtest.ipynb`** → 서버에서 백테스트 실행
   - **`4. futures_trade.ipynb`** → 실시간 거래 실행

전략 모듈 및 설정 파일이 포함된 [strategy](https://github.com/NeoMatrixAI/strategy) 레포지토리도 함께 사용해야 합니다.

---

### ❓ 문의 및 지원

질문이나 도움이 필요하신 경우 [**NeoMatrix Discord**](https://discord.gg/Xn26Q42DXD)를 통해 문의해 주세요.
