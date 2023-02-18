import strawberry
from query import Query
from mutation import Mutation
from subscription import Subscription


# RUN
schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
