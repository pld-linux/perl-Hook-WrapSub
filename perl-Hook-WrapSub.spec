#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Hook
%define		pnam	WrapSub
Summary:	Hook::WrapSub - wrap subs with pre- and post-call hooks
Summary(pl):	Hook::WrapSub - obudowanie procedur w wywo�ania przed i po wywo�aniu
Name:		perl-Hook-WrapSub
Version:	0.03
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Hook/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7a5e42aca06d6ba06dcbd5e2cb5769bf
URL:		http://search.cpan.org/dist/Hook-WrapSub/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This function enables intercepting a call to any named function;
handlers may be added both before and after the call to the
intercepted function.

For example:

  wrap_subs \&before, 'some_func', \&after;

In this case, whenever the sub named 'some_func' is called, the
&before sub is called first, and the &after sub is called afterwards.
These are both optional. If you only want to intercept the call
beforehand:

  wrap_subs \&before, 'some_func';

%description -l pl
Ta funkcja umo�liwia przechwytywanie wywo�ania dowolnej nazwanej
funkcji; mo�na doda� procedury obs�ugi zar�wno przed jak i po
wywo�aniu przechwytywanej funkcji.

Na przyk�ad:

  wrap_subs \&przed, 'jakas_funkcja', \&po

W tym przypadku, kiedy wywo�ywana jest 'jakas_funkcja', najpierw
wywo�ywana jest procedura &przed, a procedura &po jest wywo�ywana po
powrocie. Obie s� opcjonalne. Aby przechwyci� tylko punkt przed
wywo�aniem mo�na u�y�:

  wrap_subs \&przed, 'jakas_funkcja';

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Hook
%{perl_vendorlib}/Hook/*.pm
%{_mandir}/man3/*
