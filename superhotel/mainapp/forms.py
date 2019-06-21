from django import forms

# forms for booking.html

class HeaderPhotoForm(forms.Form):
    photos = forms.FileField()

class NameOfHotelForm(forms.Form):
    name_of_hotel = forms.CharField(max_length=100)

class StarsForm(forms.Form):
    STARS_CHOICES = (
        (1, _("1 star hotel")),
        (2, _("2 star hotel")),
        (3, _("3 star hotel")),
        (4, _("4 star hotel")),
        (5, _("5 star hotel"))
    )
    stars = forms.ChoiceField(choices=STARS_CHOICES, label="", initial='', required=True)

class NameOfHotelInfoForm(forms.Form):
    info = forms.CharField(max_length=6000)

class TelephoneNumberForm(forms.Form):
    number = forms.IntegerField(required=True)

class AddressForm(forms.Form):
    address = CharField(max_length=100)

class LocalityForm(forms.Form):
    locality = CharField(max_length=200)

class RegionForm(forms.Form):
    region = CharField(max_length=200)

class PostalCodeForm(forms.Form):
    postalCode = forms.IntegerField(required=True)

class MapLinkForm(forms.Form):
    link = forms.CharField(max_length=2000)

class UploadPhotoInfoForm(forms.Form):
    # for x in range(6):
    #     photo+x = forms.FileField
    photo1 = forms.FileField()
    photo2 = forms.FileField()
    photo3 = forms.FileField()
    photo4 = forms.FileField()
    photo5 = forms.FileField()
    photo6 = forms.FileField()

class LongDescriptionOfHotel(forms.Form):
    longdescr = forms.CharField(max_length=10000)

class FeatureForm(forms.Form):
    feature1 = CharField(max_length=100)
    feature2 = CharField(max_length=100)
    feature3 = CharField(max_length=100)
    feature4 = CharField(max_length=100)
    feature5 = CharField(max_length=100)
    feature6 = CharField(max_length=100)
    feature7 = CharField(max_length=100)
    feature8 = CharField(max_length=100)

class TermsAndConditionsForm(forms.Form):
    terms = forms.CharField(max_length=3000)

# forms for book_a_room.html




