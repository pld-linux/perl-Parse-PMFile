#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Parse
%define		pnam	PMFile
Summary:	Parses .pm file as PAUSE does
Name:		perl-Parse-PMFile
Version:	0.36
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	102f1901c15e1b1458b74eb4278558e8
URL:		http://search.cpan.org/dist/Parse-PMFile/
BuildRequires:	perl(JSON::PP) >= 2.00
BuildRequires:	perl(version) >= 0.83
BuildRequires:	perl-ExtUtils-MakeMaker-CPANfile
%if %{with tests}
BuildRequires:	perl(File::Temp) >= 0.19
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl-version
%endif
Requires:	perl(JSON::PP) >= 2.00
Requires:	perl(version) >= 0.83
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The most of the code of this module is taken from the PAUSE code as of
April 2013 almost verbatim. Thus, the heart of this module should be
quite stable. However, I made it not to use pipe ("-|") as well as I
stripped database related code. If you encounter any issue, that's
most probably because of my modification.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist | xargs rm -v

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Parse/PMFile.pm
%{_mandir}/man3/Parse::PMFile.3pm*
