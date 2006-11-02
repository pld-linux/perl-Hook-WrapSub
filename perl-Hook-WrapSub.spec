#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Hook
%define	pnam	WrapSub
Summary:	Hook::WrapSub - wrap subs with pre- and post-call hooks
#Summary(pl):	
Name:		perl-Hook-WrapSub
Version:	0.03
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This function enables intercepting a call to any named
function; handlers may be added both before and after
the call to the intercepted function.

For example:

  wrap_subs \&before, 'some_func', \&after;

In this case, whenever the sub named 'some_func' is called,
the &before sub is called first, and the &after sub is called
afterwards.  These are both optional.  If you only want
to intercept the call beforehand:

  wrap_subs \&before, 'some_func';



# %description -l pl
# TODO

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
%{perl_vendorlib}/Hook/*.pm
%{_mandir}/man3/*
