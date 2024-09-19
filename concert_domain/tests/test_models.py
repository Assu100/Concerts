import unittest
from app.database import session, init_db
from app.models import Band, Venue, Concert

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()

    def test_band_creation(self):
        band = Band(name="The Beatles", hometown="Liverpool")
        session.add(band)
        session.commit()
        self.assertIsNotNone(band.id)

    def test_concert_creation(self):
        band = Band(name="The Beatles", hometown="Liverpool")
        venue = Venue(title="The Cavern Club", city="Liverpool")
        concert = Concert(band=band, venue=venue, date="2024-09-11")
        session.add(concert)
        session.commit()
        self.assertIsNotNone(concert.id)

    

