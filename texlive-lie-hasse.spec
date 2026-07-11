%global tl_name lie-hasse
%global tl_revision 75301

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Draw Hasse diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/lie-hasse
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lie-hasse.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lie-hasse.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package draws Hasse diagrams of the partially ordered sets of the
simple roots of any complex simple Lie algebra. It uses the Dynkin
diagrams package dynkin-diagrams.

