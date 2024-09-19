from enum import Enum


class AuthType(Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class AlertType(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class EquipmentType(Enum):
    NEW = "NEW"
    USED = "USED"


class EquipmentStatus(Enum):
    PURCHASED = "PURCHASED"
    INSTALLED = "INSTALLED"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    REMOVED = "REMOVED"
