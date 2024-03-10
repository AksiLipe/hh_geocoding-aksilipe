from __future__ import annotations

from api import API, TreeNode
from geocoders.geocoder import Geocoder


class SimpleTreeGeocoder(Geocoder):
    def init(self, samples_count: int | None = None, data_list: list[TreeNode] | None = None):
        super().init(samples=samples_count)
        if data_list is None:
            self.__data_list = API.get_areas()
        else:
            self.__data_list = data_list

    def _apply_geocoding(self, area_id_input: int) -> str:
        area_id_str = str(area_id_input)

        for country_obj in self.__data_list:
            for country_area in country_obj.areas:
                for city_area in country_area.areas:
                    if city_area.id == area_id_str:
                        return f"country_obj.name country_area.name city_area.name"
                if country_area.id == area_id_str:
                    return f"country_obj.name country_area.name"
            if country_obj.id == area_id_str:
                return f"country_obj.name"
