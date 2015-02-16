# coding=utf-8
"""Form Validator Function."""

from validate_email import validate_email


def is_required_valid(req_input):
    """Validate input that required.

    :param req_input: input that neeeds to be validated
    :type req_input: str
    """
    req_input = req_input.strip()
    if len(req_input) != 0:
        return True

    return False


def is_email_address_valid(email):
    """Validate the email address.

    :param email: email input
    :type email: str
    This function uses library from: https://pypi.python
    .org/pypi/validate_email
    It can check if the host has SMTP Server and the email
    does exist. Due to issue here: https://github
    .com/SyrusAkbary/validate_email/issues/4 and sometimes it takes long time
    to  check SMTP Server, this feature is not used.
    """
    is_valid_email = validate_email(email)
    return is_valid_email


def is_boolean(param_input):
    """Check if param_input string is boolean 'type'.

    :param param_input: input that need to be checked
    :type param_input: str
    """
    if param_input.lower() not in ['true', 'false']:
        return False
    return True
