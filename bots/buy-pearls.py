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
        print(state.own_trades)
        print(state.position)

        for product in state.order_depths.keys():
            print(".............................")
            print(product)
            print("SELL ORDERS: " +
                  str(state.order_depths[product].sell_orders))
            print("BUY  ORDERS: " +
                  str(state.order_depths[product].buy_orders))
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

        # order_depth: OrderDepth = state.order_depths[product]

        orders: list[Order] = []
        # if state.timestamp == 100:
        orders.append(Order("PEARLS", 1000, 3))

        result["PEARLS"] = orders

        return result
