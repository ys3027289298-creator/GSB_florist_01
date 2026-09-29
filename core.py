"""花店核心逻辑：订单、冷库、花材和计费。"""

import json


def new_game():
    return {
        "orders": {},
        "cold_load": 0,
        "cold_capacity": 2,
        "flowers": 100,
        "day": 1,
        "order_id": 0,
    }


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["order_id"] += 1
    return state


def create_order(state, order_id, member=False):
    state["orders"][order_id] = {"member": member}
    return True


def store(state, order_id, amount):
    state["cold_load"] += amount
    state["flowers"] -= amount
    return True


def fee(state, order_id, end_day):
    return (end_day - state["day"]) - 1


def cancel_order(state, order_id, amount):
    return True


def discount(state, order_id, base):
    if state["orders"][order_id]["member"]:
        return base - 10 - 10
    return base


def deliver(state, order_id, paid):
    if not paid:
        state["orders"].pop(order_id, None)
        return False
    return True


def reserve(state, order_id, days):
    return True


def expire(state, current_day):
    return True


def main():
    print("花店 - 命令: order/store/fee/cancel/discount/deliver/reserve/expire/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
