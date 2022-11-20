from django.core.validators import (EmailValidator, RegexValidator,
                                    validate_email)


def validate_phone_email(value):
    email_validator = EmailValidator("Incorrect email")
    email_validator(value)
    return value
