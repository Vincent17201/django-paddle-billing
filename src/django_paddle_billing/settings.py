from django.conf import settings
from django_json_widget.widgets import JSONEditorWidget

CONFIG_DEFAULTS = {
    "PADDLE_API_TOKEN": "",
    "PADDLE_CLIENT_TOKEN": "",
    "PADDLE_SECRET_KEY": "",
    "PADDLE_API_URL": "https://sandbox-api.paddle.com",
    "PADDLE_IPS": ["34.232.58.13", "34.195.105.136", "34.237.3.244", "35.155.119.135", "52.11.166.252", "34.212.5.7"],
    "PADDLE_SANDBOX_IPS": [
        "34.194.127.46",
        "54.234.237.108",
        "3.208.120.145",
        "44.226.236.210",
        "44.241.183.62",
        "100.20.172.113",
    ],
    #34.194.127.46,100.64.0.173, 100.64.7.96, 100.64.7.216


    "PADDLE_SANDBOX": False,
    "PADDLE_ACCOUNT_MODEL": settings.AUTH_USER_MODEL,
    "ADMIN_READONLY": True,
    "ADMIN_JSON_EDITOR_WIDGET": JSONEditorWidget,
    "PADDLE_ACCOUNT_MODEL_IDENTIFIER": "user_id",
    "SYNC_AND_WEBHOOK_CUSTOMER_INCLUDE_ADDRESSES": False,
    "SYNC_AND_WEBHOOK_CUSTOMER_INCLUDE_BUSINESSES": False,
    "SYNC_CUSTOMER_INCLUDE_SUBSCRIPTIONS": True,
}


def get_config(settings_name=None):
    if settings_name is None:
        settings_name = "PADDLE_BILLING"

    return {**CONFIG_DEFAULTS, **getattr(settings, settings_name, {})}


settings = get_config()
