from rest_framework.response import Response


class CustomResponse:

    def __init__(self, data=None, success=True, message='successful', status=200):
        self.data = data
        self.success = success
        self.message = message
        self.status = 200

    def failed(self, message='unsuccessful'):
        self.message = message
        self.success = False
        self.status = 200

        return self

    def server_error(self, message='an unknown server error occurred', error=None):
        print(error)
        self.message = message
        self.success = False
        self.status = 500

        return self

    def bad_request(self, message='invalid request'):
        self.message = message
        self.success = False
        self.status = 400

        return self

    def unauthorized(self, message='unauthorized'):
        self.message = message
        self.success = False
        self.status = 401

        return self

    def forbidden(self, message='forbidden'):
        self.message = message
        self.success = False
        self.status = 403

        return self

    def get(self):
        return {
            'success': self.success,
            'message': self.message,
            'data': self.data,
        }

    def response(self):
        return Response({
            'success': self.success,
            'message': self.message,
            'data': self.data,
        }, self.status)
