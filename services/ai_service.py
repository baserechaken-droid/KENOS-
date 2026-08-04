from services.service_manager import register
from core.brain import think


class AIService:

    def process(self, text):
        return think(text)


register("ai", AIService())
