# builder/forms.py

from django import forms

class PortfolioGenerationForm(forms.Form):
    """
    This form collects all the necessary information from the user
    to generate their personal portfolio website.
    """

    # --- THEME CHOICES ---
    THEME_CHOICES = [
        ('violet', 'Dusk (Violet)'),
        ('indigo', 'Indigo Night'),
        ('teal', 'Deep Teal'),
        ('rose', 'Rose Gold'),
    ]
    FONT_CHOICES = [
        ('sans-serif', 'Modern (Sans-Serif)'),
        ('serif', 'Classic (Serif)'),
    ]

    # --- PERSONAL DETAILS ---
    full_name = forms.CharField(label="Full Name", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'e.g., Jane Doe'}))
    profession = forms.CharField(label="Profession / Title", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'e.g., Photographer & Digital Artist'}))
    
    # NEW: The ImageField for the profile picture
    profile_picture = forms.ImageField(
        label="Profile Picture",
        required=False, # Make it optional
        help_text="Upload a square profile picture or logo."
    )
    
    bio = forms.CharField(label="Short Bio", widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'A brief paragraph about you and your work.'}))
    contact_email = forms.EmailField(label="Contact Email", widget=forms.EmailInput(attrs={'placeholder': 'e.g., contact@janedoe.com'}))

    # --- CUSTOMIZATION ---
    theme_color_name = forms.ChoiceField(label="Theme Color", choices=THEME_CHOICES)
    font_family_name = forms.ChoiceField(label="Font Style", choices=FONT_CHOICES)
    
    # --- PROJECT 1 ---
    project_1_title = forms.CharField(label="Project 1 Title", max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Title of your first project'}))
    project_1_description = forms.CharField(label="Project 1 Description", required=False, widget=forms.Textarea(attrs={'rows': 3}))

    # --- PROJECT 2 ---
    project_2_title = forms.CharField(label="Project 2 Title", max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Title of your second project'}))
    project_2_description = forms.CharField(label="Project 2 Description", required=False, widget=forms.Textarea(attrs={'rows': 3}))

    # --- PROJECT 3 ---
    project_3_title = forms.CharField(label="Project 3 Title", max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Title of your third project'}))
    project_3_description = forms.CharField(label="Project 3 Description", required=False, widget=forms.Textarea(attrs={'rows': 3}))