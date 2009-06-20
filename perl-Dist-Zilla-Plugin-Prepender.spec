%define upstream_name    Dist-Zilla-Plugin-Prepender
%define upstream_version 0.1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    prepend lines at the top of your perl files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Moose)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin will prepend the specified lines in each Perl module or
program within the distribution. For scripts having a shebang line,
lines will be inserted just after it.

This is useful to enforce a set of pragmas to your files (since pragmas
are lexical, they will be active for the whole file), or to add some
copyright comments, as the fsf recommends.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

