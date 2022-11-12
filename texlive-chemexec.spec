Name:		texlive-chemexec
Version:	21632
Release:	1
Summary:	Creating (chemical) exercise sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chemexec
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
