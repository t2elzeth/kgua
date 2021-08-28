from django import forms
from .models import StaffContacts, StaffContactEmail, StaffEducation


class StaffContactsForm(forms.ModelForm):
    personal_email = forms.EmailField()
    corporate_email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, "email"):
            self.fields[
                "personal_email"
            ].initial = self.instance.email.personal
            self.fields[
                "corporate_email"
            ].initial = self.instance.email.corporate

    def save(self, commit=True):
        personal_email = self.cleaned_data["personal_email"]
        corporate_email = self.cleaned_data["corporate_email"]

        if not hasattr(self.instance, "email"):
            self.instance.email = StaffContactEmail(
                contact=self.instance,
                personal=personal_email,
                corporate=corporate_email,
            )
            self.instance.email.save()

        self.instance.email.personal = personal_email
        self.instance.email.corporate = corporate_email
        self.instance.email.save()

        return super().save()

    class Meta:
        model = StaffContacts
        fields = ["phone", "personal_email", "corporate_email"]


class StaffEducationInlineForm(forms.ModelForm):
    class Meta:
        model = StaffEducation
        fields = []

