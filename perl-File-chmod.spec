%define	upstream_name	 File-chmod
%define upstream_version 0.40

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Implements symbolic and ls chmod modes  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/File/File-chmod-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
File::chmod is a utility that allows you to bypass system calls or bit
processing of a file's permissions. It overloads the chmod() function with its
own that gets an octal mode, a symbolic mode (see below), or an "ls" mode (see
below). If you wish not to overload chmod(), you can export symchmod() and
lschmod(), which take, respectively, a symbolic mode and an "ls" mode.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3*/*
%{perl_vendorlib}/File


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.320.0-1mdv2010.0
+ Revision: 403167
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.32-3mdv2009.0
+ Revision: 256875
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.32-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2008.0
+ Revision: 64584
- import perl-File-chmod


* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2008.0
- first mdv release


