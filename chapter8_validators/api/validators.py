from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

       
def validate_watchlist_title(value):
    if len(value)<5 or len(value)>30:
        raise ValidationError("Movie title shall be meaningful")
    

def validate_watchlist_type(attrs):
    if attrs["category"]=="MOVIE" and attrs["episodes"]>0:
        raise ValidationError("Movie cannot have episodes")
    
    if attrs["category"]=="SERIES" and attrs["episodes"]==0:
        raise ValidationError("Series shall have number of episodes")
