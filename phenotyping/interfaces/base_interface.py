import gradio as gr
from abc import ABC, abstractmethod


class BaseInterface(ABC):
    @abstractmethod
    def create_interface(self) -> gr.Blocks:
        """
        Create and return a Gradio interface.

        Returns:
            gr.Blocks: The created Gradio interface.
        """
        pass

    @abstractmethod
    def launch(self) -> None:
        """
        Launch the Gradio interface.
        """
        pass
