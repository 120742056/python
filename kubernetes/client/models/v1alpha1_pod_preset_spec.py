# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1PodPresetSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'env': 'list[V1EnvVar]',
        'env_from': 'list[V1EnvFromSource]',
        'selector': 'V1LabelSelector',
        'volume_mounts': 'list[V1VolumeMount]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'env': 'env',
        'env_from': 'envFrom',
        'selector': 'selector',
        'volume_mounts': 'volumeMounts',
        'volumes': 'volumes'
    }

    def __init__(self, env=None, env_from=None, selector=None, volume_mounts=None, volumes=None):  # noqa: E501
        """V1alpha1PodPresetSpec - a model defined in OpenAPI"""  # noqa: E501

        self._env = None
        self._env_from = None
        self._selector = None
        self._volume_mounts = None
        self._volumes = None
        self.discriminator = None

        if env is not None:
            self.env = env
        if env_from is not None:
            self.env_from = env_from
        if selector is not None:
            self.selector = selector
        if volume_mounts is not None:
            self.volume_mounts = volume_mounts
        if volumes is not None:
            self.volumes = volumes

    @property
    def env(self):
        """Gets the env of this V1alpha1PodPresetSpec.  # noqa: E501

        Env defines the collection of EnvVar to inject into containers.  # noqa: E501

        :return: The env of this V1alpha1PodPresetSpec.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this V1alpha1PodPresetSpec.

        Env defines the collection of EnvVar to inject into containers.  # noqa: E501

        :param env: The env of this V1alpha1PodPresetSpec.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def env_from(self):
        """Gets the env_from of this V1alpha1PodPresetSpec.  # noqa: E501

        EnvFrom defines the collection of EnvFromSource to inject into containers.  # noqa: E501

        :return: The env_from of this V1alpha1PodPresetSpec.  # noqa: E501
        :rtype: list[V1EnvFromSource]
        """
        return self._env_from

    @env_from.setter
    def env_from(self, env_from):
        """Sets the env_from of this V1alpha1PodPresetSpec.

        EnvFrom defines the collection of EnvFromSource to inject into containers.  # noqa: E501

        :param env_from: The env_from of this V1alpha1PodPresetSpec.  # noqa: E501
        :type: list[V1EnvFromSource]
        """

        self._env_from = env_from

    @property
    def selector(self):
        """Gets the selector of this V1alpha1PodPresetSpec.  # noqa: E501


        :return: The selector of this V1alpha1PodPresetSpec.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1alpha1PodPresetSpec.


        :param selector: The selector of this V1alpha1PodPresetSpec.  # noqa: E501
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def volume_mounts(self):
        """Gets the volume_mounts of this V1alpha1PodPresetSpec.  # noqa: E501

        VolumeMounts defines the collection of VolumeMount to inject into containers.  # noqa: E501

        :return: The volume_mounts of this V1alpha1PodPresetSpec.  # noqa: E501
        :rtype: list[V1VolumeMount]
        """
        return self._volume_mounts

    @volume_mounts.setter
    def volume_mounts(self, volume_mounts):
        """Sets the volume_mounts of this V1alpha1PodPresetSpec.

        VolumeMounts defines the collection of VolumeMount to inject into containers.  # noqa: E501

        :param volume_mounts: The volume_mounts of this V1alpha1PodPresetSpec.  # noqa: E501
        :type: list[V1VolumeMount]
        """

        self._volume_mounts = volume_mounts

    @property
    def volumes(self):
        """Gets the volumes of this V1alpha1PodPresetSpec.  # noqa: E501

        Volumes defines the collection of Volume to inject into the pod.  # noqa: E501

        :return: The volumes of this V1alpha1PodPresetSpec.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this V1alpha1PodPresetSpec.

        Volumes defines the collection of Volume to inject into the pod.  # noqa: E501

        :param volumes: The volumes of this V1alpha1PodPresetSpec.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1PodPresetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
