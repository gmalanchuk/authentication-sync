from starlette import status


class BaseExceptions:
    @staticmethod
    def _is_invalid(value1: str, value2: str | None = None):
        value2 = f"or {value2} " if value2 else ""
        detail = f"{value1} {value2}is invalid"
        status_code = status.HTTP_401_UNAUTHORIZED
        return detail, status_code

    @staticmethod
    def _has_expired(value: str):
        detail = f"{value} has expired"
        status_code = status.HTTP_401_UNAUTHORIZED
        return detail, status_code

    @staticmethod
    def _must_be_confirmed(value: str):
        detail = f"To perform this action, your {value} must be confirmed"
        status_code = status.HTTP_401_UNAUTHORIZED
        return detail, status_code

    @staticmethod
    def _login_required():
        detail = "Login required"
        status_code = status.HTTP_401_UNAUTHORIZED
        return detail, status_code

    @staticmethod
    def _not_found(value: str):
        detail = f"{value} not found"
        status_code = status.HTTP_404_NOT_FOUND
        return detail, status_code
