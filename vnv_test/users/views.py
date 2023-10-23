from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.forms import UserForm, GroupForm
from users.models import User, Group


class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.order_by('user_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/user_create.html'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_update.html'

    def get_success_url(self):
        return reverse('users_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users_list')


class GroupListView(ListView):
    model = Group
    template_name = 'users/groups_list.html'
    context_object_name = 'groups'
    paginate_by = 10

    def get_queryset(self):
        return Group.objects.all().order_by('id')


class GroupCreateView(CreateView):
    form_class = GroupForm
    template_name = 'users/group_create.html'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'users/group_update.html'

    def get_success_url(self):
        return reverse('groups_list')


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'users/group_confirm_delete.html'
    success_url = reverse_lazy('groups_list')

    def form_valid(self, form):
        group = self.get_object()

        if group.user_set.exists():
            form.add_error(None, ValidationError("The group cannot be deleted because it contains users."))
            return self.form_invalid(form)

        return super().form_valid(form)

