Name:		texlive-cinzel
Version:	64550
Release:	2
Summary:	LaTeX support for Cinzel and Cinzel Decorative fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cinzel
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cinzel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cinzel.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cinzel and Cinzel Decorative fonts, designed by Natanael Gama
Natanael Gama), find their inspiration in first century roman
inscriptions, and are based on classical proportions. Cinzel is
all-caps (similar to Trajan and Michelangelo), but is available
in three weights (Regular, Bold, Black). There are no italic
fonts, but there are Decorative variants, which can be selected
by the usual italic-selection commands in the package's LaTeX
support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/cinzel
%{_texmfdistdir}/fonts/map/dvips/cinzel
%{_texmfdistdir}/fonts/truetype/ndiscovered/cinzel
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel
%{_texmfdistdir}/tex/latex/cinzel
%doc %{_texmfdistdir}/doc/fonts/cinzel

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
