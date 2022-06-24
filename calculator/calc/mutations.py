
import graphene
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType

from .types import CalculatorMemoryType, CalculationType
from .models import CalculatorMemory, Calculation
from .serializers import CalculatorMemorySerializer, CalculationSerializer

from graphene.types.scalars import Scalar

class ObjectField(Scalar): # to serialize error message from serializer
    @staticmethod
    def serialize(dt):
        return dt

class CreateCalculatorMemory(graphene.Mutation):
    calculator_memory = graphene.Field(CalculatorMemoryType)
    message=ObjectField()
    status=graphene.Int()

    class Arguments:
        session_name=graphene.String(required=True)

    @classmethod
    def mutate(cls,root,info,**kwargs):
        serializer=CalculatorMemorySerializer(data=kwargs)
        if serializer.is_valid():
            obj=serializer.save()
            msg='success'
        else:
            msg=serializer.errors
            obj=None
            print(msg)
        return cls(calculator_memory=obj,message=msg,status=200)



class CreateCalculatorMemoryMutation(SerializerMutation):
    class Meta:
            serializer_class = CalculatorMemorySerializer
            model_operations = ['create']
            lookup_field = 'name'

class CreateCalculationMutation(SerializerMutation):
	class Meta:
            serializer_class = CalculationSerializer
            model_operations = ['create']
