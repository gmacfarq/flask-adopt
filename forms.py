"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import (StringField, URLField,
                    BooleanField, SelectField, TextAreaField)
from wtforms.validators import (InputRequired, URL, Length,
                    AnyOf, Optional)

SPECIES = ['dog','cat','porcupine']
AGES = [
            ("baby"),
            ("young"),
            ("adult"),
            ("senior")
        ]

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    
    name = StringField("Name",
            validators=[
                Length(30),
                InputRequired()
                ])
    species = StringField("Species",
            validators=[
                Length(30),
                InputRequired(),
                AnyOf(SPECIES)
            ])
    photo_url = URLField("Profile Picture",
            validators=[
                Optional(),
                URL(),
            ])
    age = SelectField("Age Group",

            choices=AGES,
            validators=[
                Length(6),
                InputRequired(),
            ])

    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing pet information"""

    photo_url = URLField("Profile Picture",
            validators=[
                Optional(),
                URL(),
            ])

    notes = StringField("Notes")

    available = BooleanField("Availability")