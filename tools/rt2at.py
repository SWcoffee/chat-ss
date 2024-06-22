import random

from curl_cffi.requests import AsyncSession
from utils.logger import get_log_obj

url = "https://token.oaifree.com/api/auth/refresh"
headers = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

log_obj = get_log_obj("rt2at")


async def get_access_token(refresh_token):
    try:

        data = {
            "refresh_token": refresh_token
        }
        async with AsyncSession() as session:
            response = await session.post(url=url,
                                          impersonate=random.choice(["chrome", "safari", "safari_ios"]),
                                          headers=headers,
                                          data=data)

            access_token = response.json().get("access_token")
    except Exception as e:
        log_obj.error(f"获取access_token失败，rt：{refresh_token}")
        access_token = None

    return access_token
