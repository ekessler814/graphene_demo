
import graphene

from .models import CalculatorMemory, Calculation
from .mutations import CreateCalculatorMemory, CreateCalculatorMemoryMutation, CreateCalculationMutation
from .types import CalculatorMemoryType, CalculationType

class Query(graphene.ObjectType):
    calculator_memory = graphene.Field(CalculatorMemoryType, session_name=graphene.String())
    calculation = graphene.Field(CalculationType, id=graphene.Int())
    all_calculator_memories = graphene.List(CalculatorMemoryType)
#   session_name = graphene.List(CalculatorMemoryType)
    # calculation_by_id = graphene.Field(CalculationType, name=graphene.String(required=True))

    def resolve_all_calculator_memories(root, info):
        # We can easily optimize query count in the resolve method
        return CalculatorMemory.objects.select_related("calc_memory").all()

    def resolve_calculation(root, info, id):
        try:
            return Calculation.objects.get(pk=id)
        except Calculation.DoesNotExist:
            return None


class Mutation(graphene.ObjectType):
	create_calculator_memory = CreateCalculatorMemory.Field()
	# create_calculation = graphene.Field(CreateCalculationMutation)


schema = graphene.Schema(query=Query, mutation=Mutation)
