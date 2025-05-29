# nb-runner

이 레포지토리는 `.ipynb` 및 `.py` 파일로 구성된 노트북 실행 도구입니다.

주로 [**Google Colab**](https://colab.research.google.com)과 같은 로컬 환경에서 실행되도록 설계되었습니다.  
"Google 드라이브 마운트" 셀을 수정하고 **개인 경로**를 지정하면, 다른 로컬 환경에서도 쉽게 사용할 수 있습니다.

제공된 API 기능을 사용하려면 **NeoMatrix**로부터 `data apikey`와 `user key`를 발급받아야 합니다.

다음 중 하나를 통해 백테스트 및 실시간 트레이딩을 실행할 수 있습니다:
- 직접 만든 전략 및 설정 파일 사용  
- [strategy](https://github.com/NeoMatrixAI/strategy) 레포지토리에서 제공되는 정기 업데이트 전략 및 설정 사용

### 📘 노트북 실행 흐름

일반적인 노트북 실행 순서는 다음과 같습니다:

1. **`strategy_verify_test.ipynb`**  
   → NeoMatrix API 서버를 호출하여 전략을 검증합니다.

2. **`backtest.ipynb`**  
   → 검증된 전략과 설정을 바탕으로 백테스트를 실행합니다.

3. **`trade.ipynb`**  
   → 백테스트 결과로 도출된 최종 파라미터를 기반으로 실시간 자동 거래를 수행합니다.

---
### ❓ 문의 및 지원

질문이나 도움이 필요하신 경우 [**NeoMatrix Discord**](https://discord.gg/n6tMdrse)를 통해 문의해 주세요.
