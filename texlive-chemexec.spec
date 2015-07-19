# revision 21632
# category Package
# catalog-ctan /macros/latex/contrib/chemexec
# catalog-date 2011-03-06 18:27:32 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-chemexec
Version:	1.0
Release:	10
Summary:	Creating (chemical) exercise sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemexec
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides environments and commands that the author
needed when preparing exercise sheets and other teaching
material. In particular, the package supports the creation of
exercise sheets, with separating printing of solutions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chemexec/chemexec.sty
%doc %{_texmfdistdir}/doc/latex/chemexec/README
%doc %{_texmfdistdir}/doc/latex/chemexec/chemexec_de.pdf
%doc %{_texmfdistdir}/doc/latex/chemexec/chemexec_de.tex
%doc %{_texmfdistdir}/doc/latex/chemexec/chemexec_en.pdf
%doc %{_texmfdistdir}/doc/latex/chemexec/chemexec_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750143
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718041
- texlive-chemexec
- texlive-chemexec
- texlive-chemexec
- texlive-chemexec
- texlive-chemexec

