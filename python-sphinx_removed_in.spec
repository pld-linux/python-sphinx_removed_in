#
# Conditional build:
%bcond_with	tests	# unit tests (missing data)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx Removed In extension
Summary(pl.UTF-8):	Rozszerzenie Sphinksa Removed In
Name:		python-sphinx_removed_in
Version:	0.2.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-removed-in/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-removed-in/sphinx-removed-in-%{version}.tar.gz
# Source0-md5:	c8930e33beb7f3fcaec0166035e2ae02
URL:		https://pypi.org/project/sphinx-removed-in/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-sphinx_testing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-sphinx_testing
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Sphinx extension which recognizes the versionremoved and
removed-in directives.

%description -l pl.UTF-8
Rozszerzenie Sphinksa rozpoznające dyrektywy versionremoved i
removed-in.

%package -n python3-sphinx_removed_in
Summary:	Sphinx Removed In extension
Summary(pl.UTF-8):	Rozszerzenie Sphinksa Removed In
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx_removed_in
This is a Sphinx extension which recognizes the versionremoved and
removed-in directives.

%description -n python3-sphinx_removed_in -l pl.UTF-8
Rozszerzenie Sphinksa rozpoznające dyrektywy versionremoved i
removed-in.

%prep
%setup -q -n sphinx-removed-in-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} tests/test_extension.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} tests/test_extension.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/sphinx_removed_in
%{py_sitescriptdir}/sphinx_removed_in-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_removed_in
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/sphinx_removed_in
%{py3_sitescriptdir}/sphinx_removed_in-%{version}-py*.egg-info
%endif
