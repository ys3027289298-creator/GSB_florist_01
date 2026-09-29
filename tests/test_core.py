import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_order(self):
        state = core.new_game()
        self.assertTrue(core.create_order(state, 1))
        self.assertFalse(core.create_order(state, 1))

    def test_02_cold_capacity(self):
        state = core.new_game()
        core.store(state, 1, 1)
        core.store(state, 1, 1)
        result = core.store(state, 1, 1)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds_flowers(self):
        state = core.new_game()
        core.store(state, 1, 5)
        core.cancel_order(state, 1, 5)
        self.assertEqual(state["flowers"], 100)

    def test_05_discount_once(self):
        state = core.new_game()
        core.create_order(state, 1, member=True)
        self.assertEqual(core.discount(state, 1, 100), 90)

    def test_06_deliver_failure_keeps_order(self):
        state = core.new_game()
        core.create_order(state, 1)
        result = core.deliver(state, 1, False)
        self.assertFalse(result)
        self.assertIn(1, state["orders"])

    def test_07_expire_releases(self):
        state = core.new_game()
        state["slots"] = {"S1": 1}
        core.expire(state, 5)
        self.assertIsNone(state["slots"]["S1"])

    def test_08_load_preserves_order_id(self):
        state = core.new_game()
        state["order_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["order_id"], 4)


if __name__ == "__main__":
    unittest.main()
