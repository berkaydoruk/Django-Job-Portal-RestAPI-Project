import pycountry
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

VALID_COUNTRIES = {country.name for country in pycountry.countries}

def validate_country(value):
    if value not in VALID_COUNTRIES:
        raise ValidationError(f"{value} is not a valid country name.")
    
class Company(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=60, unique=True, blank=False, null=False)
    company_country = models.CharField(validators=[validate_country])
    company_city = models.CharField(max_length=50, blank=True, null=True)  
    company_industry = models.CharField(max_length=50)  
    company_website = models.URLField(blank=False, null=False)

    def __str__(self):
        return f"{self.owner} {self.company_name} ({self.company_website}) - {self.company_country}"