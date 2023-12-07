import logging
from pathlib import Path
from time import time


FILE = Path(__file__).parent / 'input'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Mapper:
    def __init__(self, mapper_data) -> None:
        self.mapper_raw = mapper_data
        self.name = ''
        self.map = {}

        self._create_map()

    def get(self, seed: int) -> int:
        return self.map.get(seed, seed)
    
    def _create_map(self) -> None:
        self.name, *mappers = self.mapper_raw.split('\n')
        m_length = len(mappers)
        for i, map_data in enumerate(mappers):
            t1 = time()
            print(f'Creating map: {self.name}\t[{i + 1}/{m_length}]...', end=' ')

            d, s, rng = list(map(int, map_data.split(' ')))
            row_map = dict(zip(range(s, s + rng), range(d, d + rng)))
            self.map.update(row_map)
            
            print(f'{time() - t1} sec.')


class LocationSeeker:
    def __init__(self, data: list) -> None:
        seeds, *mappers = data
        self.seed_ids = list(map(int, seeds.split(' ')[1:]))
        self.mappers = [Mapper(mapper_data) for mapper_data in mappers]

    def get_locations(self):
        locations = []
        for seed_id in self.seed_ids:
            print(f'Getting location for {seed_id}')
            previsous_map = seed_id
            for mapper in self.mappers:
                previsous_map = mapper.get(previsous_map)
            locations.append(previsous_map)

        return locations


if __name__ == '__main__':
    with FILE.open() as f:
        data = f.read().split('\n\n')

    t1 = time()
    location_seeker = LocationSeeker(data)
    locations = location_seeker.get_locations()
    print(f'Took {time() - t1} seconds', end='\n\n')

    print('All locations:', locations)
    print('ANSWER:', min(locations))
