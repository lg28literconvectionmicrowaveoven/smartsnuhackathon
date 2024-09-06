from resources.water_params import WaterParams


def initialize_routes(api):
    # Define the routes/endpoints for Water Parameters
    api.add_resource(WaterParams, "/api/water_params", "/api/water_params/<id>")
