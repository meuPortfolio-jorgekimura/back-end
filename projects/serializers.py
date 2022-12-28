from rest_framework import serializers
from .models import Project, Link
import ipdb
from rest_framework.validators import UniqueValidator
from techs.serializers import TechSerializer
from techs.models import Tech


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            "id",
            "git_hub",
            "vercel",
        ]
        extra_kwargs = {
            "git_hub": {
                "validators": [
                    UniqueValidator(
                        queryset=Link.objects.all(),
                        message="This github link is already used in other project",
                    )
                ]
            },
            "vercel": {
                "validators": [
                    UniqueValidator(
                        queryset=Link.objects.all(),
                        message="This vercel link is already used in other project",
                    )
                ]
            },
        }


class ProjectSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Project:
        links_out = validated_data.pop("links")
        links, _ = Link.objects.get_or_create(**links_out)
        validated_data["links"] = links
        techs_out = validated_data.pop("techs")
        project = Project.objects.create(**validated_data)
        for tech in techs_out:
            techs, _ = Tech.objects.get_or_create(**tech)
            project.techs.add(techs)

        return project

    links = LinkSerializer()

    techs = TechSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "objective",
            "img_url",
            "title",
            "links",
            "techs",
        ]
        extra_kwargs = {
            "img_url": {
                "validators": [
                    UniqueValidator(
                        queryset=Project.objects.all(),
                        message="This img url is already used in other project",
                    )
                ]
            },
        }
