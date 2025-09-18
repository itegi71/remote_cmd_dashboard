from django import forms 

#predeefined commands that a user can pick from
PREDEFINED_COMMANDS=[
    ('uptime','check system uptime'),
    ('df -h','check disk space'),
    ('whoami','Show current user'),
    ('ls -la','list files in directory'),
    ('free -m','Show memory usage'),
]

class SSHCommandForm(forms.Form):
    """
    django form for collecting SSH connection info and commands
    """
    hostname=forms.GenericIPAddressField(label='Server IP')
    port=forms.IntegerField(initial=22)
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

    #custom or predefined command

    use_predefined=forms.BooleanField(required=False,initial=False,label="use a predefinedd command")
    predefined_command=forms.ChoiceField(choices=PREDEFINED_COMMANDS,required=False)
    custom_command=forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}),label="or write your own command")

    def clean (self):
        cleaned_data=super().clean()
        use_predefined=cleaned_data.get('use_predefined')
        predefined=cleaned_data.get('predefined_command')
        custom=cleaned_data.get('custom_command')

        if use_predefined and not predefined:
            raise forms.ValidationError('You must select a predefined command')
        elif not use_predefined and not custom:
            raise forms.ValidationError('You must write a custom command')
        
        return cleaned_data