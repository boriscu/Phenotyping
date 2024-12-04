import cv2
from phenotyping.demo_apps.base_app import BaseApp
from phenotyping.models.enumerations.app_type import AppType
from phenotyping.modules.segmentation.GroundingDINO.groundingdino.util.inference import (
    load_model,
    load_image,
    predict,
    annotate,
)


class GroundingDinoSegmentationApp(BaseApp):
    def __init__(self, app_type: AppType) -> None:
        super().__init__()
        self.model = load_model(
            "phenotyping/modules/segmentation/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py",
            "phenotyping/modules/segmentation/GroundingDINO/weights/groundingdino_swint_ogc.pth",
        )

    def run_app_demo(
        self,
        image_path: str,
        text_prompt: str,
        box_threshold: float,
        text_threshold: float,
    ) -> None:
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
        cv2.imwrite("annotated_image.jpg", annotated_frame)
        print("Segmentation completed and image saved.")
