from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255,null=True, blank=True)
    images=models.ImageField(upload_to='media/category',null=True, blank=True)

    def __str__(self): 
        return self.name
    
class Brand(models.Model):
    brand_name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    SHOW={"YES": "YES",
    "NO": "NO",}
    name = models.CharField(max_length=255, null=True, blank=True)
    regular_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,default=None)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE, default=None)
    short_description=RichTextUploadingField(null=True, blank=True)
    product_overview=RichTextUploadingField(null=True, blank=True)
    product_specifcation=RichTextUploadingField(null=True, blank=True)
    show_product= models.CharField(choices=SHOW, max_length=3, default="YES")
    created_at = models.DateField(default=timezone.now)
   

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='media/product')

    def __str__(self):
        return self.product.name


def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(_('Only PDF files are allowed.'))
    

class Brochure(models.Model):
    product = models.ForeignKey(Product, related_name='brochure', on_delete=models.CASCADE, default=None)
    file = models.FileField(upload_to='media/brochures', validators=[validate_pdf])
    def __str__(self):
        return self.product.name
    
class Blog(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='media/blog',blank=True,null=True)
    source=models.CharField(max_length=255, null=True,blank=True)
    details=RichTextUploadingField(null=True, blank=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
    

class Contact(models.Model):
    full_name=models.CharField(max_length=255)
    email=models.EmailField()
    contact_number=models.CharField(max_length=50)
    message=models.TextField()
    created_at = models.DateField(default=timezone.now)
    

    def __str__(self):
        return f"{self.full_name}"
    

class ServiceCategory(models.Model):
    image=models.ImageField(upload_to='media/service',blank=True,null=True)
    service_category_name=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.service_category_name}"
    
class Services(models.Model):
    image=models.ImageField(upload_to='media/service',blank=True,null=True)
    category=models.ForeignKey(ServiceCategory,related_name='services', on_delete=models.CASCADE, default=None)
    service_name=models.CharField(max_length=255, blank=True, null=True)
    details=RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.service_name}"
    
class PackageCatgory(models.Model):
    package_category_name=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.package_category_name}"
    
class Packages(models.Model):
    image=models.ImageField(upload_to='media/packages',blank=True,null=True)
    category=models.ForeignKey(PackageCatgory,related_name='packages', on_delete=models.CASCADE, default=None)
    package_name=models.CharField(max_length=255, blank=True, null=True)
    details=RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f"{self.package_name}"
    
class Projects(models.Model):
    image=models.ImageField(upload_to='media/projects',blank=True,null=True)
    package_name=models.CharField(max_length=255, blank=True, null=True)
    details=RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return f"{self.package_name}"
    

class Q_FormType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class Q_BoilerData(models.Model):
     
     PROPERTY_CHOICES = [('House', 'House'),('Apartment', 'Apartment'),('Office', 'Office'),('Others', 'Others'),]
     JOB_TYPE=[('New Instalation', 'New Instalation'),('Replacement', 'Replacement'),('Service', 'Service'),('Others', 'Others'),]
     BOILER_TYPE=[('Central Heating & Hot Water', 'Central Heating & Hot Water'),('Central Heating Only', 'Central Heating Only'),
        ('Hot Water Only', 'Hot Water Only'),
        ('Do not Know', 'Do not Know'),
    ]
     POWER_TYPE=[('Gas', 'Gas'),('Oil', 'Oil'),('LPG', 'LPG'),('Others', 'Others'),]
     
     property_type=models.CharField(max_length=255, choices=PROPERTY_CHOICES,blank=False, default='Unspecified')
     job_type=models.CharField(max_length=255, choices=JOB_TYPE, blank=False,default='Unspecified')
     boiler_type=models.CharField(max_length=255, choices=BOILER_TYPE, blank=False,default='Unspecified')
     power_usage=models.CharField(max_length=255, choices=POWER_TYPE, blank=False,default='Unspecified')

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255,)
     post_code=models.CharField(max_length=255,)
     phone=models.CharField(max_length=255,)
     email=models.EmailField()
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE,)

     def __str__(self):
         return f"{self.formType}"
    


class Q_EVData(models.Model):
     
     INSTALLATION_CHOICES = [('House', 'House'),('Business Premises', 'Business Premises'),]
     OWNERSHIP_TYPE=[('Yes', 'Yes'),('No', 'No'),]
     PARKING_TYPE=[('Yes', 'Yes'),('No', 'No'),]
     CAR_TYPE=[('Yes', 'Yes'),('No', 'No'),('It will be delivered shortly','It will be delivered shortly')]
     CHARGER_TYPE=[('Yes', 'Yes'),('Yes', 'Yes'),]
  
     
     installation_type=models.CharField(max_length=255, choices=INSTALLATION_CHOICES,blank=False, default='Unspecified')
     ownership_type=models.CharField(max_length=255, choices=OWNERSHIP_TYPE,blank=False, default='Unspecified' )
     parking_type=models.CharField(max_length=255, choices=PARKING_TYPE,blank=False, default='Unspecified')
     car_type=models.CharField(max_length=255, choices=CAR_TYPE,blank=False, default='Unspecified')
     charger_type=models.CharField(max_length=255, choices=CHARGER_TYPE,blank=False, default='Unspecified')

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE, null=True, blank=True)
   

     def __str__(self):
         return f"{self.formType}"

class Q_HeatPumps(models.Model):
     
     HEATING_CHOICES = [('Gas/Oil Bioler', 'Gas/Oil Bioler'),('Electric Boiler', 'Electric Boiler'),('Others', 'Others'),]
     LOCATION_TYPE=[('Home', 'Home'),('Business', 'Business'),]
     OWENERSHIP_TYPE=[('Homeowner', 'Homeowner'),('Tenent', 'Tenent'),]
     HEAT_PUMP_TYPE=[('Air Source', 'Air Source'),('Water Source', 'Water Source'),('Ground Source','Ground Source'),('Not Sure- Need advise','Not Sure- Need advise')]
     DURATION_TYPE=[('As Soon As Possible', 'As Soon As Possible'),('1-3 months', '1-3 months'),('3-6 months', '3-6 months'),('6+ Months', '6+ Months'),]
     PROPERTY_TYPE=[('Semi Detached', 'Semi Detached'),('Detached', 'Detached'),('Apartment', 'Apartment'),('Bungalow', 'Bungalow'),('Terraced', 'Terraced'),('Other', 'Other'),]
     INSULATION_TYPE=[('Loft Insulation', 'Loft Insulation'),('Cavity Insulation', 'Cavity Insulation'),('Double Window Glazing', 'Double Window Glazing'),('Triple window Glazing', 'Triple window Glazing'),('None of the above', 'None of the above'),]
     RADIATOR_CHOICES = [('1-5 Radiators', '1-5 Radiators'),('6-10 Radiators', '6-10 Radiators'),('11-15 Radiators', '11-15 Radiators'),('16+ Radiators', '16+ Radiators'),]
     AVAILABLE_SPACE_CHOICE=[('Yes', 'Yes'),('No', 'No'),('Not Sure', 'Not Sure'),]
     POWER_TYPE=[('Gas', 'Gas'),('Oil', 'Oil'),('LPG', 'LPG'),('Electric', 'Electric'),('Others', 'Others'),]

     heating_type=models.CharField(max_length=255, choices=HEATING_CHOICES,blank=False, default='Unspecified' )
     loaction_type=models.CharField(max_length=255, choices=LOCATION_TYPE,blank=False, default='Unspecified' )
     owenership_type=models.CharField(max_length=255, choices=OWENERSHIP_TYPE,blank=False, default='Unspecified')
     heat_pump_type=models.CharField(max_length=255, choices=HEAT_PUMP_TYPE,blank=False, default='Unspecified')
     duration=models.CharField(max_length=255, choices=DURATION_TYPE,blank=False, default='Unspecified')
     property_type=models.CharField(max_length=255, choices=PROPERTY_TYPE,blank=False, default='Unspecified')
     insulation=models.CharField(max_length=255, choices=INSULATION_TYPE,blank=False, default='Unspecified')
     radiators=models.CharField(max_length=255, choices=RADIATOR_CHOICES,blank=False, default='Unspecified')
     avilable_space=models.CharField(max_length=255, choices=AVAILABLE_SPACE_CHOICE,blank=False, default='Unspecified')
     power_type=models.CharField(max_length=255, choices=POWER_TYPE,blank=False, default='Unspecified')

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE,null=True, blank=True)
    

     def __str__(self):
         return f"{self.formType}"
    


class Q_HomeSecurity(models.Model):
        
     OWNERSHIP_TYPE=[('Yes', 'Yes'),('No', 'No'),]
     RESIDENCY_TYPE=[('Yes', 'Yes'),('No', 'No'),]
      
     ownership=models.CharField(max_length=255, choices=OWNERSHIP_TYPE,blank=False, default='Unspecified')
     residency=models.CharField(max_length=255, choices=RESIDENCY_TYPE,blank=False, default='Unspecified' )
     age_of_building=models.CharField(max_length=255,)
     number_of_floors=models.CharField(max_length=255,)
     square_footage=models.CharField(max_length=255,)
     number_of_people=models.CharField(max_length=255,)
     average_age=models.CharField(max_length=255,)
     usual_stay=models.CharField(max_length=255,)

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE, null=True, blank=True)
   

     def __str__(self):
         return f"{self.formType}"
     

class Q_InfraredHeat(models.Model):
        
     OWNERSHIP_TYPE=[('Yes', 'Yes'),('No', 'No'),]
     RESIDENCY_TYPE=[('House', 'House'),('Apartment', 'Apartment'),]
     HEATING_TYPE=[('Gas', 'Gas'),('Electric', 'Electric'),('Heat Pump', 'Heat Pump'),('Other','Other')]
      
     ownership=models.CharField(max_length=255, choices=OWNERSHIP_TYPE,blank=False, default='Unspecified')
     residency=models.CharField(max_length=255, choices=RESIDENCY_TYPE,blank=False, default='Unspecified' )
     heating_type=models.CharField(max_length=255, choices=HEATING_TYPE,blank=False, default='Unspecified' )
     
     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE, null=True, blank=True)
   

     def __str__(self):
         return f"{self.formType}"
     
class Q_Solar(models.Model):
        
     INSTALATION_TYPE=[('Domestic', 'Domestic'),('Commercial', 'Commercial'),]
     RESIDENCY_TYPE=[('Detached', 'Detached'),('Terrace', 'Terrace'),('Bungalow', 'Bungalow'),('Semidetached', 'Semidetached'),]
     OWNERSHIP_TYPE=[('Yes', 'Yes'),('No', 'No')]
     SOLAR_TYPE=[('Solar Panels', 'Solar Panels'),('Solar Battery', 'Solar Battery'),('Solar Pannels & Battery', 'Solar Pannels & Battery'),('Not Sure', 'Not Sure')]
     SOLAR_EXISTS=[('Yes', 'Yes'),('No', 'No')]
     BUILDING_TYPE=[('Yes', 'Yes'),('No', 'No')]
     USAGE_TYPE=[('Low', 'Low'),('Medium', 'Medium'),('High', 'High')]
     DIRECTION_TYPE=[('North', 'North'),('Northwest', 'Northwest'),('Northeast', 'Northeast'),('East', 'East'),('South', 'South'),('Southeast', 'Southeast'),('Southwest', 'Southwest'),('West', 'West'),('Not Sure', 'Not Sure')]
     ROOF_WINDOW=[('Yes', 'Yes'),('No', 'No')]
     ROOF_SHADOW=[('None', 'None'),('Yes,Nearby Building', 'Yes,Nearby Building'),('Yes,Nearby Tree', 'Yes,Nearby Tree'),('Yes,Others', 'Yes,Others')]
     PITCH_TYPE=[('Flat', 'Flat'),('Pitched / Angled', 'Pitched / Angled'),('Others', 'Others'),('Not Sure', 'Not Sure')]
     DURATION_TYPE=[('ASAP', 'ASAP'),('Within 1 month', 'Within 1 month'),('Within 3 months', 'Within 3 months'),('Within 6 months', 'Within 6 months')]

     installation_type=models.CharField(max_length=255, choices=INSTALATION_TYPE,blank=False, default='Unspecified')
     residency=models.CharField(max_length=255, choices=RESIDENCY_TYPE,blank=False, default='Unspecified' )
     ownership=models.CharField(max_length=255, choices=OWNERSHIP_TYPE,blank=False, default='Unspecified' )
     solar_type=models.CharField(max_length=255, choices=SOLAR_TYPE,blank=False, default='Unspecified' )
     solar_exists=models.CharField(max_length=255, choices=SOLAR_EXISTS,blank=False, default='Unspecified' )
     building_type=models.CharField(max_length=255, choices=BUILDING_TYPE,blank=False, default='Unspecified' )
     bed_rooms=models.CharField(max_length=255)
     kws_usages=models.CharField(max_length=255)
     monthly_usages=models.CharField(max_length=255, choices=USAGE_TYPE,blank=False, default='Unspecified')
     avg_electricity_bill=models.CharField(max_length=255)
     roof_direction=models.CharField(max_length=255, choices=DIRECTION_TYPE,blank=False, default='Unspecified')
     roof_window=models.CharField(max_length=255, choices=ROOF_WINDOW,blank=False, default='Unspecified')
     roof_shadow_impact=models.CharField(max_length=255, choices=ROOF_SHADOW,blank=False, default='Unspecified')
     pitch_type=models.CharField(max_length=255, choices=PITCH_TYPE,blank=False, default='Unspecified')
     installation_duration=models.CharField(max_length=255, choices=DURATION_TYPE,blank=False, default='Unspecified')

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE, null=True, blank=True)
   

     def __str__(self):
         return f"{self.formType}"
     
class Q_Window(models.Model):
        
     GLAZING_TYPE=[('Windows', 'Windows'),('Doors', 'Doors'),('Other', 'Other')]
     OWNERSHIP_TYPE=[('Yes', 'Yes'),('No', 'No'),]
     NUMBER_TYPE=[('1', '1'),('2-5', '2-5'),('6+', '6+'),]
     WINDOW_TYPE=[('Supplied & fitted', 'Supplied & fitted'),('Supplied only', 'Supplied only'),]

      
     glazing_for=models.CharField(max_length=255, choices=GLAZING_TYPE,blank=False, default='Unspecified')
     ownership=models.CharField(max_length=255, choices=OWNERSHIP_TYPE,blank=False, default='Unspecified' )
     number_of_window=models.CharField(max_length=255, choices=NUMBER_TYPE,blank=False, default='Unspecified' )
     delivery=models.CharField(max_length=255, choices=WINDOW_TYPE,blank=False, default='Unspecified' )

     name=models.CharField(max_length=255)
     full_address=models.CharField(max_length=255, null=True, blank=True)
     post_code=models.CharField(max_length=255, null=True, blank=True)
     phone=models.CharField(max_length=255, null=True, blank=True)
     email=models.EmailField(null=True, blank=True)
     formType=models.ForeignKey(Q_FormType, on_delete=models.CASCADE, null=True, blank=True)
   

     def __str__(self):
         return f"{self.formType}"