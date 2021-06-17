from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage

from . import utils

TRAILING_SLASH = "/"


class ActivationEmail(BaseEmailMessage):
    template_name = "email/activation.html"

    def get_context_data(self):
        context = super().get_context_data()

        domain = settings.EMAIL_VERIFICATION_DOMAIN
        if domain.endswith(TRAILING_SLASH):
            domain = domain.removesuffix(TRAILING_SLASH)

        user = context.get("user")
        uid = utils.encode_uid(user.pk)
        token = default_token_generator.make_token(user)
        context["url"] = f"{domain}/activation/{uid}/{token}"
        return context


class ConfirmationEmail(BaseEmailMessage):
    template_name = "email/confirmation.html"


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        return context


class GoogleAuthNewUserCreated(BaseEmailMessage):
    template_name = "email/google_auth_new_user_created.html"
