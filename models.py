from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WaterQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Parameters
    temperature_Min = db.Column(db.Float)
    temperature_Max = db.Column(db.Float)

    ph_Min = db.Column(db.Float)
    ph_Max = db.Column(db.Float)

    conductivity_Min = db.Column(db.Float)
    conductivity_Max = db.Column(db.Float)

    bod_Min = db.Column(db.Float)
    bod_Max = db.Column(db.Float)

    total_coliform_Min = db.Column(db.Float)
    total_coliform_Max = db.Column(db.Float)

    fluoride_Min = db.Column(db.Float)
    fluoride_Max = db.Column(db.Float)

    arsenic_Min = db.Column(db.Float)
    arsenic_Max = db.Column(db.Float)
    
    # Date and Time of the record
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, data):
        # Initialize the object with input data (as a dict)
        self.temperature_Min = data.get('temperature_Min')
        self.temperature_Max = data.get('temperature_Max')

        self.ph_Min = data.get('ph_Min')
        self.ph_Max = data.get('ph_Max')

        self.conductivity_Min = data.get('conductivity_Min')
        self.conductivity_Max = data.get('conductivity_Max')

        self.bod_Min = data.get('bod_Min')
        self.bod_Max = data.get('bod_Max')

        self.total_coliform_Min = data.get('total_coliform_Min')
        self.total_coliform_Max = data.get('total_coliform_Max')

        self.fluoride_Min = data.get('fluoride_Min')
        self.fluoride_Max = data.get('fluoride_Max')

        self.arsenic_Min = data.get('arsenic_Min')
        self.arsenic_Max = data.get('arsenic_Max')
