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
        print("*************")

        print("TIME")
        print("LISTINGS")
        print(state.listings)
        print("ORDER DEPTHS")
        for product in state.order_depths.keys():
            print(".............................")
            print(product)
            print("SELL ORDERS: " +
                  str(state.order_depths[product].sell_orders))
            print("BUY  ORDERS: " +
                  str(state.order_depths[product].buy_orders))
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
        print("OWN TRADES")
        print(state.own_trades)
        print("MARKET TRADES")
        print(state.market_trades)
        print("POSITIONS")
        print(state.position)
        print("OBSERVATIONS")
        print(state.observations)
        print("############")
        return result
