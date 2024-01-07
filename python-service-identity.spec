# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-service-identity
Epoch: 100
Version: 24.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Service identity verification for pyOpenSSL & cryptography
License: MIT
URL: https://github.com/pyca/service-identity/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
service-identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes. In
the simplest case, this means host name verification. However,
service-identity implements RFC 6125 fully.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-service-identity
Summary: Service identity verification for pyOpenSSL & cryptography
Requires: python3
Requires: python3-attrs >= 19.1.0
Requires: python3-pyasn1-modules
Requires: python3-pyasn1
Requires: python3-cryptography
Provides: python3-service-identity = %{epoch}:%{version}-%{release}
Provides: python3dist(service-identity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-service-identity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(service-identity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-service-identity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(service-identity) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-service-identity
service-identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes. In
the simplest case, this means host name verification. However,
service-identity implements RFC 6125 fully.

%files -n python%{python3_version_nodots}-service-identity
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-service-identity
Summary: Service identity verification for pyOpenSSL & cryptography
Requires: python3
Requires: python3-attrs >= 19.1.0
Requires: python3-pyasn1-modules
Requires: python3-pyasn1
Requires: python3-cryptography
Provides: python3-service-identity = %{epoch}:%{version}-%{release}
Provides: python3dist(service-identity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-service-identity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(service-identity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-service-identity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(service-identity) = %{epoch}:%{version}-%{release}

%description -n python3-service-identity
service-identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes. In
the simplest case, this means host name verification. However,
service-identity implements RFC 6125 fully.

%files -n python3-service-identity
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-service-identity
Summary: Service identity verification for pyOpenSSL & cryptography
Requires: python3
Requires: python3-attrs >= 19.1.0
Requires: python3-pyasn1-modules
Requires: python3-pyasn1
Requires: python3-cryptography
Provides: python3-service-identity = %{epoch}:%{version}-%{release}
Provides: python3dist(service-identity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-service-identity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(service-identity) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-service-identity = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(service-identity) = %{epoch}:%{version}-%{release}

%description -n python3-service-identity
service-identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes. In
the simplest case, this means host name verification. However,
service-identity implements RFC 6125 fully.

%package -n python3-service-identity+idna
Summary: Metapackage for python3-service-identity: idna extras
Requires: python3-service-identity = %{epoch}:%{version}-%{release}
Requires: python3-idna

%description -n python3-service-identity+idna
This is a metapackage bringing in idna extras requires for
python3-service-identity. It makes sure the dependencies are installed.

%files -n python3-service-identity
%license LICENSE
%{python3_sitelib}/*

%files -n python3-service-identity+idna
%license LICENSE
%endif

%changelog
