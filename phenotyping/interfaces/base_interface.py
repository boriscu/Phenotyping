from abc import ABC, abstractmethod
from typing import Any


class BaseInterface(ABC):
    @abstractmethod
    def create_interface(self) -> Any:
        """
        Create and return a Gradio interface.

        Returns:
            Any: The created Gradio interface.
        """
        pass
