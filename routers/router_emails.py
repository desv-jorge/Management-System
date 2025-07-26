from fastapi import APIRouter

from providers.email_provider import confirm_email

from models.email import Model_email_confirm

router = APIRouter()

@router.post("/confirm")
def email_confirm(confirm_email_body : Model_email_confirm):
    return confirm_email(confirm_email_body)