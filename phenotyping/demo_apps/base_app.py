from abc import ABC, abstractmethod


class BaseApp(ABC):
    """Abstract base class for applications."""

    @abstractmethod
    def run_app_demo(self, **kwargs) -> None:
        """Run a demo execution for the application. Must be implemented by each subclass."""
        pass
