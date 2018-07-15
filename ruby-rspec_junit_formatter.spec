%define	pkgname	rspec_junit_formatter
Summary:	RSpec JUnit XML formatter
Name:		ruby-%{pkgname}
Version:	0.4.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	d73b8e71c3081da34e7bcc4b3252bdda
URL:		http://github.com/sj26/rspec_junit_formatter
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-builder
Requires:	ruby-rspec >= 2.0
Requires:	ruby-rspec-core > 2.12.0
Requires:	ruby-rubygems >= 1.3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RSpec results that Hudson/Jenkins can read.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{ruby_vendorlibdir}/rspec_junit_formatter.rb
%{ruby_vendorlibdir}/rspec_junit_formatter
