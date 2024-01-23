from fastapi import APIRouter, Depends, BackgroundTasks

from auth.base_config import current_user
from tasks.tasks import send_email_report_test

router = APIRouter(prefix="/report")


@router.get("/test")
def get_test_mail(background_tasks: BackgroundTasks, user=Depends(current_user)):
    background_tasks.add_task(send_email_report_test. user.username)
    # send_email_report_test(user.username)
    return{
        "status": 200,
        "data": "Письмо отправлено",
        "derails": None
    }
