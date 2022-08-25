from rest_framework import serializers
from APP.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagForPostSerializer(serializers.ModelSerializer):
    name = serializers.MultipleChoiceField(choices=Tag.get_choices())

    class Meta:
        model = Tag
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Post
        exclude = ['description', 'text']


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostAddSerializer(serializers.ModelSerializer):
    tags = TagForPostSerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tags').get('name')
        p = Post.objects.create(**validated_data)
        p.tags.set(tags)
        return p

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', )
        instance.description = validated_data.get('description')
        instance.text = validated_data.get('text')
        instance.source = validated_data.get('source')
        instance.date = validated_data.get('date')

        tags = validated_data.get('tags').get('name')
        instance.tags.set(tags)
        instance.save()
        return instance

