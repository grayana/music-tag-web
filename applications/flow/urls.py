from rest_framework.routers import DefaultRouter

from . import views

flow_router = DefaultRouter()
flow_router.register(r"flow", viewset=views.ProcessViewSets, base_name="flow")
flow_router.register(r"run", viewset=views.ProcessRunViewSets, base_name="run")

node_router = DefaultRouter()
node_router.register(r"template", viewset=views.NodeTemplateViewSet, base_name="template")
