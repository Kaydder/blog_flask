from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NewPostForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[
            DataRequired(message="Title is required."),
            Length(min=3, max=100, message="Title must be between 3 and 100 characters."),
        ],
    )
    
    content = TextAreaField(
        "Content",
        validators=[
            DataRequired(message="Content is required."),
            Length(min=10, message="Content must be at least 10 characters long."),
        ],
    )

    author = StringField(
        "Author",
        validators=[
            DataRequired(message="Author is required."),
            Length(min=2, max=50, message="Author must be between 2 and 50 characters."),
        ],
    )

    submit = SubmitField("Publish Post")