from marshmallow import Schema, fields, INCLUDE


class SuccessSchema(Schema):
    result = fields.String()


class BadRequestSchema(Schema):
    error = fields.Integer()


class TimeSuccessSchema(Schema):
    time = fields.String()


class FibonacciRequestSchema(Schema):
    n = fields.Integer()


class FibonacciSuccessSchema(Schema):
    fibonacci_seq = fields.List(fields.Integer())


class DictUpdateSuccessSchema(Schema):
    class Meta:
        unknown = INCLUDE
