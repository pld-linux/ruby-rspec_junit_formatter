%define	pkgname	rspec_junit_formatter
Summary:	RSpec JUnit XML formatter
Name:		ruby-%{pkgname}
Version:	0.1.6
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	43fa23745ef40fb2a2132fe26d11a469
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
%{ruby_vendorlibdir}/rspec/core/formatters/j_unit_formatter.rb
