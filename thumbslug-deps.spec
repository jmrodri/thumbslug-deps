%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio
%define __jar_repack %{nil}

Name: thumbslug-deps
Summary: Build dependencies for Thumbslug
Group: Internet/Applications
License: Various
Version: 0.0.4
Release: 1%{?dist}
URL: http://fedorahosted.org/thumbslug
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: Red Hat, Inc
BuildArch: noarch

%description
Fill me in!

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/thumbslug/lib/
cp repo/*.jar $RPM_BUILD_ROOT%{_datadir}/thumbslug/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/thumbslug/lib/

%changelog
* Tue Jul 12 2011 Chris Duryee (beav) <cduryee@redhat.com>
- add files (cduryee@redhat.com)

* Tue Jul 12 2011 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Mon Jul 11 2011 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Mon Jul 11 2011 Chris Duryee <cduryee@redhat.com> 0.0.1-1
- first cut
