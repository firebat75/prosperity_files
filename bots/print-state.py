from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order


class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        # Initialize the method output dict as an empty dict
        result = {}

        print(state.position)

        print("===========================================")
        for product in state.order_depths.keys():
            print("---------------------------------")
            print(product)
            print(state.order_depths["sell_orders"])
            print(state.order_depths["buy_orders"])
            print("---------------------------------")
        print("=============================================")

        return result
