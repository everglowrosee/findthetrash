from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from common.models import Profile


# ID = username
# 이름(닉네임) = first_name
# 연락처 = last_name

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    last_name = forms.IntegerField(label="phone")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'greenpoint', 'coupon')
        

# class PointsForm(forms.Form):

#     meetingKey = forms.CharField(
#         validators=[RegexValidator(regex='^.{64}$', message='Length has to be 64', code='nomatch')],
#         label="Meeting Key",
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class' :'form-control',
#                 'type' : 'password',
#                 'id' : 'inputPassword4',
#                 'placeholder' : 'Password'
#                 }
#             )
#         )
#     student_ID = forms.CharField(
#         validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')],
#         label="Student ID",
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "type" : "text",
#                 "class" : "form-control",
#                 "id" : "InputID",
#                 "placeholder" : "0609067234"
#             }
#         )
#     )
#     firstName = forms.CharField(
#         label="Last Name",
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "type" : "text",
#                 "class" : "form-control",
#                 "id" : "firstName",
#                 "placeholder" : "John"
#             }
#         )
#     )
#     lastName = forms.CharField(
#         label="Last Name",
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 "type" : "text",
#                 "class" : "form-control",
#                 "id" : "lastName",
#                 "placeholder" : "Smith"
#             }
#         )
#     )

#     def save(self):
#         data = self.cleaned_data
#         newID = hashStudentNo(data['student_ID'])
#         print(newID)
#         tMeeting = MeetingKey.objects.filter(meetingKey=data['meetingKey']).first()
#         tStudent=Student.objects.filter(studentNo=newID).first()
#         print(tStudent)
#         newEntry = PointsEntry(student=tStudent, points=tMeeting.points, reason=tMeeting.name, meeting=tMeeting)
#         print(newEntry)
#         newEntry.save()
#         meetingEntry = MeetingEntry(student=tStudent, meeting=tMeeting)
#         meetingEntry.save()
