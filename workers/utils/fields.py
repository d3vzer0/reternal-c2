
class SchemaFields:
    def __init__(self, schema, iterate=False):
        self.schema = schema
        self.iterate = iterate

    def nested(self, nested):
        field_parameters = { }
        for field_name, options in nested.items():
            field_type = options.__class__.__name__
            field_options = {'required': options.required,
                'metadata': options.metadata, 'type': field_type }
            field_options['default'] = '' if not options.default else options.default
            if field_type == 'Nested' and self.iterate == True: 
                    field_options['nested'] = self.nested(options.nested)
            field_parameters[field_name] = field_options
        return field_parameters

    def get(self):
        attribute_tree = self.nested(self.schema.fields)
        return attribute_tree
