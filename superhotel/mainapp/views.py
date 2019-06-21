from django.shortcuts import render
from django.shortcuts import get_object_or_404, HttpResponseRedirect
import mainapp.forms
# Create your views here.
def dataFromInputBooking(request):
    headerPhoto = HeaderPhotoForm(request.POST)
    nameOfHotel_form = NameOfHotelForm(request.POST)
    starsForm = StarsForm(request.POST)
    nameOfHotelInfo = NameOfHotelInfoForm(request.Post)
    telephoneNumberForm = TelephoneNumberForm(request.POST)
    addressForm = AddressForm(request.POST)
    localityForm = LocalityForm(request.POST)
    regionForm = RegionForm(request.POST)
    postal_codeForm = PostalCodeForm(request.POST)
    mapLinkForm = MapLinkForm(request.POST)
    uploadPhotoInfoForm = UploadPhotoInfoForm(request.POST)
    longDescriptionOfHotel =
