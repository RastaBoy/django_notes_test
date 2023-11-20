from dataclasses import dataclass


@dataclass
class RegisterRequest:
    name : str
    email : str
    password : str


@dataclass
class AuthorizationRequest:
    email : str
    password : str