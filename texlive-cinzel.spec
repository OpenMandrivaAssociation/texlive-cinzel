# revision 33386
# category Package
# catalog-ctan /fonts/cinzel
# catalog-date 2014-04-08 11:06:38 +0200
# catalog-license ofl
# catalog-version undef
Name:		texlive-cinzel
Version:	20140408
Release:	3
Summary:	LaTeX support for Cinzel and Cinzel Decorative fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cinzel
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cinzel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cinzel.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/cinzel/cnzl_7luz43.enc
%{_texmfdistdir}/fonts/enc/dvips/cinzel/cnzl_7t2zcj.enc
%{_texmfdistdir}/fonts/enc/dvips/cinzel/cnzl_fzt4gv.enc
%{_texmfdistdir}/fonts/enc/dvips/cinzel/cnzl_k6z3ge.enc
%{_texmfdistdir}/fonts/map/dvips/cinzel/cinzel.map
%{_texmfdistdir}/fonts/opentype/ndiscovered/cinzel/Cinzel-Black.otf
%{_texmfdistdir}/fonts/opentype/ndiscovered/cinzel/Cinzel-Bold.otf
%{_texmfdistdir}/fonts/opentype/ndiscovered/cinzel/Cinzel-Regular.otf
%{_texmfdistdir}/fonts/opentype/ndiscovered/cinzel/CinzelDecorative-Black.otf
%{_texmfdistdir}/fonts/opentype/ndiscovered/cinzel/CinzelDecorative-Bold.otf
%{_texmfdistdir}/fonts/opentype/ndiscovered/cinzel/CinzelDecorative-Regular.otf
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Black-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/Cinzel-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Black-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel/Cinzel-Black.pfb
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel/Cinzel-Bold.pfb
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel/Cinzel-Regular.pfb
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel/CinzelDecorative-Black.pfb
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel/CinzelDecorative-Bold.pfb
%{_texmfdistdir}/fonts/type1/ndiscovered/cinzel/CinzelDecorative-Regular.pfb
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Black-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Black-lf-t1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Black-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/Cinzel-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Black-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Black-lf-t1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Black-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/ndiscovered/cinzel/CinzelDecorative-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/cinzel/LY1Cinzel-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/LY1CinzelDecorative-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/OT1Cinzel-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/OT1CinzelDecorative-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/T1Cinzel-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/T1CinzelDecorative-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/TS1Cinzel-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/TS1CinzelDecorative-LF.fd
%{_texmfdistdir}/tex/latex/cinzel/cinzel.sty
%doc %{_texmfdistdir}/doc/fonts/cinzel/README
%doc %{_texmfdistdir}/doc/fonts/cinzel/SIL_Open_Font_License.txt
%doc %{_texmfdistdir}/doc/fonts/cinzel/cinzel-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/cinzel/cinzel-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
