from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from authapp.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('Имя'), max_length=30,blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=30,blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    avatar = models.ImageField(_('Аватар'),upload_to='user_avatars/', null=True, blank=True, default='user_avatars/common_avatar.jpg')
    birth_date = models.DateField(_('Дата рождения'), null=True, blank=True, )
    bio = models.TextField(_('Обо мне'),blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        if full_name.strip() == '':
            full_name = self.email
        return full_name.strip()

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        if self.first_name:
            return self.first_name
        return self.get_full_name()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)