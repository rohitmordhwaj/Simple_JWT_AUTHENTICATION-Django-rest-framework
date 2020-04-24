from rest_framework import serializers
from Post.models import Post,Author



class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ['first_name', 'last_name', 'username']
		#read_only_fields = ['first_name', 'last_name', 'username']
class PostSerializer(serializers.ModelSerializer):
	created_by = AuthorSerializer(required=True)
	class Meta:
		model = Post
		fields = ['id', 'text', 'created_by', 'created_at', 'updated_at']


	def create(self, validated_data):
		user_data = validated_data.pop('created_by')
		created_by = AuthorSerializer.create(AuthorSerializer(), validated_data=user_data)
		student, created = Post.objects.update_or_create(created_by=created_by,
                            text=validated_data.pop('text'))
		return student






