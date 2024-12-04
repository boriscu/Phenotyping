import gradio as gr
from phenotyping.interfaces.base_interface import BaseInterface
from phenotyping.services.app_factory_service import AppFactoryService
from phenotyping.models.enumerations.app_type import AppType


class HomePageInterface(BaseInterface):
    def __init__(self) -> None:
        """Initialize DemoService with the list of available application types."""
        self.app_instance = None
        self.interface = None

    def create_interface(self):
        """Create the Gradio interface for the demo service."""
        app_choices = [""] + [app.name.replace("_", " ").title() for app in AppType]
        with gr.Blocks(theme=gr.themes.Soft()) as interface:
            gr.Markdown("# Phenotyping playground")
            gr.Markdown("***BioSense Institute***")
            gr.Markdown("## Select an Application and Run the Demo")

            dropdown = gr.Dropdown(
                choices=app_choices, label="Choose Application", value=""
            )
            with gr.Row():
                run_button = gr.Button("Run Demo")
                app_status = gr.Textbox(label="App Status", interactive=False)

            image_output = gr.Image(label="Demo Output", type="numpy")

            def on_dropdown_change(choice):
                """Handle changes in the dropdown to initialize the app or reset the interface."""
                if choice:
                    message = self.choose_app(choice)
                else:
                    self.app_instance = None
                    message = "Please select an application."
                return message

            def run_demo():
                """Execute the demo of the selected application."""
                if self.app_instance:
                    image_path = self.app_instance.run_app_demo()
                    return image_path
                else:
                    return "No application selected or loaded."

            dropdown.change(on_dropdown_change, inputs=[dropdown], outputs=[app_status])
            run_button.click(run_demo, inputs=[], outputs=[image_output])

            self.interface = interface
        return interface

    def choose_app(self, choice: str):
        """Select and initialize the application based on user choice."""
        app_type_name = choice.replace(" ", "_").upper()
        try:
            app_type = AppType[app_type_name]
            self.app_instance = AppFactoryService.get_app(app_type)
            return f"{choice} loaded. Click 'Run Demo' to start."
        except KeyError:
            self.app_instance = None
            return "Application not found."

    def launch(self):
        """Launch the Gradio interface."""
        if not self.interface:
            self.create_interface()
        self.interface.launch()
