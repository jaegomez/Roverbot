from flask import Flask
from flask_restful import Resource, Api, reqparse

import RPi.GPIO as gpio

from time import sleep

app = Flask(__name__)
api = Api(app)

# These are the ways the robot will move
# left motor pins
motor_left_forward = 27
motor_left_backward = 22

# right motor pins
motor_right_forward = 5
motor_right_backward = 6


class Movement(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("direction", type=str, required=True, help="I need a direction to move")
        args = parser.parse_args()

        dir = args["direction"]

        self.move(dir.lower())

        return {"success": True}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("direction", type=str, required=True, help="I need a direction to move")
        args = parser.parse_args()

        dir = args["direction"]

        self.move(dir.lower())

        return {"success": True}

    def move(self, direction):
        if direction == "forward":
            gpio.output(motor_left_forward, gpio.HIGH)
            gpio.output(motor_right_forward, gpio.HIGH)
        elif direction == "backward":
            gpio.output(motor_right_backward, gpio.HIGH)
            gpio.output(motor_left_backward, gpio.HIGH)
        elif direction == "left":
            gpio.output(motor_right_forward, gpio.HIGH)
            gpio.output(motor_left_forward, gpio.LOW)
        elif direction == "right":
            gpio.output(motor_left_forward, gpio.HIGH)
            gpio.output(motor_right_forward, gpio.LOW)
        elif direction == "rightreverse":
            gpio.output(motor_right_backward, gpio.LOW)
            gpio.output(motor_left_backward, gpio.HIGH)
        elif direction == "leftreverse":
            gpio.output(motor_left_backward, gpio.LOW)
            gpio.output(motor_right_backward, gpio.HIGH)


class Stop(Resource):

    def get(self):
        gpio.output(motor_left_forward, gpio.LOW)
        gpio.output(motor_right_backward, gpio.LOW)
        gpio.output(motor_right_forward, gpio.LOW)
        gpio.output(motor_left_backward, gpio.LOW)

        return {"success": True}

    def post(self):
        gpio.output(motor_left_forward, gpio.LOW)
        gpio.output(motor_left_backward, gpio.LOW)
        gpio.output(motor_right_backward, gpio.LOW)
        gpio.output(motor_right_forward, gpio.LOW)

        return {"success": True}

api.add_resource(Movement, "/movement")
api.add_resource(Stop, "/stop")

if __name__ == "__main__":
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(True)
    gpio.setup(motor_left_forward, gpio.OUT)
    gpio.setup(motor_left_backward, gpio.OUT)
    gpio.setup(motor_right_forward, gpio.OUT)
    gpio.setup(motor_right_backward, gpio.OUT)

    app.run(debug=True, host="")
