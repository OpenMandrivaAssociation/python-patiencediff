%global pypi_name patiencediff
Name:           python-%{pypi_name}
Version:        0.2.1
Release:        2
Summary:        Python implementation of the patiencediff algorithm

License:        GPLv2+
URL:            https://www.breezy-vcs.org/
Source0:        https://files.pythonhosted.org/packages/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Remove redundant shebang and conditional from __main__.py
Patch1:   https://github.com/breezy-team/patiencediff/pull/5.patch
# Remove redundant shebang from _patiencediff_py.py
Patch2:   https://github.com/breezy-team/patiencediff/commit/7b2657d92ac7b56b07a92e5acfebf05f67a70e9c.patch
# Fix typo in README
Patch3:   https://github.com/breezy-team/patiencediff/pull/6.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  gcc

%global _description %{expand:
This package contains the implementation of the patiencediff algorithm, as
first described by Bram Cohen. Like Python's difflib, this module provides
both a convenience unified_diff function for the generation of unified diffs of
text files as well as a SequenceMatcher that can be used on arbitrary
lists. Patiencediff provides a good balance of performance, nice output for
humans, and implementation simplicity.}

%description %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
export CC=gcc
export CXX=g++
%py_build

%install
%py_install

%check
python setup.py test

%files
%license COPYING
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 15 2020 Ondřej Pohořelský <opohorel@redhat.com> - 0.2.1-1
- Initial package.

