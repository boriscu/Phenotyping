import numpy as np

from phenotyping.demo_apps.base_app import BaseApp
from phenotyping.models.enumerations.app_type import AppType
from phenotyping.modules.segmentation.GroundingDINO.groundingdino.util.inference import (
    load_model,
    load_image,
    predict,
    annotate,
)


class GroundingDinoSegmentationApp(BaseApp):
    def __init__(self) -> None:
        super().__init__()

    def run_app_demo(
        self,
        image_path: str = "assets/apple_tree.jpg",
        text_prompt: str = "leaf . apple . branch .",
        box_threshold: float = 0.25,
        text_threshold: float = 0.15,
    ) -> np.ndarray:
        self.model = load_model(
            "phenotyping/modules/segmentation/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py",
            "phenotyping/modules/segmentation/GroundingDINO/weights/groundingdino_swint_ogc.pth",
        )

        image_source, image = load_image(image_path)
        boxes, logits, phrases = predict(
            model=self.model,
            image=image,
            caption=text_prompt,
            box_threshold=box_threshold,
            text_threshold=text_threshold,
            device="cpu",
        )
        annotated_frame = annotate(
            image_source=image_source, boxes=boxes, logits=logits, phrases=phrases
        )
        return annotated_frame
