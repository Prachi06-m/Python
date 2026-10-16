from fastapi import APIRouter
# schemas मध्ये request आणि response चा data कसा असावा हे define केलेले असते.
from schemas import (
    OTPRequest,
    OTPVerifyRequest,
    OTPResponse,
    VerifyResponse
)
from controller import OTPController
from service import OTPService
from repository import OTPRepository


router = APIRouter(prefix="/api/otp", tags=["OTP"])

repository = OTPRepository()           
service = OTPService(repository)
controller = OTPController(service)


@router.post("/generate", response_model=OTPResponse)
def generate_otp(request: OTPRequest):
    return controller.generate(request)
# (याचा अर्थ त्या controller object मधील generate() method call करणे आणि त्याला request object देणे.)

@router.post("/verify", response_model=VerifyResponse)
def verify_otp(request: OTPVerifyRequest):
    return controller.verify(request)
# Import म्हणजे दुसऱ्या file मधील class किंवा function आपल्या file मध्ये वापरण्यासाठी उपलब्ध करून घेणे.
# response_model=OTPResponse म्हणजे FastAPI ला सांगणे की, या API चा response OTPResponse schema प्रमाणे असावा.