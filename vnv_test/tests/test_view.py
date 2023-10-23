from django.test import TestCase
from django.urls import reverse
from users.models import User, Group


class UserListViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(title="TestGroup")
        self.user = User.objects.create(user_name="TestUser", group=self.group)
        self.url = reverse('users_list')

    def test_user_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestUser")
        self.assertContains(response, "TestGroup")

    def tearDown(self):
        self.user.delete()
        self.group.delete()


class UserCreateViewTest(TestCase):
    def test_user_create_view(self):
        url = reverse('create_user')
        data = {'user_name': 'NewUser', 'group': 'TestGroup'}
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "NewUser")


class UserUpdateViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(title="TestGroup")
        self.user = User.objects.create(user_name="TestUser", group=self.group)

    def test_user_update_view(self):
        url = reverse('edit_user', args=[self.user.pk])
        data = {'user_name': 'UpdatedUser', 'group': 'UpdatedGroup'}
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "UpdatedUser")


class UserDeleteViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(title="TestGroup")
        self.user = User.objects.create(user_name="TestUser", group=self.group)

    def test_user_delete_view(self):
        url = reverse('delete_user', args=[self.user.pk])
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Users")


class GroupCreateViewTest(TestCase):
    def test_group_create_view(self):
        url = reverse('create_group')
        data = {'title': 'NewGroup'}
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "NewGroup")


class GroupUpdateViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(title="TestGroup")

    def test_group_update_view(self):
        url = reverse('edit_group', args=[self.group.pk])
        data = {'title': 'UpdatedGroup'}
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "UpdatedGroup")


class GroupDeleteViewTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(title="TestGroup")

    def test_group_delete_view(self):
        url = reverse('delete_group', args=[self.group.pk])
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Groups")
