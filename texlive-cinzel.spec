%global tl_name cinzel
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for Cinzel and Cinzel Decorative fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cinzel
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cinzel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cinzel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Cinzel and Cinzel Decorative fonts, designed by Natanael Gama Natanael
Gama), find their inspiration in first century roman inscriptions, and
are based on classical proportions. Cinzel is all-caps (similar to
Trajan and Michelangelo), but is available in three weights (Regular,
Bold, Black). There are no italic fonts, but there are Decorative
variants, which can be selected by the usual italic-selection commands
in the package's LaTeX support.

