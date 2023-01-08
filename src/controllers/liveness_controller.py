from instance import server
from flask_restplus import Resource

health_check = server.health_check


@health_check.route('/liveness', methods=['GET'])
class LivenessController(Resource):
    def get(self):
        return 'I am alive'