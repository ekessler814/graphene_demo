
from graphene_django.types import DjangoObjectType
from .models import CalculatorMemory, Calculation

class CalculatorMemoryType(DjangoObjectType):
    class Meta:
        model = CalculatorMemory
        fields = ('id', 'session_name', 'datetime_created')

    # def create(self, validated_data):
    #     if 'datetime_created' in validated_data:
    #         # disallow user specifying datetime_created on creation
    #         del validated_data['datetime_created']
    #     return super(CalculatorMemorySerializer, self).create(validated_data)

class CalculationType(DjangoObjectType):
    class Meta:
        model = Calculation
        fields = ('id', 'inputs', 'result', 'calculator_memory', 'datetime_created')

    # override create function so we may modify param
    # def create(self, validated_data):
    #     if 'datetime_created' in validated_data:
    #         # disallow user specifying datetime_created on creation
    #         del validated_data['datetime_created']
    #     # run our calculate function from operations file on inputs and set
    #     # value of result to output of calculate
    #     validated_data['result'] = calculate(validated_data['inputs'])
    #     return super(CalculationSerializer, self).create(validated_data)
