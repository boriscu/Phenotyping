import gradio as gr
from phenotyping.services.app_factory_service import AppFactoryService
from phenotyping.models.enumerations.app_type import AppType


def create_interface():
    def run_demo(image_path, text_prompt, box_threshold, text_threshold):
        app_instance = AppFactoryService.get_app(AppType.GROUNDING_DINO_SEGMENTATION)
        app_instance.run_app_demo(
            image_path, text_prompt, box_threshold, text_threshold
        )
        return "Annotated image saved as 'annotated_image.jpg'"

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
        run_button.click(
            run_demo,
            inputs=[image_path, text_prompt, box_threshold, text_threshold],
            outputs=None,
        )

    return interface


def launch():
    interface = create_interface()
    interface.launch()
