from django.test import TestCase
from django.urls import reverse
from users.models import User, Group


class TestURLs(TestCase):
    def setUp(self):
        self.group = Group.objects.create(title="TestGroup")
        self.user = User.objects.create(user_name="TestUser", group=self.group)

    def test_users_list_url(self):
        url = reverse('users_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_url(self):
        url = reverse('create_user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_user_url(self):
        url = reverse('edit_user', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_user_url(self):
        url = reverse('delete_user', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_groups_list_url(self):
        url = reverse('groups_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_group_url(self):
        url = reverse('create_group')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_group_url(self):
        url = reverse('edit_group', args=[self.group.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_group_url(self):
        url = reverse('delete_group', args=[self.group.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.user.delete()
        self.group.delete()