from http.client import HTTPException

from fastapi import FastAPI
from auth import auth_router
from category import category_router
from orders import order_router
from product import product_router
from fastapi_jwt_auth import AuthJWT
from schemas import JwtModel

app = FastAPI()
@AuthJWT.load_config
def config():
    return JwtModel()

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(order_router)
app.include_router(product_router)

@app.get("/")
async def landing():
    return {
        "message": "This is landing page"
    }

@app.get("/user")
async def intro():
    return {
        "message": "user page"
    }

@app.get("/user/{id}")
async def intro(id: int):
    return {
        "message": f"user - {id}"
    }

@app.post("/user")
async def intro():
    return {
        "message": "This is post request"
    }

@app.get("/test2")
async def test2():
    return {
        "message": "This is test page"

    }


@auth_router.post("/login")
async def login(user: LoginModel, Authorize: AuthJWT=Depends()):
    check_user = session.query(User).filter(User.username == user.username).first()

    if check_user and security.check_password_hash(check_user.password, user.password):
        access_token = Authorize.create_access_token(subject=check_user.username)
        refresh_token = Authorize.create_refresh_token(subject=check_user.username)
        data = {
            "success": True,
            "code": 200,
            "msg": "Success Login",
            "token": {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        }
        return jsonable_encoder(data)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"username yoki password xato")