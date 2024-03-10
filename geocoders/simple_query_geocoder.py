from geocoders.geocoder import Geocoder
from api import API

class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, target_id: str) -> str:

        current_node = API.get_area(target_id)
        full_address = current_node.name

        if current_node.parent_id is None:
            return full_address

        while parent_node := API.get_area(current_node.parent_id):

            full_address = parent_node.name + ' ' + full_address

            if parent_node.parent_id is None:
                break

        return full_address