from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField


class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.RegexField(required=True, regex=r'^(?![\d+_@.-0-9]+$)[a-zA-Zа-яА-ЯіІ]*$',)
    last_name = serializers.RegexField(required=False, allow_blank=True,
                                       regex=r'^(?![\d+_@.-0-9]+$)[a-zA-Zа-яА-ЯіІ]*$')
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    phone = PhoneNumberField(min_length=13, required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

