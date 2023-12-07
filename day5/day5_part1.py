from pathlib import Path
from time import time

FILE = Path(__file__).parent / 'input'


class Mapper:
    def __init__(self, mapper_data) -> None:
        self.mapper_raw = mapper_data
        self.name = ''
        self.mappers = []

        self._create_map()

    def get(self, seed: int) -> int:
        for mapper in self.mappers:
            if seed in mapper['range']:
                return seed + mapper['destination'] - mapper['source']
        return seed

    def _create_map(self) -> None:
        self.name, *mappers = self.mapper_raw.split('\n')
        for i, map_data in enumerate(mappers):
            d, s, rng = list(map(int, map_data.split(' ')))
            self.mappers.append(
                {
                    'range': range(s, s + rng),
                    'source': s,
                    'destination': d,
                }
            )


class LocationSeeker:
    def __init__(self, data: list) -> None:
        seeds, *mappers = data
        self.seed_ids = list(map(int, seeds.split(' ')[1:]))
        self.mappers = [Mapper(mapper_data) for mapper_data in mappers]

    def get_locations(self) -> list[int]:
        final_locations = []
        for seed_id in self.seed_ids:
            print(f'Getting location for {seed_id}')
            previous_map = seed_id
            for mapper in self.mappers:
                previous_map = mapper.get(previous_map)
            final_locations.append(previous_map)

        return final_locations


if __name__ == '__main__':
    with FILE.open() as f:
        data = f.read().split('\n\n')

    t1 = time()
    location_seeker = LocationSeeker(data)
    locations = location_seeker.get_locations()

    print('\nAll locations:', locations)
    print('ANSWER:', min(locations))
    print(f'Took {time() - t1} seconds', end='\n\n')
