from fastapi import FastAPI
from app.api.routes.email_routes import router as email_router
from app.services.email_service import EmailService


app=FastAPI(title="Forgot Password API",description="Password reset")
app.state.email_service=Emailservice()
app.include_router(email_router)
@app.get("/")
def home():
    return{
        "application":"Email API",
        "message":"Welcome to Email REST API",
        "docs":"/docs"

    }
