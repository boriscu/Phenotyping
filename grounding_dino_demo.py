from modules.segmentation.GroundingDINO.groundingdino.util.inference import (
    load_model,
    load_image,
    predict,
    annotate,
)
import cv2

model = load_model(
    "modules/segmentation/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py",
    "modules/segmentation/GroundingDINO/weights/groundingdino_swint_ogc.pth",
)
IMAGE_PATH = "assets/apple_tree.jpg"
TEXT_PROMPT = "apple . leaf . dog ."
BOX_TRESHOLD = 0.35
TEXT_TRESHOLD = 0.25

image_source, image = load_image(IMAGE_PATH)

boxes, logits, phrases = predict(
    model=model,
    image=image,
    caption=TEXT_PROMPT,
    box_threshold=BOX_TRESHOLD,
    text_threshold=TEXT_TRESHOLD,
    device="cpu",
)

annotated_frame = annotate(
    image_source=image_source, boxes=boxes, logits=logits, phrases=phrases
)
cv2.imwrite("annotated_image.jpg", annotated_frame)
