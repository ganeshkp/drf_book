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


class RequiredTogetherValidator(object):
    
    message = _("The fields {field_names} are required together.")
    missing_message = _("This field is required.")
    requires_context = True
    
    def __init__(self, fields, message=None, missing_message=None):
        self.fields = fields
        self.serializer_field = None
        self.message = message or self.message
        self.missing_message = missing_message or self.missing_message
        
    def enforce_required_fields(self, attrs):
        raise NotImplementedError

    def __call__(self, attrs):
        self.enforce_required_fields(attrs)
        
class CreateRequiredValidator(RequiredTogetherValidator):
    def enforce_required_fields(self, attrs):
        return super().enforce_required_fields(attrs)