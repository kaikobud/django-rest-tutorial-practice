# Created by kaikobud at ২০/৭/২০
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


"""
HyperlinkedRelatedField: when we use HyperlinkedModelSerializer instead of
ModelSerializer, use should use HyperlinkedRelatedField intead of PrimaryKeyRelatedField.
PrimaryKeyRelatedField is used for reverse relation.

HyperlinkedIdentityField: it is used for any direct field of current Model to show as a hyperlinked
field in the api.
"""


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'title', 'code',
                  'linenos', 'language', 'style', 'created_by']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='snippet-detail',
                                                   queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
