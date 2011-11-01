Name:		texlive-chemexec
Version:	1.0
Release:	1
Summary:	Creating (chemical) exercise sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemexec
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides environments and commands that the author
needed when preparing exercise sheets and other teaching
material. In particular, the package supports the creation of
exercise sheets, with separating printing of solutions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
