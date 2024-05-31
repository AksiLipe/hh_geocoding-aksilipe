from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """
        area = API.get_area(area_id)
        result = [area.name]
        while area.parent_id is not None:
            area = API.get_area(area.parent_id)
            result.append(area.name)
        result = result[::-1]
        return ', '.join(result)
