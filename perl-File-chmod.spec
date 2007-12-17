%define	module	File-chmod
%define name	perl-%{module}
%define	version	0.32
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Implements symbolic and ls chmod modes  
Group:		Development/Perl
License:	GPL or Artistic
Url:		http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
File::chmod is a utility that allows you to bypass system calls or bit
processing of a file's permissions. It overloads the chmod() function with its
own that gets an octal mode, a symbolic mode (see below), or an "ls" mode (see
below). If you wish not to overload chmod(), you can export symchmod() and
lschmod(), which take, respectively, a symbolic mode and an "ls" mode.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3*/*
%{perl_vendorlib}/File

