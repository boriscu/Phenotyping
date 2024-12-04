import gradio as gr

from phenotyping.services.app_factory_service import AppFactoryService
from phenotyping.models.enumerations.app_type import AppType


class DemoService:
    def __init__(self) -> None:
        """Initialize DemoService with the list of available application types."""
        self.apps = list(AppType)
        self.app_instance = None
        self.interface = None

    def create_interface(self):
        """Creates a Gradio interface for the demo service."""
        with gr.Blocks() as interface:
            gr.Markdown("### GroundingDINO Segmentation Demo")
            image_path = gr.Textbox(label="Image Path")
            text_prompt = gr.Textbox(label="Text Prompt")
            box_threshold = gr.Slider(
                minimum=0.0, maximum=1.0, step=0.01, label="Box Threshold"
            )
            text_threshold = gr.Slider(
                minimum=0.0, maximum=1.0, step=0.01, label="Text Threshold"
            )
            run_button = gr.Button("Run Segmentation")
            output_text = gr.Textbox(label="Output", visible=False)
            run_button.click(
                self.run_demo,
                inputs=[image_path, text_prompt, box_threshold, text_threshold],
                outputs=output_text,
            )
        self.interface = interface
        return interface

    def choose_app(self, choice: str) -> str:
        """Select an application based on the user's choice and initialize it."""
        try:
            app_type_name = choice.replace(" ", "_").upper()
            app_type = AppType[app_type_name]
            self.app_instance = AppFactoryService.get_app(app_type)
            if self.app_instance:
                return "Application loaded successfully. Click 'Run Demo' to start."
            else:
                return "Failed to load application."
        except KeyError:
            return "Invalid selection. Please select a valid application type."

    def run_demo(self, image_path, text_prompt, box_threshold, text_threshold) -> str:
        """Run the selected application demo with provided parameters."""
        if not self.app_instance:
            self.choose_app("GROUNDING_DINO_SEGMENTATION")
        if self.app_instance:
            self.app_instance.run_app_demo(
                image_path=image_path,
                text_prompt=text_prompt,
                box_threshold=box_threshold,
                text_threshold=text_threshold,
            )
            return "Segmentation completed and image saved as 'annotated_image.jpg'"
        return "No application loaded. Please select an application first."

    def launch(self) -> None:
        """Launch the Gradio interface for the demo service."""
        if not self.interface:
            self.create_interface()
        self.interface.launch()
