# from django.test import TestCase
#
# from order.models import Order
# from order.tasks import pay_for_orders
# from fixtures.test_services.services import create_user, create_shop_product, create_product, create_shop, \
#     create_order, create_order_good, create_payment_info
#
#
# class TestPayment(TestCase):
#
#     def test_success_payment_twenty_orders(self):
#         """Тест проверяет работу задачи при оплате двадцати заказов"""
#         for num in range(20):
#             user = create_user(email=f'test{num}@ya.ru')
#             order = create_order(user)
#             create_order_good(order, create_shop_product(create_shop(user), create_product(name=f'test{num}')))
#             create_payment_info(order)
#
#         pay_for_orders.run()
#         self.assertEqual(Order.objects.count(), 20)
#         self.assertTrue(all([order.paid for order in Order.objects.all()]))
