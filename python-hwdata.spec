%if ! (0%{?fedora} || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif
#%global with_python2 1
%if (0%{?fedora} || 0%{?rhel} > 6)
%global with_python3 1
%else
%global with_python3 0
%endif

Name:		python-hwdata
Version:	2.3.3
Release:	1%{?dist}
Summary:	Python bindings to hwdata package
BuildArch:  noarch
Group:		Development/Libraries
License:	GPLv2
URL:		https://github.com/xsuchy/python-hwdata
# git clone https://github.com/xsuchy/python-hwdata.git
# cd python-hwdata
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python-devel
Requires:	hwdata

%description
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

%if 0%{?with_python3}
%package -n python3-hwdata
Summary:	Python bindings to hwdata package
Group:		Development/Languages

BuildRequires:  python3-devel
Requires:	hwdata

%description -n python3-hwdata
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

This is the Python 3 build of the module.
%endif

%prep
%setup -q

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%license LICENSE
%doc README.md example.py
%doc html
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-hwdata
%license LICENSE
%doc README.md example.py
%doc html
%{python3_sitelib}/*
%endif

%changelog
* Wed Jan 28 2015 Miroslav Suchý <msuchy@redhat.com> 2.3.3-1
- upstream location changed

* Wed Jan 28 2015 Miroslav Suchý <msuchy@redhat.com>
- move upstream location

* Wed Dec 04 2013 Miroslav Suchý <msuchy@redhat.com> 1.10.1-1
- create python3-hwdata subpackage
- Bumping package versions for 1.9
- %%defattr is not needed since rpm 4.4

* Fri Mar 02 2012 Miroslav Suchý 1.7.3-1
- 798375 - fix PCI device name translation (Joshua.Roys@gtri.gatech.edu)
- use setup from distutils

* Fri Mar 02 2012 Jan Pazdziora 1.7.2-1
- Update the copyright year info.

* Fri Mar 02 2012 Jan Pazdziora 1.7.1-1
- correct indentation (mzazrivec@redhat.com)

* Mon Oct 31 2011 Miroslav Suchý 1.6.2-1
- point URL to specific python-hwdata page

* Fri Jul 22 2011 Jan Pazdziora 1.6.1-1
- We only support version 14 and newer of Fedora, removing conditions for old
  versions.

* Mon Apr 26 2010 Miroslav Suchý <msuchy@redhat.com> 1.2-1
- 585138 - change %%files section and patial support for python3

* Fri Apr 23 2010 Miroslav Suchý <msuchy@redhat.com> 1.1-1
- initial release
