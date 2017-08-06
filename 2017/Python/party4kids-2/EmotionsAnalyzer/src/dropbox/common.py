# -*- coding: utf-8 -*-
# Auto-generated by Stone, do not modify.
# flake8: noqa
# pylint: skip-file
try:
    from . import stone_validators as bv
    from . import stone_base as bb
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import stone_validators as bv
    import stone_base as bb

class InvalidPathRootError(object):
    """
    :ivar path_root: The latest path root id for user's team if the user is
        still in a team.
    """

    __slots__ = [
        '_path_root_value',
        '_path_root_present',
    ]

    _has_required_fields = False

    def __init__(self,
                 path_root=None):
        self._path_root_value = None
        self._path_root_present = False
        if path_root is not None:
            self.path_root = path_root

    @property
    def path_root(self):
        """
        The latest path root id for user's team if the user is still in a team.

        :rtype: str
        """
        if self._path_root_present:
            return self._path_root_value
        else:
            return None

    @path_root.setter
    def path_root(self, val):
        if val is None:
            del self.path_root
            return
        val = self._path_root_validator.validate(val)
        self._path_root_value = val
        self._path_root_present = True

    @path_root.deleter
    def path_root(self):
        self._path_root_value = None
        self._path_root_present = False

    def __repr__(self):
        return 'InvalidPathRootError(path_root={!r})'.format(
            self._path_root_value,
        )

InvalidPathRootError_validator = bv.Struct(InvalidPathRootError)

class PathRoot(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar home: Paths are relative to the authenticating user's home directory,
        whether or not that user belongs to a team.
    :ivar member_home: Paths are relative to the authenticating team member's
        home directory. (This results in :field:`PathRootError.invalid' if the
        user does not belong to a team.)
    :ivar str team: Paths are relative to the given team directory. (This
        results in :field:`PathRootError.invalid` if the user is not a member of
        the team associated with that path root id.)
    :ivar user_home: Paths are relative to the user's home directory. (This
        results in ``PathRootError.invalid`` if the belongs to a team.)
    :ivar str shared_folder: Paths are relative to given shared folder id (This
        results in :field:`PathRootError.no_permission` if you don't have access
        to  this shared folder.)
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    home = None
    # Attribute is overwritten below the class definition
    member_home = None
    # Attribute is overwritten below the class definition
    user_home = None
    # Attribute is overwritten below the class definition
    other = None

    @classmethod
    def team(cls, val):
        """
        Create an instance of this class set to the ``team`` tag with value
        ``val``.

        :param str val:
        :rtype: PathRoot
        """
        return cls('team', val)

    @classmethod
    def shared_folder(cls, val):
        """
        Create an instance of this class set to the ``shared_folder`` tag with
        value ``val``.

        :param str val:
        :rtype: PathRoot
        """
        return cls('shared_folder', val)

    def is_home(self):
        """
        Check if the union tag is ``home``.

        :rtype: bool
        """
        return self._tag == 'home'

    def is_member_home(self):
        """
        Check if the union tag is ``member_home``.

        :rtype: bool
        """
        return self._tag == 'member_home'

    def is_team(self):
        """
        Check if the union tag is ``team``.

        :rtype: bool
        """
        return self._tag == 'team'

    def is_user_home(self):
        """
        Check if the union tag is ``user_home``.

        :rtype: bool
        """
        return self._tag == 'user_home'

    def is_shared_folder(self):
        """
        Check if the union tag is ``shared_folder``.

        :rtype: bool
        """
        return self._tag == 'shared_folder'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def get_team(self):
        """
        Paths are relative to the given team directory. (This results in
        ``PathRootError.invalid`` if the user is not a member of the team
        associated with that path root id.)

        Only call this if :meth:`is_team` is true.

        :rtype: str
        """
        if not self.is_team():
            raise AttributeError("tag 'team' not set")
        return self._value

    def get_shared_folder(self):
        """
        Paths are relative to given shared folder id (This results in
        ``PathRootError.no_permission`` if you don't have access to  this shared
        folder.)

        Only call this if :meth:`is_shared_folder` is true.

        :rtype: str
        """
        if not self.is_shared_folder():
            raise AttributeError("tag 'shared_folder' not set")
        return self._value

    def __repr__(self):
        return 'PathRoot(%r, %r)' % (self._tag, self._value)

PathRoot_validator = bv.Union(PathRoot)

class PathRootError(bb.Union):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar InvalidPathRootError invalid: The path root id value in
        Dropbox-API-Path-Root header is no longer valid.
    :ivar no_permission: You don't have permission to access the path root id in
        Dropbox-API-Path-Root  header.
    """

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    no_permission = None
    # Attribute is overwritten below the class definition
    other = None

    @classmethod
    def invalid(cls, val):
        """
        Create an instance of this class set to the ``invalid`` tag with value
        ``val``.

        :param InvalidPathRootError val:
        :rtype: PathRootError
        """
        return cls('invalid', val)

    def is_invalid(self):
        """
        Check if the union tag is ``invalid``.

        :rtype: bool
        """
        return self._tag == 'invalid'

    def is_no_permission(self):
        """
        Check if the union tag is ``no_permission``.

        :rtype: bool
        """
        return self._tag == 'no_permission'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def get_invalid(self):
        """
        The path root id value in Dropbox-API-Path-Root header is no longer
        valid.

        Only call this if :meth:`is_invalid` is true.

        :rtype: InvalidPathRootError
        """
        if not self.is_invalid():
            raise AttributeError("tag 'invalid' not set")
        return self._value

    def __repr__(self):
        return 'PathRootError(%r, %r)' % (self._tag, self._value)

PathRootError_validator = bv.Union(PathRootError)

Date_validator = bv.Timestamp(u'%Y-%m-%d')
DisplayName_validator = bv.String(min_length=1, pattern=u'[^/:?*<>"|]*')
DropboxTimestamp_validator = bv.Timestamp(u'%Y-%m-%dT%H:%M:%SZ')
EmailAddress_validator = bv.String(max_length=255, pattern=u"^['&A-Za-z0-9._%+-]+@[A-Za-z0-9-][A-Za-z0-9.-]*.[A-Za-z]{2,15}$")
NamePart_validator = bv.String(min_length=1, max_length=100, pattern=u'[^/:?*<>"|]*')
NamespaceId_validator = bv.String(pattern=u'[-_0-9a-zA-Z:]+')
PathRootId_validator = NamespaceId_validator
SessionId_validator = bv.String()
SharedFolderId_validator = NamespaceId_validator
InvalidPathRootError._path_root_validator = bv.Nullable(PathRootId_validator)
InvalidPathRootError._all_field_names_ = set(['path_root'])
InvalidPathRootError._all_fields_ = [('path_root', InvalidPathRootError._path_root_validator)]

PathRoot._home_validator = bv.Void()
PathRoot._member_home_validator = bv.Void()
PathRoot._team_validator = PathRootId_validator
PathRoot._user_home_validator = bv.Void()
PathRoot._shared_folder_validator = PathRootId_validator
PathRoot._other_validator = bv.Void()
PathRoot._tagmap = {
    'home': PathRoot._home_validator,
    'member_home': PathRoot._member_home_validator,
    'team': PathRoot._team_validator,
    'user_home': PathRoot._user_home_validator,
    'shared_folder': PathRoot._shared_folder_validator,
    'other': PathRoot._other_validator,
}

PathRoot.home = PathRoot('home')
PathRoot.member_home = PathRoot('member_home')
PathRoot.user_home = PathRoot('user_home')
PathRoot.other = PathRoot('other')

PathRootError._invalid_validator = InvalidPathRootError_validator
PathRootError._no_permission_validator = bv.Void()
PathRootError._other_validator = bv.Void()
PathRootError._tagmap = {
    'invalid': PathRootError._invalid_validator,
    'no_permission': PathRootError._no_permission_validator,
    'other': PathRootError._other_validator,
}

PathRootError.no_permission = PathRootError('no_permission')
PathRootError.other = PathRootError('other')

ROUTES = {
}

