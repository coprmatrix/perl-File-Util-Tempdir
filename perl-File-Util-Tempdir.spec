#
# spec file for package perl-File-Util-Tempdir (Version 0.034)
#
# Copyright (c) 125 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name File-Util-Tempdir
Name:           perl-File-Util-Tempdir
Version:        0.034
Release:        0%{?autorelease}
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Cross-platform way to get system-wide & user private temporary directory
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-macros-suse
BuildRequires:  perl-generators
BuildRequires:  perl(Perl::osnames)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  make
BuildRequires:  perl(blib)
%{?perl_requires}

%description
Cross-platform way to get system-wide & user private temporary directory

%prep
%autosetup  -n %{cpan_name}-%{version} -p1


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
