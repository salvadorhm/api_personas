from fastapi import FastAPI
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import status
from fastapi import Depends

users = {
    "dejah@email.com": {
        "username": "dejah",
        "full_name": "Dejah Thoris",
        "email": "dejah@email.com",
        "hashed_password": "12345",
        "disabled": False,
        "token": "dejahToken"
    },
    "john@email.com": {
        "username": "johh",
        "full_name": "John Carter",
        "email": "john@email.com",
        "hashed_password": "67890",
        "disabled": True,
        "token": "johnToken"
    },
}

app = FastAPI()

security = HTTPBasic()
securityBearer = HTTPBearer()

@app.get(
    "/token/",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Regresa el token de un usuario",
    description="Valida username y password con los usuarios registrados",
    tags=["token"],
)
def getToken(credentials: HTTPBasicCredentials = Depends(security)):
    try:
        response = None
        email = credentials.username
        password = credentials.password.encode().decode(("utf-8") )
        
        usuario = users[email]

        if password == usuario["hashed_password"]:
            response = {"token":usuario["token"]}
        else:
            response = {"message":"Error en la contraseña"} 

        return response
    except KeyError:
        response = {"message":"El usuario no existe"} 
        return response

    except Exception as error:
        print(f"Error interno: {error.args}")
        response = {"error": error.args}

@app.get("/",status_code=status.HTTP_202_ACCEPTED,)
async def read_root(credentials: HTTPAuthorizationCredentials = Depends(securityBearer),):
    token = credentials.credentials
    if token == "johnToken":
        response = {"mensaje": f"Bienvenido "}
    else:
        response = {"mensaje": f"MMM algo fallo "}
    return response

