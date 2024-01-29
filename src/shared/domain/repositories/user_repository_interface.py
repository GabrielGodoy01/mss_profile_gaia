from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from src.shared.domain.entities.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create_profile(self, user_id: str, name: str, email: str) -> User:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def update_user_by_id(self, new_user_data: User) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass