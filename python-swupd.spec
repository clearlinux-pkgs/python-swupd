#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-swupd
Version  : 0.1
Release  : 8
URL      : https://github.com/clearlinux/python-swupd/archive/0.1.tar.gz
Source0  : https://github.com/clearlinux/python-swupd/archive/0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: python-swupd-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Python swupd bindings
=====================
Module Description
``````````````````

%package python
Summary: python components for the python-swupd package.
Group: Default

%description python
python components for the python-swupd package.


%prep
%setup -q -n python-swupd-0.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
