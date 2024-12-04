from typing import Optional
from phenotyping.models.enumerations.app_type import AppType
from phenotyping.demo_apps.base_app import BaseApp
from phenotyping.demo_apps.grounding_dino_segmentation_app import (
    GroundingDinoSegmentationApp,
)


class AppFactoryService:
    @staticmethod
    def get_app(app_type: AppType) -> Optional[BaseApp]:
        if app_type == AppType.GROUNDING_DINO_SEGMENTATION:
            return GroundingDinoSegmentationApp()
        return None
