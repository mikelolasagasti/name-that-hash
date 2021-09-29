%global pypi_name name-that-hash


Name:           python-%{pypi_name}
Version:        1.10
Release:        2%{?dist}
Summary:        The Modern Hash Identification System

License:        GPLv3+
URL:            https://github.com/HashPals/Name-That-Hash
Source0:        https://github.com/HashPals/Name-That-Hash/archive/%{version}/Name-That-Hash-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other
hashes.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# required for check
BuildRequires:  pytest

%description -n python3-%{pypi_name}
Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other
hashes.

%prep
%autosetup -n Name-That-Hash-%{version}
sed --in-place '1{\@^#! /usr/bin/env python@d}' name_that_hash/__main__.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files name_that_hash

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/name-that-hash
%{_bindir}/nth

%changelog
* Wed Sep 29 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.10.0-2
- Changes based on revision BZ#2007765

* Fri Sep 24 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.10.0-1
- Initial package.
