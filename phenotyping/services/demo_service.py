from phenotyping.interfaces.home_page_interface import HomePageInterface


class DemoService:
    def __init__(self) -> None:
        """Initialize DemoService with the desired interface."""
        self.interface = HomePageInterface()

    def launch(self) -> None:
        """Launch the Gradio interface for the demo service."""
        if not self.interface:
            self.create_interface()
        self.interface.launch()
