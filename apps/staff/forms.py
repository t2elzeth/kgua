from django import forms

from .models import StaffContactEmail, StaffContacts, StaffEducation


class StaffContactsForm(forms.ModelForm):
    personal_email = forms.EmailField(required=False)
    corporate_email = forms.EmailField(required=False)

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
        res = super().save()
        personal_email = self.cleaned_data["personal_email"]
        corporate_email = self.cleaned_data["corporate_email"]

        if not hasattr(self.instance, "email"):
            StaffContactEmail.objects.create(
                contact=res,
                personal=personal_email,
                corporate=corporate_email,
            )

        self.instance.email.personal = personal_email
        self.instance.email.corporate = corporate_email
        self.instance.email.save()

        return res

    class Meta:
        model = StaffContacts
        fields = ["phone", "personal_email", "corporate_email"]


class StaffEducationInlineForm(forms.ModelForm):
    class Meta:
        model = StaffEducation
        fields = []
