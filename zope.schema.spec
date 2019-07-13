#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.schema
Version  : 4.9.3
Release  : 30
URL      : https://files.pythonhosted.org/packages/42/eb/23663ac53661641340f74cb27647f5dcdde63fc4629b4a4c1a0a29c049dc/zope.schema-4.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/eb/23663ac53661641340f74cb27647f5dcdde63fc4629b4a4c1a0a29c049dc/zope.schema-4.9.3.tar.gz
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
BuildRequires : tox
BuildRequires : virtualenv

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

%description python3
python3 components for the zope.schema package.


%prep
%setup -q -n zope.schema-4.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541281708
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.schema
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.schema/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.schema/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
