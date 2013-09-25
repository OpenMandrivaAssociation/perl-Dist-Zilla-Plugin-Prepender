%define upstream_name    Dist-Zilla-Plugin-Prepender
%define upstream_version 1.112280

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Prepend lines at the top of your perl files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/J/JQ/JQUELIN/Dist-Zilla-Plugin-Prepender-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch

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
perl Build.PL installdirs=vendor
./Build

%check
# Doesn't find user config
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*



