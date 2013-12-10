from django.contrib.auth.models import User, Group
from django.forms import widgets
from rest_framework import serializers
from models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, EducationInformation, PersonalInformation

# if you want to use 'url' in field you must declare HyperlinkedModelSerializer in class
# HyperlinkedModelSerializer and ModelSerializer are request class Meta:
# class Meta must have model and fields
# ModelSerializer is normal to get fields

# HyperlinkedModelSerializer
# ModelSerializer
# Serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')     # define field that use to show in json or api


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')    # define field that use to show in json or api


class EducationInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EducationInformation
        fields = ('url', 'primary_school', 'secondary_school', 'post_secondary_education')  # define field that use to show in json or api


class PersonalInformationSerializer(serializers.HyperlinkedModelSerializer):
    education = EducationInformationSerializer()

    class Meta:
        model = PersonalInformation
        fields = ('first_name', 'last_name', 'age', 'url', 'education')  # define field that use to show in json or api


class SnippetSerializer(serializers.Serializer):

    # define field that use to show in json or api and you can define filed name that show in api 'pk' >>> 'primary'

    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    title = serializers.CharField(required=False,
                                  max_length=100)
    code = serializers.CharField(widget=widgets.Textarea,
                                 max_length=100000)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
                                       default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES,
                                    default='friendly')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance

        # Create new instance
        return Snippet(**attrs)