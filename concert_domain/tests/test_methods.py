#!/usr/bin/env python3
import unittest
from app.database import session, init_db
from app.models import Band, Venue, Concert
from app.methods import get_band_concerts, get_venue_bands

class TestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()

    def test_get_band_concerts(self):
        band = Band(name="The Beatles", hometown="Liverpool")
        venue = Venue(title="The Cavern Club", city="Liverpool")
        concert = Concert(band=band, venue=venue, date="2024-09-11")
        session.add_all([band, venue, concert])
        session.commit()
        concerts = get_band_concerts(band.id)
        self.assertIn(concert, concerts)

    def test_get_venue_bands(self):
        band = Band(name="The Beatles", hometown="Liverpool")
        venue = Venue(title="The Cavern Club", city="Liverpool")
        concert = Concert(band=band, venue=venue, date="2024-09-11")
        session.add_all([band, venue, concert])
        session.commit()
        bands = get_venue_bands(venue.id)
        self.assertIn(band, bands)

    # def get_band_concerts(band_id):
    #     return session.query(Concert).filter(Concert.band_id == band_id).all()

# if __name__ == "__main__":
#     unittest.main()
