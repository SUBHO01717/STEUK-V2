from django.forms import ModelForm
from . models import *
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model= Contact
        fields=["full_name", "email", "contact_number","message"]


class BoilerForm(ModelForm):
    class Meta:
        model= Q_BoilerData
        exclude = ['formType']
        labels = {
            'property_type': 'What type of property is the new boiler for?',
            'job_type': 'Please select the job type you require.',
            'boiler_type': 'What type of boiler do you have?',
            'power_usage': 'What is your current method of gathering hot water?',
            'full_address': 'What is your address',
        }

        widgets = {
            'property_type': forms.RadioSelect(choices=Q_BoilerData.PROPERTY_CHOICES),
            'job_type': forms.RadioSelect(choices=Q_BoilerData.JOB_TYPE),
            'boiler_type': forms.RadioSelect(choices=Q_BoilerData.BOILER_TYPE),
            'power_usage': forms.RadioSelect(choices=Q_BoilerData.POWER_TYPE),
        }




class EVForm(ModelForm):
    class Meta:
        model= Q_EVData
        exclude = ['formType']

        labels = {
            'installation_type': 'Where are you looking to install your charging point?',
            'ownership_type': 'Are you a home owner?',
            'parking_type': 'Do you have off street parking?',
            'car_type': 'Do you have electric Car?',
            'charger_type': 'Do you already have an electric vehicle charger?',
        }
        
        widgets = {
            'installation_type': forms.RadioSelect(choices=Q_EVData.INSTALLATION_CHOICES),
            'ownership_type': forms.RadioSelect(choices=Q_EVData.OWNERSHIP_TYPE),
            'parking_type': forms.RadioSelect(choices=Q_EVData.PARKING_TYPE),
            'car_type': forms.RadioSelect(choices=Q_EVData.CAR_TYPE),
            'charger_type': forms.RadioSelect(choices=Q_EVData.CHARGER_TYPE),
        }


class HeatPumpForm(ModelForm):
    class Meta:
        model= Q_HeatPumps
        exclude = ['formType']

    
        labels = {
            'heating_type': 'What is your current heating system?',
            'loaction_type': 'Where do you need heat pump for?',
            'owenership_type': 'Are you homeowner or tenant?',
            'heat_pump_type': 'What type of heat pump you are interested in?',
            'duration': 'How soon do you need your heat pump?',
            'property_type': 'What type of property do you have?',
            'insulation': 'What type of insulation does your property have?',
            'radiators': 'How many radiators does your property have',
            'avilable_space': 'Does your property have ground floor space available outside for a heat pump unit?',
            'power_type': 'What is your existing Heating system?',
            }
        
        widgets = {
                    'heating_type': forms.RadioSelect(choices=Q_HeatPumps.HEATING_CHOICES),
                    'loaction_type': forms.RadioSelect(choices=Q_HeatPumps.LOCATION_TYPE),
                    'owenership_type': forms.RadioSelect(choices=Q_HeatPumps.OWENERSHIP_TYPE),
                    'heat_pump_type': forms.RadioSelect(choices=Q_HeatPumps.HEAT_PUMP_TYPE),
                    'duration': forms.RadioSelect(choices=Q_HeatPumps.DURATION_TYPE),
                    'property_type': forms.RadioSelect(choices=Q_HeatPumps.PROPERTY_TYPE),
                    'insulation': forms.RadioSelect(choices=Q_HeatPumps.INSULATION_TYPE),
                    'radiators': forms.RadioSelect(choices=Q_HeatPumps.RADIATOR_CHOICES),
                    'avilable_space': forms.RadioSelect(choices=Q_HeatPumps.AVAILABLE_SPACE_CHOICE),
                    'power_type': forms.RadioSelect(choices=Q_HeatPumps.POWER_TYPE),
                }
        
class HomeSecurityForm(ModelForm):
    class Meta:
        model= Q_HomeSecurity
        exclude = ['formType']
       

        labels = {
            'ownership': 'Do you own your home?',
            'residency': 'Type of your residence',
            'age_of_building': 'Age of your building',
            'number_of_floors': 'Number of floors',
            'square_footage': 'Square Footage',
            'number_of_people': 'How many people reside there',
            'average_age': 'Peoples ages who is living in the residence',
            'usual_stay': 'When people are usually home/away',
           
        }
        
        widgets = {
            'ownership': forms.RadioSelect(choices=Q_HomeSecurity.OWNERSHIP_TYPE),
            'residency': forms.RadioSelect(choices=Q_HomeSecurity.RESIDENCY_TYPE),
         
        }

        
class InfraredHeatForm(ModelForm):
    class Meta:
        model= Q_InfraredHeat
        exclude = ['formType']
       

        labels = {
            'OWNERSHIP_TYPE': 'Are you the property owner?',
            'RESIDENCY_TYPE': 'Do you live in a House or Apartment?',
            'HEATING_TYPE': 'What is the current heating system in your house?',
    
           
        }
        
        widgets = {
            'ownership': forms.RadioSelect(choices=Q_InfraredHeat.OWNERSHIP_TYPE),
            'residency': forms.RadioSelect(choices=Q_InfraredHeat.RESIDENCY_TYPE),
            'heating_type': forms.RadioSelect(choices=Q_InfraredHeat.HEATING_TYPE),
         
        }


class SolarForm(ModelForm):
    class Meta:
        model= Q_Solar
        exclude = ['formType']
       

        labels = {

            'installation_type':'What Type of Solar System you want to Install?',
            'residency':'Which of the below best describes the property you live in?',
            'ownership':'Are you the property owner?',
            'solar_type':'Which solar products you are interested in?',
            'solar_exists':'Do you already have the Solar Panel System installed?',
            'building_type':'Do you live in a conservation area or listed building?',
            'bed_rooms':'How many Bedrooms do you have?',
            'kws_usages':'Total kWh Using Per Year',
            'monthly_usages':'Average monthly Energy Usage',
            'avg_electricity_bill':'What is your average monthly electricity bill?',
            'roof_direction':'Is which direction does your roof face?',
            'roof_window':'Are there any windows on your roof?',
            'roof_shadow_impact':'Is there any shading that impacts your roof?',
            'pitch_type':'What is the pitch of our roof?',
            'installation_duration':'How Quickly do you need the work doing?',
         
    
           
        }
        
        widgets = {
            'installation_type': forms.RadioSelect(choices=Q_Solar.INSTALATION_TYPE),
            'residency': forms.RadioSelect(choices=Q_Solar.RESIDENCY_TYPE),
            'ownership': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
            'solar_type': forms.RadioSelect(choices=Q_Solar.SOLAR_TYPE),
            'solar_exists': forms.RadioSelect(choices=Q_Solar.SOLAR_EXISTS),
            'building_type': forms.RadioSelect(choices=Q_Solar.USAGE_TYPE),
            'monthly_usages': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
            'roof_direction': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
            'roof_window': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
            'roof_shadow_impact': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
            'pitch_type': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
            'installation_duration': forms.RadioSelect(choices=Q_Solar.OWNERSHIP_TYPE),
         
        }

class WindowForm(ModelForm):
    class Meta:
        model= Q_Window
        exclude = ['formType']
       

        labels = {

            'glazing_for':'What do you need double glazing for?',
            'ownership':'Are you the property Owner?',
            'number_of_window':'How many windows do you need',
            'delivery':'Are your looking for your windows to be?',
           
    
           
        }
        
        widgets = {
            'glazing_for': forms.RadioSelect(choices=Q_Window.GLAZING_TYPE),
            'ownership': forms.RadioSelect(choices=Q_Window.OWNERSHIP_TYPE),
            'number_of_window': forms.RadioSelect(choices=Q_Window.NUMBER_TYPE),
            'delivery': forms.RadioSelect(choices=Q_Window.WINDOW_TYPE),
           
         
        }
