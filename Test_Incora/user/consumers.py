from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

from .models import User
from .serializers import UserProfileSerializer
from djangochannelsrestframework.mixins import ListModelMixin


class Consumer(ListModelMixin, ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    @action()
    async def subscribe_to_message(self, **kwargs):
        await self.message_activity.subscribe()

    @model_observer(User)
    async def message_activity(self, message, **kwargs):
        await self.send_json(message)

    @message_activity.serializer
    def message_activity(self, instance: User, action, **kwargs):
        return dict(data=UserProfileSerializer(instance).data, action=action.value)



