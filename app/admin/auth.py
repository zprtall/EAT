from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):

    async def login(
        self,
        request: Request
    ) -> bool:

        form = await request.form()

        username = form["username"]
        password = form["password"]


        if (
            username == "admin"
            and password == "secret"
        ):
            request.session["admin"] = True
            return True

        return False


    async def logout(
        self,
        request: Request
    ) -> bool:

        request.session.clear()
        return True


    async def authenticate(
        self,
        request: Request
    ) -> bool:

        return request.session.get("admin", False)