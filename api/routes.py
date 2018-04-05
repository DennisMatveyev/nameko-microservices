from flask import request
from nameko.standalone.rpc import ClusterRpcProxy


CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}


def init_routes(app):
    @app.route('/calculate', methods=['POST'])
    def calculate():
        """
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: data
              properties:
                operation:
                  type: string
                  enum:
                    - sum
                    - mul
                    - sub
                    - div
                email:
                  type: string
                value:
                  type: integer
                other:
                  type: integer
        responses:
          200:
            description: Wait the calculation, you'll receive an email with result
        """
        operation = request.json.get('operation')
        value = request.json.get('value')
        other = request.json.get('other')
        email = request.json.get('email')
        msg = "Wait the calculation, you'll receive an email with result"
        subject = "Calc started"

        with ClusterRpcProxy(CONFIG) as rpc:
            rpc.email.send.async(email, subject, msg)
            rpc.calculate.calculate.async(operation, value, other, email)
            return msg, 200
