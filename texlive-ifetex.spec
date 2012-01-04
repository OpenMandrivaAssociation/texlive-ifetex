# revision 24853
# category Package
# catalog-ctan /macros/latex/contrib/ifetex
# catalog-date 2011-12-15 16:49:50 +0100
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-ifetex
Version:	1.2
Release:	2
Summary:	Provides \ifetex switch
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ifetex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifetex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifetex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the switch \ifetex which indicates whether
e-TeX is available or not. The package can be loaded as LaTeX
package using \usepackage{ifetex} or in plain TeX using \input
ifetex. In either case it aborts silently if the \ifetex macro
is already defined. The package's test is whether \eTeXversion
is defined as a primitive; if it is, the package assumes e-TeX
features are available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifetex/ifetex.sty
%{_texmfdistdir}/tex/plain/ifetex/ifetex.tex
%doc %{_texmfdistdir}/doc/latex/ifetex/README
%doc %{_texmfdistdir}/doc/latex/ifetex/ifetex.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifetex/ifetex.dtx
%doc %{_texmfdistdir}/source/latex/ifetex/ifetex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
