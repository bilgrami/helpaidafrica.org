# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.location import Location  # noqa: F401,E501
from swagger_server import util


class AuditInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, created_date: datetime=None, created_by_user_id: int=None, created_location: Location=None, last_updated_date: datetime=None, last_updated_by_user_id: int=None, last_updated_location: Location=None):  # noqa: E501
        """AuditInfo - a model defined in Swagger

        :param created_date: The created_date of this AuditInfo.  # noqa: E501
        :type created_date: datetime
        :param created_by_user_id: The created_by_user_id of this AuditInfo.  # noqa: E501
        :type created_by_user_id: int
        :param created_location: The created_location of this AuditInfo.  # noqa: E501
        :type created_location: Location
        :param last_updated_date: The last_updated_date of this AuditInfo.  # noqa: E501
        :type last_updated_date: datetime
        :param last_updated_by_user_id: The last_updated_by_user_id of this AuditInfo.  # noqa: E501
        :type last_updated_by_user_id: int
        :param last_updated_location: The last_updated_location of this AuditInfo.  # noqa: E501
        :type last_updated_location: Location
        """
        self.swagger_types = {
            'created_date': datetime,
            'created_by_user_id': int,
            'created_location': Location,
            'last_updated_date': datetime,
            'last_updated_by_user_id': int,
            'last_updated_location': Location
        }

        self.attribute_map = {
            'created_date': 'createdDate',
            'created_by_user_id': 'createdByUserId',
            'created_location': 'createdLocation',
            'last_updated_date': 'lastUpdatedDate',
            'last_updated_by_user_id': 'lastUpdatedByUserId',
            'last_updated_location': 'lastUpdatedLocation'
        }
        self._created_date = created_date
        self._created_by_user_id = created_by_user_id
        self._created_location = created_location
        self._last_updated_date = last_updated_date
        self._last_updated_by_user_id = last_updated_by_user_id
        self._last_updated_location = last_updated_location

    @classmethod
    def from_dict(cls, dikt) -> 'AuditInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AuditInfo of this AuditInfo.  # noqa: E501
        :rtype: AuditInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_date(self) -> datetime:
        """Gets the created_date of this AuditInfo.


        :return: The created_date of this AuditInfo.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date: datetime):
        """Sets the created_date of this AuditInfo.


        :param created_date: The created_date of this AuditInfo.
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def created_by_user_id(self) -> int:
        """Gets the created_by_user_id of this AuditInfo.


        :return: The created_by_user_id of this AuditInfo.
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id: int):
        """Sets the created_by_user_id of this AuditInfo.


        :param created_by_user_id: The created_by_user_id of this AuditInfo.
        :type created_by_user_id: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def created_location(self) -> Location:
        """Gets the created_location of this AuditInfo.


        :return: The created_location of this AuditInfo.
        :rtype: Location
        """
        return self._created_location

    @created_location.setter
    def created_location(self, created_location: Location):
        """Sets the created_location of this AuditInfo.


        :param created_location: The created_location of this AuditInfo.
        :type created_location: Location
        """

        self._created_location = created_location

    @property
    def last_updated_date(self) -> datetime:
        """Gets the last_updated_date of this AuditInfo.


        :return: The last_updated_date of this AuditInfo.
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date: datetime):
        """Sets the last_updated_date of this AuditInfo.


        :param last_updated_date: The last_updated_date of this AuditInfo.
        :type last_updated_date: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def last_updated_by_user_id(self) -> int:
        """Gets the last_updated_by_user_id of this AuditInfo.


        :return: The last_updated_by_user_id of this AuditInfo.
        :rtype: int
        """
        return self._last_updated_by_user_id

    @last_updated_by_user_id.setter
    def last_updated_by_user_id(self, last_updated_by_user_id: int):
        """Sets the last_updated_by_user_id of this AuditInfo.


        :param last_updated_by_user_id: The last_updated_by_user_id of this AuditInfo.
        :type last_updated_by_user_id: int
        """

        self._last_updated_by_user_id = last_updated_by_user_id

    @property
    def last_updated_location(self) -> Location:
        """Gets the last_updated_location of this AuditInfo.


        :return: The last_updated_location of this AuditInfo.
        :rtype: Location
        """
        return self._last_updated_location

    @last_updated_location.setter
    def last_updated_location(self, last_updated_location: Location):
        """Sets the last_updated_location of this AuditInfo.


        :param last_updated_location: The last_updated_location of this AuditInfo.
        :type last_updated_location: Location
        """

        self._last_updated_location = last_updated_location