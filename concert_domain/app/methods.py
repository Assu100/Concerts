from .models import Band, Venue, Concert
from .database import session

def get_band_concerts(band_id):
    band = session.get(Band, band_id)  
    if band:
        return band.concerts
    return []

def get_venue_bands(venue_id):
    venue = session.get(Venue, venue_id)  
    if venue:
        return venue.bands()
    return []

