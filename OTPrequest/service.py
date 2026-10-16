import secrets
from datetime import datetime, timedelta, timezone

from repository import OTPRepository


class OTPService:
    def __init__(self, repository: OTPRepository):
        self.repository = repository
    #    self.repository = repository — मिळालेला Repository object Service मध्ये जतन केला जातो, जेणेकरून Service त्याच्या methods वापरू शकेल
    def generate_otp(self, mobile: str) -> str:
        # (mobile: str — mobile number string स्वरूपात येतो.
        #  -> str — ही method string परत करेल, अशी type hint आहे.
        
        otp = f"{secrets.randbelow(1_000_000):06d}"

        expires_at = datetime.now(timezone.utc) + timedelta(minutes=5)

        self.repository.save(mobile, otp, expires_at)
        #   “या mobile number साठी OTP, त्याची expiry time आणि सुरुवातीचे attempts save कर.”
        return otp

    def verify_otp(self, mobile: str, submitted_otp: str) -> bool:
        record = self.repository.get(mobile)
        # (mobile)user ne taklela mobile no

        if not record:
            return False

        now = datetime.now(timezone.utc)

        if now >= record["expires_at"]:
            self.repository.delete(mobile)
            return False

        if record["attempts"] >= 5:
            self.repository.delete(mobile)
            return False

        if secrets.compare_digest(record["otp"], submitted_otp):
            self.repository.delete(mobile)
            return True

        self.repository.increment_attempts(mobile)
        return False