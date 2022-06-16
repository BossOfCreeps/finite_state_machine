from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from main.models import BaseProcess, STATES
from main.serializers import BaseProcessSerializer


class ProcessesView(ListAPIView):
    queryset = BaseProcess.objects.all()
    serializer_class = BaseProcessSerializer


class ProcessView(CreateAPIView, RetrieveAPIView):
    queryset = BaseProcess.objects.all()
    serializer_class = BaseProcessSerializer

    def post(self, request, *args, **kwargs):
        process = BaseProcess.deep_get(kwargs.get("pk"))
        process.transition(STATES(request.data.get("state", "").lower()))
        return Response(self.get_serializer_class()(process).data)
