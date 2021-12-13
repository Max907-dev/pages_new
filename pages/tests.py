from django.test import SimpleTestCase #используем simpletestcase так как не используем базу данных
 
 #проверяем нашу страницу на существование до 200 стр, но ничего не говорит о ее содержании
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)