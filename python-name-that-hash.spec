%global pypi_name name-that-hash
%global name_with_underscore name_that_hash
%global name_capitalized Name-That-Hash


Name:           python-%{pypi_name}
Version:        1.10
Release:        1%{?dist}
Summary:        The Modern Hash Identification System

License:        GPLv3+
URL:            https://github.com/HashPals/Name-That-Hash
Source0:        https://github.com/HashPals/Name-That-Hash/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other
hashes

%package -n     python3-%{pypi_name}
Summary:        %{summary}

# required for check
BuildRequires:  pytest

%description -n python3-%{pypi_name}
Name That Hash will name that hash type! Identify MD5, SHA256 and 300+ other
hashes

%prep
%autosetup -n %{name_capitalized}-%{version}
sed --in-place '1{\@^#! /usr/bin/env python@d}' name_that_hash/__main__.py

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name_with_underscore}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/name-that-hash
%{_bindir}/nth

%changelog
* Fri Sep 24 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.10.0-1
- Initial package.
