from django.core.validators import validate_email, RegexValidator, EmailValidator


def validate_phone_email(value):
    if "@" not in value:
        phone_validator = RegexValidator("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$",  # noqa: W605
                                         "Incorrect phone")
        phone_validator(value)
        return value
    email_validator = EmailValidator("Incorrect email")
    email_validator(value)
    return value
