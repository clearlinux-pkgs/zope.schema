#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.schema
Version  : 6.2.0
Release  : 53
URL      : https://files.pythonhosted.org/packages/b3/db/53f1ae9115b357ad012c5297ce9e3597a1608a02bdcc4707718a16060a27/zope.schema-6.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b3/db/53f1ae9115b357ad012c5297ce9e3597a1608a02bdcc4707718a16060a27/zope.schema-6.2.0.tar.gz
Summary  : zope.interface extension for defining data schemas
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.schema-license = %{version}-%{release}
Requires: zope.schema-python = %{version}-%{release}
Requires: zope.schema-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.event
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.event
BuildRequires : zope.interface

%description
zope.schema
        =============

%package license
Summary: license components for the zope.schema package.
Group: Default

%description license
license components for the zope.schema package.


%package python
Summary: python components for the zope.schema package.
Group: Default
Requires: zope.schema-python3 = %{version}-%{release}

%description python
python components for the zope.schema package.


%package python3
Summary: python3 components for the zope.schema package.
Group: Default
Requires: python3-core
Provides: pypi(zope.schema)
Requires: pypi(setuptools)
Requires: pypi(zope.event)
Requires: pypi(zope.interface)

%description python3
python3 components for the zope.schema package.


%prep
%setup -q -n zope.schema-6.2.0
cd %{_builddir}/zope.schema-6.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634587307
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.schema
cp %{_builddir}/zope.schema-6.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.schema/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.schema/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
