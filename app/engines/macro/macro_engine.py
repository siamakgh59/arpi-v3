class MacroEngine:

    def run(self, data):

        macro = data.get("macro", {})

        return {
            "fed_rate": macro.get("fed_rate"),
            "cpi": macro.get("cpi"),
            "liquidity": macro.get("liquidity")
        }
