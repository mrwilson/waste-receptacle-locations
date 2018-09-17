import csv
import json


def read_csv():
    with open('receptacles.csv') as f:
        return list(csv.DictReader(f))


def row_to_point(row):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [
                float(row['longitude']),
                float(row['latitude'])
            ]
        },
        'properties': {
            'general': int(row['general']),
            'recycle_plastic': int(row['recycle_plastic']),
            'recycle_paper': int(row['recycle_paper']),
            'dog': int(row['dog'])

        }
    }


def generate_geojson():
    return {
        'type': 'FeatureCollection',
        'features': [row_to_point(row) for row in read_csv()]
    }


def write_to_file(output):
    with open('receptacles.geojson', "w") as schema:
        schema.write(json.dumps(output))


if __name__ == '__main__':
    write_to_file(generate_geojson())
