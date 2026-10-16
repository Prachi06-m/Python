from fastapi import FastAPI
from router import router
# print ("server started")for create fastapi application
app = FastAPI(
    title="TFLInsurance OTP API",
    version="1.0.0",
    description="OTP generation and verification learning project"
)
# (establish connection between application and routes)
app.include_router(router) 

# print("route config")
@app.get("/")
def home():
    # print("url handler function invoke")
    return {"message": "Welcome to TFLInsurance OTP API"}


