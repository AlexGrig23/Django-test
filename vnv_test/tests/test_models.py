from django.test import TestCase
from users.models import Group, User


class GroupModelTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            title="TestGroup",
            description="Test description for the group."
        )

    def test_group_absolute_url(self):
        group = Group.objects.get(title="TestGroup")
        url = group.get_absolute_url()
        self.assertIsInstance(url, str)

class UserModelTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(
            title="TestGroup",
            description="Test description for the group."
        )
        self.user = User.objects.create(
            user_name="TestUser",
            group=self.group
        )

    def test_user_absolute_url(self):
        user = User.objects.get(user_name="TestUser")
        url = user.get_absolute_url()
        self.assertIsInstance(url, str)
