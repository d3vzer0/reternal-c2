MARSHMALLOW_TO_PY_TYPES_PAIRS = (
    # This part of a mapping is carefully selected from marshmallow source code,
    # see marshmallow.BaseSchema.TYPE_MAPPING.
    (fields.String, text_type),
    (fields.DateTime, datetime.datetime),
    (fields.Float, float),
    (fields.Raw, text_type),
    (fields.Boolean, bool),
    (fields.Integer, int),
    (fields.UUID, uuid.UUID),
    (fields.Time, datetime.time),
    (fields.Date, datetime.date),
    (fields.TimeDelta, datetime.timedelta),
    (fields.Decimal, decimal.Decimal),
    # These are some mappings that generally make sense for the rest
    # of marshmallow fields.
    (fields.Email, text_type),
    (fields.Dict, dict),
    (fields.Url, text_type),
    (fields.List, list),
    (fields.Number, decimal.Decimal),
    # This one is here just for completeness sake and to check for
    # unknown marshmallow fields more cleanly.
    (fields.Nested, dict),
)