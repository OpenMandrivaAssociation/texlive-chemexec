%global tl_name chemexec
%global tl_revision 21632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Creating (chemical) exercise sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemexec
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemexec.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides environments and commands that the author needed
when preparing exercise sheets and other teaching material. In
particular, the package supports the creation of exercise sheets, with
separating printing of solutions

