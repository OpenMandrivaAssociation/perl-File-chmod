%define	upstream_name	 File-chmod
%define	upstream_version 0.32

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Implements symbolic and ls chmod modes  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
File::chmod is a utility that allows you to bypass system calls or bit
processing of a file's permissions. It overloads the chmod() function with its
own that gets an octal mode, a symbolic mode (see below), or an "ls" mode (see
below). If you wish not to overload chmod(), you can export symchmod() and
lschmod(), which take, respectively, a symbolic mode and an "ls" mode.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
