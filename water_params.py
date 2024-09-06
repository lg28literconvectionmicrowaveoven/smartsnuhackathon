from datetime import datetime

from flask_restful import Resource, reqparse
from models import WaterQuality, db


class WaterParams(Resource):
    def get(self, id=None):
        if id:
            # Get specific water quality record by ID
            water_quality = WaterQuality.query.get_or_404(id)
            return water_quality.to_dict()
        else:
            # Get all records
            records = WaterQuality.query.all()
            return [record.to_dict() for record in records], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True)
        parser.add_argument("temperature_min", type=float, required=True)
        parser.add_argument("temperature_max", type=float, required=True)
        parser.add_argument("pH_min", type=float, required=True)
        parser.add_argument("pH_max", type=float, required=True)
        parser.add_argument("conductivity_min", type=float, required=False)
        parser.add_argument("conductivity_max", type=float, required=False)
        parser.add_argument("bod_min", type=float, required=False)
        parser.add_argument("bod_max", type=float, required=False)
        parser.add_argument("coliform_min", type=float, required=True)
        parser.add_argument("coliform_max", type=float, required=True)
        parser.add_argument("fluoride_min", type=float, required=True)
        parser.add_argument("fluoride_max", type=float, required=True)
        parser.add_argument("arsenic_min", type=float, required=True)
        parser.add_argument("arsenic_max", type=float, required=True)
        parser.add_argument(
            "timestamp",
            type=lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S"),
            required=True,
        )

        # Parse input arguments
        data = parser.parse_args()

        # Create a new water quality record
        new_record = WaterQuality(data)
        db.session.add(new_record)
        db.session.commit()

        return {
            "message": "Water quality record created successfully",
            "data": new_record.to_dict(),
        }, 201

    def delete(self, id):
        water_quality = WaterQuality.query.get_or_404(id)
        db.session.delete(water_quality)
        db.session.commit()
        return {"message": "Record deleted successfully"}, 200
