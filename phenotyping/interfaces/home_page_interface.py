import gradio as gr
from typing import Optional

from phenotyping.services.app_factory_service import AppFactoryService
from phenotyping.interfaces.base_interface import BaseInterface
from phenotyping.models.enumerations.app_type import AppType


class HomePageInterface(BaseInterface):
    def __init__(self) -> None:
        """Initialize with no app instance or interface."""
        self.app_instance = None
        self.interface: Optional[gr.Blocks] = None

    def create_interface(self) -> gr.Blocks:
        """Create and return a Gradio interface."""
        app_choices = self._get_app_choices()
        with gr.Blocks(theme=gr.themes.Soft()) as interface:
            self._setup_interface(app_choices)
        self.interface = interface
        return interface

    def _get_app_choices(self) -> list[str]:
        """Return a list of application names for the dropdown."""
        return [""] + [app.name.replace("_", " ").title() for app in AppType]

    def _setup_interface(self, app_choices: list[str]) -> None:
        """Configure UI components and event handlers."""
        gr.Markdown("# Phenotyping Playground")
        gr.Markdown("***BioSense Institute***")
        gr.Markdown("## Select an Application and Run the Demo")

        dropdown = gr.Dropdown(choices=app_choices, label="Choose Application")
        uploaded_image = gr.Image(label="Upload an Image", type="filepath")
        run_button = gr.Button("Run Demo")
        app_status = gr.Textbox(label="App Status", interactive=False)
        image_output = gr.Image(label="Demo Output", type="numpy")

        dropdown.change(
            self._on_dropdown_change, inputs=[dropdown], outputs=[app_status]
        )
        run_button.click(
            self._run_demo, inputs=[uploaded_image], outputs=[image_output]
        )

    def _on_dropdown_change(self, choice: str) -> str:
        """Handle changes in the dropdown to initialize or reset the app."""
        if choice:
            return self._choose_app(choice)
        self.app_instance = None
        return "Please select an application."

    def _run_demo(self, image_path: str) -> str:
        """Execute the demo of the selected application."""
        if self.app_instance:
            return self.app_instance.run_app_demo(image_path=image_path)
        return "No application selected or loaded."

    def _choose_app(self, choice: str) -> str:
        """Select and initialize the application based on user choice."""
        app_type_name = choice.replace(" ", "_").upper()
        try:
            app_type = AppType[app_type_name]
            self.app_instance = AppFactoryService.get_app(app_type)
            return f"{choice} loaded. Click 'Run Demo' to start."
        except KeyError:
            self.app_instance = None
            return "Application not found."

    def launch(self) -> None:
        """Launch the Gradio interface."""
        if not self.interface:
            self.create_interface()
        self.interface.launch()
