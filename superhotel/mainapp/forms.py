from django import forms

# forms for booking.html

class HeaderPhotoForm(forms.Form):
    photos = forms.FileField()

class NameOfHotelForm(forms.Form):
    name_of_hotel = forms.CharField(max_length=100)

class StarsForm(forms.Form):
    STARS_CHOICES = (
        (1, ("1 star hotel")),
        (2, ("2 star hotel")),
        (3, ("3 star hotel")),
        (4, ("4 star hotel")),
        (5, ("5 star hotel"))
    )
    stars = forms.ChoiceField(choices=STARS_CHOICES, label="", initial='', required=True)

class NameOfHotelInfoForm(forms.Form):
    info = forms.CharField(max_length=6000)

class TelephoneNumberForm(forms.Form):
    number = forms.IntegerField(required=True)

class AddressForm(forms.Form):
    address = forms.CharField(max_length=100)

class LocalityForm(forms.Form):
    locality = forms.CharField(max_length=200)

class RegionForm(forms.Form):
    region = forms.CharField(max_length=200)

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
    feature1 = forms.CharField(max_length=100)
    feature2 = forms.CharField(max_length=100)
    feature3 = forms.CharField(max_length=100)
    feature4 = forms.CharField(max_length=100)
    feature5 = forms.CharField(max_length=100)
    feature6 = forms.CharField(max_length=100)
    feature7 = forms.CharField(max_length=100)
    feature8 = forms.CharField(max_length=100)

class TermsAndConditionsForm(forms.Form):
    terms = forms.CharField(max_length=3000)

# forms for book_a_room.html




