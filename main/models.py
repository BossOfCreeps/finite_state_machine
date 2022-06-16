from typing import Union

from django.db import models
from rest_framework.exceptions import NotFound


class STATES(models.TextChoices):
    FALSE = "false", 'Процесс не начат'
    NEW = 'new', 'Заполнен'
    CLOSED = 'closed', 'Отменён'
    IN_PROGRESS = 'in_progress', 'В работе'
    SUCCESS = 'success', 'Успешен'
    ERROR = 'error', 'Ошибка'
    TRUE = "true", 'Процесс завершён'


def decorator(func):
    def wrapper(*args, **kwargs):
        process = args[0]
        state = kwargs.get("state", args[1])

        if state not in process.STATE_MACHINE[process.state]:
            raise NotFound("Из данного состояния нельзя перейти в запрашиваемое")

        return func(*args, **kwargs)

    return wrapper


class BaseProcess(models.Model):
    text = models.CharField("Текст", max_length=256)
    state = models.CharField("Состояние", max_length=256, choices=STATES.choices, default="False")

    STATE_MACHINE = {
        STATES.FALSE: (STATES.NEW,),
        STATES.NEW: (STATES.SUCCESS,),
        STATES.SUCCESS: (STATES.TRUE,),
    }

    @property
    def type(self):
        return "Base"

    @classmethod
    def deep_get(cls, pk) -> Union['BaseProcess', 'ProcessA', 'ProcessB']:
        process = cls.objects.get(id=pk)
        if hasattr(process, "processa"):
            process = process.processa
        elif hasattr(process, "processb"):
            process = process.processb
        return process

    @decorator
    def transition(self, state: STATES, data: dict = None) -> None:
        prev_state = self.state
        self.state = state
        if hasattr(self, f"change_state_from_{prev_state}_to_{state}"):
            getattr(self, f"change_state_from_{prev_state}_to_{state}")(data)
        self.save()

    def change_state_from_false_to_new(self, data: dict = None):
        if data is None:
            data = {}
        self.text = data["text"]

    def __str__(self):
        return self.text


class ProcessA(BaseProcess):
    STATE_MACHINE = {
        STATES.FALSE: (STATES.NEW,),
        STATES.NEW: (STATES.IN_PROGRESS, STATES.CLOSED),
        STATES.IN_PROGRESS: (STATES.SUCCESS, STATES.ERROR),
        STATES.ERROR: (STATES.TRUE,),
        STATES.CLOSED: (STATES.TRUE,),
        STATES.SUCCESS: (STATES.TRUE,),
    }

    @property
    def type(self):
        return "A"


class ProcessB(BaseProcess):
    STATE_MACHINE = {
        STATES.FALSE: (STATES.TRUE,),
    }

    @property
    def type(self):
        return "B"
