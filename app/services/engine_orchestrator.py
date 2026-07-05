from app.engines.macro.macro_engine import MacroEngine

from app.data.providers.prediction_markets import PredictionMarketsProvider
from app.data.providers.market_data import MarketDataProvider
from app.data.providers.macro_data import MacroDataProvider


class EngineOrchestrator:

    def __init__(self):
        self.market_provider = MarketDataProvider()
        self.macro_provider = MacroDataProvider()
        self.prediction_provider = PredictionMarketsProvider()
        self.macro_engine = MacroEngine()

    def run(self):

        market = self.market_provider.get_data()
        macro = self.macro_provider.get_data()
        prediction = self.prediction_provider.get_data()

        data = {
            "market": market,
            "macro": macro,
            "prediction": prediction
        }

        result = self.macro_engine.run(data)

        return {
            "status": "ok",
            "macro": result
        }
