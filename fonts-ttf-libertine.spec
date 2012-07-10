%define archivename	LinLibertineTTF
%define reldate		2012_07_02
%define fontdir		%{_datadir}/fonts/ttf/libertine

Name:		fonts-ttf-libertine
Version:	5.3.0
Release:	%mkrel 1
Summary:	Linux Libertine Open Fonts
Group:		System/Fonts/True type
License:	GPLv2 and OFL
URL:		http://linuxlibertine.sf.net
Source0:	http://downloads.sourceforge.net/project/linuxlibertine/linuxlibertine/5.3.0/%{archivename}_%{version}_%{reldate}.tgz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
Provides:	linux-libertine-fonts
Obsoletes:	linux-libertine-fonts

%description
The Linux Libertine Open Fonts are a TrueType font family for practical
use in documents. They were created to provide a free alternative to
proprietary standard fonts.


%prep
%setup -qc


%install
install -d -m 0755 %{buildroot}%{fontdir}
install -p -m 0644 *.ttf  %{buildroot}%{fontdir}
ttmkfdir -d %{buildroot}%{fontdir} -o %{buildroot}%{fontdir}/fonts.scale
cp -f %{buildroot}%{fontdir}/fonts.scale %{buildroot}%{fontdir}/fonts.dir
mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d
ln -s %{fontdir} %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50


%files
%doc *.txt
%{fontdir}
%{_sysconfdir}/X11/fontpath.d/ttf-libertine:pri=50
