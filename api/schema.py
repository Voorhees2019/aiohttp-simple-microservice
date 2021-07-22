from marshmallow import Schema, fields


class SuccessSchema(Schema):
    result = fields.String()


class BadRequestSchema(Schema):
    error = fields.Integer()
