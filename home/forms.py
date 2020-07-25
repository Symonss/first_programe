from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.db import transaction
from home.models import User, Customer, Vendor, Review, Salon, Service, Product, Appointment, Gallery, Profile
from bootstrap_datepicker_plus import DatePickerInput
from django.utils.translation import ugettext_lazy as _


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        # TODO determine type of user and create appropriate model
        user.is_customer = True
        user.save()
        Customer.objects.create(user=user)
        return user

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        user.save()
        Vendor.objects.create(user=user)
        return user


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Current password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False)


class UserSetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', )
        widgets = {
            'contet':
            forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Share your feedback about this salon'
                })
        }


class CreateSalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('name', 'description',
                  'paybill', 'location')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'cost', 'duration', 'availability')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'brand')


class CustomerAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', ]
        labels = {
            'appointment_date': ''
        }
        widgets = {
            'appointment_date': DatePickerInput()
        }


class SalonAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['services', 'appointment_date', 'products']
        widgets = {
            'services': forms.CheckboxSelectMultiple,
            'appointment_date': DatePickerInput(),
            'products': forms.CheckboxSelectMultiple,
        }


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['services']
        widgets = {
            'services': forms.CheckboxSelectMultiple,
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image', 'is_selected', 'image_type')
