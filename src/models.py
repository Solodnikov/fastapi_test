from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # активный реферальный код
    referral_code_id = Column(
        Integer, ForeignKey("referral_codes.id"), nullable=True)
    # реферер, который пригласил реферала
    referrer_id = Column(
        Integer, ForeignKey("users.id"), nullable=True)

    referral_code = relationship("ReferralCode", back_populates="user")
    referrer = relationship(
        "User", remote_side=[id], back_populates="referrals")
    referrals = relationship("User", back_populates="referrer")


class ReferralCode(Base):
    __tablename__ = "referral_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    expiration_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="referral_code")
