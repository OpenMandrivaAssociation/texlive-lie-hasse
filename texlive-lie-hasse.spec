Name:		texlive-lie-hasse
Version:	71883
Release:	1
Summary:	Draw Hasse diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lie-hasse
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lie-hasse.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lie-hasse.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package draws Hasse diagrams of the partially ordered sets
of the simple roots of any complex simple Lie algebra. It uses
the Dynkin diagrams package dynkin-diagrams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lie-hasse
%doc %{_texmfdistdir}/doc/latex/lie-hasse

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
