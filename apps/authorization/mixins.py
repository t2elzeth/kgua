from .models import User
from .utils import get_user_email


class SendEmailMixin:
    email_classes = {}

    def _get_email(self, receiver):
        return get_user_email(receiver) if isinstance(receiver, User) else receiver

    def _get_receivers(self, to):
        return (
            [self._get_email(receiver) for receiver in to]
            if isinstance(to, list)
            else [self._get_email(to)]
        )

    def get_email_class(self):
        key = self.action if hasattr(self, "action") else self.request.method

        if key not in self.email_classes:
            raise KeyError(f"Email class for {key} not found")

        return self.email_classes.get(key)

    def send_email(self, to, context):
        email_class = self.get_email_class()
        receivers = self._get_receivers(to)
        email_class(self.request, context).send(receivers)
