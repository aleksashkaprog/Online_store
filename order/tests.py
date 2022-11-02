from django.test import TestCase
from users.models import CustomUser


class OrderTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@test.ru", password="test", full_name="test", phone_number="375299999999"
        )

    def test_order(self):

        self.client.force_login(user=self.user)
        self.client.post(
            "/order/step1/", {"email": "test@test.ru", "first_second_names": "Тест", "phone": "375299999999"}
        )
        self.client.post("/order/step2/", {"city": "Город", "address": "Адрес"})
        self.client.post("/order/step3/", {"payment": "картой"})
        response = self.client.get("/order/step4/")
        self.assertEquals(response.status_code, 200)
