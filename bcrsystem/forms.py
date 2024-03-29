from django import forms
from django.contrib import auth
from bcrsystem.models import bookInfo, classroom


class FeedbackEditAdminForm(forms.ModelForm):
    class Meta:
        model = bookInfo
        fields = '__all__'
        exclude = ['book_date', 'start_hour', 'end_hour', 'start_time', 'end_time', 'is_cancel', 'is_used', 'booker_id',
                   'classroom_id']


class LoginForm(forms.Form):
    username = forms.CharField(label='User', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('username or password error')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class bookingForm(forms.Form):
    Type = forms.ChoiceField(
        initial=1,
        choices=((1, 'Normal'), (2, 'Lab'))
    )

    Date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))

    Start_Time = forms.ChoiceField(
        choices=((8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'),
                 (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'),
                 (21, '21:00'), (22, '22:00'))
    )

    End_Time = forms.ChoiceField(
        choices=((8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'),
                 (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'),
                 (21, '21:00'), (22, '22:00'))
    )

    classroom_location = forms.ModelChoiceField(label='Classroom', required=True, queryset=classroom.objects.all(),
                                                empty_label='Choose classroom',
                                                widget=forms.Select(attrs={'class': 'form-control'}))

    book_requirement = forms.TextInput()

    def clean_Date(self):
        chooseDate = self.cleaned_data['Date']
        return chooseDate

    def clean_Type(self):
        roomtype = self.cleaned_data['Type']
        return roomtype

    def clean_classroom_location(self):
        classroom_location = self.cleaned_data['classroom_location']
        return classroom_location

    def clean_Start_Time(self):
        starttime = self.cleaned_data['Start_Time']
        return starttime

    def clean_End_Time(self):
        starttime = int(self.cleaned_data['Start_Time'])
        endtime = int(self.cleaned_data['End_Time'])
        if endtime <= starttime:
            raise forms.ValidationError("Time Error")
        elif (endtime - starttime) >= 2:
            raise forms.ValidationError("Only Book 1 Hour per booking")
        return endtime

    def clean_book_requirement(self):
        bookRequirement = self.cleaned_data['book_requirement']
        return bookRequirement


class longbookForm(forms.Form):
    Type = forms.ChoiceField(
        initial=1,
        choices=((1, 'Normal'), (2, 'Lab'))
    )

    Selete_Day = forms.ChoiceField(
        initial=1,
        choices=(
            (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'),
            (7, 'Sunday'))
    )

    Start_Time = forms.ChoiceField(
        choices=((8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'),
                 (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'),
                 (21, '21:00'), (22, '22:00'))
    )

    End_Time = forms.ChoiceField(
        choices=((8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'),
                 (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'),
                 (21, '21:00'), (22, '22:00'))
    )
    classroom_location = forms.ModelChoiceField(label='Classroom', required=True, queryset=classroom.objects.all(),
                                                empty_label='Choose classroom',
                                                widget=forms.Select(attrs={'class': 'form-control'}))
    Times = forms.IntegerField()

    def clean_Type(self):
        roomtype = self.cleaned_data['Type']
        return roomtype

    def clean_Selete_Day(self):
        bookDay = self.cleaned_data['Selete_Day']
        return bookDay

    def clean_Times(self):
        bookTimes = self.cleaned_data['Times']
        return bookTimes

    def clean_classroom_location(self):
        classroom_location = self.cleaned_data['classroom_location']
        return classroom_location

    def clean_Start_Time(self):
        starttime = self.cleaned_data['Start_Time']
        return starttime

    def clean_End_Time(self):
        starttime = int(self.cleaned_data['Start_Time'])
        endtime = int(self.cleaned_data['End_Time'])
        if endtime <= starttime:
            raise forms.ValidationError("Time Error")
        elif (endtime - starttime) >= 2:
            raise forms.ValidationError("Only Book 1 Hour per booking")
        return endtime
