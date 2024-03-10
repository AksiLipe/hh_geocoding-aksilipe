from __future__ import annotations

from api import TreeNode, API
from geocoders.geocoder import Geocoder


class MemorizedTreeGeocoder(Geocoder):
    def init(self, samples_count: int | None = None, data_list: list[TreeNode] | None = None):
        super().init(samples=samples_count)
        if data_list is None:
            self.__data = API.get_areas()
        else:
            self.__data = data_list

        self.memory_map = {}

        for country_data in self.__data:
            for area_data in country_data.areas:
                for city_data in area_data.areas:
                    self.memory_map[city_data.id] = f"{country_data.name} {area_data.name} {city_data.name}"
                self.memory_map[area_data.id] = f"{country_data.name} {area_data.name}"
            self.memory_map[country_data.id] = f"{country_data.name}"

    def _apply_geocoding(self, target_id: int) -> str:
        target_id_str = str(target_id)
        return self.memory_map.get(target_id_str, 'Ошибка...')
