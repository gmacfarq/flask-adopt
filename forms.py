"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import (StringField, URLField,
                    BooleanField, SelectField, TextAreaField)
from wtforms.validators import (InputRequired, URL,
                    AnyOf, Optional)

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name",
            validators=[InputRequired()])
    species = StringField("Species",
            validators=[
                InputRequired(),
                AnyOf(['dog','cat','porcupine']),
            ])
    photo_url = URLField("Profile Picture",
            validators=[
                Optional(),
                URL(),
            ])
    age = SelectField("Age Group",
            choices=[
                ("baby"),
                ("young"),
                ("adult"),
                ("senior")
            ],
            validators=[
                InputRequired(),
            ])

    notes = StringField("Notes",
            validators=[
                Optional(),
            ])

class EditPetForm(FlaskForm):
    """Form for editing pet information"""

    photo_url = URLField("Profile Picture",
            validators=[
                Optional(),
                URL(),
            ])

    notes = StringField("Notes",
            validators=[
                Optional(),
            ])

    available = BooleanField("Availability",
            validators=[
                Optional(),
            ])