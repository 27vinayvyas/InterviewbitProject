from django import forms
from .models import Participant, Interview

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ('participant', 'date_Start', 'date_End')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_end'].queryset = Interview.objects.none()

"""        if 'date_start' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
"""